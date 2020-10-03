from burberryCrawl.loaders import ClothesLoader
from burberryCrawl.spiders.burberry.constants.extract import XPATHS_CLOTHES


def extract_clothes(response):
    loader = ClothesLoader(response=response)
    loader.add_xpaths(XPATHS_CLOTHES)
    loader.add_value('brandId', "burberry")
    item = loader.load_item()
    yield item
