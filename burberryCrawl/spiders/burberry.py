import scrapy


class BurberrySpider(scrapy.Spider):
    name = 'burberry'
    allowed_domains = ['us.burberry.com']
    start_urls = ['http://us.burberry.com/']

    def parse(self, response):
        pass
