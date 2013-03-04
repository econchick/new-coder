---
layout: post.html
title: "Part 1: Setup Raw Data"
tags: [api]
---

A walkthrough of grabbing raw data from publicly available information.

```python
from __future__ import print_function
```

You might be curious as to why we're importing a `print_function`, and why it's from `__future__`.  This is a gentle introduction of the differences between Python 2.x and Python 3.x.  In Python 3, `print()` is a function, while in Python 2, `print` is a keyword. For now, the difference is just that using `print` requires paretheses around what you are printing.

### CPI data

First, we'll grab the CPI data from the FRED.  This is where we'll use the `requests` library:

```python
import requests
```

And we'll be grabbing data from a specific URL, so let's create a global variable first:

```python
CPI_DATA_URL = 'http://research.stlouisfed.org/fred2/data/CPIAUCSL.txt'
```

Next, we should create a CPI class to initialize the CPI data, load data from the URL, load data from a file, and get the adapted price.

# TODO: add intro to classes!

The scaffolding for our `class CPIData()` is as follows:

```python
class CPIData(object):
    """Abstraction of the CPI data provided by FRED. 

    This stores internally only one value per year.

    """

    def __init__(self):
        self.year_cpi = {}
        self.last_year = None
        self.first_year = None

    def load_from_url(self, url, save_as_file=None):
        """Loads data from a given url. 

        The downloaded file can also be saved into a location for later 
        re-use with the "save_as_file" parameter specifying a filename.

        After fetching the file this implementation uses load_from_file
        internally.
        
        """

    def load_from_file(self, fp):
        """Loads CPI data from a given file-like object."""

    def get_adapted_price(self, price, year, current_year=None):
        """Returns the adapted price from a given year compared to what current
        year has been specified.

        """
```

We first initialize our `CPIData` class with `year_cpi`, `last_year`, and `first_year`, as these are all common attributes for a piece of CPI data.

# TODO intro to dunders

```python
def __init__(self):
    # Each year available to the dataset will end up as a simple key-value
    # pair within this dict. We don't really need any order here so going
    # with a plain old dictionary is the best approach.
    self.year_cpi = {}

    # Later on we will also remember the first and the last year we
    # have found in the dataset to handle years prior or after the
    # documented time span.
    self.last_year = None
    self.first_year = None
```

Next, we define a function that will take in a url, and where/what to save our output file as.  Comments are inline to help you walk through:

```
def load_from_url(self, url, save_as_file=None):
    """
    Loads data from a given url. The downloaded file can also be saved
    into a location for later re-use with the "save_as_file" parameter
    specifying a filename.

    After fetching the file this implementation uses load_from_file
    internally.
    """
    # We don't really know how much data we are going to get here, so
    # it is recommended to just keep as little data as possible in memory
    # at all times. Since python-requests supports gzip-compression by
    # default and decoding these chunks on their own isn't that easy,
    # we just disable gzip with the empty "Accept-Encoding" header.
    fp = requests.get(url, stream=True,
                      headers={'Accept-Encoding': None}).raw

    # If we did not pass in a save_as_file parameter, we just return the
    # raw data we got from the previous line.
    if save_as_file is None:
        return self.load_from_file(fp)

    # Else, we write to the desired file.
    else:
        with open(save_as_file, 'wb+') as out:
            while True:
                buffer = fp.read(81920)
                if not buffer:
                    break
                out.write(buffer)
        with open(save_as_file) as fp:
            return self.load_from_file(fp)
```

After we've grabbed the data from the URL, we then pass it to our function, `load_from_file()`.  Comments inline:

```python
def load_from_file(self, fp):
    """
    Loads CPI data from a given file-like object.
    """
    # When iterating over the data file we will need a handful of temporary
    # variables:
    reached_dataset = False
    current_year = None
    year_cpi = []
    for line in fp:
        # The actual content of the file starts with a header line
        # starting with the string "DATE ". Until we reach this line
        # we can skip ahead.
        if not reached_dataset:
            if line.startswith("DATE "):
                reached_dataset = True
            continue

        # Each line ends with a new-line character which we strip here
        # to make the data easier usable.
        data = line.rstrip().split()

        # While we are dealing with calendar data the format is simple
        # enough that we don't really need a full date-parser. All we
        # want is the year which can be extracted by simple string
        # splitting:
        year = int(data[0].split("-")[0])
        cpi = float(data[1])

        if self.first_year is None:
            self.first_year = year
        self.last_year = year

        # The moment we reach a new year, we have to reset the CPI data
        # and calculate the average CPI of the current_year.
        if current_year != year:
            if current_year is not None:
                self.year_cpi[current_year] = sum(year_cpi) / len(year_cpi)
            year_cpi = []
            current_year = year
        year_cpi.append(cpi)

    # We have to do the calculation once again for the last year in the
    # dataset.
    if current_year is not None and current_year not in self.year_cpi:
        self.year_cpi[current_year] = sum(year_cpi) / len(year_cpi)
```

For the last portion of our `class CPIData()`, we need to define a method to return the CPI price from a specific year when needed.

```python
def get_adjusted_price(self, price, year, current_year=None):
    """Returns the price of a purchased item from a given year compared to 
    what current year has been specified.

    This essentially is the calculated inflation for an item.

    """
    if current_year is None:
        current_year = datetime.datetime.now().year
    # If our data range doesn't provide a CPI for the given year, use
    # the edge data.
    if year < self.first_year:
        year = self.first_year
    elif year > self.last_year:
        year = self.last_year

    year_cpi = self.year_cpi[year]
    current_cpi = self.year_cpi[current_year]

    return float(price) / year_cpi * current_cpi
```

In review, we've essentially defined the container, our `CPIData` class, to handle the the processing of our CPI data.  We initialize each field for a piece of CPI data in `__init__`, we define how to load data from a given URL (of which we define as a global variable, `CPI_DATA_URL` before we defined our class), we define how to load and parse that data that we just grabbed from the URL and saved, and lastly, we define a method to grab the price for a given year (adjusted if we didn't grab that specific year from the FRED earlier).

[Continue on to the Game API &rarr;]( {{ get_url("Part-2-Giantbomb-API/")}})