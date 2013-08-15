# Part 0: Setup

<p style="text-align:center">Initial setup for our Data Visualization tutorial.</p>

Within your terminal/command line (note: if using Windows, your prompt will look like `C:\` rather than `$`)

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

* To make a virtual environment specific to your Data Viz project, run the following command. You should see `(DataVizProject)` before your prompt.

	```bash
	# for Linux/Mac OS X
	$ mkvirtualenv DataVizProj
	(DataVizProj)$
	# for Windows
	C:\Projects\new-coder\dataviz\virtualenv.py DataVizProj
	(DataVizProj) C:\
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
* If you have no errors (you would just see the `>>>` prompt), then you’re good to go. You can close out of the Python interpreter by pressing `CTRL+D`. If you do have errors, I’d try downloading numpy and matplotlib manually from http://scipy.org/Download and http://matplotlib.org/downloads.html, respectively.


**Continue on to Part 1: Parsing our Data &rarr;**