# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html



from scrapy.conf import settings
import pymysql

class EntrancePipeline(object):
    # def __init__(self):
    #     client = pymysql.Connection(host='127.0.0.1', user='root',password='123456',)
    #     self.post = tdb[settings['MONGODB_DOCNAME']]
    #
    # def process_item(self, item, spider):
    #     Info = dict(item)
    #     self.post.insert(Info)
    #     return item
    def process_item(self,spider):
        pass
