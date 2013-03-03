---
layout: post.html
title: "Introduction to the Data Visualization Tutorial"
tags: [intro-dataviz]
---

Data visualization is quite fun. Perhaps when you think of data visualization, you think of ugly Microsoft Excel spreadsheets with half-a$$ed graphs.

This tutorial is meant to push you out of the Excel mindset just a little bit, and introduce you to the popular Python library, [matplotlib](http://matplotlib.org/). 

### The Project

**TODO**

### Goals

**TODO** what should folks expect to learn from this tutorial

### Intro to Numpy and matplotlib

**TODO**

### Intro to Google Mapping

It'd be kind of cool to place all the coordinates in our data on a map, wouldn't it?  Google Maps allows folks to upload KML-type documents, which is essentially a type of an XML document for displaying geographic-related data.  

Google has a great KML [intro](https://developers.google.com/kml/documentation/) and [tutorial](https://developers.google.com/kml/documentation/kml_tut) for those interested. 

Wiki has a pretty readable [explanation](http://en.wikipedia.org/wiki/XML) of XML, and w3 has a simple [tutorial](http://www.w3schools.com/xml/) if you want to learn more (_side comment_: w3 is not the greatest for learning front-end related web development, but fine for quick references). 

Both KML and XML, as well as HTML and XHTML, follow the [DOM](http://en.wikipedia.org/wiki/Document_Object_Model) convention, Document Object Model. It's basically how you interact with different objects through defined functions.

As you are starting to realize the awesomeness of Python, you can assume there is an `xml` module in the standard library. How convenient!  Python's `xml.dom` module uses the DOM convention and gives us access to functions that HTML, XML, and KML will understand when we build our own KML document.

[Continue on to Part 0: Setup for DataViz &rarr;]( {{ get_url("Part-0-Setup-for-DataViz/")}})