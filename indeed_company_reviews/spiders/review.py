# -*- coding: utf-8 -*-
import os

import scrapy

from indeed_company_reviews.items import IndeedCompanyReviewsItem

company = os.getenv("indeed_company", None)

assert company, "[indeed] company not set"


class ReviewSpider(scrapy.Spider):
    name = "review"
    allowed_domains = ["indeed.com"]
    start_urls = [f"https://indeed.com/cmp/{company}/reviews?fcountry=ALL"]

    def parse(self, response):
        reviews = response.css(".cmp-Review-container")
        for review in reviews:
            rating = float(review.css(".cmp-ReviewRating-text ::text").get())
            text = "\n".join(review.css(".cmp-Review-text ::text").getall())
            pros = "\n".join(review.css(".cmp-ReviewProsCons-prosText ::text").getall())
            cons = "\n".join(review.css(".cmp-ReviewProsCons-consText ::text").getall())
            date_created = review.css(".cmp-ReviewAuthor ::text").getall()[-1]
            id = review.attrib["data-tn-entityid"]

            yield IndeedCompanyReviewsItem(
                id=id,
                rating=rating,
                text=text,
                pros=pros,
                cons=cons,
                date_created=date_created,
            )

        next_page = response.css(
            '.icl-Button[data-tn-element="next-page"] ::attr(href)'
        ).get()

        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
