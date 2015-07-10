# Setting up your Mac OS X

<p style="text-align:center">All the needed dependencies for setting up your machine for these tutorials.</p>


## Overview of requirements

The installation will depend on your operating system, but overall, you will need:

* Python 2.x – there are plans to update/include Python 3.x
* git
* A C compiler
* pip
* virtualenv
* virtualenvwrapper
* text editor of your choice 

## Installation

<h5 style="text-align:center"><span style="color:#8c8c8c">Python</span></h5>
Macs come with Python pre-installed.  To check, open up the Terminal application, then type `python`:

```bash
$ python
Python 2.7.2 (default, Jun 20 2012, 16:23:33)
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Python.org\[1] has a good Python on the Mac\[2] page if the above does not work for you.

<h5 style="text-align:center"><span style="color:#8c8c8c">git</span></h5>
You will need to install git\[3] on your machine through their download page\[4]. You can then follow the Save your Progress\[5] page to set it up.

<h5 style="text-align:center"><span style="color:#8c8c8c">C compiler</span></h5>

To test if you have either GCC or clang, type `$ gcc` or `$ clang` into your terminal. If you get an error that says “command not found” then follow the install instructions:

You will need the XCode\[6] application. Once you have XCode on your machine, you will need to navigate to Preferences &rarr; Downloads, then select **Command Line Tools** to download & install (this may take a while, get some coffee, go take a shower). 

This gives you the GCC\[7] or the GNU Compiler Collection. To test installation, within the Terminal application, type `gcc` and you should get the following:

```bash
$ gcc
i686-apple-darwin11-llvm-gcc-4.2: no input files
```

<h5 style="text-align:center"><span style="color:#8c8c8c">pip</span></h5>

pip\[8], stands for “python install python”, is a tool for installing and managing Python packages. Within your Terminal application, use the following commands (ignore the leading `$` as that is your terminal prompt) for downloading & installing. It may prompt you for your computer login password.

```bash
$ curl https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py | sudo python
$ pip
Usage: pip COMMAND [OPTIONS]
You must give a command (use "pip help" to see a list of commands)
$ sudo pip install --upgrade setuptools
```

<h5 style="text-align:center"><span style="color:#8c8c8c">virtualenv & virtualenvwrapper</span></h5>

virtualenv\[9] creates isolated environments for each of your Python projects. It helps to solve version & dependency problems with multiple Python installations and/or multiple versions of different Python packages.  We’ll use `pip` to install it:

```bash
$ sudo pip install virtualenv
```

virtualenvwrapper\[10] is a great (but not required) tool for using virtualenv by simplifying the commands that virtualenv needs.  We’ll use `pip` again to install it:

```bash
$ sudo pip install virtualenvwrapper
$ export WORKON_HOME=~/Envs
$ mkdir -p $WORKON_HOME
$ source /usr/local/bin/virtualenvwrapper.sh
```

## Text Editor

If you already have a text editor that you like to use, great! 

If not, I would suggest grabbing Sublime Text 2\[11].  It’s free, and very user-friendly, especially for the beginner.

Now continue on to “Test your setup”.


