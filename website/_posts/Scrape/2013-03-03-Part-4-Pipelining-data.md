---
layout: post.html
title: "Part 4: Pipelining Data to Database"
tags: [scrape]
url: "/scrape/part-4/"
---

Pipelining our scraped data into our Postgres database.

### Setup our Pipeline

We’ve setup our spider to crawl and parse the HTML, and we’ve set up our database to take the parse data. Now we have to connect the two together through a pipeline.

Create a file called `pipelines.py` in `my_scraper/scraper_app/` directory. In `pipelines.py`, we will define a session (the actual connecting to the database), as well as the feeding/writing of data to the database.

We’ll need to import SQLAlchemy's `sessionmaker` function to bind to the database (create that connection), as well as import our models.

```python
from sqlalchemy.orm import sessionmaker
from models import Deals, db_connect, create_deals_table


class LivingSocialPipeline(object):
    """Livingsocial pipeline for storing scraped items in the database"""
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_deals_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save deals in the database.

        This method is called for every item pipeline component.

        """
        session = self.Session()
        deal = Deals(**item)

        try:
            session.add(deal)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
```

Here, we create a class, `LivingSocialPipeline()`.  We have a constructor function, `def __init__(self)` to initialize the class by defining the engine, the deals table, and binding/connecting to the database with the defined engine.

We then define `process_item()` that takes the parameters, `item` and `spider`. We establish a session with the database, then unpack an item (the data of one scraped deal) within our `Deal()` model.  We then add the `deal` to our database by calling `session.add()` – on this step, it’s not saved into the database - it’s still on SQLAlchemy level. Then, by calling `session.commit()`, it will put the into the database and the transaction will be committed.

However, if something went wrong during the `save()` and `commit()` portion of the database transaction, we will need to “undo” or `rollback()` the data that was committed since we do not want partial data in our database. The `commit()` and `rollback()` pair is meant to ensure that we have made **all** the changes or **none** if there was any sort of failure during the transaction.

In Python, we do this with a `try` and `except` clause. A `try` and `except` clause allows us to “catch” any errors if our desired operation fails.

We use the `finally` keyword to close the session – this basically means that whether or not we were successful in committing data, close the session/connection with the database.

### Return to settings.py

Nearly there – we need to add a variable to `settings.py` that tells scrapy where to find our pipeline when processing data.

So within `settings.py`, add another variable, `ITEM_PIPELINES`:

```python
ITEM_PIPELINES = {'scraper_app.pipelines.LivingSocialPipeline': 1}
```

This variable defines the classes that will be used for pipelining. The integer value assigned to a particular class determine the order they are run in - items go through pipelines from order number low to high.

[Part 5 puts the project all together &rarr;]( {{ get_url("/scrape/part-5/")}})