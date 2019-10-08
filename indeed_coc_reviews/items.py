# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IndeedCompanyReviewsItem(scrapy.Item):
    id = scrapy.Field()
    rating = scrapy.Field()
    text = scrapy.Field()
    pros = scrapy.Field()
    cons = scrapy.Field()
    date_created = scrapy.Field()
