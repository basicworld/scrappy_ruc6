# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Ruc6Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class PostItem(scrapy.Item):
    # define the fields for your item here like:
    post_id = scrapy.Field()
    post_title = scrapy.Field()
    post_link = scrapy.Field()
    post_author = scrapy.Field()
    post_date = scrapy.Field()
    post_viewer_count = scrapy.Field()
    post_reply_count = scrapy.Field()
    post_has_img = scrapy.Field()
    pass
