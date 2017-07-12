# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class EntranceItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    school = Field()
    years = Field()
    batch = Field()
    max_score = Field()
    avg_score = Field()

class BankuaiItem(Item):
    time = Field()
    user = Field()
    title = Field()
    content = Field()
    bankuai = Field()


