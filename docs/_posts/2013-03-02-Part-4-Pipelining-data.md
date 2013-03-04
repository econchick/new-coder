---
layout: post.html
title: "Part 4: Pipelining Data to Database"
tags: [scrape]
---

Pipelining our scraped data into our Postgres database.

**TODO** add commit/rollback intro

### Setup our Pipeline

We've setup our spider to crawl and parse the HTML, and we've set up our database to take the parse data. Now we have to connect the two together through a pipeline.

In `pipelines.py`, we will define a session (the actual connecting to the database), as well as the feeding/writing of data to the database.

We'll need to import SQLAlchemy's `sessionmaker` function to bind to the database (create that connection), as well as import our models.

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

    def save_item(self, item, spider):
        """
        Save deals in the database.
        This method is called for every item pipeline component.
        """
        session = self.Session()
        deal = Deals(**item)
        session.add(deal)
        session.commit()
        return item
```

Here, we create a class, `LivingSocialPipeline()`.  We have a constructor function, `def __init__(self)` to initialize the class by defining the engine, the deals table, and binding/connecting to the database with the defined engine.

We then define `save_item()` that takes the parameters, `item` and `spider`. We establish a session with the database, then unpack an item (the data of one scraped deal) within our `Deal()` model.  We then add the `deal` to our database by calling `session.add()` – this is the actual writing to the database with our information.

Finally, we commit the the transaction (a transaction here would be the act of writing to the database). The reason why we have to commit after adding data is 

**TODO** Do we need to `return item`?

### Return to settings.py

Nearly there – we need to add a variable to `settings.py` that tells scrapy where to find our pipeline when processing data.

So within `settings.py`, add another variable, `ITEM_PIPELINES`:

```python
ITEM_PIPELINES = ['living_social.pipelines.LivingSocialPipeline']
```

This is the directory/module path to the pipeline we just defined.

[Part 5 puts the project all together &rarr;]( {{ get_url('Part-5-Running-our-scraper')}})