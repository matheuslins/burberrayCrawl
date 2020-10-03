import scrapy
from scrapy import Selector
from scrapy.http import Request

from burberryCrawl.spiders.burberry.steps.consult import consult_clothes


class BurberrySpider(scrapy.Spider):
    name = 'burberry'
    allowed_domains = ['us.burberry.com']
    start_urls = ['http://us.burberry.com']
    custom_settings = {
        'DOWNLOAD_DELAY': 0.5
    }

    def parse(self, response):
        women_url = f"{self.start_urls[0]}/women"
        request = Request(
            url=women_url,
            callback=self.parse_clothes
        )

        yield request

    def parse_clothes(self, response):
        selector = Selector(response)
        consult_clothes(self.start_urls[0], selector)
