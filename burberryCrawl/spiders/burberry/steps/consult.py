from scrapy.http import Request
from scrapy import Selector
from scrapy_splash import SplashRequest

from burberryCrawl.spiders.burberry.constants.consult import CONSULT_XPATHS, START_URL
from burberryCrawl.spiders.burberry.steps.extract import extract_product


def consult_categories(selector):
    categories_endpoints = selector.xpath(CONSULT_XPATHS['CATEGORIES']).getall()

    for category_endpoint in categories_endpoints:
        url = f"{START_URL}{category_endpoint}"
        yield Request(url=url, callback=consult_product)


def consult_product(response):
    selector = Selector(response)
    product_links = selector.xpath(CONSULT_XPATHS['PRODUCT_LINKS']).getall()

    for product_link in product_links:
        url_product = f"{START_URL}{product_link}"
        yield Request(url=url_product, callback=extract_product)
