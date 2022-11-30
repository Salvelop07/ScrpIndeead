# -*- coding: utf-8 -*-
import os

import scrapy
from bs4 import BeautifulSoup

from indeed_company_reviews.items import IndeedCompanyReviewsItem

company = os.getenv("indeed_company", None)

assert company, "[indeed] company not set"


class ReviewSpider(scrapy.Spider):
    name = "review"
    allowed_domains = ["indeed.com"]
    start_urls = [f"http://indeed.com/cmp/{company}/reviews?fcountry=ALL"]
    user_agent = "Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion"

    def parse(self, response):
        reviews = response.selector.xpath('//div[@data-tn-entitytype="reviewId"]')
        for review in reviews:
            rating = float(
                review.xpath('*//meta[@itemprop="ratingValue"]').attrib["content"]
            )

            text = BeautifulSoup(
                review.xpath('*//span[@itemprop="reviewBody"]').get()
            ).get_text()

            find_pros = review.xpath('*//h2[text() = "Pros"]/following::*/text()')
            pros = find_pros[0].get() if find_pros else None

            find_cons = review.xpath('*//h2[text() = "Cons"]/following::*/text()')
            cons = find_cons[0].get() if find_cons else None

            position = (
                BeautifulSoup(review.xpath('*//span[@itemprop="author"]').get())
                .get_text()
                .split(" - ")[0]
            )

            date_created = (
                BeautifulSoup(review.xpath('*//span[@itemprop="author"]').get())
                .get_text()
                .split(" - ")[-1]
            )
            id = review.attrib["data-tn-entityid"]

            yield IndeedCompanyReviewsItem(
                id=id,
                rating=rating,
                text=text,
                pros=pros,
                cons=cons,
                position=position,
                date_created=date_created,
            )

        next_page = response.selector.xpath('//a[@data-tn-element="next-page"]').attrib[
            "href"
        ]

        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
