import scrapy
from scrapy import Selector
from scrapy.http import Request

from burberryCrawl.spiders.burberry.steps.consult import consult_categories
from burberryCrawl.spiders.burberry.constants.consult import START_URL
from burberryCrawl.settings import SAVE_DB


class BurberrySpider(scrapy.Spider):
    name = 'burberry'
    allowed_domains = ['us.burberry.com']
    start_urls = [START_URL]
    custom_settings = {
        'DOWNLOAD_DELAY': 0.3,
        'COOKIES_ENABLED': False,
        'ES_PIPELINE_ENABLE': SAVE_DB
    }

    def parse(self, response):
        women_url = f"{START_URL}/women"
        request = Request(
            url=women_url,
            callback=self.parse_clothes
        )
        yield request

    def parse_clothes(self, response):
        selector = Selector(response)
        return consult_categories(selector)
