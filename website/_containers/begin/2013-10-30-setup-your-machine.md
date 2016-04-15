---
layout: post.html
title: "Setting up your computer"
tags: [setup, installation, begin]
---

All the needed dependencies for setting up your Mac, Linux, or Windows machine for these tutorials.

1. [Overview](#overview-of-requirements)
2. Install:
    1. [Mac OS X](#mac-os-x)
    2. [Linux](#linux)
    3. [Windows](#windows)
3. [Test your setup](#test-your-setup)
4. [Get the Tutorial Code](#get-the-tutorial-code)

<br/><br/><hr/>
## Overview of requirements

The installation will depend on your operating system, but overall, you will need:

* Python 2.x – there are [plans][1] to update/include Python 3.x
* git – an intro given [here]( {{get_url("begin/save-your-progress")}})
* A C compiler
* pip
* virtualenv
* virtualenvwrapper

## Mac OS X
<p/>
### Python
Macs come with Python pre-installed.  To double-check, open up the Terminal application (Applications &rarr; Utilities &rarr; Terminal like [so][2]), then type `python`:

```bash
$ python
Python 2.7.2 (default, Jun 20 2012, 16:23:33)
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

This is the Python shell.  To close out, press `CTRL`+`D`, or type `exit()`.

[Python.org][3] has a good [Python on the Mac][4] page if the above does not work for you.

### git
You will need to install [git][5] on your machine through their [download page][6]. You can then follow the [Save your Progress]({{ get_url("begin/save-your-progress")}}) page to set it up.

### C compiler

For Mac OS X 10.9 and higher (Mavericks and later): Within your terminal, run `xcode-select --install`. A pop-up will ask you to install command line developer tools.

For Mac OS X 10.8 and lower (Mountain Lion and earlier), you will need to download the Command Line Tools from Apple [here](https://developer.apple.com/downloads/index.action#).  A (free) developer’s account is required.  Search for your OS version (which can be found by clicking on the Apple in the top left of your menu bar, and selecting “About this Mac”) and select “Command Line Tools for XCode”.

This gives you the [GCC][7] or the GNU Compiler Collection. To test installation, within the Terminal application, type `gcc` and you should get the following:

```bash
$ gcc
i686-apple-darwin11-llvm-gcc-4.2: no input files
```

### pip

[pip][9] is a tool for installing and managing Python packages. Within your Terminal application, use the following commands (ignore the leading `$` as that is your terminal prompt) for downloading & installing. It may prompt you for your computer login password.

```bash
$ curl https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py | sudo python
$ pip --version
pip 1.5.6 from /Users/lynn/.virtualenvs/gui/lib/python2.7/site-packages (python 2.7)
$ sudo pip install --upgrade setuptools
```

### virtualenv & virtualenvwrapper

[virtualenv][10] creates isolated environments for each of your Python projects. It helps to solve version & dependency problems with multiple Python installations and/or multiple versions of different Python packages.  We’ll use `pip` to install it:

```bash
$ sudo pip install virtualenv
```

[virtualenvwrapper][11] is a great (but not required) tool for using virtualenv by simplifying the commands that virtualenv needs.  We’ll use `pip` again to install it:

<div class="well">
<b>NOTE</b>: If you use <code>zsh</code> instead of <code>bash</code> (the default), then replace all instances below of <code>~/.bash_profile</code> with <code>~/.zshrc</code>
</div>

```bash
$ sudo pip install virtualenvwrapper
$ export WORKON_HOME=~/Envs
$ echo 'export WORKON_HOME=~/Envs' >> ~/.bash_profile
$ echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bash_profile
$ mkdir -p $WORKON_HOME
$ source /usr/local/bin/virtualenvwrapper.sh
```

<hr/>

## Linux

<p/>

### Python
Linux come with Python pre-installed.  To double-check, open up the Terminal application, then type `python`:

```bash
$ python
Python 2.7.3 (default, Aug  9 2012, 17:23:57)
[GCC 4.7.1 20120720 (Red Hat 4.7.1-5)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

This is the Python shell.  To close out, press `CTRL`+`D`, or type `exit()`.

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
* Ubuntu/Debian:
    * you may need to run `sudo apt-get update` first.
    * `sudo apt-get install build-essential python-dev libxml2-dev libxslt-dev`

### pip

[pip][9] is a tool for installing Python packages. Within your Terminal application, use the following commands (ignore the leading `$` as that is your terminal prompt) for downloading & installing. It may prompt you for your computer login password.

```bash
$ curl https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py | sudo python
$ pip --version
pip 1.5.6 from /Users/lynn/.virtualenvs/gui/lib/python2.7/site-packages (python 2.7)
$ sudo pip install --upgrade setuptools
```

### virtualenv & virtualenvwrapper

[virtualenv][10] creates isolated environments for each of your Python projects. It helps to solve version & dependency problems with multple Python installations and/or multiple versions of different Python packages.  We’ll use `pip` to install it:

```bash
$ sudo pip install virtualenv
```

[virtualenvwrapper][11] is a great (but not required) tool for using virtualenv by simplifying the commands that virtualenv needs.  We’ll use `pip` again to install it.

<div class="well">
<b>NOTE</b>: If you use <code>zsh</code> instead of <code>bash</code> (the default), then replace all instances below of <code>~/.bash_profile</code> with <code>~/.zshrc</code>
</div>

For Fedora/RHEL/CentOS:

```bash
$ sudo pip install virtualenvwrapper
$ export WORKON_HOME=~/Envs
$ echo 'export WORKON_HOME=~/Envs' >> ~/.bash_profile
$ echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bash_profile
$ mkdir -p $WORKON_HOME
$ source ~/.bash_profile
```

For Debian/Ubuntu:


```bash
$ sudo pip install virtualenvwrapper
$ export WORKON_HOME=~/Envs
$ echo 'export WORKON_HOME=~/Envs' >> ~/.bash_profile
$ echo 'source /etc/bash_completion.d/virtualenvwrapper' >> ~/.bash_profile
$ mkdir -p $WORKON_HOME
$ source ~/.bash_profile
```

<hr/>

## Windows
<p/>
### powershell

1. This step depends on the version of Windows you are running.
    *   For Windows 8: To run it, press the Windows key (bottom row on the keyboard, third key from left) to navigate to the Start Screen. Type `powershell`, right click on the Windows Powershell tile bar and select 'Run as Administrator'.
    *   For Windows 7: To run it, click on the Start menu (the Windows logo in the lower left of the screen), type `powershell` into the Search field directly above the Start menu button, right click on Powershell in the search results above the Search field, select “Run as Administrator”.
    *   For Windows Vista: Go [here](https://www.microsoft.com/en-us/download/details.aspx?id=9864), click “run” if given the option. Otherwise, save it to your Desktop, then minimize windows to see your desktop, and double click on it to start the installer. Follow the installer instructions to            completion. Restart your computer.
    *   For Windows XP: Go [here](http://www.microsoft.com/en-us/download/details.aspx?id=16818), click “run” if given the option. Otherwise, save it to your Desktop, then minimize windows to see your desktop, and double click on it to start the installer. Follow the installer instructions to            completion. Restart your computer.

### python

1. Go [here](http://python.org/ftp/python/2.7.5/python-2.7.5.msi) and click “run” if given the option. Otherwise, save it to your Desktop, then minimize windows to see your desktop, and double click on it to start the installer. Follow the installer instructions to completion.
2. Open up a Powershell prompt (we will be doing this multiple times, so make a note of how to do this!):
    * **Windows 8**: Press the Windows key (bottom row on the keyboard, third key from left) to navigate to the Start Screen. Type `powershell`, right click on the Windows Powershell tile bar and select “Run as Administrator”.
    * **Windows Vista and Windows 7**: Click on the Start menu (the Windows logo in the lower left of the screen), type `powershell` into the Search field directly above the Start menu button, and right click on “powershell” in the search results above the Search field, and select “Run as Administrator”.
    * **Windows XP**: Click on the Start menu (the Windows logo in the lower left of the screen), navigate to Programs, then to Accessories, then to Windows PowerShell and right click on “Windows PowerShell” and select “Run as Administrator”.
3. At this `C:\>` prompt that appears, test your Python install by typing `python` and hitting `enter`. You should see something like

    ```python
    Python 2.7.3 (r271:86832,...) on win32
    Type "help", "copyright", "credits" or "license" for more information
    >>>
    ```

4. You just started Python! The `>>>` indicates that you are at a new type of prompt – a Python prompt. The Powershell prompt lets you navigate your computer and run programs, and the Python prompt lets you write and run Python code interactively.
5. To exit the Python prompt, type `quit()` and press Enter. This will take you back to the Windows command prompt (the `C:\>` you saw earlier).
6. If you do not see the above specified return message, put Python on the PATH:
    1. Go to System Properties
        1. **Windows 8:**
            * Get to the Start screen(see above steps), search for Control Panel and select the Control Panel app tile from the results.
            * Within Control Panel, search (upper right corner) for and open System.
            * In the dialog box, select "Advanced Settings".
            * In the next dialog box, select "Environment Variables".
        2. **Windows 7, Vista, XP:**
            * Open up “My Computer” by clicking on the Start menu or the Windows logo in the lower-left hand corner, and navigate to “My Computer” (for Windows XP) or “Computer” (For Vista and Windows 7).
            * Right-click on the empty space in the window, and choose “Properties”.
                1. If you’re using XP: window labeled "System Properties" will pop up. Click the “Advanced” tab. A window with the title “System Properties” will appear.
                2. If you’re **not** using XP: A window labeled “View basic information about your computer”  will appear. In this window, click “Advanced system settings”.  A window with the title “System Properties” will appear.
    2. Edit the Path
        1. Within “System Properties”, make sure you are in the tab labeled “Advanced”. [Windows 7/XP/Vista]
        2. Click the button labeled “Environment Variables”.  A window labeled “Environment Variables” will appear. [Windows 7/XP/Vista]
        3. In the “Environment Variables” window, the screen is split between “User variables” and “System variables”.
        4. Within “System variables", scroll down and find the one labeled “Path”. Click the “Edit...” button.
            * A window with the "Variable name" and the “Variable value” should appear.  The “Variable value” should already have some text in it; click in the box to  unhighlight it (we don’t want to accidentally delete that text).
            * In the “Variable value” box, scroll to the end. Add the following text, and hit OK. Make sure to include the semicolon at the start!

                `;c:\python27\;c:\python27\scripts;c:\python27\tools\scripts`

        5. If within “System variables” you do not find “Path”, click on New. It will bring up a dialog box, type in “Path” in the first section, and then in the second section labelled “Variable value”, type in the following text and hit “OK”.

            `;c:\python27\;c:\python27\scripts;c:\python27\tools\scripts`

    3. Hit “OK” to close out the system properties window.
    4. Test your change:
        1. Open up a new Powershell prompt: you do this the same way you did above when installing python. This needs to be a new Powershell prompt because the changes you just made didn’t take affect in prompts that were already open.
        2. Type `python` into the Powershell prompt to start Python
        3. Notice that you now get a Python interpreter, indicated by the change to a `>>>` prompt.
        4. Exit the Python prompt by typing `quit()` and hitting enter. Now you’re back at the Powershell prompt (`PS C:\>`).


Success! You have installed Python!

### git

1. Download git [here](http://msysgit.github.io/).  This installs git for Windows, as well as MSYS, a Unix-like shell, that also includes a GCC compiler, [MinGW](http://mingw.org/).
2. Go back into System Properties and add `;C:\Program Files\Git\bin` to the end of PATH in “System Variables” (see above Python Installation instructions). Make sure to click in the box to unhighlight before adding this new text.
3. Test your change:
    *   Open up a new Powershell prompt: you do this the same way you did above when installing python. This needs to be a new Powershell prompt because the changes you just made didn‘t take affect in prompts that were already open.
    *   Type `git --version` into the Powershell prompt.
    *   Notice that you now get some information about the version of Git you have installed.
4. Within your reopened PowerShell prompt, `Set-ExecutionPolicy RemoteSigned` type and hit enter.  When you see the Execution Policy Change prompt, type in `Y` and hit enter.

git is ready to go!


### pip, virtualenv + virtualenvwrapper

####  Setuptools + Pip
1. You’ll first need to install Setuptools and use `ez_setup.py` to run it:
    1. Navigate [here](https://bootstrap.pypa.io/ez_setup.py).
    2. Right click within the webpage, select “Save As” to your Desktop folder. Then type in `ez_setup` as the filename, make sure it’s saved as a `.py` file, and click “Save”.
    3. Go back into the PowerShell prompt and run the `ez_setup` file by typing the following and hitting enter `python ~\Desktop\ez_setup.py`
2. Now Install Pip:
    1. Navigate [here](https://bootstrap.pypa.io/get-pip.py)
    2. Right click within the webpage, select “Save As” and save to the Desktop folder or else Then type in `get_pip` as the filename, ensure it’s being saved as a `.py` file and click “Save”.
    3. Within the PowerShell prompt, type the followng text and hit enter: `python ~\desktop\get_pip.py`

#### Virtualenv + Virtualenvwrapper

1. With pip installed we can now eaily install virtualenv, and  then virtualenvwrapper-powershell. Within your PowerShell prompt, type the following:
    1. `pip install virtualenv`
    2. `pip install virtualenvwrapper-powershell`
    3. `mkdir ~/.virtualenvs`
2. You should see some result that reads something similar to `Directory: C:\Users`.
3. To check if all is installed well, type:
    1. `Import-Module virtualenvwrapper`
    2. `Get-Command *virtualenv*`

Success! You have installed Virtualenvwrapper!

<hr/>

## Test your setup

Now let’s test our installation and get familiar with creating & using virtual environments, let’s return to our terminal:

### Mac OS X and Linux


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


## Windows


```powershell
C:\> mkvirtualenv TestEnv
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

```powershell
(TestEnv) C:\>
```

Let’s play around with commands for virtualenv:


```powershell
# deactivate the TestEnv
(TestEnv) C:\> deactivate
C:\>
# reactivate the TestEnv
C:\> workon TestEnv
(TestEnv) C:\>
```

Next, we’ll practice installing a package into the virtualenv:

```powershell
# install the Django package in your TestEnv environment
(TestEnv) C:\> pip install django
Downloading/unpacking django
  Downloading Django-1.1.1.tar.gz (5.6Mb): 5.6Mb downloaded
  Running setup.py egg_info for package django
Installing collected packages: django
  Running setup.py install for django
    changing mode of build/scripts-2.6/django-admin.py from 644 to 755
    changing mode of /Users/lynnroot/Envs/TestEnv/bin/django-admin.py to 755
Successfully installed django
(TestEnv) C:\>
```


```powershell
# test the installation of Django
(TestEnv) C:\> python
Python 2.7.2 (default, Jun 20 2012, 16:23:33)
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>> quit()
# deactivate the TestEnv virtual environment
(TestEnv) C:\> deactivate
C:\>
```

```powershell
# try to import Django again
# we should get an error because we deactivated the virtualenv
C:\> python
Python 2.7.2 (default, Jun 20 2012, 16:23:33)
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named django
>>> quit()
C:\>
```

```powershell
# reactivate the TestEnv virtual environment
C:\> workon TestEnv
(TestEnv) C:\>
# try again to import Django
(TestEnv) C:\> python
Python 2.7.2 (default, Jun 20 2012, 16:23:33)
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>> quit()
(TestEnv) C:\>
```

```powershell
# see what libraries are installed in the TestEnv virtual environment:
(TestEnv) C:\> pip freeze
django==1.5
(TestEnv) C:\>
```

For Powershell:

* `pwd` : Get and display the current location
* `cd <path>` :  Move to a different directory/location
* `cd ..`: Move to the parent location
* `ls <path>` :List all objects in that directory
* `ls`:List all objects in current directory
* `mkdir` : create a new directory

<hr/>

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



<nav>
  <ul class="pager">
    <li class="previous"><a href="{{ get_url('/begin/how-to-work-through-tutorials/') }}"><span aria-hidden="true">&larr;</span> How to Work through Tutorials</a></li>
    <li class="next"><a href="{{ get_url('/begin/save-your-progress/') }}">Save Your Progress <span aria-hidden="true">&rarr;</span></a></li>
  </ul>
</nav>
