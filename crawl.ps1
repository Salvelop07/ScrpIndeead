$companies = @("City-of-Calgary", "City-of-Edmonton", "City-of-Toronto")

foreach ($company in $companies) {
    $Env:indeed_company = $company
    scrapy crawl review -o reviews_$Env:indeed_company.json
}
python visualize.py
