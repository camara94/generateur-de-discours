# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DiscoursGouvFrItem(scrapy.Item):
    # define the fields for your item here like:
    titre = scrapy.Field()
    date = scrapy.Field()
    discours = scrapy.Field()


class UrlPattern(scrapy.Item):
    path = scrapy.Field()
