# ScrpIndeead

ScrpIndeead is a scrapy app that gathers company reviews from Indeed, helping you make informed career decisions! 🕷️💼✨

## Environment

- Python 3.9

## Install

1. create virtualenv
2. activate virtualenv
3. update pip
4. install deps

> Use `pip install -r requirements-dev.txt` for development.

## Usage

1. set environment variables for company
2. run scrapy to crawl the company reviews and save in json

## Example

### Windows

```powershell
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install -U pip
pip install -r requirements-dev.txt
$Env:indeed_company="City-of-Calgary"
scrapy crawl review -O data/reviews_$Env:indeed_company.json
```

See the [crawl.ps1](https://github.com/Salvelop07/ScrpIndeead/blob/master/crawl.ps1) powershell script for batching example

### Linux

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install -r requirements-dev.txt
export indeed_company="City-of-Calgary"
scrapy crawl review -O data/reviews_$indeed_company.json
```

## Demo

See the demo app at [https://indeed-municipality-reviews.streamlit.app/](https://indeed-municipality-reviews.streamlit.app/) for some crawled company reviews

## Credits

- [Icon][1] by [Becris .][2]

[1]: https://www.iconfinder.com/icons/3209401/chat_commenting_more_review_typing_icon
[2]: https://www.iconfinder.com/becris
