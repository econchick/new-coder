---
layout: post.html
title: "Part 0: Setup for APIs"
tags: [api]
---

Setting up our environment for the API tutorial.

### Initial Requirements:
* [Python 2.x](http://www.python.org/download/releases/2.7.3/)
* [virtualenv](http://pypi.python.org/pypi/virtualenv) You can either download directly, or:
	* Mac: `$ sudo easy_install virtualenv`
	* Ubuntu: `$ sudo apt-get virtualenv`
	* Fedora: `$ sudo yum install python-virtualenv`
	* Windows: [Download manually](http://pypi.python.org/pypi/virtualenv)
* [virtualenvwrapper](http://pypi.python.org/pypi/virtualenvwrapper) You can either download it directly, or:
	* Mac: `$ sudo easy_install virtualenvwrapper`
	* Ubuntu: `$ sudo apt-get virtualenvwrapper`
	* Fedora: `$ sudo yum install python-virtualenvwrapper`
	* For Mac, Ubuntu, and Fedora:
		* `$ export WORKON_HOME=~/Envs`
		* `$ mkdir -p $WORKON_HOME`
		* `$ source /usr/local/bin/virtualenvwrapper.sh`
	* Windows: [Download manually](http://pypi.python.org/pypi/virtualenvwrapper) and follow install instructions

### Setup
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

[Continue on to Part 1: Setup Raw Data &rarr;]( {{ get_url("Part-1-Setup-raw-data/")}})