---
layout: post.html
title: "Part 0: Setup for APIs"
tags: [api]
url: "/api/part-0/"
---

Setting up our environment for the API tutorial.

### Setup

**IMPORTANT**: Please be sure to work through the [machine setup]({{ get_url("/begin/setup-your-machine")}}) before proceeding.

Within your terminal:

* Change into the APIs project:

```bash
$ cd new-coder/apis
```
* Make sure you’ve installed [virtualenvwrapper](http://pypi.python.org/pypi/virtualenvwrapper) and followed the steps above from Initial Requirements above to set up your terminal correctly.  More information can be find at virtualenvwrapper’s [docs](http://virtualenvwrapper.readthedocs.org/en/latest/).
* Make a virtual environment specific to your API project project:

```bash
$ mkvirtualenv APIProj
```
* You should see `(APIProj)` before your prompt. Now install package requirements with the following command for this project.

```bash
(APIProj) $ pip install -r requirements.txt
```
* Your virtual environment will store the required packages in a self-contained area to not mess up with other Python projects.

[Continue on to Part 1: Setup Raw Data &rarr;]( {{ get_url("/api/part-1/")}})