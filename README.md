# scrapy-indeed-coc-reviews

## Envrionment

- Python 3.6
- Windows 10

## Coding Style

![coding_style](https://img.shields.io/badge/code%20style-black-000000.svg)

## Install

    python -m venv venv
    .\venv\Scripts\activate
    python -m pip install -U pip setuptools
    pip install -r requirements.txt

Use `pip install -r requirements-dev.txt` for development.
It will install `pylint` and `black` to enable linting and auto-formatting.

## Usage

    scrapy crawl review -o reviews.json
