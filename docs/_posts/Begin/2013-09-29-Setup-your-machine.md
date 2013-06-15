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

## Overview of requirements

The installation will depend on your operating system, but overall, you will need:

* Python 2.x – there are [plans][1] to update/include Python 3.x
* git – an intro given [here]("http://newcoder.io/Save-your-progress")
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
You will need to install [git][5] on your machine through their [download page][6]. You can then follow the [Save your Progress]("http://newcoder.io/Save-your-progress") page to set it up.

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
$ sudo curl -O http://python-distribute.org/distribute_setup.py | python 
$ sudo curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python
$ pip
Usage: pip COMMAND [OPTIONS]
You must give a command (use "pip help" to see a list of commands)
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
You will need to install [git][5] either from commands below or through their [download page][6]. You can then follow the [Save your Progress]("http://newcoder.io/Save-your-progress") page to set it up.

* Fedora: `sudo yum git`
* Ubuntu: `sudo apt-get install git`


### C Compiler

A C compiler, either GCC or clang, is needed because the `numpy` library we are using has some C extensions, which will need to be compiled.  

To test if you have either GCC or clang, type `$ gcc` or `$ clang` into your terminal. If you get an error that says “command not found” then follow the install instructions:

* Fedora: 
	* `sudo yum groupinstall "Developer Tools"`
	* `sudo yum install python-devel`
* Ubuntu: 
	* you may need to run `sudo apt-get update` first.
	* `sudo apt-get install build-essential python-dev`

### pip

[pip][9], stands for “python install python”, is a tool for installing and managing Python packages. Within your Terminal application, use the following commands (ignore the leading `$` as that is your terminal prompt) for downloading & installing. It may prompt you for your computer login password.

```bash
$ sudo curl -O http://python-distribute.org/distribute_setup.py | python 
$ sudo curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python
$ pip
Usage: pip COMMAND [OPTIONS]
You must give a command (use "pip help" to see a list of commands)
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

1. Go [here](http://python.org/ftp/python/2.7.1/python-2.7.1.msi) and click “run” if given the option. Otherwise, save it to your Desktop, then minimize windows to see your desktop, and double click on it to start the installer. Follow the installer instructions to completion.
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

Download git [here]("http://git-scm.com/download/win").

### C Compiler

Download the MinGW GCC compiler [here]("http://sourceforge.net/projects/mingw/files/latest/download?source=files") and follow installation instructions [here]("http://www.mingw.org/wiki/InstallationHOWTOforMinGW").

### virtualenv + pip

1. From [here]("http://pypi.python.org/pypi/virtualenv"), under Installation, see “You can just grab the single file virtualenv.py ..”. Right-click and save-as and place in the Scripts folder that we earlier added to system PATH.
2. From the command line, `cd` into the directory that you want to save your Python work. **IMPORTANT TIP**: Do not create or use a directory that has spaces in the name. For instance, ‘Python Projects’ is not good, but ‘PythonProjects’ is fine.
3. Within your Python project directory, type: `virtualenv.py dataviz`. A virtual environment called “dataviz” has been created, and now lives in your Python projects directory. This also installs pip: pip is a tool that is used to install Python packages
4. You will now need to activate the virtual environment by typing in your command line: `dataviz\Scripts\activate.bat`.  You should see something like this:  `(dataviz) C:\PythonProjects>`
5. To stop working in the virtual environment, type the following in your command line: `dataviz\Scripts\deactivate.bat`.  You will need to run the activate script again (stated in #4) to start up the virtual environment.


## Test your setup


Now let’s test our installation and get familiar with creating & using virtual environments:
	
- Mac OS X/Linux: 

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

* Windows:

```cmd
# Within your ProjectFolder
C:\dataviz\Scripts> virtualenv.py TestEnv
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

* Mac OS X/Linux: 

```bash
# deactivate the TestEnv
(TestEnv) $ deactivate
$ 
# reactivate the TestEnv
$ workon TestEnv
(TestEnv) $ 
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

* Windows:

```cmd
# deactivate the TestEv
(TestEnv) dataviz\Scripts> deactivate.bat
C:\dataviz\Scripts>
C:\dataviz\Scripts> activate.bat
(TestEnv) C:\dataviz\Scripts>
# install the Django package in your TestEnv environment
(TestEnv) C:\ pip install django
Downloading/unpacking django
  Downloading Django-1.1.1.tar.gz (5.6Mb): 5.6Mb downloaded
  Running setup.py egg_info for package django
Installing collected packages: django
  Running setup.py install for django
    changing mode of build/scripts-2.6/django-admin.py from 644 to 755
    changing mode of /Users/lynnroot/Envs/TestEnv/bin/django-admin.py to 755
Successfully installed django
(TestEnv) C:\dataviz\Scripts>

```


* All operating systems (for Windows, know that instead of the `$` prompt, you will see `C:\` + folder name:

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

* here’s a run-down of useful commands for pip, virtualenv & virtualenvwrapper:
	* For Linux + Mac OS:
		* `mkvirtualenv [ENV_NAME]` – creates and activates a fresh virtual environment
		* `workon [ENV_NAME]` – activates an already-created virtual environment
		* `deactivate` – deactivates the virtual environment that is currently active
		* within an activated virtualenv, `pip install [PACKAGE_NAME]` installs a package into the virtualenv
		* within an activated virtualenv, `pip freeze` lists the packages that is installed & accessible within the virtualenv
	* For Windows:
		* `virtualenv.py [ENV_NAME]` – creates and activates a fresh virtual environment within `ProjectFolder`.
		* `ProjectFolder\Scripts\activate.bat` – activates an already-created virtual environment
		* `ProjectFolder\Scripts\deactivate.bat` – deactivates the virtual environment that is currently active
		* within an activated virtualenv, `pip install [PACKAGE_NAME]` installs a package into the virtualenv
		* within an activated virtualenv, `pip freeze` lists the packages that is installed & accessible within the virtualenv

You’re good to go with your setup! Go start on [dataviz]("http://newcoder.io/dataviz")!

[1]: https://github.com/econchick/new-coder/issues/28
[2]: http://www.python.org/images/terminal-in-finder.png
[3]: http://www.python.org
[4]: http://www.python.org/getit/mac/
[5]: http://git-scm.com
[6]: http://git-scm.com/downloads
[7]: http://gcc.gnu.org/
[8]: https://github.com/econchick/new-coder/issues/29
[9]: http://www.pip-installer.org/en/latest/
[10]: https://pypi.python.org/pypi/virtualenv
[11]: http://virtualenvwrapper.readthedocs.org/en/latest/