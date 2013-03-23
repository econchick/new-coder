---
layout: post.html
title: "Setting up your computer for these tutorials"
tags: [setup, begin]
---

Let’s setup your machine for these tutorials. The goal is to go through some pain **now** so you have a decent development environment later on, i.e. no short cuts. This does not go into **why** we need these tools, [not yet at least][8].

### Overview of requirements

The installation will depend on your operating system, but overall, you will need:

* Python 2.x – there are [plans][1] to update/include Python 3.x
* git – an intro given [here]("{{ get_url('Save-your-progress') }}")
* A C compiler
* pip
* virtualenv
* virtualenvwrapper (**optional** but a very handy tool for managing virtualenvs)


### Mac OS X

##### Python
Macs come with Python pre-installed.  To check, open up the Terminal application (Applications &rarr; Utilities &rarr; Terminal like [so][2]), then type `python`:

```bash
$ python
Python 2.7.2 (default, Jun 20 2012, 16:23:33)
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

[Python.org][3] has a good [Python on the Mac][4] page if the above does not work for you.

##### git
You will need to install [git][5] on your machine through their [download page][6]. You can then follow the [Save your Progress]("{{ get_url('Save-your-progress') }}") page to set it up.

##### C compiler

You will need the [XCode](http://developer.apple.com/xcode) application. Once you have XCode on your machine, you will need to navigate to Preferences &rarr; Downloads, then select **Command Line Tools** to download & install (this may take a while, get some coffee, go take a shower). 

This gives you the [GCC][7] or the GNU Compiler Collection. To test installation, within the Terminal application, type `gcc` and you should get the following:

```bash
$ gcc
i686-apple-darwin11-llvm-gcc-4.2: no input files
```

##### pip

[pip][9], stands for “python install python”, is a tool for installing and managing Python packages. Within your Terminal application, use the following commands (ignore the leading `$` as that is your terminal prompt) for downloading & installing. It may prompt you for your computer login password.

```bash
$ sudo curl -O http://python-distribute.org/distribute_setup.py | python 
$ sudo curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python
$ pip
Usage: pip COMMAND [OPTIONS]
You must give a command (use "pip help" to see a list of commands)
```

##### virtualenv & virtualenvwrapper

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

Now let’s test our installation and get familiar with creating & using virtual environments:

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

Let’s play around with commands for virtualenvwrapper:

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

# test the installation of Django
(TestEnv) $ python
Python 2.7.2 (default, Jun 20 2012, 16:23:33)
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>> exit()
(TestEnv) $ 

# deactivate the TestEnv virtual environment
(TestEnv) $ deactivate
$ 

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

# see what libraries are installed in the TestEnv virtual environment:
(TestEnv) $ pip freeze
django==1.5
(TestEnv) $ 
```

As you can see, you’ll need to activate a virtual environment in order to access the libraries that you installed.  Here’s a run-down of useful commands for pip, virtualenv & virtualenvwrapper:

* `mkvirtualenv [ENV_NAME]` – creates and activates a fresh virtual environment
* `workon [ENV_NAME]` – activates an already-created virtual environment
* `deactivate` – deactivates the virtual environment that is currently active
* within an activated virtualenv, `pip install [PACKAGE_NAME]` installs a package into the virtualenv
* within an activated virtualenv, `pip freeze` lists the packages that is installed & accessible within the virtualenv

You’re good to go with your setup! Go start on [dataviz]("{{ get_url('dataviz')}}")!




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