from scrapy import Selector

from burberryCrawl.loaders import ProductLoader
from burberryCrawl.spiders.burberry.constants.extract import XPATHS_PRODUCTS


def extract_product(response):
    loader = ProductLoader(response=response)
    loader.add_xpaths(XPATHS_PRODUCTS)
    loader.add_value('brandId', 'burberry')
    loader.add_value('url', response.url)
    loader.add_value('variants', load_variants(response))
    item = loader.load_item()
    yield item


def load_variants(response):
    variants = []

    no_sizes = Selector(response).xpath(XPATHS_PRODUCTS['_no_sizes']).getall()
    sizes = Selector(response).xpath(XPATHS_PRODUCTS['_sizes']).getall()
    price = Selector(response).xpath(XPATHS_PRODUCTS['_price']).extract_first()
    color = Selector(response).xpath(XPATHS_PRODUCTS['color']).extract_first()

    for size in sizes:
        variants.append({
            'size': size,
            'color': color,
            'price': price,
            'stock': 1
        })

    if no_sizes:
        variants.extend([{
            'size': size,
            'color': color,
            'price': price,
            'stock': 0
        } for size in no_sizes])

    if not sizes:
        variants.append({
            'size': None,
            'color': color,
            'price': price,
            'stock': 0 if no_sizes else 1
        })

    return variants
