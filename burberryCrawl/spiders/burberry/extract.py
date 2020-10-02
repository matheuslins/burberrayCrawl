from burberryCrawl.loaders import ClothesLoader


def extract_clothes(response):
    loader = ClothesLoader(response=response)
#    loader.add_xpaths(XPATHS_JOB)
#    loader.add_value('url', response.url)
    item = loader.load_item()
    yield item
