# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from entrance.items import EntranceItem


class Jobspider(CrawlSpider):
    # start_urls = ['http://kaoshi.edu.sina.com.cn/college/scorelist?tab=&wl=2&local=8&provid=&batch=&syear=2011']

    name = "entrance"

    url = 'http://kaoshi.edu.sina.com.cn/college/scorelist?tab=&wl=2&local=8&provid=&batch=&syear={}&page={}'

    i = 0

    j = 2009

    def start_requests(self):
        if self.j < 2015:
            self.j += 1
            i = 1
            url = self.url.format(str(self.j), str(i))
            yield Request(url, self.pare_everyyear,dont_filter=True)

    def pare_everyyear(self, response):
        item = EntranceItem()
        selector = Selector(response)
        infos = selector.xpath('//tr[@class = "tbl2tbody"]')
        for info in infos:
            item['school'] = info.xpath('td[1]/a/text()').extract_first()
            item['years'] = info.xpath('td[5]/text()').extract_first()
            item['batch'] = info.xpath('td[4]/text()').extract_first()
            item['max_score'] = info.xpath('td[6]/text()').extract_first()
            item['avg_score'] = info.xpath('td[7]/text()').extract_first()
            yield item
        if self.i < 40:
            self.i += 1
            url = self.url.format(str(self.j), str(self.i))
            yield Request(url, callback=self.pare_everyyear,dont_filter=True)
