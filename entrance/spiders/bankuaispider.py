# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from entrance.items import BankuaiItem
import re


class Jobspider(CrawlSpider):
    start_urls = ['http://bbs.51cto.com/thread-1014628-1.html']

    name = "bankuai"

    url_format = 'http://bbs.51cto.com/thread-{}-1.html'

    i = 1014000




    def parse(self, response):
        selector = Selector(response)
        item = BankuaiItem()
        if self.i < 1024000:
            info = selector.xpath('//div[@class="tz_main"]//table[1]')

            item['title'] = info.xpath('//div[@class="postinfo01 bd4"]/h2/strong/a/text()').extract_first()
            item['user'] = info.xpath('//td[@class="postauthor bd4b"]/cite/a/text()').extract_first()
            time = info.xpath('//div[@class="postinfo02"]/p[1]/text()').extract()
            if len(time) != 0:
                time_1 = time[0].split(" ")
                item['time'] = time_1[0] + time_1[1]
            else:
                item['time'] = ''
            content = info.xpath('//div[@class="postmessage defaultpost"]/div[3]').extract()
            if len(content) !=0:
                content_all = content[0] + '>'
                d = re.findall('>(.*?)<', content_all, re.S)
                content_find_all = ''
                for each in d:
                    content_find_all = each + content_find_all
                item['content'] = content_find_all.strip()
            else:
                item['content'] = ''
            bankuai = selector.xpath('//div[@class="position"]//div[@id="site-nav"]/ul/li[5]/a/text()').extract()
            if len(bankuai) !=0:
                item['bankuai'] = bankuai[0].strip()
            else:
                item['bankuai'] = ''
            yield item
            self.i += 1
            url_all = self.url_format.format(str(self.i))
            yield Request(url=url_all, callback=self.parse,dont_filter=True)
