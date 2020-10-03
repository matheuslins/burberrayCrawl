import scrapy
from scrapy import Selector
from scrapy.http import Request

from burberryCrawl.spiders.burberry.steps.consult import consult_categories
from burberryCrawl.spiders.burberry.constants.consult import START_URL


class BurberrySpider(scrapy.Spider):
    name = 'burberry'
    allowed_domains = ['us.burberry.com']
    start_urls = [START_URL]
    custom_settings = {
        'DOWNLOAD_DELAY': 0.5
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
