---
title: "Introduction to the Data Visualization Tutorial"
layout: post.html
tags: [dataviz, file I/O, import, data structures, docstrings, iterators, generators, licensing, shell, packages]
url: "/dataviz/intro/"
---

Data visualization is quite fun. Perhaps when you think of data visualization, you think of ugly Microsoft Excel spreadsheets with half-a$$ed graphs.

This tutorial is meant to push you out of the Excel mindset just a little bit, and introduce you to the popular Python library, [matplotlib](http://matplotlib.org/). 

### The Project

The project we will create takes the sample data from the repository that you will download (a.k.a. clone) in [Part 0: Setup]( {{ get_url("Part-0-Setup-for-DataViz")}}), parse the sample data from columns and rows to a list of dictionaries, then render that data in two different graphs and in [Google Maps](http://maps.google.com).

The sample data that is included is a snapshot of public crime filings from the San Francisco police. Once you’ve gone through this tutorial, feel free to find other data that interests you, and rework our visualization functions.

### Goals

Understand how to:

* run a Python file from the command line
* import a Python file
* take a raw file and parse its data with Python’s data structures
* make a simple graph
* produce a Google Maps-readable file

What else you will be exposed to:

* Importing Python’s standard library as well as your own module
* Installing and importing third party packages
* Licensing & copyrights when using third-party packages
* File Input/Output
* Counter data structure from the `collections` module
* Global variables, docstrings, list comprehensions
* Python’s interactive shell in the terminal
* Iterators versus Generators

### Intro to NumPy and matplotlib

[NumPy](http://www.numpy.org/) (pronounced num-pie) is a popular scientific library for Python that gives a developer, academic, or scientist tools to work with high-level mathematical functions as well as multi-dimensional arrays and matrices. 

We won't be using much of NumPy, but it is required that we install this library before we can install and use `matplotlib`.

[matplotlib](http://matplotlib.org/) is another popular scientific library that gives the developer tools to produce 2D figures. No longer do you need your [TI-89](http://www.amazon.com/Texas-Instruments-Titanium-Calculator-Packaging/dp/B0001EMLZ2) calculator where you must punch in long lines of formulas, waiting precious seconds for it to render a graph that may be too zoomed in to realize you are missing an important axis point. Packed with detailed [examples](http://matplotlib.org/examples/index.html), you are able to make publication/presentation-quality graphs from the comfort of your keyboard.

### Intro to Google Mapping

It’d be kind of cool to place all the coordinates in our data on a map, wouldn’t it?  Google Maps allows folks to upload KML-type documents, which is essentially a type of an XML document for displaying geographic-related data.  

Google has a great KML [intro](https://developers.google.com/kml/documentation/) and [tutorial](https://developers.google.com/kml/documentation/kml_tut) for those interested. 

Wikipedia has a pretty readable [explanation](http://en.wikipedia.org/wiki/XML) of XML, and w3 has a simple [tutorial](http://www.w3schools.com/xml/) if you want to learn more (_side comment_: w3 is not the greatest for learning front-end related web development, but fine for quick references). 

Both KML and XML, as well as HTML and XHTML, follow the [DOM](http://en.wikipedia.org/wiki/Document_Object_Model) convention, Document Object Model. It’s basically how you interact with different objects through defined functions.

As you are starting to realize the awesomeness of Python, you can assume there is an `xml` module in the standard library. How convenient!  Python’s `xml.dom` module uses the DOM convention and gives us access to functions that HTML, XML, and KML will understand when we build our own KML document.

For the record, do not use Python’s `xml` library in production code until the core developers have implemented security fixes. For information, you can read [here](http://blog.python.org/2013/02/announcing-defusedxml-fixes-for-xml.html).

[Continue on to the Setup for DataViz &rarr;]( {{ get_url("Part-0-Setup-for-DataViz/")}})