# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FrasesHistoricasItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    autor = scrapy.Field()
    data = scrapy.Field()
    texto = scrapy.Field()
