# -*- coding: utf-8 -*-
import scrapy

from indeed_coc_reviews.items import IndeedCompanyReviewsItem


class ReviewSpider(scrapy.Spider):
    name = "review"
    allowed_domains = ["ca.indeed.com"]
    start_urls = ["https://ca.indeed.com/cmp/City-of-Calgary/reviews"]

    def parse(self, response):
        reviews = response.css(".cmp-review")
        for review in reviews:
            rating = float(review.css(".cmp-ratingNumber ::text").get())
            text = "\n".join(review.css(".cmp-review-text ::text").getall())
            pros = "\n".join(review.css(".cmp-review-pro-text ::text").getall())
            cons = "\n".join(review.css(".cmp-review-con-text ::text").getall())
            date_created = review.css(".cmp-review-date-created ::text").get()
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
            '.cmp-Pagination-link[data-tn-element="next-page"] ::attr(href)'
        ).get()

        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
