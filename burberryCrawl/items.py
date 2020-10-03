from scrapy.item import Item, Field
from itemloaders.processors import Identity


class ClothesItem(Item):
    brandId = Field()
    url = Field()
    name = Field()
    description = Field()
    images = Field(output_processor=Identity())
    color = Field()
