$companies = @(
    "Calgary",
    "Charlottetown",
    "Edmonton",
    "Fredericton",
    "Halifax",
    "Iqaluit",
    "Montreal",
    "Ottawa",
    "Quebec",
    "Regina",
    "Saint-John",
    "Saskatoon"
    "Toronto"
    "Vancouver",
    "Victoria",
    "Whitehorse",
    "Winnipeg",
    "Yellowknife"
)

foreach ($company in $companies) {
    $Env:indeed_company = "City-of-$company"
    scrapy crawl review -O data/reviews_$Env:indeed_company.json
}
