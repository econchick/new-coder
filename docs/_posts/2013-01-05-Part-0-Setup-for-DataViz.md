---
layout: post.html
title: "Part 0: Setup"
tags: [DataViz]
---

Initial setup for our Data Visualization Tutorial.

### Initial Requirements:
* [Python 2.x](http://www.python.org/download/releases/2.7.3/)
* [git](http://git-scm.com/downloads)
* A C compiler: [GCC](http://gcc.gnu.org/) or [clang](http://clang.llvm.org/) – the numpy library has some C extensions, which will need to be compiled.
	* To test if you have either GCC or clang, type `$ gcc` or `$ clang` into your terminal. If you get an error that says “command not found” then follow the install instructions for your OS:
		* Mac: 
			* You will need [XCode](http://developer.apple.com/xcode). Once you have XCode on your machine, you will need to navigate to **Preferences** –> **Downloads** –> and select **Command Line Tools** to download & install.
		* Fedora: `sudo yum install gcc python-devel`
		* Ubuntu: `sudo apt-get install build-essential python-dev` – you may need to run `sudo apt-get update` first.
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
Within your terminal

* To get to your “Home” directory:

```bash
$ cd
```
* To create a new `Projects` folder and move to that directory. You can name it whatever you want, just remember what you named it, and where it is:

```bash
$ mkdir Projects && cd Projects
```
* Clone the New Coder project into the directory you’re currently in, which is `Projects` (unless you named it something else):

```bash
$ git clone https://github.com/econchick/new-coder.git
```
* Change into the Data Viz project:

```bash
$ cd new-coder/dataviz
```
* Make sure you’ve installed [virtualenvwrapper](http://pypi.python.org/pypi/virtualenvwrapper) and followed the steps above from Initial Requirements to set up your terminal correctly.  More information can be find at virtualenvwrapper’s [docs](http://virtualenvwrapper.readthedocs.org/en/latest/).
* To make a virtual environment specific to your Data Viz project, run the following command. You should see `(DataVizProject)` before your prompt.

```bash
$ mkvirtualenv DataVizProj
(DataVizProj)$
```
* Now we will install the package requirements for this project. Your virtual environment will store the required packages in a self-contained area to not mess up with other Python projects.

```bash
(DataVizProject) $ pip install -r requirements.txt
```
* **NOTE** Sometimes, NumPy is finicky. If the previous step returns errors, try:

```bash
(DataVizProj)$ pip install numpy
(DataVizProj)$ pip install matplotlib
```
* Test the installation real quick by starting up the Python interpreter:

```bash
(DataVizProj)$ python
>>> import numpy
>>> import matplotlib
```
* If you have no errors (you would just see the `>>>` prompt), then you’re good to go. You can close out of the Python interpreter by pressing `CTRL+D`. If you do have errors, I’d try downloading [numpy](http://scipy.org/Download) and [matplotlib](http://matplotlib.org/downloads.html) manually.


[Continue on to Part 1: Parsing our Data &rarr;]( {{ get_url("Part-1-Parse/")}})