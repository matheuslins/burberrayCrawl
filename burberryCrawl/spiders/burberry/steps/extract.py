from burberryCrawl.loaders import ClothesLoader
from burberryCrawl.spiders.burberry.constants.extract import XPATHS_PRODUCTS


def extract_product(response):
    loader = ClothesLoader(response=response)
    loader.add_xpaths(XPATHS_PRODUCTS)
    loader.add_value('brandId', 'burberry')
    loader.add_value('url', response.url)
    item = loader.load_item()
    yield item
