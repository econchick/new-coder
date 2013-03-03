---
layout: post.html
title: "Part 2: Writing our Spider"
tags: [scrape]
---

Writing the spider portion of our scraper.

### Defining our spider

**TODO** Module location once directory structure is all setup

This is where the magic happens - this is where we tell scrapy how to find the exact data we're looking for. As you can imagine, writing a spider is specific to a web page. This won't work on Groupon or another website.

We will define one class, `LivingSocialSpider` with common attributes, like `name` and `url`. We'll also define one function within our `LivingSocialSpider` class.

First we'll setup our `LivingSocialSpider` class with attributes (variables that are defined within a class, also referred to as fields).  We'll inherit from scrapy's `BaseSpider`:

```python

from scrapy.spider import BaseSpider

from tutorial.items import LivingSocialDeal

class LivingSOcialSpider(BaseSpider):
	"""Spider for regularly updated livingsocial.com site, New York Page"""
	name = "livingsocial"
	allowed_domains = ["livingsocial.com"]
	start_urls = ["http://www.livingsocial.com/cities/1719-newyork-citywide"]

    deals_list_xpath = '//ul[@class="unstyled cities-items"]/li[@dealid]'
    item_fields = {'title': './/a/div[@class="bd"]/h1/text()',
                   'link': './/a/@href',
                   'description': './/a/div[@class="bd"]/h2/text()',
                   'category': './/@data-categories',
                   'location': './/a/div[@class="hd"]/div[@class="meta"]/span/text()',
                   'original_price': './/a/div[@class="bd"]/p[@class="meta"]/span[@class="original-price"]/del/text()',
                   'price': './/a/div[@class="bd"]/p[@class="meta"]/span[@class="price"]/text()'}
```

I've chosen to not build out the scaffolding with comments, but to throw this at you instead.  Let's walk it through.

The first few variables are self-explanatory: the `name` defines the name of the Spider, the `allowed_domains` list the base-URLs for the allowed domains for the spider to crawl, and the `start_urls` is a list of URLs for the spider to start crawling from.  All subsequent URLs will start from the data that the spider downloads from the `start_urls`.

