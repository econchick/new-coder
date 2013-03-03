---
layout: post.html
title: "Part 5: Running our Scraper"
tags: [scrape]
---

Putting all the pieces together to scrape our data.

### scrapy.cfg file

Scrapy needs a config file to direct it to where our project lies. The config file needs to be in the project root directory. An example of our directory structure for scrapy:

```
scrapy.cfg
living_social/
    __init__.py
    items.py
    models.py
    pipelines.py
    settings.py
    spiders/
        __init__.py
        livingsocial_spider.py
```

This file contains the name of the python module that defines the project settings:

```
[settings]
default = living_social.settings
```

### Manually run the scraper

Within your terminal, with your ScrapeProj virtualenv activated:

```bash
(ScrapeProj) $ cd new-coder/scrape/lib/full_source/living_social
(ScrapeProj) $ scrapy crawl livingsocial
```

