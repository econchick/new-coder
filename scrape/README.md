## Web Scraper

### Project
Scrape data from a regularly updated website (e.g. cafeteria's weekly lunch menu, local bank interest rates, Groupon/LivingSocial/etc deals), save to a database (postgres), hook up to a cron job, and use the Data Visualization tutorial to play with different visualization techniques.

#### Full Source
Within your terminal:

* Create database for storing scraped data
* `(WebScraperProj) $ cd new-coder/living_social`
* Edit settings.py and set your database settings
* `(WebScraperProj) $ scrapy crawl livingsocial`

#### Running tests
Within your terminal:

* `(WebScraperProj) $ cd new-coder/scrape/living_social`
* `(WebScraperProj) $ scrapy check livingsocial`