Next, scrapy uses XPath selectors to extract data from a website - they select certain parts of the HTML data based on a given XPath. As said in [their documentation](http://doc.scrapy.org/en/0.16/topics/selectors.html#topics-selectors), "XPath is a language for selecting nodes in XML documents, which can also be used with HTML." You may read more about XPath selectors in [their docs](http://doc.scrapy.org/en/0.16/topics/selectors.html#topics-selectors).

We basically tell scrapy where to start looking for information based on a defined Xpath.  Let's navigate to our [LivingSocial](http://www.livingsocial.com/cities/1719-newyork-citywide) site and right-click to "View Source":

![View Source of LivingSocial](https://www.dropbox.com/s/nzwav6rat685luy/Screen%20Shot%202013-03-02%20at%2012.53.03%20PM.png)

I mean - look at that mess. We need to give the spider a little guidance.

You see that `deals_list_xpath = '//ul[@class="unstyled cities-items"]/li[@dealid]'` sort of looks like the code we see with HTML.  You can read about how to contruct an XPath and working with relative XPaths in their [docs](http://doc.scrapy.org/en/0.16/topics/selectors.html#working-with-relative-xpaths). But essentially, the `'//ul[@class="unstyled cities-items"]/li[@dealid]'`  is saying: within all `<ul>` elements, if a `<ul class=` is defined as "unstyled cities-items", then go within that `<ul>` element to find `<li>` elements that have a parameter called `dealid`. 

Try it out: within your "View Source" page of the Living Social website, search within the source itself (either pressing CMD+F or CTRL+F within the page) and search for `"unstyled cities-items"` - you will see ![](https://www.dropbox.com/s/vszc7750rffzhjd/Screen%20Shot%202013-03-02%20at%201.03.08%20PM.png) (highlighted with the portion of searched text). Scroll a few lines down to see something like `<li dealid="123456">`. BAM! those are where our deals are specifically located on the web site.

Next – the `item_fields`. This should look similar – it's a dictionary of all of our items we defined in `Items.py` earlier (and imported above), with the associated values as _their_ XPaths, relative to `deals_list_xpath`.  The `.//` before the location means it is relative to `deals_list_xpath`. The Spider would only grab data from those paths if the `deals_list_xpath` preceded it.

Okay – next is the actual `parse()` function.  We have to add a few more import statements from scrapy to make use of XPaths.  Our import statements, including the new ones, are now:

```python
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose

from tutorial.items import LivingSocialDeal
```

We're using the HtmlXPathSelector – this will handle the response of when we request a webpage, and give us the ability to select certain parts of that response, defined by our `deals_list_xpath` field.  For understanding of scrapy's handling of responses, read [what happens under the hood](http://doc.scrapy.org/en/0.16/intro/tutorial.html#what-just-happened-under-the-hood).

We're also using XPathItemLoader to load data into our `item_fields`.

Lastly, we import `Join` and `MapCompose` for processing our data. `MapCompose()` will help the input processing of our data, and will be used to help clean up the data that we extract. The `Join()` will help the output processing of our data, and will join together the elements that we process.  A better explanation for these two functions can be found in their [documentation](http://doc.scrapy.org/en/0.16/topics/loaders.html#scrapy.contrib.loader.processor.Join).

Here's what our `parse()` function looks like:

```python
class LivingSocialSpider(BaseSpider)
"""Spider for regularly updated livingsocial.com site, New York page"""
# snip
    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        # iterate over deals
        for qxs in hxs.select(self.deals_list_xpath):
            loader = XPathItemLoader(LivingSocialDeal(), selector=qxs)

            # define processors
            loader.default_input_processor = MapCompose(unicode.strip)
            loader.default_output_processor = Join()

            # iterate over fields and add xpaths to the loader
            for field, xpath in self.item_fields.iteritems():
                loader.add_xpath(field, xpath)
            yield loader.load_item()
```

We'll go through this line-by-line again.  As an aside, the `parse()` function is actually referred to as a **method**, as it is a method of the `LivingSocialSpider` class.

The `parse()` method takes in one parameter: `response`. Hey, wait – what about this `self` thing – looks like two parameters!

Each instance method (in this case, `parse()` is an instance method) receives a reference to itself as its first argument. It’s conventionally called “self”.  The explicit self allows the coder to do some fun – for example:

```python
>>> class C:
...   def f(self, s):
...     print s
...
>>> c = C()
>>> C.f(c, "Hello!")
Hello!
```
**TODO** For the curious, brief intro to static + class methods (versus instance methods)

The `response` parameter is what the spider gets back in return after making a request to the Living Social site. We are parsing that response with our XPaths.

First, we will instantiate `HtmlXPathSelector()` by giving it the parameter, `response` and assigning it to the variable `selector`.  We'll be able access `HtmlXPathSelector()`'s method, `select()` to grab the exact data we want using the xpaths we defined before.

Now, since there are multiple deals within one page,

```python
for deal in selector.select(self.deals_list_xpath):
```

we'll iterate over each deal we find from the `deals_list_xpath`, and then we load them so we can process the data:

```python
	loader = XPathItemLoader(LivingSocialDeal(), selector=deal)

	# define processors
	loader.default_input_processor = MapCompose(unicode.strip)
	loader.default_output_processor = Join()
```

Here we grab the deal and pass it into XPathItemLoader through the `selector` parameter, along with the `LivingSocialSpider()` class, and assign the `loader` variable.  We then setup the process for deal data first by stripping out white-space of unicode strings, then join the data together. Since we did not define any separater within `Join()`, the data items are just joined by a space, and is helpful for when we have multi-line data.

We then iterate over each key and value of `items_fields` and add a the specific data piece's xpath to the loader.

Finally, with each deal, we process each data parcel by calling `load_item()`, which will grab each item field, 'title', 'link', etc, for each deal, get its xpath, process its data with the input & output processer.  We finally then `yield` each item, then move on to the next deal that we find:

```python

    # iterate over fields and add xpaths to the loader
    for field, xpath in self.item_fields.iteritems():
        loader.add_xpath(field, xpath)
    yield loader.load_item()
```

**For the curious**, the `yield` keyword is similar to `return`. The `parse()` function, specifically the `for deal in selector` bit, we've essentially built a Generator (it will generate data on the fly). StackOverflow has a good [explanation](http://stackoverflow.com/questions/231767/the-python-yield-keyword-explained) of what's happening in our function: The first time the function will run, it will run from the beginning until it hits yield, then it'll return the first value of the loop. Then, each other call will run the loop you have written in the function one more time, and return the next value, until there is no value to return.  The generator is considered empty once the function runs but does not hit yield anymore. It can be because the loop had come to ends, or because you do not satisfy a "if/else" anymore. 

We've now implemented our Spider based off of our Items that we are seeking.

[Part 3 will continue with how we setup our data model for eventual saving into the database &rarr;]( {{ get_url('Part-3-Setting-up-SQLAlchemy')}})