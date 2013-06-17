---
layout: post.html
title: "Part 0: Setup"
tags: [Network]
url: "/~drafts/networks/part-0/"
---

Initial setup for our Network/IRC Bot Tutorial.

### Setup

**IMPORTANT**: Please be sure to work through the [machine setup][machinesetup] before proceeding.

Within your terminal:

* `$ cd` to get to your 'Home' directory
* If you haven’t already made a `Projects` folder for your new coder projects (or perhaps named it something else), then: `$ mkdir Projects` to create a new 'Projects' folder. You can name it whatever you want, just remember what you named it, and where it is.
* Move into your `Projects` directory (or whatever you named it to): `cd Projects`.
* `$ git clone https://github.com/econchick/new-coder.git` This clones the New Coder project into the directory you're currently in, which is Projects (unless you named it something else).
* `$ cd new-coder/network` Change into the Network tutorial.
* If you have [virtualenv-wrapper](http://pypi.python.org/pypi/virtualenvwrapper) and followed the steps above from [Initial Requirements](#initial-requirements) installed (which you should if you are on **Mac** or **Linux**, follow [machine setup][machinesetup] if not): `$ mkvirtualenv NetworkProj` Make a virtual environment specific to your Data Viz project. You should see (DataVizProject) before your prompt, now.
* If you have **Windows**, within your Python project directory, type:  `virtualenv.py NetworkProj`. A virtual environment called “NetworkProj” will be started.  Now you will need to activate it, type: `NetworkProj\Scripts\activate.bat` and you’ll see something like `(NetworkProj) C:\PythonProjects>`
* `(NetworkProj) $ pip install -r requirements.txt` Now installing package requirements for this project. Your virtual environment will store the required packages in a self-contained area to not mess up with other Python projects.


Now you’re ready to move onto [defining our bot settings &rarr;]( {{ get_url("/~drafts/networks/part-1/")}})


[machinesetup]({{ get_url("/setup-your-machine")}})