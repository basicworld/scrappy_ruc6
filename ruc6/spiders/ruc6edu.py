# -*- coding: utf-8 -*-
import scrapy
import time
from random import random
from ruc6.items import PostItem
import re


class Ruc6eduSpider(scrapy.Spider):
    name = "ruc6edu"
    allowed_domains = ["bt.ruc6.edu.cn"]
    start_urls = [
        'http://bt.ruc6.edu.cn/b/forum.php?mod=forumdisplay&fid=33&filter=typeid&typeid=74&page=1',
    ]

    def parse(self, response):
        if response.status == 200:
            # save
            for sel in response.xpath('//table[@id="forum_33"]/tbody'):
                # pass strange post
                temp_id = sel.xpath('@id').extract()
                if not (temp_id and temp_id[0].startswith('normal')):
                    continue

                # get post content
                item = PostItem()
                item['post_id'] = sel.xpath('@id').extract()
                item['post_title'] = sel.xpath('tr/th/a[@class="xst"]/text()').extract()
                item['post_link'] = sel.xpath('tr/th/a[@class="xst"]/@href').extract()
                item['post_author'] = sel.xpath('tr/td[@class="by"]')[0].xpath('cite/a/text()').extract()
                item['post_date'] = sel.xpath('tr/td[@class="by"]')[0].xpath('em/span/text()').extract()
                item['post_viewer_count'] = sel.xpath('tr/td[@class="num"]/a[@class="xi2"]/text()').extract()
                item['post_reply_count'] = sel.xpath('tr/td[@class="num"]/em/text()').extract()
                item['post_has_img'] = (1 if sel.xpath('tr/th/img') else 0)

                yield item

                # another loop
                this_page_count = int(re.findall('page=(\d+)', response.url)[-1])
                with open('output/ruc6edu.page%s.html' % this_page_count, 'wb') as f:
                    f.write(response.body)

                page_count = this_page_count + 1
                next_url = ('http://bt.ruc6.edu.cn/b/forum.php?mod=forumdisplay&fid=33&filter=typeid&typeid=74&page=%s' % page_count)
                print('page_count:', page_count)

                yield scrapy.Request(next_url, callback=self.parse)

    def parse_posts_list(self, response):
        pass
