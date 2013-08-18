---
layout: post.html
title: "Part 0: Setup"
tags: [scrape]
url: "/scrape/part-0/"
---

Initial setup of your scraper environment.


### Setup

**IMPORTANT**: Please be sure to work through the [machine setup][1]<sup>1</sup> before proceeding.

Within your terminal:

* Change into the Web Scraping project.

```bash
$ cd new-coder/scrape
```

* Make sure you’ve installed [virtualenvwrapper][2]<sup>2</sup> and followed the steps above from Initial Requirements above to set up your terminal correctly.  More information can be find at virtualenvwrapper’s [docs][3]<sup>3</sup>.
* Make a virtual environment specific to your Scrape project:

```bash
$ mkvirtualenv ScrapeProj
```

* You should see `(ScrapeProj)` before your prompt. Now install package requirements with the following command for this project.

```bash
(ScrapeProj) $ pip install -r requirements.txt
```

* Your virtual environment will store the required packages in a self-contained area to not mess up with other Python projects.

[Continue on to Part 1: Scraper Setup &rarr;][4]<sup>4</sup>

[1]: http://newcoder.io/begin/setup-your-machine
[2]: http://pypi.python.org/pypi/virtualenvwrapper
[3]: http://virtualenvwrapper.readthedocs.org/en/latest/
[4]: http://newcoder.io/scrape/part-1/