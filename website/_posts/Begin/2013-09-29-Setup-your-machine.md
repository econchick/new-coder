---
layout: post.html
title: "Setting up your computer"
tags: [setup, installation, begin]
url: "/begin/setup-your-machine/"
---

All the needed dependencies for setting up your Mac, Linux, or Windows machine for these tutorials.

1. [Overview](#overview-of-requirements)
2. Install:
	* [Mac OS X](#mac-os-x)
	* [Linux](#linux)
	* [Windows](#windows)
3. [Test your setup](#test-your-setup)
4. [Get the Tutorial Code](#get-the-tutorial-code)

## Overview of requirements

The installation will depend on your operating system, but overall, you will need:

* Python 2.x – there are [plans][1] to update/include Python 3.x
* git – an intro given [here]( {{get_url("begin/save-your-progress")}})
* A C compiler
* pip
* virtualenv
* virtualenvwrapper

## Mac OS X

### Python
Macs come with Python pre-installed.  To check, open up the Terminal application (Applications &rarr; Utilities &rarr; Terminal like [so][2]), then type `python`:

```bash
$ python
Python 2.7.2 (default, Jun 20 2012, 16:23:33)
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

[Python.org][3] has a good [Python on the Mac][4] page if the above does not work for you.

### git
You will need to install [git][5] on your machine through their [download page][6]. You can then follow the [Save your Progress]({{ get_url("begin/save-your-progress")}}) page to set it up.

### C compiler


You will need the [XCode](http://developer.apple.com/xcode) application. Once you have XCode on your machine, you will need to navigate to Preferences &rarr; Downloads, then select **Command Line Tools** to download & install (this may take a while, get some coffee, go take a shower).

This gives you the [GCC][7] or the GNU Compiler Collection. To test installation, within the Terminal application, type `gcc` and you should get the following:

```bash
$ gcc
i686-apple-darwin11-llvm-gcc-4.2: no input files
```

### pip

[pip][9], stands for “python install python”, is a tool for installing and managing Python packages. Within your Terminal application, use the following commands (ignore the leading `$` as that is your terminal prompt) for downloading & installing. It may prompt you for your computer login password.

```bash
$ curl https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py | sudo python
$ pip
Usage: pip COMMAND [OPTIONS]
You must give a command (use "pip help" to see a list of commands)
$ sudo pip install --upgrade setuptools
```

### virtualenv & virtualenvwrapper

[virtualenv][10] creates isolated environments for each of your Python projects. It helps to solve version & dependency problems with multple Python installations and/or multiple versions of different Python packages.  We’ll use `pip` to install it:

```bash
$ sudo pip install virtualenv
```

[virtualenvwrapper][11] is a great (but not required) tool for using virtualenv by simplifying the commands that virtualenv needs.  We’ll use `pip` again to install it:

```bash
$ sudo pip install virtualenvwrapper
$ export WORKON_HOME=~/Envs
$ mkdir -p $WORKON_HOME
$ source /usr/local/bin/virtualenvwrapper.sh
```



## Linux

### Python
Linux come with Python pre-installed.  To check, open up the Terminal application, then type `python`:

```bash
$ python
Python 2.7.3 (default, Aug  9 2012, 17:23:57)
[GCC 4.7.1 20120720 (Red Hat 4.7.1-5)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

### git
You will need to install [git][5] either from commands below or through their [download page][6]. You can then follow the [Save your Progress]( {{ get_url("begin/save-your-progress")}}) page to set it up.

* Fedora: `sudo yum install git`
* Ubuntu: `sudo apt-get install git`


### C Compiler

A C compiler, either GCC or clang, is needed because the `numpy` library we are using has some C extensions, which will need to be compiled.

To test if you have either GCC or clang, type `$ gcc` or `$ clang` into your terminal. If you get an error that says “command not found” then follow the install instructions:

* Fedora:
	* `sudo yum groupinstall "Developer Tools"`
	* `sudo yum install python-devel`
* Ubuntu:
	* you may need to run `sudo apt-get update` first.
	* `sudo apt-get install build-essential python-dev libxml2-dev libxslt-dev`

### pip

[pip][9], stands for “python install python”, is a tool for installing and managing Python packages. Within your Terminal application, use the following commands (ignore the leading `$` as that is your terminal prompt) for downloading & installing. It may prompt you for your computer login password.

```bash
$ curl https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py | sudo python
$ pip
Usage: pip COMMAND [OPTIONS]
You must give a command (use "pip help" to see a list of commands)
$ sudo pip install --upgrade setuptools
```

### virtualenv & virtualenvwrapper

[virtualenv][10] creates isolated environments for each of your Python projects. It helps to solve version & dependency problems with multple Python installations and/or multiple versions of different Python packages.  We’ll use `pip` to install it:

```bash
$ sudo pip install virtualenv
```

[virtualenvwrapper][11] is a great (but not required) tool for using virtualenv by simplifying the commands that virtualenv needs.  We’ll use `pip` again to install it:

```bash
$ sudo pip install virtualenvwrapper
$ export WORKON_HOME=~/Envs
$ mkdir -p $WORKON_HOME
$ source /usr/local/bin/virtualenvwrapper.sh
```


## Windows

### python

1. Go [here](http://python.org/ftp/python/2.7.5/python-2.7.5.msi) and click “run” if given the option. Otherwise, save it to your Desktop, then minimize windows to see your desktop, and double click on it to start the installer. Follow the installer instructions to completion.
2. Open a command prompt (we will be doing this multiple times, so make a note of how to do this!):
	- On Windows Vista or Windows 7: click on the Start menu (the Windows logo in the lower left of the screen), type cmd into the Search field directly above the Start menu button, and click on "cmd" in the search results above the Search field.
	- On Windows XP: click on the Start menu (the Windows logo in the lower left of the screen), click on "Run...", type cmd into the text box, and hit enter.
3. At this `C:\` prompt that appears, test your Python install by typing `\Python27\python.exe` and hitting `enter`. You should see something like

```bash
Python 2.7.3 (r271:86832,...) on win32
Type "help", "copyright", "credits" or "license" for more information
>>>
```
4. You just started Python! The `>>>` indicates that you are at a new type of prompt – a Python prompt. The command prompt lets you navigate your computer and run programs, and the Python prompt lets you write and run Python code interactively.
5. To exit the Python prompt, type `exit()` and press Enter. This will take you back to the Windows command prompt (the `C:\` you saw earlier).
6. Put Python on the PATH – You might have noticed that you typed a "full path" to the Python application above when launching Python (`python.exe` is the application, but we typed `\Python27\python.exe`). In this step, you will configure your computer so that you can run Python without typing the ''Python27'' directory name.
	* Get to System Properties
		1. Open up “My Computer” by clicking on the Start menu or the Windows logo in the lower-left hand corner, and navigate to "My Computer" (for Windows XP) or "Computer" (For Vista and Windows 7).
		2. Right-click on the empty space in the window, and choose “Properties”.
			* If you’re using XP: window labeled "System Properties" will pop up. Click the "Advanced" tab. A window with the title "System Properties" will appear.
			* If you’re **not** using XP: A window labeled “View basic information about your computer” will appear. In this window, click "Advanced system settings".  A window with the title "System Properties" will appear.
	* Edit the Path
		1. Within System Properties, make sure you are in the tab labeled “Advanced’.
		2. Click the button labeled “Environment Variables”.  A window labeled "Environment Variables" will appear.
		3. In this window, the screen is split between “User variables” and “System variables”. Within “System variables’, scroll down and find the one labeled “Path’. Click the “Edit...” button A window with the "Variable name" and the "Variable value" should appear.  The “Variable value” will already have some text in it; click in the box to unhighlight it (we don't want to accidentally delete that text).
	* In the "Variable value" box, scroll to the end. Add the following text, and hit OK. Make sure to include the semicolon at the start! `;c:\python27\;c:\python27\scripts;c:\python27\tools\scripts`
	* Hit "OK" to close out the system properties window.
	* Test your change:
		1. Open up a new command prompt: you do this the same way you did above when installing python. This needs to be a new command prompt because the changes you just made didn't take affect in prompts that were already open.
		2. Type python into the command prompt to start Python
		3. Notice that you now get a Python interpreter, indicated by the change to a `>>>` prompt.
		4. Exit the Python prompt by typing `exit()` and hitting enter. Now you're back at the Windows command prompt (`C:\`).

Success! You have installed Python!

### git

Download git [here](http://msysgit.github.io/).  This installs git for Windows, as well as Msys, a Unix-like shell, that also includes a GCC compiler, [MinGW](http://mingw.org/).


### pip, virtualenv + virtualenvwrapper

1. You’ll first need to install setuptools, and use `ez_setup.py` to run it.  Download [ez_setup.py](https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py) and run it.
2. Once installation is complete, you will find an `easy_install.exe` program in your Python `Scripts` subdirectory. For simple invocation and best results, add this directory to your `PATH` environment variable, if it is not already present.
3. Next, run `easy_install pip` to install [pip](https://pypi.python.org/pypi/pip).
4. Open/run the Git Bash program. **NOTE**:  Windows users: We will use this Git Bash program for whenever the “terminal”, “shell”, or “command line” is referred to.
5. Run the following command to install [virtualenv](http://www.virtualenv.org/en/latest/#installation):

	```bash
	$ pip install virtualenv
	```

	or, if you get a permission error:

	```bash
	$ sudo pip install virtualenv
	```

4. Next, run the command to install [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/install.html):

	```bash
	$ pip install virtualenvwrapper
	```

	or, if you get a permission error:

	```bash
	$ sudo pip install virtualenvwrapper
	```

5. And now setup virtualenvwrapper:

	```bash
	$ export WORKON_HOME=$HOME/.virtualenvs
	$ export MSYS_HOME=/c/msys/1.0
	$ source /usr/local/bin/virtualenvwrapper.sh
	```

	or,

	```bash
	$ export WORKON_HOME=$HOME/.virtualenvs
	$ export MSYS_HOME=C:\msys\1.0
	$ source /usr/local/bin/virtualenvwrapper.sh
	```



## Test your setup


Now let’s test our installation and get familiar with creating & using virtual environments, let’s return to our terminal:


```bash
$ mkvirtualenv TestEnv
Installing
distribute..........................................
....................................................
....................................................
...............................done.
virtualenvwrapper.user_scripts Creating /Users/lynnroot/Envs/TestEnv/bin/predeactivate
virtualenvwrapper.user_scripts Creating /Users/lynnroot/Envs/TestEnv/bin/postdeactivate
virtualenvwrapper.user_scripts Creating /Users/lynnroot/Envs/TestEnv/bin/preactivate
virtualenvwrapper.user_scripts Creating /Users/lynnroot/Envs/TestEnv/bin/postactivate
virtualenvwrapper.user_scripts creating /Users/lynnroot/Envs/TestEnv/bin/get_env_details
```


Now that you made a virtual environment called `TestEnv`, you should see `(TestEnv)` before your prompt:

```bash
(TestEnv) $
```

Let’s play around with commands for virtualenv:


```bash
# deactivate the TestEnv
(TestEnv) $ deactivate
$
# reactivate the TestEnv
$ workon TestEnv
(TestEnv) $
```

Next, we’ll practice installing a package into the virtualenv:

```bash
# install the Django package in your TestEnv environment
(TestEnv) $ pip install django
Downloading/unpacking django
  Downloading Django-1.1.1.tar.gz (5.6Mb): 5.6Mb downloaded
  Running setup.py egg_info for package django
Installing collected packages: django
  Running setup.py install for django
    changing mode of build/scripts-2.6/django-admin.py from 644 to 755
    changing mode of /Users/lynnroot/Envs/TestEnv/bin/django-admin.py to 755
Successfully installed django
(TestEnv) $
```


```bash
# test the installation of Django
(TestEnv) $ python
Python 2.7.2 (default, Jun 20 2012, 16:23:33)
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>> exit()
# deactivate the TestEnv virtual environment
(TestEnv) $ deactivate
$
```

```bash
# try to import Django again
# we should get an error because we deactivated the virtualenv
$ python
Python 2.7.2 (default, Jun 20 2012, 16:23:33)
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named django
>>> exit()
$
```

```bash
# reactivate the TestEnv virtual environment
$ workon TestEnv
(TestEnv) $
# try again to import Django
(TestEnv) $ python
Python 2.7.2 (default, Jun 20 2012, 16:23:33)
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>> exit()
(TestEnv) $
```

```bash
# see what libraries are installed in the TestEnv virtual environment:
(TestEnv) $ pip freeze
django==1.5
(TestEnv) $
```

Here’s a run-down of useful commands for pip, virtualenv & virtualenvwrapper.

* `mkvirtualenv [ENV_NAME]` – creates and activates a fresh virtual environment
* `workon [ENV_NAME]` – activates an already-created virtual environment
* `deactivate` – deactivates the virtual environment that is currently active
* within an activated virtualenv, `pip install [PACKAGE_NAME]` installs a package into the virtualenv
* within an activated virtualenv, `pip freeze` lists the packages that is installed & accessible within the virtualenv


## Get the Tutorial Code

Within your terminal:

1. To get to your “Home” directory:

	```bash
	$ cd
	```

2. To create a new `Projects` folder and move to that directory. You can name it whatever you want, just remember what you named it, and where it is:

	```bash
	$ mkdir Projects
	$ cd Projects
	```

3. Clone the New Coder project into the directory you’re currently in, which is `Projects` (unless you named it something else):

	```bash
	$ git clone https://github.com/econchick/new-coder.git
	```

When you clone a repo with the above command, git creates a directory.  Here, git created the `new-coder` directory within our `Projects` directory.  If you were to open up your file browser (e.g. Finder in Mac), the file hierarchy would look like the following:

```bash
.
└── Projects/
    └── new-coder/
	    ├── AUTHORS.md
	    ├── CONTRIBUTING.md
	    ├── LICENSE
	    ├── README.md
	    ├── apis/     # sample code for tutorial #2
	    ├── dataviz/  # sample code for tutorial #1
	    ├── gui/      # sample code for tutorial #5
	    ├── network/  # sample code for tutorial #4
	    ├── scrape/   # sample code for tutorial #3
	    └── website/  # files that make newcoder.io
```

When you work through each project, make a new directory within `Projects` to keep your code away from the sample code.  For example:

```bash
.
└── Projects/
    └── new-coder/
		# <-- snip -->
	    ├── apis/     # sample code for tutorial #2
	    ├── apis_workspace/ # your code for tutorial #2
	    ├── dataviz/  # sample code for tutorial #1
	    ├── dataviz_workspace/ # your code for tutorial #1
	    ├── gui/      # sample code for tutorial #5
	    ├── gui_workspace/ # your code for tutorial #5
	    ├── network/  # sample code for tutorial #4
	    ├── network_workspace/ # your code for tutorial #4
	    ├── scrape/   # sample code for tutorial #3
	    ├── scrape_workspace/ # your code for tutorial #3
	    └── website/  # files that make newcoder.io
```



You’re good to go with your setup! Go start on [dataviz]({{ get_url("dataviz")}})!

[1]: https://github.com/econchick/new-coder/issues/28
[2]: http://www.python.org/images/terminal-in-finder.png
[3]: http://www.python.org
[4]: https://www.python.org/download/mac/
[5]: http://git-scm.com
[6]: http://git-scm.com/downloads
[7]: http://gcc.gnu.org/
[8]: https://github.com/econchick/new-coder/issues/29
[9]: http://www.pip-installer.org/en/latest/
[10]: https://pypi.python.org/pypi/virtualenv
[11]: http://virtualenvwrapper.readthedocs.org/en/latest/
[mingw]: http://sourceforge.net/projects/mingw/files/latest/download?source=files
[virtualenv]: http://pypi.python.org/pypi/virtualenv
[install]: http://www.mingw.org/wiki/InstallationHOWTOforMinGW
[gitwin]: http://git-scm.com/download/win
