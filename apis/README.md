## APIs

### Project

Video games have always been a pricy hobby. With the next generation of consoles
just being announced (or about to be) it makes sense to look at how pricing
has changed on that front over time.

To this end we will write a simple script that fetches video game platform
information from [Giantbomb.com][gb], combine that with CPI information made
available by the [Federal Reserve Bank of St. Louis][fred] ([http://research.stlouisfed.org/fred2/data/CPIAUCSL.txt](http://research.stlouisfed.org/fred2/data/CPIAUCSL.txt)) to adapt the value
of the US dollar over time (this calculation is not meant to be accurate but it
provides a nice example of working with diverse datasets) and generate a bar 
chart and a CSV file displaying the price development.

During the course of this tutorial you will also get to know some non-core
Python libraries: [requests][requests] for making interactions with HTTP
much more easier, [matplotlib][matplotlib] for generating graphs and charts
of various kinds and [tablib][tablib] for easily generating CSV datasets.

### Requirements

As mentioned above, we will also use matplotlib here to generate a nice
bar chart. matplotlib requires numpy which, sadly, requires some extra
hoops to jump through to get them both installed. So before installing
matplotlib simply make sure, that you've installed numpy first. To do that
simply run ``pip install numpy==1.7.0`` followed by your usual
``pip install -r requirements.txt``.


### How to run

    python platform_pricing.py\
        --giantbomb-api-key=<your_key>\
        --plot-file=output.png\
        --csv-file=output.csv --limit=20

### General advice

Especially when working with multiple components and libraries, try to divide
your problem-space into as many small chunks as possible. For scripts like this
I usually at first write a small main-function that contains tons of calls
to other (not-yet-existing) functions and methods that match what the script's
supposed to do on a very high level.

When working with APIs that might easily change in the future and you don't
necessarily get notified about (like a classic web API that doesn't provide
multiple versions of itself to allow for backwards-compatibility) it is
generally a good idea to wrap the provided functionality. This way if something
changes, you only have to change your own API wrapper but not the code that
uses it.

[fred]: http://research.stlouisfed.org/fred2/
[gb]: http://www.giantbomb.com/api/
[requests]: http://docs.python-requests.org/en/latest/
[matplotlib]: http://matplotlib.org/
[tablib]: http://docs.python-tablib.org/en/latest/
