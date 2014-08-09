# Setting up your Linux machine

<p style="text-align:center">All the needed dependencies for setting up your machine for these tutorials.</p>


## Overview of requirements

The installation will depend on your operating system, but overall, you will need:

* Python 2.x – there are plans to update/include Python 3.x
* git
* A C compiler
* pip
* virtualenv
* virtualenvwrapper

## Installation

<h5 style="text-align:center"><span style="color:#8c8c8c">Python</span></h5>
Linux machines come with Python pre-installed.  To check, open up the Terminal application, then type `python`:

```bash
$ python
Python 2.7.3 (default, Aug  9 2012, 17:23:57)
[GCC 4.7.1 20120720 (Red Hat 4.7.1-5)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

<h5 style="text-align:center"><span style="color:#8c8c8c">git</span></h5>
You will need to install git\[12] either from commands below or through their download page\[13]. You can then follow the Save your Progress\[14] page to set it up.

* Fedora: `sudo yum git`
* Ubuntu: `sudo apt-get install git`


<h5 style="text-align:center"><span style="color:#8c8c8c">C Compiler</span></h5>

A C compiler, either GCC or clang, is needed because the `numpy` library we are using has some C extensions, which will need to be compiled.  

To test if you have either GCC or clang, type `$ gcc` or `$ clang` into your terminal. If you get an error that says “command not found” then follow the install instructions:

* Fedora: 
	* `sudo yum groupinstall "Developer Tools"`
	* `sudo yum install python-devel`
* Ubuntu: 
	* you may need to run `sudo apt-get update` first.
	* `sudo apt-get install build-essential python-dev`

This gives you the GCC\[15] or the GNU Compiler Collection. To test installation, within the Terminal application, type `gcc` and you should get something like the following:

```bash
$ gcc
gcc: fatal error: no input files
compilation terminated.
```

<h5 style="text-align:center"><span style="color:#8c8c8c">pip</span></h5>

pip\[16], stands for “python install python”, is a tool for installing and managing Python packages. Within your Terminal application, use the following commands (ignore the leading `$` as that is your terminal prompt) for downloading & installing. It may prompt you for your computer login password.

```bash
$ curl https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py | sudo python
$ pip
Usage: pip COMMAND [OPTIONS]
You must give a command (use "pip help" to see a list of commands)
$ sudo pip install --upgrade setuptools
```

<h5 style="text-align:center"><span style="color:#8c8c8c">virtualenv & virtualenvwrapper</span></h5>

virtualenv\[17] creates isolated environments for each of your Python projects. It helps to solve version & dependency problems with multple Python installations and/or multiple versions of different Python packages.  We’ll use `pip` to install it:

```bash
$ sudo pip install virtualenv
```

virtualenvwrapper\[18] is a great (but not required) tool for using virtualenv by simplifying the commands that virtualenv needs.  We’ll use `pip` again to install it:

```bash
$ sudo pip install virtualenvwrapper
$ export WORKON_HOME=~/Envs
$ mkdir -p $WORKON_HOME
$ source /usr/local/bin/virtualenvwrapper.sh
```

## Text Editor

If you already have a text editor that you like to use, great! 

If not, I would suggest grabbing Sublime Text 2\[19].  It’s free, and very user-friendly, especially for the beginner.

Now continue on to “Test your setup”.

Now continue on to “Test your setup”.

