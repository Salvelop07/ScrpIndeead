<div align="center">
    <img src="https://cdn2.iconfinder.com/data/icons/essential-web-4/50/commenting-more-typing-chat-review-512.png" alt="logo" height="196">
</div>

# scrapy-indeed-company-reviews

![coding_style](https://img.shields.io/badge/code%20style-black-000000.svg)
[![time tracker](https://wakatime.com/badge/github/zehengl/scrapy-indeed-company-reviews.svg)](https://wakatime.com/badge/github/zehengl/scrapy-indeed-company-reviews)

A scrapy app to crawl company reviews from Indeed

## Environment

- Python 3.6

## Install

1. create virtualenv
2. activate virtualenv
3. update pip and setuptools
4. install deps

Use `pip install -r requirements-dev.txt` for development.
It will install `pylint` and `black` to enable linting and auto-formatting.

## Usage

1. set environment variables for company
2. run scrapy to crawl the company reviews and save in json

## Example

### Windows

```powershell
python -m venv venv
.\venv\Scripts\activate
python -m pip install -U pip setuptools
pip install -r requirements-scrapy.txt
$Env:indeed_company="City-of-Calgary"
scrapy crawl review -o data/reviews_$Env:indeed_company.json
```

See the [crawl.ps1](https://github.com/zehengl/scrapy-indeed-company-reviews/blob/master/crawl.ps1) powershell script for batching example

### Linux

```bash
python -m venv venv
source venv/bin/activate
python -m pip install -U pip setuptools
pip install -r requirements-scrapy.txt
export indeed_company="City-of-Calgary"
scrapy crawl review -o data/reviews_$indeed_company.json
```

## Demo

See the demo app at [https://scrapy-indeed-company-reviews.herokuapp.com/](https://scrapy-indeed-company-reviews.herokuapp.com/) for some crawled company reviews

<hr>

<sup>

## Credits

- [Icon][1] by [Becris .][2]

</sup>

[1]: https://www.iconfinder.com/icons/3209401/chat_commenting_more_review_typing_icon
[2]: https://www.iconfinder.com/becris
