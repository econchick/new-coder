---
layout: post.html
title: "Part 5: Running our Scraper"
tags: [scrape]
---

----
**NOTE**
Typo: bash scripe -> bash script
----

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

Next, to see the data that's saved into the database, start up Postgres and enter these commands:

```bash
$ psql -h localhost
psql (9.1.4, server 9.1.3)
Type "help" for help.

lynnroot=# \connect scrape
psql (9.1.4, server 9.1.3)
You are now connected to database "scrape" as user "lynnroot".
scrape=# select * from deals;
 id | title | description | link | location | category | original_price | price
----+-------+-------------+------+----------+----------+----------------+-------
(0 rows)
```

Try a few of these select queries:

**TODO** Add example queries when I have data into database.


### Hook up to a Cron job

It'd be pretty annoying if we had to manually run this script regularly.  This is where cron jobs come in.

We'll first create a bash script that simulates what we would do if we were to run scrapy manually.  There is a sample one in the `new-coder/scrape/living_social/` directory called `scrape.sh`. Edit the bash scripe to where your `(ScrapeProj)` virtualenv is as well as where your scraper root directory is (where the `scrapy.cfg` file lies).

Next, within your terminal, type:

```bash
$ crontab -e
```
to edit your crontab file.  This opens up the editor for your cron tab.  Add a line:

```cron
0 13  * * * sh ~/Projects/new-coder/scrape/living_social/scrapy.sh
```

This says that ever day at hour 13 (1pm, relative to your local machine time), run the `scrapy.sh` script.  To schedule your cron job at a different time, check out Wiki's [overview](http://en.wikipedia.org/wiki/Cron#Predefined_scheduling_definitions).

**NOTE:** The cron job will run automatically for whenever you schedule it to run (in this example, daily at 1pm). But! It will only run when your computer is on (not hibernate/sleep or powered off), and in particular with this script, connected to the internet.  To run the cron job regardless of the state your computer is in, you would host the scraper code + the bash script and cron job on a separate server (either your own, or a company's) that will always be 'on'.  You can host your own cron jobs on [OpenShift](http://openshift.redhat.com).

**TODO** Extended, Real Life Usage, Where to Go from Here
