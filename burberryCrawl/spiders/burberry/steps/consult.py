from burberryCrawl.spiders.burberry.constants.consult import CATEGORIES_XPATH


def consult_clothes(start_url, selector):
    categories_endpoints = selector.xpath(CATEGORIES_XPATH).getall()

    for category_endpoint in categories_endpoints:
        url = f"{start_url}{category_endpoint}"
        pass
