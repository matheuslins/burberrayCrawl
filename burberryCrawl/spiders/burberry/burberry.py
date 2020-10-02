import scrapy

from burberryCrawl.spiders.burberry.extract import extract_clothes


class BurberrySpider(scrapy.Spider):
    name = 'burberry'
    allowed_domains = ['us.burberry.com']
    start_urls = ['http://us.burberry.com/']
    custom_settings = {
        'DOWNLOAD_DELAY': 0.5,
    }

    def parse(self, response):
        for item in extract_clothes(response) or []:
            yield item