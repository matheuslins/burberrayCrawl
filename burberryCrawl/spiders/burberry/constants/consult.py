
START_URL = 'http://us.burberry.com'

CONSULT_XPATHS = {
    'CATEGORIES': '//a[@class="css-g38vah e1268c320"]//@href',
    'PRODUCT_LINKS': '//a[@class="product-card__link"]//@href | '
                     '//div[contains(@class, "cell-asset")]//a[contains(@class, "product-internal-link")]/@href',
    'SHOW_MORE_BUTTON': '//button[@aria-label="View more products"]',
    'SHOW_MORE_LINK': '//div[contains(@class, "view-more-button")]'
}

