#!usr/bin/env bash

# be sure to change both virtualenv directory and scrape/living_social
# directory to where your venv and code is.
cd ~/.virtualenvs/ScrapeProj
source bin/activate
cd ~/Projects/new-coder/scrape/living_social
scrapy crawl livingsocial
