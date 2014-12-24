---
layout: post.html
title: "Part 1: Setup Raw Data"
tags: [api]
url: "/api/part-1/"
---

A walkthrough of grabbing raw data from publicly available information.

Let’s first think about the organization of how we want this script to run. We’ll have a `main` function again like we did in the previous tutorial. We’ll also have helper functions and classes defined outside of the `main` function. But for the actual logic of grabbing CPI and game platform data, parsing, validating, plotting, and saving as a file will be in our main function.

First let’s build some scaffolding:

```python
def main():
    """This function handles the actual logic of this script."""

    # Grab CPI/Inflation data.

    # Grab API/game platform data.

    # Figure out the current price of each platform.
    # This will require looping through each game platform we received, and 
    # calculate the adjusted price based on the CPI data we also received.
    # During this point, we should also validate our data so we do not skew
    # our results.

    # Generate a plot/bar graph for the adjusted price data.

    # Generate a CSV file to save for the adjusted price data.
```

Doesn’t seem _too_ bad; we’ve laid out what we want our script to do. Now let’s tackle each comment/process one at a time.  

Before we start off with CPI data, let’s look at our first import statement:

```python
from __future__ import print_function
```
You might be curious as to why we’re importing a `print_function`, and why it’s from `__future__`.  This is a gentle introduction to the differences between Python 2.x and Python 3.x.  In Python 3, `print()` is a function, while in Python 2, `print` is a keyword. For now, the difference is just that using `print` now requires paretheses around what you are printing.

### CPI data

First, we’ll grab the CPI data from the FRED.  This is where we’ll use the `requests` library:

```python
import requests
```

And we’ll be grabbing data from a specific URL, so let’s create a global variable first:

```python
CPI_DATA_URL = 'http://research.stlouisfed.org/fred2/data/CPIAUCSL.txt'
```

Next, we should create a CPI class to initialize the CPI data, load data from the URL, load data from a file, and get the adapted price.

#### For the curious

In Python, a class is just another object. It allows us to create a blueprint to create another object: instances. It also allows us to group like-things together. For example

```python
class Human(object):
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
    def get_sleep_time(self):
        return "8 hours"
```
So every new human that we make from `Human` can have a name, birthday, and has a method to return hours of sleep:

```python
>>> bob = Human(name="bob", birthday="Jan 15th, 1967")
>>> bob.name
'bob'
>>> bob.birthday
'Jan 15th, 1967'
>>> bob.get_sleep_time()
'8 hours'
```
It wouldn’t make sense if we included a method that returned the value of how many eggs we laid (should probably go in a `Fowl` class).

Classes also give us the ability to inherit from other classes, like so:

```python
class Superwoman(Human):
    def get_sleep_time(self):
        return None
```
`Superwoman` still has ‘access’ to the constructor that we defined in `Human`, `__init__()`, but we redefined the `get_sleep_time()` function:

```python
>>> jill = Superwoman("Jill", "Oct 8th, 1972")
>>> jill.name
'Jill'
>>> jill.birthday
'Oct 8th, 1972'
>>> jill.get_sleep_time()
>>>
```
We explore inheritance a bit more in our next tutorial, [Web Scraping]({{ get_url('scrape')}}).

#### Back to the tutorial

The scaffolding for our `class CPIData` will include a constructor method, the `__init__` method, as well as methods to load data from a URL, load data from a file, and return adjusted prices for when we want to compare platform prices between different years:

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

    def get_adjusted_price(self, price, year, current_year=None):
        """Returns the adapted price from a given year compared to what current
        year has been specified.

        """
```

We first initialize our `CPIData` class with `year_cpi`, `last_year`, and `first_year`, as these are all common attributes for a piece of CPI data.

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

#### For the curious
You might be wondering what methods that are surrounded with double underscores are in Python, specifically methods like `__init__()`. These are called **magic methods** or **dunders**, but there is nothing magical about them. 

When we write a class, `MyClass`, and later instantiate that class with `x = MyClass()`, what Python is doing under the hood is calling `x.__init__()` to initialize that class. If you want the informal representation of a string, you would call `str(x)` and Python does `x.__str__()`.

There are many magic methods that are just given to a class: `__init__`, `__str__`, `__repr__`, `__dir__`, etc, and you can **overwrite** them, which is what we did above with our `def __init__(self)` method. We want to give additional initialized parameters for every time we instantiate a new `CPIData` class.

[Dive into Python](http://getpython3.com/diveintopython3/special-method-names.html) has a handy little tool to learn more about these methods; [Rafe Kettler](http://www.rafekettler.com/magicmethods.html) wrote up a nice series of blogs about what each one does.

#### Back to the tutorial

Next, we define a function that will take in a url, and where/what to save our output file as.  Comments are inline to help you walk through:

```python
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

After we’ve grabbed the data from the URL, we then pass it to our function, `load_from_file()`.  Comments inline:

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
        # to make the data easier to use.
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

For the last portion of our `class CPIData`, we need to define a method to return the CPI price from a specific year when needed.

```python
def get_adjusted_price(self, price, year, current_year=None):
    """Returns the price of a purchased item from a given year compared to 
    what current year has been specified.

    This essentially is the calculated inflation for an item.

    """
    # Currently there is no CPI data for 2014
    if current_year is None or current_year > 2013:
        current_year = 2013
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

In review, we’ve essentially defined the container, our `CPIData` class, to handle the the processing of our CPI data.  We initialize each field for a piece of CPI data in `__init__`, we define how to load data from a given URL (of which we define as a global variable, `CPI_DATA_URL` before we defined our class), we define how to load and parse that data that we just grabbed from the URL and saved, and lastly, we define a method to grab the price for a given year (adjusted if we didn’t grab that specific year from the FRED earlier).

[Continue on to the Game API &rarr;]( {{ get_url("/api/part-2/")}})