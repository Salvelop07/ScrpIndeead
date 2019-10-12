# scrapy-indeed-company-reviews

![coding_style](https://img.shields.io/badge/code%20style-black-000000.svg)

## Envrionment

- Python 3.6

## Install

1. create virtualenv
2. activate virtualenv
3. update pip and setuptools
4. install deps

Use `pip install -r requirements-dev.txt` for development.
It will install `pylint` and `black` to enable linting and auto-formatting.

## Usage

1. set envrionment variables for company
2. run scrapy to crawl the company reviews and save in json

## Example

### Windows

```powershell
python -m venv venv
.\venv\Scripts\activate
python -m pip install -U pip setuptools
pip install -r requirements.txt
$Env:indeed_company="City-of-Calgary"
scrapy crawl review -o reviews_$Env:indeed_company.json
python visualize.py
```

See the [crawl.ps1](https://github.com/zehengl/scrapy-indeed-company-reviews/blob/master/crawl.ps1) powershell script for batching example

### Linux

```bash
python -m venv venv
source venv/bin/activate
python -m pip install -U pip setuptools
pip install -r requirements.txt
export indeed_company="City-of-Calgary"
scrapy crawl review -o reviews_$indeed_company.json
python visualize.py
```
