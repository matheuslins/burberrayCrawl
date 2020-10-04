import pytz
import hashlib
from datetime import datetime

from scrapy.exceptions import DropItem, NotConfigured
from elasticsearch.helpers import bulk
from burberryCrawl.settings import BULK_SIZE, ES_INDEX
from burberryCrawl.database import config_client


class DuplicatesProductPipeline(object):

    def __init__(self):
        self.products = set()

    def process_item(self, item, spider):
        url_product = item.get('url')

        if not url_product:
            raise DropItem('Job not found. Item dropped')

        if url_product in self.products:
            self.inc_duplicated(spider)
            raise DropItem('Duplicated job')
        else:
            self.products.add(url_product)
            return item

    def inc_duplicated(self, spider):
        stat = spider.crawler.stats.get_value('burberryCrawl/jobs') or {}
        stat['duplicated'] = stat.get('duplicated', 0) + 1
        spider.crawler.stats.set_value('burberryCrawl/jobs', stat)


class BaseDBPipeline(object):
    client = None

    def __init__(self, settings):
        self.bulk = []
        self.tz = pytz.timezone('America/Sao_Paulo')

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)


class ElasticSearchPipeline(BaseDBPipeline):

    def __init__(self, settings, *args, **kwargs):
        if not settings.getbool('ES_PIPELINE_ENABLE'):
            raise NotConfigured
        super(ElasticSearchPipeline, self).__init__(settings, *args, **kwargs)

    def open_spider(self, spider):
        self.client = config_client()

    @staticmethod
    def generate_id(item):
        return hashlib.sha1(
            f"{item['url']}_{item['name']}".encode()
        ).hexdigest()[:40]

    def insert_items(self):
        date_timezone = datetime.now(tz=self.tz).date()
        for item in self.bulk:
            yield {
                "_index": f"{ES_INDEX}-{date_timezone}",
                "_type": "product",
                "_id": self.generate_id(item),
                '_op_type': 'create',
                '_source': item
            }

    def process_item(self, item, spider):
        dict_item = dict(item)
        dict_item.update({
            "dateTime": datetime.now(tz=self.tz).isoformat(),
        })
        self.bulk.append(dict_item)
        if len(self.bulk) >= BULK_SIZE:
            bulk(self.client, self.insert_items())
            self.bulk = []
        return item

    def close_spider(self, spider):
        if len(self.bulk) < BULK_SIZE:
            bulk(self.client, self.insert_items())
            self.bulk = []
