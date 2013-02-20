## Data Visualization Tutorial


### Initial Requirements:
* [Python 2.x](http://www.python.org/download/releases/2.7.3/)
* [git](http://git-scm.com/downloads)
* [virtualenv](http://pypi.python.org/pypi/virtualenv) You can either download directly, or:
	* Mac: ` $ sudo easy_install virtualenv`
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

### Setup (if you have not done so from the [README](https://github.com/econchick/new-coder/blob/master/dataviz/README.md))
Within your terminal
* `$ cd` to get to your 'Home' directory
* `$ mkdir Projects && cd Projects` to create a new 'Projects' folder and move to that directory. You can name it whatever you want, just remember what you named it, and where it is.
* `$ git clone https://github.com/econchick/new-coder.git` This clones the New Coder project into the directory you're currently in, which is Projects (unless you named it something else).
* `$ cd new-coder/dataviz` Change into the Data Viz project.
* Make sure you've installed [virtualenv-wrapper](http://pypi.python.org/pypi/virtualenvwrapper) and followed the steps above from [Initial Requirements](#initial-requirements) to set up your Terminal correctly.  More information can be find at virtualenv-wrapper's [docs](http://virtualenvwrapper.readthedocs.org/en/latest/).
* `$ mkvirtualenv DataVizProj` Make a virtual environment specific to your Data Viz project. You should see (DataVizProject) before your prompt, now.
* `(DataVizProject) $ pip install -r requirements.txt` Now installing package requirements for this project. Your virtual environment will store the required packages in a self-contained area to not mess up with other Python projects.

### Part I: Parsing

**Module Location:** `new-coder/dataviz/lib/tutorial_source/parse.py`

#### Module Setup

- Open up `parse.py`.
- Notice the first two lines - the first defines the type of language (Python)
that this file is, and that the Python interpreter should use UTF-8 encoding as
opposed to ASCII (default), Latin-1, or other encodings.

		1	#!/usr/bin/python
		2	# -*- coding: utf-8 -*-


- [Lines 4 - 15](https://github.com/econchick/new-coder/blob/master/dataviz/lib/tutorial_source/parse.py#4) is an introduction to the module, as well as any copyright and/or license information.
- In order to read a CSV/Excel file, we have to import the csv module from Python's standard library.

		17	import csv


- <code>[MY_FILE](https://github.com/econchick/new-coder/blob/master/dataviz/lib/tutorial_source/parse.py#21)</code> is defining a global - notice how it's all caps. Included in this repo is a sample file to which this variable is assigned.

#### The Parse Function

- In defining the function, we know that we want to give it the CSV file, as well as the delimiter in which the CSV file uses to delimit each element/column.
```python
def parse(raw_file, delimiter):
```

- We also know that we want to return a [JSON](http://en.wikipedia.org/wiki/JSON)-like object. A JSON file/object is just a collection of dictionaries, much like Python's dictionary.
```python
def parse(raw_file, delimiter):

		return parsed_data
```

- Let's be good coders and write a documentation-string (doc-string) for future folks that may read our code. Notice the triple-quotes:
```python
def parse(raw_file, delimiter):
		"""Parses a raw CSV file to a JSON-line object"""

		return parsed_data
```
- What we have now is a pretty good skeleton - we know what parameters the function will take (`raw_file` and `delimiter`), what it is supposed to do (our """doc-string"""), and what it will return, `parsed_data`. Notice how the parameters and the return value is descriptive in itself.
- Let's sketch out, with comments, how we want this function to take a raw file and give us the format that we want. First, let's open the file, and the read the file, then build the parsed_data element.
```python
def parse(raw_file, delimiter):
		"""Parses a raw CSV file to a JSON-line object"""

		# Open CSV file

		# Read CSV file

		# Build a data structure to return parsed_data

		return parsed_data
```
- Thankfully, there are a lot of built-in methods that Python has that we can use to do all the steps that we've outlined with our comments.  The first one we'll use is `open()` and pass `raw_file` to it, which we got from defining our own parameters in the `parse()` function:
```python
		opened_file = open(raw_file)
```
- So we've told Python to open the file, now we have to read the file. We have to use the CSV module that we [imported earlier](#module-setup):
```python
		csv_data = csv.reader(opened_file, delimiter=delimiter)
```
- Here, `csv.reader()` is a function of the CSV module. We gave it two parameters: opened_file, and delimiter. It's easy to get confused when parameters and variables share names. In `delimiter=delimiter`, the first 'delimiter' is referring to the parameter that `csv.reader()` needs; the second 'delimiter' refers to the parameter that our `parse()` function takes in.
- Just to quickly put these two lines in our `parse()` function: 
```python
def parse(raw_file, delimiter):
		"""Parses a raw CSV file to a JSON-line object"""

		# Open CSV file
		opened_file = open(raw_file)

		# Read CSV file
		csv_data = csv.reader(opened_file, delimiter=delimiter)

		# Build a data structure to return parsed_data

		return parsed_data
```
**Note:** For the curious - the csv_data object, in Python terms, is now a generator. In simple terms, this means we can iterate over each element in csv_data later.

- Alright - the building of the data structure might seem tricky. The best way to start off is to set up an empty Python list to our `parsed_data` variable so we can add every row of data that we will parse through.
```python
		parsed_data = []
```
- Good - we have a good data structure to add to. Now let's first address our column headers that came with the CSV file. They will be the first row, and we'll asign them to the variable `fields`:
```python
		fields = csv_data.next()
```
**Note:** For the curious - we were able to call the .next() method on csv_data because it is a generator.

- Let's loop over each row now that we have the headers properly taken care of. With each loop, we will add a dictionary that maps a field (those column headers) to the value in the CSV cell.
```python
		for row in csv_data:
			parsed_data.append(dict(zip(fields, row)))
```
Here, we iterated over each row in the csv_data item.  With each loop, we appended to the list,`parsed_data` a dictionary.  We use Python's built-in `zip()` function to zip together field -> value to make our dictionary of every row.

- Now let's put the function together:
```python
def parse(raw_file, delimiter):
		"""Parses a raw CSV file to a JSON-like object"""
	    # Open CSV file
	    opened_file = open(raw_file)
	    # Read CSV file
	    csv_data = csv.reader(opened_file, delimiter=delimiter)
	    # Setup an empty list
	    parsed_data = []
	    # Skip over the first line of the file for the headers
	    fields = csv_data.next()
	    # Iterate over each row of the csv file, zip together field -> value
	    for row in csv_data:
	        parsed_data.append(dict(zip(fields, row)))

	    return parsed_data
```

**TODO** Add clearer text of what `parsed_data.append(dict(zip(fields, row)))` does. Remove the magic! :D

#### Using the new Parse function
Let's define a `main()` function to call our new `parse()` function:
```python
def main():
	    # Call our parse function and give it the needed parameters
	    new_data = parse(MY_FILE, ",")
	    # Let's see what the data looks like!
	    print new_data
```
We called our function `parse()` and gave it the `MY_FILE` global variable that we defined at the beginning, as well as the delimiter `","`.  We assign the function to the variable `new_data` since the `parse()` function will return a `parsed_data` object. Last - we print `new_data` to see our list of dictionaries!
<br />
One final bit - when running a Python file from the command line, Python will execute all of the code found on it. Since the following bit is True,
```python
if __name__ == "__main__":
		main()
```
it will call the `main()` function. By doing the name == main check, you can have that code only execute when you want to run the module as a program (via the command line) and not have it execute when someone just wants to import the `parse()` function itself.

#### Putting it to action
So you've written the parse function and your `parse.py` file looks like [mine](https://github.com/econchick/new-coder/blob/master/dataviz/lib/tutorial_source/parse.py). Now what?  Let's run it and parse some d*mn files!
* Be sure to have your virtualenv activated that you created earlier in [setup](#setup). Your terminal prompt should look something like this:
```bash
	(DataVizProject) $
```
* Within the `new-coder/dataviz/lib/` directory, let's make a directory for the python files you are writing with the bash command `mkdir <Directory_Name>`. The `ls` command will show you the list of what the current directory (new-coder/dataviz/lib/) contains, and should show your new directory.  The `pwd` command shows you where exactly you are in the terminal (your path may be different). Finally, `cd` into your new directory:

```bash
	(DataVizProject) $ mkdir MySourceFiles
	(DataVizProject) $ ls
	data    full_source    MySourceFiles    tutorial_source
	(DataVizProject) $ pwd
	Users/lynnroot/MyProjects/new-coder/dataviz/lib
	(DataVizProject) $ cd MySourceFiles
```

* Go ahead and save your copy of parse.py into MySourceFiles (through Save As within your text editor). You should see the file in the directory if you return to your Terminal and type `ls`.
* To run the python code, you have to tell the Terminal to execute the parse.py file with python:

```bash
	(DataVizProject) $ python parse.py
```

* If you got a Traceback, or an error message, compare your parse.py file with new-coder/dataviz/lib/tutorial_source/parse.py. Perhaps a typo, or perhaps you don't have your virtualenv setup.
* The output from the `(DataVizProject) $ python parse.py` should look like a bunch of dictionaries in one list.  For reference, the last bit of output you should see in your terminal should look like (doesn't have to be exact data, but the structure of {"key": "value"} should look familiar):

```
	'ARRESTED, BOOKED'},{'Category': 'OTHER OFFENSES', 'IncidntNum': '030204238',
	'DayOfWeek': 'Tuesday', 'Descript': 'OBSCENE PHONE CALLS(S)', 'PdDistrict':
	'PARK', 'Y': '37.7773636900243', 'Location': '800 Block of CENTRAL AV', 'Time': 
	'18:59', 'Date': '02/18/2003', 'X': '-122.445006858202', 'Resolution': 'NONE'}]
```

* You see this output because in the ` def main()` function, you explicitly say `print new_data` which feeds to the output of the Terminal. You could, for instance, not print the `new_data` variable, and just pass the `new_data` variable to another function. Coincidently, that's what [Part II](#part-ii-graphing) and [Part III](#part-iii-map-plotting) are about!

#### Explore further

Play around with parse.py within your Python interpreter itself:
* Make sure you're in your `MySourceFiles` directory, then start the Python interpreter from there:

```bash
	(DataVizProject) $ python
	Python 2.7.2 (default, Jun 20 2012, 16:23:33)
	[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)] on darwin
	Type "help", "copyright", "credits" or "license" for more information.
	>>>
```

* Next, import your parse.py file into the interpreter. Notice there is no need to include the .py portion when importing:

```bash
	>>> import parse
	>>>
```

* If all things go well with `import parse` you should just see the `>>>` prompt. If there's an error, perhaps you are not in the correct directory from two steps ago.
* Play with the following commands. Notice to access any object defined in parse.py (object meaning a variable, function, etc), you must preface it with `parse`:

```bash
	>>> parse.MY_FILE
	'../data/sample_sfpd_incident_all.csv'
	>>> type(parse.MY_FILE)
	<type: 'str'>
	>>> copy_my_file = parse.MY_FILE
	>>> copy_my_file
	'../data/sample_sfpd_incident_all.csv'
	>>> type(copy_my_file)
	<type: 'str'>
```

* So we made a what seems like a copy. Not so! check it out:

```bash
	>>> id(copy_my_file)
	4404350288
	>>> id(parse.MY_FILE)
	4404350288
	>>>
```

* Those numbers from calling the `id()` function reflect where the variable is saved in the computer's memory.  Since they are the _same_ number, Python has set up a pointer from `copy_my_file` to the same location that `parse.MY_FILE `was saved. No need to allocate new memory for the same variable.

* Let's play with the parser function a bit:

```bash
	>>> new_data = parse.parse(copy_my_file, ",")
	>>> type(new_data)
	<type: 'list'>
	>>> type(new_data[0])
	<type: 'dict'>
	>>> type(new_data[0]["DayOfWeek"])
	<type: 'str'>
	>>> new_data[0].keys()
	['Category', 'IncidntNum', 'DayOfWeek', 'Descript', 'PdDistrict', 'Y', 'Location', 'Time', 'Date', 'X', 'Resolution']
	>>> new_data[0].values()
	['FRAUD', '030203898', 'Tuesday', 'FORGERY, CREDIT CARD', 'NORTHERN', '37.8014488257836', '2800 Block of VAN NESS AV', '16:30', '02/18/2003', '-122.424612993055', 'NONE']
	>>> for dict_item in new_data:
	...   print dict_item["Descript"]
	...
	DRIVERS LICENSE, SUSPENDED OR REVOKED
	LOST PROPERTY
	POSS OF LOADED FIREARM
	<--snip-->
	BATTERY
	OBSCENE PHONE CALLS(S)
	>>>
```

* Here we checked ot the type of data that gets returned back to use from the parse function, as well as ways to simply check out what is the contents of the parsed data.
* You can continue to play around; try `>>> help(parse.parse)` to see our docstring, see what happens if you feed the parse function a different file, delimiter, or just a different variable. Challenge yourself to see if you can create a new file to save the parsed data, rather than just a variable.  The example in the [python docs](http://docs.python.org/2/library/stdtypes.html#file.close) may help.

### Part II: Graphing

**Module Location:** `new-coder/dataviz/lib/tutorial_source/graph.py`

#### Module Setup

- Simililar as before, when you upoen up `graph.py`, you'll see the language and encoding setup, as well as an introduction to the module itself. 
- [Lines 14 - 18](https://github.com/econchick/new-coder/blob/master/dataviz/lib/tutorial_source/graph.py#14) are the libraries we import. Notice how the import statements are in alphabetical order. The general rule of ordering imports, in alphabetical order:
	1. Standard Library modules
	2. External/third party packages/modules
	3. Internal/self-written modules
- When importing, we can also give the object we're importing whatever name we want because we're lazy programmers. When we `import matplotlib.pyplot as plt` we're essentially renaming the `pyplot` object (which FYI is `<type: 'module'>`) of `matplotlib` as `plt`. You don't have to name it plt, but it's a handy trick when you want to access different objects that the `pyplot` module has, as you'll see later.

#### Intro to numpy & matplotlib

**TODO**

#### Review: Parse Function

- Once again, you see the `MY_FILE` as a global variable that points to the sample data file that's included in the repository. 
- In a quick review of [Part I: Parse](#the-parse-function) - tutorial comments removed - we see that the `parse()` function still takes in two parameters: `raw_file` and `delimiter`. The process of the `parse()` function is as follows:
	1. Open the raw file.
	2. Read the CSV file with the appropriate delimiter.
	3. Initialize an empty list which will be returned by the function.
	4. Grab the first row of the CSV file, the headers/column names, and assign them to the `fields` variable, which will be a list.
	5. Iterate over each row in the CSV file, mapping column headers -> row values, and add to our list we initialized in step 3.
	6. Return the `parsed_data` variable.
- We include the parse function here so we build on the process of parse -> plot.  We need to parse the data into the list of dictionaries so that we can easily tell matplotlib what and how to plot. We could, however, imported it from parse.py. As a challenge to you, try editing away the parse function in `graph.py` and import it from `parse.py`.

#### Visualize Functions
Let's first take a look at a chuck of data that we just parsed to get a better idea of what sort of data we're working with:

```bash
	{
	'Category'   : 'ASSAULT', 
	'IncidntNum' : '030204181', 
	'DayOfWeek'  : 'Tuesday', 
	'Descript'   : 'BATTERY', 
	'PdDistrict' : 'CENTRAL', 
	'Y'          : '37.7981847618287', 
	'Location'   : '300 Block of COLUMBUS AV', 
	'Time'       : '18:15', 
	'Date'       : '02/18/2003', 
	'X'          : '-122.407069627873', 
	'Resolution' : 'ARREST, BOOKED'
	},
```

By looking at a snippet of data, we can understand how we can play/visualize it.  The kind of data we are working with is where one entry equals an incident that the San Francisco Police recorded. The following two functions are just two ways of playing with the data, but note that these functions are specific to _our_ data.

**Disclaimer**: As with understanding statistics, correlation does _not_ mean causation.  This is a small sample size, not current, and it's from the point of view of officers reporting incidents.  Take everything with a grain of salt!

##### Visualize Days Function
1. As we read from the docstring, this will give us a visualization of data by the day of the week.  For instance, are SF policy officers more likely to file incidents on Monday versus a Tuesday? Or, tongue-in-cheek, should you stay in your house Friday night versus Sunday morning?
2. You'll also notice that the `def visualize_days()` function does not take any parameters. An option to explore would be to pass this function already-parsed data. If you feel up to it after understanding this function, explore redefining the function like so: `def visualize_days(parsed_data)`.
3. Let's walk through this function like we did the parse function.  Below is the walk through of comments for the code that we will want to write:
```python
def visualize_days():
    """Visualize data by day of week"""
    # grab our parsed data that we parsed earlier

    # make a new variable, 'counter', from iterating through each line of data in the parsed data, and count how many incidents happen on each day of the week

    # separate the x-axis data (the days of the week) from the 'counter' variable from the y-axis data (the number of incidents for each day)

    # with that y-axis data, assign it to a matplotlib plot instance

    # make a tuple of labels to be assigned to the x-axis

    # create the amount of ticks needed for our x-axis, and assign the tuple from earlier for labeling the x-axis

    # show the plot!
```
4. Working through the first in-line comment should force you to recall our parse function. How do we get a parsed data object that is returned from our parse function to a variable? Well thankfully we still have the parse function in our `graph.py` file so we can easily access it's parsing-abilities! Like so:

```python
def visualize_days():
    """Visualize data by day of week"""
    # grab our parsed data that we parsed earlier
    data_file = parse(MY_FILE, ",")
```

5. Notice how we assign data_file to our parse function, and the parameters we feed through our parse functions are `MY_FILE` and a comma-delimiter. Because we know the parse function returns `parsed_data`, we can expect that `data_file` will be that exact return value.

6. This next one is a little tricky, and not very intuitive at all.  Remember earlier, we imported Counter from the module `collections`. This is demonstrative of Python's powerful standard library. Here, Counter behaves very similarly to Python's dictionary structure (because under the hood, the Counter class inherits from dictionary).  What we will do with Counter is iterate through each line item in our `data_file` variable (since it's just a list of dictionaries), grabbing each key labelled "DayOfWeek". What the Counter does is everytime it sees the "DayOfWeek" key set to a value of "Monday", it will give it a tally; same with "DayOfWeek" key set to "Tuesday", etc. This works great for very well structured data.

```python
def visualize_days():
    """Visualize data by day of week"""
    # grab our parsed data that we parsed earlier
    data_file = parse(MY_FILE, ",")
    # make a new variable, 'counter', from iterating through each line of data
    #in the parsed data, and count how many incidents happen on each day of the week
    counter = Counter(item["DayOfWeek"] for item in data_file)
```
7. Notice, within Counter(...) we have an interesting loop construct, `item ["DayOfWeek"] for item in data_file`. This is called a list comprehension. You can read it as, "count every dictionary value of every dictionary key set to 'DayOfWeek' for every line item in data_file." A list comprehension just a for-loop put in a more elegant, "Pythonic" way. **Challenge yourself:** write out a for-loop for our `counter` variable.

##### Visualize Type Function

### Part III: Map Plotting

### Extended

#### Real-life Usage

#### Where to go from here