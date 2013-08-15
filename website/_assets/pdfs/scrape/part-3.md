---
layout: post.html
title: "Part 3: Setting up SQLAlchemy"
tags: [scrape]
url: "/scrape/part-3/"
---

Setting up our data models using SQLAlchemy.

### Create a Database

Our initial step needs to create the database that we plan to use to save all of our crawled data.

To do that, we will start a Postgres shell on localhost:

```bash
(ScrapProj)$ psql -h localhost
psql (9.1.4, server 9.1.3)
Type "help" for help.

newcoder=#
```
The `newcoder=#` is the PostGres prompt. We simply create a database with this command:

```psql
newcoder=# create database scrape;
```

Notice I had to include the semicolon there.  This is pretty much all the raw SQL code we're going to touch. If you are curious, you can learn more on how to interact with PostGres in their [docs][1]<sup>1</sup>.

### Settings.py

Our `settings.py` file only has 5 variables defined (pop quiz: these variables are all caps, do you remember why? Refer to the Data Viz tutorial for a refresher).

When walking through the scrapy [tutorial][2]<sup>2</sup> on your own, it creates a `settings.py` file for you with a few variables that you should define.

Our `settings.py` file is simply a list of global variables specific to our project so we can import our settings later.

We first give our web scraper a name, and where our spider module is located.


```python

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['living_social.spiders']
```
We then define our database through a dictionary:

```python
DATABASE = {'drivername': 'postgres',
            'host': 'localhost',
            'port': '5432',
            'username': 'lynnroot',
            'password': 'root',
            'database': 'scrape'}
```

The `drivername` is the type of database we're using – Postgres.  Since we're using Postgres that we installed on our own computer, the location, or the `host` is `localhost`.  The port is the default port that Postgres listens on.

The `username` is _your_ username for your machine.  The `password` may not be needed, or may be the password used when setting up Postgres initially.

The `database` is the name of the database we created earlier, `newcoder=#  create database scrape;`.

We will return to our `settings.py` file to add a fifth variable, `ITEM_PIPELINES`, once we setup our pipelines (how we handle the scraped & parsed data – e.g. we save them to the database).

### Models.py

We'll now setup our database models using SQLAlchemy as our ORM.

First, we'll define a function to actually connect to the database.  For this, we'll need to import SQLAlchemy as well as our `settings.py` file:

```python
from sqlalchemy import *
from sqlalchemy.engine.url import URL

import settings

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))
```

A few things I want to point out with this example. First, the `from sqlalchemy import *` line. The `import *` literally imports everything into our `models.py` file. This is typically not good; it can sacrifice performance, and is also unclear to whomever reads your code later.  We specifically want the `create_engine()` function from `sqlalchemy`, and if we just `import *`, it is difficult to initially see that `create_engine()` is defined in and imported from `sqlalchemy`.

Let’s be better developers and change our import statement to `from sqlalchemy import create_engine`. Here, we avoid importing everything from the `sqlalchemy` package, and we are more explicit with what we are using from `sqlalchemy`.

We make a general `import settings` statement – it does not import every item in `settings.py`, but it gives us access to any item we want by later using `settings.DATABASE`.  You can think of the difference between `import settings` versus `from sqlalchemy import *` as "take the basket" versus "take everything out of the basket."

Last item I want to point out before we move on is the usage of the double astricks within the `URL()` function: `**settings.DATABASE`. First, we are accessing the `DATABASE` variable within `settings.py`. The `**` actually unpacks all the values within the `DATABASE` dictionary.  The `URL` function, a constructor defined within SQLAlchemy, will map keys and values to a URL that SQLAlchemy can understand to make a connection to our database.

So first, our dictionary looks like:

```python
DATABASE = {'drivername': 'postgres',
            'host': 'localhost',
            'port': '5432',
            'username': 'lynnroot',
            'password': 'root',
            'database': 'scrape'}
```

Then, the `URL()` function will parse out the elements, and create the following URL for the `create_engine()` function to read:

```python
'postgresql://lynnroot:root@localhost:5432/scrape'
```

Now `create_engine()` can read that URL to eventually make a connection to our database.

Next, we create the table for our ORM. We have to import `declarative_base()` from SQLAlchemy in order to map a class that defines our table structure to Postgres, as well as a function that will take our metadata of our table to create the table(s) we need.

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings


DeclarativeBase = declarative_base()

# <--snip-->

def create_deals_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)
```

Last, we define our actual table by inheriting from `DeclarativeBase` and setting up how we want to define each field we want to collect.  We also have to import a few more things from SQLAlchemy:

```python
from sqlalchemy import create_engine, Column, Integer, String

# <--snip-->

class Deals(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "deals"

    id = Column(Integer, primary_key=True)
    title = Column('title', String)
    description = Column('description', String, nullable=True)
    link = Column('link', String, nullable=True)
    location = Column('location', String, nullable=True)
    category = Column('category', String, nullable=True)
    original_price = Column('original_price', String, nullable=True)
    price = Column('price', String, nullable=True)
```

We give our class a table name, “deals”, as well as 8 fields. Each field will be mapped to a column in our table which it's created through `create_deals_table()`.

For each field, we define the type of field that it is, `Integer` for our primary key field, and the rest are `String`s. We pass in the label of the column as a string for everything but the `id` field. Last, for most fields, we allow them to be empty (`nullable=True`) if we don't have those fields in the deal data that we collect.

All together:

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings


DeclarativeBase = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))


def create_deals_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)


class Deals(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "deals"

    id = Column(Integer, primary_key=True)
    title = Column('title', String)
    description = Column('description', String, nullable=True)
    link = Column('link', String, nullable=True)
    location = Column('location', String, nullable=True)
    category = Column('category', String, nullable=True)
    original_price = Column('original_price', String, nullable=True)
    price = Column('price', String, nullable=True)
```

[Part 4 will wrap up with how we pipeline our scraped data to save to our database &rarr;][3]<sup>3</sup>

[1]: http://www.postgresql.org/docs/9.2/static/index.html
[2]: http://doc.scrapy.org/en/0.16/intro/tutorial.html#creating-a-project
[3]: http://newcoder.io/scrape/part-4/