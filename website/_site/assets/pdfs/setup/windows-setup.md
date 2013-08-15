# Setting up your Windows machine

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

1. Go here: `http://python.org/ftp/python/2.7.1/python-2.7.1.msi`\[20] and click “run” if given the option. Otherwise, save it to your Desktop, then minimize windows to see your desktop, and double click on it to start the installer. Follow the installer instructions to completion.
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

<h5 style="text-align:center"><span style="color:#8c8c8c">git</span></h5>

Download git through git’s website: `http://git-scm.com/download/win`\[21].

<h5 style="text-align:center"><span style="color:#8c8c8c">C Compiler</span></h5>

Download the MinGW GCC compiler here: `http://sourceforge.net/projects/mingw/files/latest/download?source=files` \[22] and follow installation instructions here: `http://www.mingw.org/wiki/InstallationHOWTOforMinGW` \[23]

<h5 style="text-align:center"><span style="color:#8c8c8c">virtualenv + pip</span></h5>

1. From here, `http://pypi.python.org/pypi/virtualenv` \[24], under Installation, see “You can just grab the single file virtualenv.py ..”. Right-click and save-as and place in the Scripts folder that we earlier added to system PATH.
2. From the command line, `cd` into the directory that you want to save your Python work. **IMPORTANT TIP**: Do not create or use a directory that has spaces in the name. For instance, ‘Python Projects’ is not good, but ‘PythonProjects’ is fine.
3. Within your Python project directory, type: `virtualenv.py dataviz`. A virtual environment called “dataviz” has been created, and now lives in your Python projects directory. This also installs pip: pip is a tool that is used to install Python packages
4. You will now need to activate the virtual environment by typing in your command line: `dataviz\Scripts\activate.bat`.  You should see something like this:  `(dataviz) C:\PythonProjects>`
5. To stop working in the virtual environment, type the following in your command line: `dataviz\Scripts\deactivate.bat`.  You will need to run the activate script again (stated in #4) to start up the virtual environment.


## Text Editor

If you already have a text editor that you like to use, great! 

If not, I would suggest grabbing Sublime Text 2\[25].  It’s free, and very user-friendly, especially for the beginner.

Now continue on to “Test your setup”.
