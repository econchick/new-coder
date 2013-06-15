---
layout: post.html
title: "Part 0: Setup"
tags: [Network]
url: "/~drafts/networks/part-0/"
---

Initial setup for our Network/IRC Bot Tutorial.

**TODO**: not reviewed/complete

### Setup

**IMPORTANT**: Please be sure to work through the [machine setup]({{ get_url("/setup-your-machine")}}) before proceeding.

Within your terminal:

* `$ cd` to get to your 'Home' directory
* `$ mkdir Projects && cd Projects` to create a new 'Projects' folder and move to that directory. You can name it whatever you want, just remember what you named it, and where it is.
* `$ git clone https://github.com/econchick/new-coder.git` This clones the New Coder project into the directory you're currently in, which is Projects (unless you named it something else).
* `$ cd new-coder/network` Change into the Data Viz project.
* Make sure you've installed [virtualenv-wrapper](http://pypi.python.org/pypi/virtualenvwrapper) and followed the steps above from [Initial Requirements](#initial-requirements) to set up your Terminal correctly.  More information can be find at virtualenv-wrapper's [docs](http://virtualenvwrapper.readthedocs.org/en/latest/).
* `$ mkvirtualenv NetworkProj` Make a virtual environment specific to your Data Viz project. You should see (DataVizProject) before your prompt, now.
* `(NetworkProject) $ pip install -r requirements.txt` Now installing package requirements for this project. Your virtual environment will store the required packages in a self-contained area to not mess up with other Python projects.


Now you’re ready to move onto [defining our bot settings &rarr;]( {{ get_url("/~drafts/networks/part-1/")}})