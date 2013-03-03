---
layout: post.html
title: "Part 0: Setup for APIs"
tags: [api]
---

Setting up our environment for the API tutorial.

### Initial Requirements:
* [Python 2.x](http://www.python.org/download/releases/2.7.3/)
* [virtualenv](http://pypi.python.org/pypi/virtualenv) You can either download directly, or:
	* Mac: ` $ sudo easy_install virtualenv`
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

* `$ cd new-coder/apis` to change into the APIs project.
* Make sure you've installed [virtualenv-wrapper](http://pypi.python.org/pypi/virtualenvwrapper) and followed the steps above from [Initial Requirements](#initial-requirements) to set up your Terminal correctly.  More information can be find at virtualenv-wrapper's [docs](http://virtualenvwrapper.readthedocs.org/en/latest/).
* `$ mkvirtualenv APIProj` Make a virtual environment specific to your Data Viz project. You should see (APIProj) before your prompt, now.
* `(APIProj) $ pip install -r requirements.txt` Now installing package requirements for this project. Your virtual environment will store the required packages in a self-contained area to not mess up with other Python projects.

[Continue on to Part 1: Setup Raw Data &rarr;]( {{ get_url("Part-1-Setup-raw-data/")}})