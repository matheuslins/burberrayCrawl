from burberryCrawl.parsers.extract import parser_url_images, parser_description


XPATHS_PRODUCTS = {
    'name': '//h1[@class="product-info-panel__title"]//span[1]/text() | //h1[contains(@class, "product-title")]/text()',
    'description': ('//div[@class="description-modal__text-container"]//text() | //h2[contains(., "Description")]/following-sibling::div[contains(@class, "details")]//text()',
                    parser_description),
    'images': (
        '//source[@media="(min-width:2560px)"]/@srcset | //source[@media="(min-width:2560px)"]/@data-srcset | //div[contains(@class, "product-image-asset-content")]/@style',
        parser_url_images
    ),
    'color': '//span[@class="color-picker__label"]/text() | //div[@id="colour-picker-value"]//text()',
    '_no_sizes': '//label[contains(@class, "size-picker__size-box--disabled")]//input/@value',
    '_sizes': '//label[@class="size-picker__size-box"]//input/@value | '
              '//label[@class="size-picker__size-box size-picker__size-box--selected"]//input/@value | '
              '//ul[contains(@class, "dimensions-inline-list")]//li//a/text()',
    '_price': '//div[@class="product-info-panel__price"]//text() | '
              '//p[@class="price-info"]/span[contains(@class, "price-amount")][1]//text()[2]'
}
