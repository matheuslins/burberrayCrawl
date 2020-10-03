from scrapy.item import Item, Field
from itemloaders.processors import Identity


class VariantItem(Item):
    size = Field()
    color = Field()
    price = Field()
    stock = Field()


class ProductItem(Item):
    brandId = Field()
    url = Field()
    name = Field()
    description = Field()
    images = Field(output_processor=Identity())
    color = Field()
    variants = Field(output_processor=Identity(), serializer=VariantItem)


