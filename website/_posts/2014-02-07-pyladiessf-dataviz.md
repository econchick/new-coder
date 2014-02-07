---
layout: post.html
title: "PyLadies SF - Data Viz Tutorial"
tags: [pyladiessf]
---

<img src="{{ get_asset('images/pyladies_logo.png') }}" width="200px" style="display:block;margin-left:auto;margin-right:auto;"/>

## PyLadiesSF Intro to Python with Data Visualization
### Friday, February 7th: Setting up our Environment



## Table of Contents

0. [Preface](#preface)
1. [Intro](#intro)
2. [Mac](#mac)
	1. [OS X 5 or 6](#osx5or6)
	2. [OS X 7, 8 or 9](#osx78or9)
3. [Linux](#linux)
4. [Windows](#windows)
5. [PythonAnywhere](#pythonanywhere)
6. [Setup Environment](#setupenvironment)
7. [Check your Environment](#checkyourenvironment)

## Preface


* Friday:
	* 6:30-8:30pm: Install-fest!
	* Follow these instructions closely!
	* You may leave when you have completed the section [Check your Environment](#checkyourenvironment).
* Saturday:
	* 10am: Doors open/breakfast
	* 10:30am: Suprise Guest! Learn about data visualization with a super secret Pythonista.
	* 11:00a - 4pm: Workshop! with breaks & lunch provided.
	* You'll follow along with me via the projector.
	* You'll have mentors walking around for help.
* Materials:
	* This setup page you're reading is available to view online at [http://newcoder.io/pyladiessf](http://newcoder.io/pyladiessf)
	* All of the workshop materials for Saturday are straight from [http://newcoder.io/dataviz](http://newcoder.io/dataviz).
	* Everything will be cross-posted on the Meetup event page.


 
## Intro
#### READ ME PLZ!

If you get any errors that you are not familiar with, feel free to copy & paste the text of the error into Google; you are definitely not the only one to get errors! (actually, that's how a lot of developers learn!).

Everything that `looks like this` you can copy and paste into the Terminal application.

**Note**: If at any time you are struggling for more than an hour to get a single thing installed or working, go ahead to the PythonAnywhere setup instructions.  I don't want you wasting a lot of your precious time (and patience!) troubleshooting errors.  

Python Anywhere is a web application that makes it very easy to create the environment you need for Saturday's workshop. If you choose this route, please follow the instructions for PythonAnywhere below.

## Mac 

### OS X 5 or 6 
#### (Leopard and Snow Leopard)

Since these versions of Mac's operating is very outdated, you have two options:

1. Upgrade to Mavericks via [Apple](http://www.apple.com/osx/how-to-upgrade/) (I highly recommend you back up your files beforehand, though!).  Installing the operating system can take about an hour.  Backing up your system first depends on how much you are backing up, but can take from 30 minutes up to a few hours.  If you choose this route, once you are done upgrading, please follow the instructions for OS 7/8/9 below.
2. Use [PythonAnywhere](http://www.pythonanywhere.com) and follow the instructions below.

### OS X 7, 8 or 9
#### (Lion, Mountain Lion, or Mavericks)
 

1. Install the "Command Line Tools" from Apple via the [Developer's Site](https://developer.apple.com/downloads/index.action) for your particular operating version of Mac (you may need to create a free "Developer" account.)
2. Open the Terminal App: Navigate to Applications, then Utilities, and double-click on Terminal.
4. Installing the non-Python package manager for Mac, called "brew":
	1. Copy the following command into your Terminal application: `ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"` then hit enter.
	2. Once it is finished, run the command: `brew update`, followed by `brew doctor`. Read the last couple of lines of output; if either finishes with any instructions of commands to run, please run them.  Otherwise, you're okay.
5. Install the following non-Python libraries via `brew` with the following commands:
	1. `brew install libpng`
	2. `brew install freetype`
	3. `brew install pkg-config`
6. Install the Python package manager for Mac, called "pip" with the following command: `sudo easy_install pip`.  If you are prompted for your password, enter your machine login password.
7. Install the Python virtual environment manager, "virtualenv", and a popular tool for that manager, "virtualenvwrapper", with the following commands:
	1. `sudo pip install virtualenv`
	2. `sudo pip install virtualenvwrapper`
8. Setup your terminal configuration to use virtualenv and virtualenvwrapper to use every time you open your Terminal application with the following commands:
	1. `export WORKON_HOME=~/.virtualenvs`
	2. `mkdir -p $WORKON_HOME` (notice the "`$`" before `WORKON_HOME`.)
	3. `echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bash_profile` 
		1. **NOTE** If you do not use bash (e.g. zsh), replace `~/.bash_profile` with the appropriate shell profile file (e.g. `~/.zshrc` ).
	4. `source ~/.bash_profile`
		1. **NOTE** If you do not use bash (e.g. zsh), replace `~/.bash_profile` with the appropriate shell profile file (e.g. `~/.zshrc` ).
9. Continue on to "Setup Environment"

## Linux

Note: every linux has slightly different commands from the others, and perhaps slightly different package names.  If something doesn't work, best google something like "ubuntu install python" or "debian install virtualenv".

1. Open up your Terminal application.
2. Install the following packages, where if you are a Fedora/Red Hat/CentOS "flavor" linux, you replace `apt-get` with `yum`:
	1. `sudo apt-get install git`
	2. `sudo apt-get install libfreetype6*` (search for 'freetype' with your OS if apt-get/yum has issues finding the package)
	3. `sudo apt-get install libpng12-dev`(search for 'libpng' with your OS if apt-get/yum has issues finding the package)
	4. `sudo apt-get install python-dev` (or it may be `python-devel`)
	5. `sudo apt-get install pip` (or it may be `python-pip`)
	6. `sudo pip install virtualenv virtualenvwrapper`
3. Save `virtualenvwrapper` script to your bash profile:
	1. `export WORKON_HOME=~/.virtualenvs`
	2. `mkdir -p $WORKON_HOME`
	3. `echo "source /etc/bash_completion.d/virtualenvwrapper" >> ~/.bash_profile`
		1. **NOTE** If you do not use bash (e.g. zsh), replace `~/.bash_profile` with the appropriate shell profile file (e.g. `~/.zshrc` ).
	4. `source ~/.bash_profile` If you get an error about not finding virtualenvwrapper, google for "virtualenvwrapper location" with your operating system. If it's located elsewhere, then edit the `~/.bash_profile` file (via `vim ~/.bash_profile` or opening it up in a text editor) and editing that last line, `source /etc/bash_completion.d/virtualenvwrapper` to the appropriate location (keep the `source` there though). Save, close, then try the `source ~/.bash_profile` again.
		1. **NOTE** If you do not use bash (e.g. zsh), replace `~/.bash_profile` with the appropriate shell profile file (e.g. `~/.zshrc` ).
4. Continue on to "Setup Environment"


## Windows

It's really difficult to setup Windows for this particular tutorial. This is because a lot of tools we're using have been geared towards Linux/Mac systems.  Bummer.

If you have virtual machine software (like VirtualBox or VMWare Fusion), go ahead and create a VM of Ubuntu 12.04 and follow the instructions for Linux above.

Otherwise, instead of causing you a lot of pain, let's use [PythonAnywhere](http://www.pythonanywhere.com).  You will need to create an account (the free tier should be enough).  Once you create an account, follow the instructions for PythonAnywhere below.

## PythonAnywhere

Signing up is required, but you can use the free account.  Go ahead and navigate to "sign up", and create a "Beginner Account".  

**NOTE**: Unfortunately, typical copy & paste does not work with this website.  You will have to type out each command. Bummer :(


Once you have verified your account, continue on:

1. If prompted with "what's next?", click on "I don't want any help!". [Pic](http://glui.me/?i=prdt4sc04v71c9p/2014-02-05_at_7.12_PM_2x_(1).png/)
2. Under "Start a new console", select "Bash". [Pic](http://glui.me/?i=jtwi8vrqkukbrus/2014-02-05_at_7.14_PM_2x.png/)
3. Follow the following commands to setup virtualenvs:
	1. `export WORKON_HOME=~/.virtualenvs`
	2. `mkdir -p $WORKON_HOME` (notice the "`$`" before `WORKON_HOME`.)
	3. Edit your `.bashrc` file with Vim:
		1. `vim ~/.bashrc`
		2. Press SHIFT+O (capital O)
		3. On the second line, type `source /usr/local/bin/virtualenvwrapper.sh`
		4. Press `esc`, then `:`, then `w` then `q` and `Enter`.  You should be back in the Bash Console (it'll appear at the very bottom).
	4. Lastly, `source ~/.bashrc`
4. Create a virtual environment for the workshop with the following command: `mkvirtualenv DataVizProj  --system-site-packages`.  Should should now see `(DataVizProj)` in front of your Terminal prompt (e.g. `(DataVizProj) ~ $`). That means your environment is "activated". If you turn off your computer or close the Terminal application window, to re-activate the virtual environment, you can run `workon DataVizProj`.  To deactivate the virtual environment when you're done, run `deactivate`.  **NOTE**: we use `--system-site-packages` because PythonAnywhere already has both `numpy` and `matplotlib` packages, which are needed for our workshop on Saturday.
5. With the virtualenv `DataVizProj` activated, run the following command: `pip install geojson`.
6. Get the code for Saturday's workshop with the following commands in the Terminal application:
	1. `cd`
	2. `git clone https://github.com/econchick/new-coder.git`
	3. If you run `ls`, you should see `new-coder` folder there, along with what PythonAnywhere has put in your Home directory (Dropbox, README.txt)   
7. You can log out and log back in, and the Bash console should still be there, ready for you when you return. Click on the "Bash Console ######" link to get back to your console [Pic](http://glui.me/?i=wt534zxq6vkepw0/2014-02-05_at_7.26_PM_2x_(1).png/).  **NOTE**: Be sure you know how to get back to your console!  I suggest logging out of PythonAnywhere, logging back in, returning to your Console, and see if your `DataVizProj` virtual environment is "activated".  If it's not, be sure you know how to activate it! (hint: `workon DataVizProj`).
8. Continue onto Check Your Environment below.


## Setup Environment

1. Create a virtual environment for the workshop with the following command: `mkvirtualenv DataVizProj`.  Should should now see `(DataVizProj)` in front of your Terminal prompt (e.g. `(DataVizProj) ~ $`). That means your environment is "activated". If you turn off your computer or close the Terminal application window, to re-activate the virtual environment, you can run `workon DataVizProj`.  To deactivate the virtual environment when you're done, run `deactivate`. 
2. With your `DataVizProj` environment activated, install the necessary Python libraries for tomorrow's workshop with the following commands:
	1. `pip install numpy`
	2. `pip install matplotlib`
	3. `pip install geojson`
3. Get the code for Saturday's workshop with the following commands in the Terminal application:
	1. `cd`
	2. `git clone https://github.com/econchick/new-coder.git`
	3. If you run `ls`, you should see `new-coder` folder there, along with anything else in your Home directory, like Desktop, Downloads, etc.   
	
4. Continue onto Check Your Environment below.


## Check Your Environment

Before you go, follow these steps to make sure that everything is installed correctly.  If all is good, then I'll see you tomorrow!

1. Close your Terminal program, then reopen it.
2. In your terminal, type `workon DataVizProj` (or whatever you named your virtual environment).  
	1. **ERROR?** If you see something like `workon: command not found`, then repeat the steps above for setting up virtualenv and virtualenvwrapper (for Macs, that's Step 7.  For Linux, that is step 3.  For PythonAnywhere, that is step 3).  After, repeat the above command.
	2. **NO ERROR?** continue onto step 3.
3. In your terminal, type: `cd`.  Then type `cd new-coder`. 
	1. **ERROR?** If you get an error of "no such file or directory", repeat the steps to "get the code" (for Python Anywhere, that's step 6, for everyone else, it's step 3 in "Setup Environment").
	2. **NO ERROR?** continue onto step 4.
4. In your terminal, type `cd dataviz`.  Then type `python`.  You should see a prompt like `>>>`.  This is the Python shell.
5. Type the following command within the Python shell: `import geojson`.
	1. **ERROR?** If you get an error, type `exit()` in the Python shell, and you'll get back to your terminal.  Then type `pip install geojson`.  After, repeat `import geojson`.
	2. **NO ERROR?** If no error (you will just see `>>>` again if it was successful), continue on. Stay in the Python shell (the `>>>` prompt).
6. Type the following command within the Python shell: `import numpy`.
	1. **ERROR?** If you get an error, type `exit()` in the Python shell, and you'll get back to your terminal.  Then type `pip install numpy`.  
		1. **ERROR?** If you see errors, find a mentor to help you.
		2. **NO ERROR?** If there are no errors (pay attention to the last few lines once it's done), then start up the python shell again via `python` (you'll see `>>>`), and repeat the command `import numpy`.  Continue on to step 7 (still within the Python shell).
	2.  **NO ERROR?** If there are no errors, then continue onto step 7 within the Python shell.
7. Type the following command within the Python shell: `import matplotlib`.
	1. **ERROR?** If you get an error, type `exit()` in the Python shell, and you'll get back to your terminal.  Then type `pip install matplotlib`.  
		1. **ERROR?** If you see errors, find a mentor to help you.
		2. **NO ERROR?** If there are no errors (pay attention to the last few lines once it's done), then start up the python shell again via `python` (you'll see `>>>`), and repeat the command `import matplotlib`.  
	2. **NO ERROR?** If there are no errors, then you are **DONE!** You can go home!
		
