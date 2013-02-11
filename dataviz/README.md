## Data Visualization

### Project
To parse data from a CSV or Excel file and plot it with matplotlib. Examples include: parsing local crime data and visualizing how often crime happens on Mondays versus Thursdays, etc.


### Initial Requirements:
* [Python 2.x](http://www.python.org/download/releases/2.7.3/)
* [git](http://git-scm.com/downloads)
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

* _Note_: If you are running zsh, check out [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh). You can easily activate <code>virualenv</code> and <code>virtualenvwrapper</code> as a plugin in your `.zshrc` file.

### To Run
Within your terminal

* `$ cd` to get to your 'Home' directory
* `$ mkdir Projects && cd Projects` to create a new 'Projects' folder and move to that directory. You can name it whatever you want, just remember what you named it, and where it is.
* `$ git clone https://github.com/econchick/new-coder.git` This clones the New Coder project into the directory you're currently in, which is Projects (unless you named it something else).
* `$ cd new-coder/dataviz` Change into the Data Viz project.
* `$ mkvirtualenv DataVizProj` Make a virtual environment specific to your Data Viz project. You should see (DataVizProject) before your prompt, now.
* `(DataVizProject) $ pip install -r requirements.txt` Now installing package requirements for this project. Your virtual environment will store the required packages in a self-contained area to not mess up with other Python projects.

#### Virtual Env Practice
Just to show the ease of virtualenv and virtualenvwrapper:
* `(DataVizProject) $ deactivate` You've deactivated your virtual environment. You will not have access to those packages we've downloaded until we reactivate the virtual environment again.
* `$ workon DataVizProject` The virtual environment now is reactivated. The packages you previously installed are now accessible. You should see (DataVizProject) before your prompt again.
* `(DataVizProject) $ pip freeze` This will show you the installed packages in this virtual environment.

**Don't forget** to [deactivate](#virtual-env-practice) your virtual environment after you're all done!

#### Full Source
Within your terminal:

* `(DataVizProject) $ cd new-coder/dataviz/lib/full_source`
* `(DataVizProject) $ python dataviz.py --csvfile=<absolute path to csv file> --type=[Days, Type, Map] --delimiter=<csv file delimiter>`


#### Tutorial Parts
Within your terminal:
* `(DataVizProject) $ cd new-coder/dataviz/lib/tutorial_source`
* Open the desired file (parse.py, graph.py, or map.py) in a text editor
* Edit the `my_file` variable to the full path of your csv file
* Save and return to your terminal
* `(DataVizProject) $ python [parse.py | graph.py | map.py ]`


