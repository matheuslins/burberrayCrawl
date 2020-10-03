from burberryCrawl.parsers.extract import parser_url_images, parser_description


XPATHS_PRODUCTS = {
    'name': '//h1[@class="product-info-panel__title"]//span/text()',
    'description': ('//div[@class="description-modal__text-container"]//text()', parser_description),
    'images': (
        '//picture[@class="desktop-product-gallery-image__picture"]//source/@srcset',
        parser_url_images
    )
}
