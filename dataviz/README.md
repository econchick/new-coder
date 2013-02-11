## Data Visualization

### Project
To parse data from a CSV or Excel file and plot it with matplotlib. Examples include: parsing local crime data and visualizing how often crime happens on Mondays versus Thursdays, etc.


### Initial Requirements:
* [Python 2.x](http://www.python.org/download/releases/2.7.3/)
* [git](http://git-scm.com/downloads)
* [pip](http://pypi.python.org/pypi/pip)

### To Run
Within your terminal

* `$ git clone https://github.com/econchick/new-coder.git`
* `$ cd new-coder/dataviz`
* `$ pip install -r requirements.txt`


#### Full Source
Within your terminal:

* `$ cd new-coder/dataviz/lib/full_source`
* `$ python dataviz.py --csvfile=<absolute path to csv file> --type=[Days, Type, Map] --delimiter=<csv file delimiter>`


#### Tutorial Parts
Within your terminal:
* `$ cd new-coder/dataviz/lib/tutorial_source`
* Open the desired file (parse.py, graph.py, or map.py) in a text editor
* Edit the `my_file` variable to the full path of your csv file
* Save and return to your terminal
*`$ python [parse.py | graph.py | map.py ]`