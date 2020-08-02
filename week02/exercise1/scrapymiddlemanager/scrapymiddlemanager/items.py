# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class QuotesItem(scrapy.Item):
    author = scrapy.Field()
    quotes = scrapy.Field()

class ScrapymiddlemanagerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
