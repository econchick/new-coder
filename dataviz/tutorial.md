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
We called our function `parse()` and gave it the `MY_FILE` global variable that we defined at the beginning, as well as the delimiter `","`.  We assign the return value of the function to the variable `new_data` since the `parse()` function will return a list. Last - we print `new_data` to see our list of dictionaries!
<br />
One final bit - when running a Python file from the command line, Python will execute all of the code found on it. Since the expression in the if statement evaluates to True,
```python
if __name__ == "__main__":
		main()
```
it will call the `main()` function. By doing the __name__ == "__main__" check, you can have that code only execute when you want to run the module as a program (via the command line) and not have it execute when someone just wants to import the `parse()` function itself.

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
* To exit out of the Python shell, press `CTRL-D`.
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
- In a quick review of [Part I: Parse](#the-parse-function) we see that the `parse()` function still takes in two parameters: `raw_file` and `delimiter`. The process of the `parse()` function is as follows:
	1. Open the raw file.
	2. Read the CSV file with the appropriate delimiter.
	3. Initialize an empty list which will be returned by the function.
	4. Grab the first row of the CSV file, the headers/column names, and assign them to the `fields` variable, which will be a list.
	5. Iterate over each row in the CSV file, mapping column headers -> row values, and add to our list we initialized in step 3.
	6. Return the `parsed_data` variable.
- We include the parse function here so we build on the process of parse -> plot.  We need to parse the data into the list of dictionaries so that we can easily tell matplotlib what and how to plot. We could, however, import it from parse.py. As a challenge to you, try editing away the parse function in `graph.py` and import it from `parse.py`.

#### Visualize Functions
Let's first take a look at a chunk of data that we just parsed to get a better idea of what sort of data we're working with:

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
* As we read from the docstring, this will give us a visualization of data by the day of the week.  For instance, are SF policy officers more likely to file incidents on Monday versus a Tuesday? Or, tongue-in-cheek, should you stay in your house Friday night versus Sunday morning?
* You'll also notice that the `visualize_days()` function does not take any parameters. An option to explore would be to pass this function already-parsed data. If you feel up to it after understanding this function, explore redefining the function like so: `def visualize_days(parsed_data)`.
* Let's walk through this function like we did the parse function.  Below is the walk through of comments for the code that we will want to write:
```python
def visualize_days():
    """Visualize data by day of week"""
    # Grab our parsed data that we parsed earlier

    # Make a new variable, 'counter', from iterating through each line of data in the parsed data, and count how many incidents happen on each day of the week

    # Separate the x-axis data (the days of the week) from the 'counter' variable from the y-axis data (the number of incidents for each day)

    # With that y-axis data, assign it to a matplotlib plot instance

    # Make a tuple of labels to be assigned to the x-axis

    # Create the amount of ticks needed for our x-axis, and assign the tuple from earlier for labeling the x-axis

    # Show the plot!
```
* Working through the first in-line comment should force you to recall our parse function. How do we get a parsed data object that is returned from our parse function to a variable? Well, thankfully we still have the parse function in our `graph.py` file so we can easily access it's parsing-abilities! Like so:

```python
def visualize_days():
    """Visualize data by day of week"""
    # grab our parsed data that we parsed earlier
    data_file = parse(MY_FILE, ",")
```

* Notice how we assign data_file to our parse function, and the parameters we feed through our parse functions are `MY_FILE` and a comma-delimiter. Because we know the parse function returns `parsed_data`, we can expect that `data_file` will be that exact return value.

* This next one is a little tricky, and not very intuitive at all. Remember that earlier, we imported Counter from the module `collections`. This is demonstrative of Python's powerful standard library. Here, Counter behaves very similarly to Python's dictionary structure (because under the hood, the Counter class inherits from dictionary).  What we will do with Counter is iterate through each line item in our `data_file` variable (since it's just a list of dictionaries), grabbing each key labelled "DayOfWeek". What the Counter does is everytime it sees the "DayOfWeek" key set to a value of "Monday", it will give it a tally; same with "DayOfWeek" key set to "Tuesday", etc. This works great for very well structured data.

```python
def visualize_days():
    """Visualize data by day of week"""
    # grab our parsed data that we parsed earlier
    data_file = parse(MY_FILE, ",")
    # make a new variable, 'counter', from iterating through each line of data
    #in the parsed data, and count how many incidents happen on each day of the week
    counter = Counter(item["DayOfWeek"] for item in data_file)
```
* Notice, within Counter(...) we have an interesting loop construct, `item ["DayOfWeek"] for item in data_file`. This is called a list comprehension. You can read it as, "count every dictionary value of every dictionary key set to 'DayOfWeek' for every line item in data_file." A list comprehension is just a for-loop put in a more elegant, "Pythonic" way. **Challenge yourself:** write out a for-loop for our `counter` variable.

* The counter object is a dictionary with the keys as days of the week, and values as the count of incidents per day. In order for our visualization to make sense, we need to make sure the order that we plot the data makes sense.  For instance, it would make no sense to plot our data in alphabetical order rather than order of the days of the week. We can force our order by separating keys and values to lists:

```python
    # separate the x-axis data (the days of the week) from the 'counter' variable from the y-axis data (the number of incidents for each day)
    data_list = [
                  counter["Monday"], counter["Tuesday"],
                  counter["Wednesday"], counter["Thursday"],
                  counter["Friday"], counter["Saturday"],
                  counter["Sunday"]
                ]
    day_list = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]
```

* Here, `data_list` takes each key of `counter` to grab the value associated with each day.  Because we manually write out each `counter` key, we force the order that we want. **Note:** a dictionary does _not_ preserve order, but a list does; this is why we're electing to manually key into each value of a dictionary to make a list of each value.

* The `day_list` is just a list of strings that we will use for our x-axis labels.

* We now tell `matplotlib` to use our `data_list` as data points to plot. The `pyplot` module, what we've renamed as `plt`, has a function called `plot()` which takes a list of data points to plot on the y-axis:

```python
    # with that y-axis data, assign it to a matplotlib plot instance
    plt.plot(data_list)
```

* If you are curious about the `plot()` function, type `python` in your terminal, then `import matplotlib.pyplot as plt` followed by `help(plt)` and/or `dir(plt)`. Again, to exit out of the Python shell, press `CTRL-D`. 

* Next, we'll make a tuple out of the day_list (a list of strings, each string being "Mon", "Tues", etc) and assign it to a `labels` variable:

```python
    # Create labels for our x-axis
    labels = tuple(day_list)
```
* By simply 'wrapping' tuple() around our list of strings makes will make `labels` a tuple full of strings.
* Just creating the varible `labels` for our x-axis isn't enough - we also have to assign it to our `plt` by using the method `xticks()`:

```python
    # Assign labels to the plot
    plt.xticks(range(len(data_list)), labels)
```
* We give `plt.xticks()` two parameters, one being a list and the other being our tuple, `labels`. The first parameter is `range(len(data_list))`.  Here, we call `len()` on our `data_list` variable - `len()` returns an integer, a count of the number of items in our list `data_list`. Since we have seven items in our `data_list` (**q:** why do we have seven items?), the `len()` will return 7. Now we have `range()` on our length of the `data_list`. If you feed `range()` one parameter `x`, it will produce a list of integers from 0 to `x` (not including `x`). So, deconstructed, we fed `plt.xticks()` the following: parameter 1 = `[0, 1, 2, 3, 4, 5, 6]`; parameter 2 = ("Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"). The first parameter is so matplotlib knows how many tickets it needs to place.  A final note: we had to make our `labels` variable a tuple because `plt.xticks()` only accepts tuples for labeling the x-axis.  This is because tuples are an immutable type of data structure in Python's library, meaning you can't change it (not without making a copy of the variable onto a new variable), as well as it preserves order.

* We're nearly there! So far, we've assigned our `plt` instance data with just the y-axis variables through the `plot()` method, as well as the count and string labels for the x-axis with `xticks()`. Now all we need is to render the visualization! Here we use `plt`'s `show()` method:

```python
    # Render the plot!
    plt.show()
```

* Notice we didn't finish with `return` - you can put a `return` call at the end of the function, but we aren't returning anything, per se, and because we aren't, we don't need to have the `return` call in there.

* To actually see the visualization (and to test your code), add the following (for why, refer to [parse](#using-the-new-parse-function)):

```python
def main():
    visualize_days()

if __name__ == "__main__":
    main()
```
* Next, save this file as `graph.py` into the `MySourceFiles` directory that we created earlier, and make sure you are in that directory in your Terminal by using `cd` and `pwd` to navigate as we did [before](#putting-it-to-action). Also - make sure your virtualenv is active. Now, in your Terminal, run:

```bash
(DataVizProject) $ python graph.py
```

* You should see a nice rendering of our graph:

![visualize-days](http://dl.dropbox.com/u/15999054/newcoder/dataviz/graph_days.png)


* When you're done marveling at your work, close the graph window and you should be back at your terminal.

* You can also start up a Python shell, and play around a little bit:
```bash
>>> from graph import visualize_days
>>> visualize_days() # should see the graph pop up again
>>> MY_FILE
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'MY_FILE' is not defined
>>> from graph import MY_FILE
>>> MY_FILE
'../data/sample_sfpd_incident_all.csv'
>>> parse()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'parse' is not defined
>>> from graph import parse
>>> parse()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: parse() takes exactly 2 arguments (0 given)
>>> parse(MY_FILE, ",") # should see a big list of dicts
```
* Remember that `CTRL+D` exits out of the Python shell and brings you back to where you were in the terminal. 

##### Visualize Type Function
The next function that we will walk through, `visualize_type()`, is constructed very similarly, but takes advantage of how you can manipulate the size and image of the graph. I will not rehash familiar/repetitive lines of code since a lot is similar to `visualize_days()`.

* Starting with our comment outline and function scaffolding:
```python
def visualize_type():
    """Visualize data by category in a bar graph"""
    # Grab our parsed data

    # Make a new variable, 'counter', from iterating through each line of data
    # in the parsed data, and count how many incidents happen by category

    # Set the labels which are based on the keys of our counter.
    # Since order doesn't matter, we can just use counter.keys()

    # Set exactly where the labels hit the x-axis 

    # Width of each bar that will be plotted

    # Assign data to a bar plot (similar to plt.plot()!)

    # Assign labels and tick location to x-axis

    # Give some more room so the x-axis labels aren't cut off in the graph

    # Make the overall graph/figure larger

    # Render the graph!
```

* The first three lines of code should look familiar.  Here, we're counting over "Category" rather than "DayOfWeek". And since order doesn't matter to us here, we can just use `counter.keys()` and `counter.values()` to get the items we need for plotting:

```python
    # grab our parsed data
    data_file = parse(MY_FILE, ",")

    # Same as before, this returns a dict where it sums the total
    # incidents per Category.
    counter = Counter(item["Category"] for item in data_file)

    # Set the labels which are based on the keys of our counter.
    # Since order doesn't matter, we can just used counter.keys()
    labels = tuple(counter.keys())
```

* Next we finally use a bit of numpy magic (imported as `na`):

```python
    # Set where the labels hit the x-axis
    xlocations = na.array(range(len(labels))) + 0.5
```

* We have a new variable, `xlocations`, which will be used to help place the `plt.xticks()`. We're using the `numpy.numarray` (aka `na`) module to access the `array` function. This turns the list that `range(len(labels))` would make into an array that you can manipulate a bit differently. Here, we're adding `0.5`. If you were to `print xlocations`, you would see `[0.5, 1.5, 2.5, ... , 16.5, 17.5]` where `0.5` was added to each int of the list.  You'll see why we need the `0.5` a bit later.

* TODO: Insert explanation of the below code.

```python
    # Width of each bar
    width = 0.5
    
    # Assign data to a bar plot
    plt.bar(xlocations, counter.values(), width=width)
```

* Now we assign our x- & y-ticks (should be familiar to visualize_days()):

```python
    # Assign labels and tick location to x-axis
    plt.xticks(xlocations + width / 2, labels, rotation=90)
```
* For the `plt.xticks()`, the first parameter should look similar to before, but here we're feeding three parameters: `xlocations + width / 2`, `labels`, and `rotation=90`. The first parameter will place the center of the bar in the middle of the xtick. `labels` we know already. `rotation=90` is, as you might have guess, rotates each label 90 degrees. This allows our x-axis to be more readable. You can try out another values.

* Notice how we can pass `xticks()` more parameters than we did before. If you read the [documentation](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.xticks) of that function, you can pass it `*args` and `**kwargs`, or arguments and keyword arguments. It mentions that you can pass matplotlib-defined [text properties](http://matplotlib.org/api/artist_api.html#matplotlib.text.Text) for the labels - so that would explain the `**kwargs` element there. If nothing is passed in for `rotation` then it's set to a default defined in their text properties documentation.

* Next, we just add a little bit of spacing to the bottom of the graph so the labels (like "Forgery/Counterfeiting") aren't too long. We use the `.subplots_adjust()` function. In matplotlib, you have the ability to render multiple graphs on one window/function, called subplots. With one graph, subplots can be used to adjust the spacing around the graph itself.

```python
    # Give some more room so the labels aren't cut off in the graph
    plt.subplots_adjust(bottom=0.4)
```
* I'll be honest, `0.4` was a guess-and-check. When the graph shows up, the button on the bottom, one in from the right (right next to the Save button) will show you the Subplot Configuration Tool to play with spacing.

* Nearly there - before we render the graph, the actual size of the window can be played with too. `rcParams` dictionary, explained in their [docs](http://matplotlib.org/users/customizing.html#dynamic-rc-settings), allows us to dynamically play with matplotlib's global settings. In particular, the `'figure.figsize'` key is expecting two values: height + width:

```python
    # Make the overall graph/figure larger
    plt.rcParams['figure.figsize'] = 12, 8
```

* Again - here I just played with the numbers until I got something I liked. I encourage you to put in different numbers to change the size of your graph.

* Finally, our favorite - rendering the graph!

```python
    # Render the graph!
    plt.show()
```

* A reiteration: notice we didn't finish with `return` - you can put a `return` call at the end of the function, but we aren't returning anything, per se, and because we aren't, we don't need to have the `return` call in there.

* To actually see the visualization (and to test your code), add the following (for why, refer to [parse](#using-the-new-parse-function)): 

```python
def main():
    # visualize_days() # commenting out the visualize_days() function
    visualize_type()

if __name__ == "__main__":
    main()
```
* Next, save this file as `graph.py` into the `MySourceFiles` directory that we created earlier, and make sure you are in that directory in your Terminal by using `cd` and `pwd` to navigate as we did [before](#putting-it-to-action). Also - make sure your virtualenv is active. Now, in your Terminal, run:
```bash
(DataVizProject) $ python graph.py
```

* and you should see:

![visualize-type](http://dl.dropbox.com/u/15999054/newcoder/dataviz/graph_type.png)


* When you're done marveling at your work, close the graph window and you should be back at your terminal.

* You can also start up a Python shell, and play around a little bit like we did with our `visualize_days()` code. Remember that `CTRL+D` exits out of the Python shell and brings you back to where you were in the terminal. 


### Part III: Map Plotting

It'd be kind of cool to place all the coordinates in our data on a map, wouldn't it?  Google Maps allows folks to upload KML-type documents, which is essentially a type of an XML document for displaying geographic-related data.  Google has a great KML [intro](https://developers.google.com/kml/documentation/) and [tutorial](https://developers.google.com/kml/documentation/kml_tut) for those interested. Wiki has a pretty readable [explanation](http://en.wikipedia.org/wiki/XML) of XML, and w3 has a simple [tutorial](http://www.w3schools.com/xml/) if you want to learn more (_side comment_: w3 is not the greatest for learning front-end related web development, but fine for quick references). Both KML and XML, as well as HTML and XHTML, follow the [DOM](http://en.wikipedia.org/wiki/Document_Object_Model) convention, Document Object Model. It's basically how you interact with different objects through defined functions.

As you are starting to realize the awesomeness of Python, you can assume there is an `xml` module in the standard library. How convenient!  Python's `xml.dom` module uses the DOM convention and gives us access to functions that HTML, XML, and KML will understand when we build our own KML document.

**Module Location:** `new-coder/dataviz/lib/tutorial_source/map.py`

#### Module Setup

* Here you see in lines [Lines 17 - 19](https://github.com/econchick/new-coder/blob/master/dataviz/lib/tutorial_source/map.py#17) we're importing `xml.dom.minidom` which is Python's [minimal implementation](http://docs.python.org/2/library/xml.dom.minidom.html) of DOM interface, as well as our own module, `parse` as `p`. 

* Other ways you could have done the import statements:

```python
from xml.dom import minidom
import xml.dom.minidom as m
import xml.dom
import xml

import parse
from parse import parse, MY_FILE
import parse as iLoveParsingSoMuch
```

* Of course, we're lazy programmers, so we're not going to `import parse as iLoveParsingSoMuch` because each time we want to refer to our `parse()` function in the `parse` module, we'd have to type out `iLoveParsingSoMuch.parse(iLoveParsingSoMuch.MY_FILE, ",")` - you can probably see why I elected `p`. 

* We also don't import the whole `xml` library, or `xml.dom` library for that matter. We want to run lean code, so only import the specific module that you need, or even objects (classes, functions, variables, etc) defined from within that module.

#### For the curious

* Library is a collection of packages. A package is a collection of modules. A module is one python file, so a library is a collection of python files.

* Python has a standard library already built in (standard meaning that you don't have to download extra packages, it's default within the language and you just have to import what you need), but that standard library contains many packages and modules. 

* Python will follow your import statements like a file structure. For instance, we have `new-coder/dataviz/lib/tutorial_source` - `lib` is within `dataviz`. So within Python's standard library, `minidom` is defined within `dom`, and that within `xml`. 

* A bit of a **warning**: if you try to run `map.py` outside of `new-coder/dataviz/lib/tutorial_source` without adjusting the `import parse`, you may see an `ImportError`. When making a package yourself for distribution, there are ways to avoid this issue, and you can read more in the Python [docs](http://docs.python.org/2/tutorial/modules.html#packages)


Back to the tutorial!

#### Helper Functions

We've defined two helper functions for our `create_gmap()` function: `create_document()` and `create_placemark`. I won't spend too much time on the detail of these two functions, but what I want you to understand is the concept of breaking out your code to have functions do one thing and one thing only. We don't want `create_gmap()` to get too muddled up, the main reasons being that it lends to code being far more readable, as well as testable and debuggable.

* The `create_document(title, description='')` function essentially will create/initialize a KML document. It first makes an XML document, then defines it as KML, grabs common KML attributes that are defined at `www.opengis.net` (which catalogs web resources for anyone to refer to).  Lastly, it creates meta data that we want for our map: Title and Description.

```python
def create_document(title, description=''):
    """Create the overall KML document."""

    # Initialization of an XML doc
    doc = xml.dom.minidom.Document()

    # Define as a KML-type XML doc
    kml = doc.createElement('kml')

    # Pull in common attributes and set it for our doc
    kml.setAttribute('xmlns', 'http://www.opengis.net/kml/2.2')
    doc.appendChild(kml)

    # Create common elements that Google will read/plot
    document = doc.createElement('Document')
    kml.appendChild(document)
    docName = doc.createElement('name')
    document.appendChild(docName)
    docName_text = doc.createTextNode(title)
    docName.appendChild(docName_text)
    docDesc = doc.createElement('description')
    document.appendChild(docDesc)
    docDesc_text = doc.createTextNode(description)
    docDesc.appendChild(docDesc_text)
    return doc
```

* The `createElement()` and `appendChild()` is specific to DOM functions that the `xml.dom.minidom` gives us access to.  We first create an element (either Document, name, or description), then assign that element a value if needed (title, and description, if given).  Finally, we return the initialized document.

* The `create_placemark(address)` function creates an initial XML document so we can build one placemark (equal to one piece of our data). The function actually creates the placemark data by doing the same process from earlier, `createElement` to create a type of DOM element, and assign it a value if needed (e.g. name, coordinates, description). This just returns one placemark in the correct format.

```python
def create_placemark(address):
    """Generate the KML Placemark for a given address.
    This is the function that takes the info from the
    file we parse at the end of this script"""

    # Create an initial XML document
    doc = xml.dom.minidom.Document()

    # Create elements for Placemark and add to our new doc
    pm = doc.createElement("Placemark")
    doc.appendChild(pm)
    name = doc.createElement("name")
    pm.appendChild(name)
    name_text = doc.createTextNode('%(name)s' % address)
    name.appendChild(name_text)
    desc = doc.createElement("description")
    pm.appendChild(desc)
    desc_text = doc.createTextNode('Date: %(date)s, %(description)s' % address)
    desc.appendChild(desc_text)
    pt = doc.createElement("Point")
    pm.appendChild(pt)
    coords = doc.createElement("coordinates")
    pt.appendChild(coords)
    coords_text = doc.createTextNode('%(longitude)s,%(latitude)s' % address)
    coords.appendChild(coords_text)
    return doc
```

* I want to point out the following syntax: `Date: %(date)s, %(description)s' % address)`. The parameter, `address` is passed to the function. We can access elements in that parameter (you'll see later that it's a dictionary) with Python's 'string-fu' - it has a built-in method with the `%` operator (aka Modulo) for string formatting, following the convention `format % values`. You can access values in a dictionary by calling the dictionary key in parenthesis: 

```python
>>> print '%(language)s has %(number)03d quote types.' % {"language": "Python", "number": 2}
Python has 002 quote types.
```
* You see that `(language)` is specified to be a string with the s, and `(number)` is a decimal specified by the d.  The `03` in front of the d refers to number of digits (3) and with zeros padding the number. More information can be read in the Python [docs](http://docs.python.org/2/library/stdtypes.html#string-formatting-operations).

#### Create GMap!

Now on to the good stuff.  The function `create_gmap(data_file)` uses the two helper functions to build a KML document with our data.  Again with our initial comment setup:

```python
def create_gmap(data_file):
    # Create a new KML doc with our previously-defined
    # create_document() function

    # Get the specific DOM element that we created with create_document()
    # Returns a list, so get the first element

    # Iterate over our data to create KML document
    for line in data_file:
        # Parses the data into a dictionary

        # Avoid null values for lat/long

        # Calls create_placemark() to parse line of data into KML-format

        # Adds the placemark we just created to the KML doc

    # Now that all data is parsed in KML-format, write to a file so we
    # can upload it to maps.google.com
```

* The first thing that we need to do is just to create a new KML document for us to work with. We'll use our helper function, `create_document` and pass in a title and description as parameters to create a new variable, `kml_doc`:

```python
    # Create a new KML doc with our previously-defined
    # create_document() function
    kml_doc = create_document("Crime map", "Plots of Recent SF Crimes")
```

* Next, we just want to get that specific DOM element, `"Document"` to build each placemark to. So we need to create the document, then grab the right element, coincidently named Document, so we can add placemarks to it.

```python
    # Get the specific DOM element that we created with create_document()
    # Returns a list, so call the first one
    document = kml_doc.documentElement.getElementsByTagName("Document")[0]
```

* Next, we iterate through the parsed data (`data_file`) that we fed the `create_gmap(data_file)` function and make sure we build our dictionary of data, `placemark_info` so that `create_placemark` can build a placemark out of it.

```python
    # Iterate over our data to create KML document
    for line in data_file:
        # Parses the data into a dictionary
        placemark_info = {'longitude': line['X'],
                       'latitude': line['Y'],
                       'name': line['Category'],
                       'description': line['Descript'],
                       'date': line['Date']}

        # Avoid null values for lat/long
        if placemark_info['longitude'] == "0":
            continue
```

* So for each line in our `data_file`, we take certain values of that line, `X`, `Y`, `Category`, etc, and assign it to a key.  If, for whatever instance, longitude is `0`, we'll skip over it.  The assumption is if the longitude is 0, then we can't plot it (or it will be plotted as 0,0 and screw with our map). This is a simple form of skipping over errors in the data.

* We then create the variable `placemark` by calling the `create_placemark()` function, and feeding it our dictionary, `placemark_info`.  `create_placemark()` will return an object that can easily be added to our KML document, `document`:
```python
        # Calls create_placemark() to parse line of data into KML-format
        placemark = create_placemark(placemark_info)

        # Adds the placemark we just created to the KML doc
        document.appendChild(placemark.documentElement)
```

* So looping over each line item is done, we've built our KML document, now how do we _get_ that document so we can upload it to Google Maps?  We can do that with Python's file I/O - by opening a file (if it doesn't exist, it will be created for us), and writing to that file.

```python
    # Now that all data is parsed in KML-format, write to a file so we
    # can upload it to maps.google.com
    with open('file_sf.kml', 'w') as f:
        f.write(kml_doc.toprettyxml(indent="  ", encoding='UTF-8'))
```

* This is a new loop construct: `with` - it allows us to not have to worry about closing a file; it will be done automatically for us.  More about the `with` built-in can be read [here](http://preshing.com/20110920/the-python-with-statement-by-example).

* So `with open('file_sf.kml', 'w') as f` assigns the opened file as f; it also will either open the file `file_sf.kml` or create it (**note**: it will be in your current directory unless you specify otherwise, like `Users/lynnroot/NotMyDevFolder/file_sf.kml` with absolute file paths), and give it `write` capabilities (versus read-only).

* Then we write the `kml_doc` to the file. We use the `toprettyxml()` method so that we can specify encoding and indentation, making it more readable for us.

* That's it! Now we just have that `main()` function: 
```python
def main():
    data = p.parse(p.MY_FILE, ",")

    create_gmap(data)

if __name__ == "__main__":
    main()
```

* Here we just first parse our data, then return the KML document using that parsed data.

* Next, save this file as `map.py` into the `MySourceFiles` directory that we created earlier, and make sure you are in that directory in your Terminal by using `cd` and `pwd` to navigate as we did [before](#putting-it-to-action). Also - make sure your virtualenv is active. Now, in your Terminal, run:
```bash
(DataVizProject) $ python map.py
(DataVizProject) $ ls
```
* You should see `file_sf.kml` file now! You can open it up in your text editor; a snipit should look like this:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>
      Crime map
    </name>
    <description>
      Plots of Recent SF Crime
    </description>
    <Placemark>
      <name>
        FRAUD
      </name>
      <description>
        Date: 02/18/2003, FORGERY, CREDIT CARD
      </description>
      <Point>
        <coordinates>
          -122.424612993055,37.8014488257836
        </coordinates>
      </Point>
    </Placemark>
```

* To see it up on Google maps, navigate to [maps.google.com](maps.google.com), then click the button "My Places", then "Create Map", then "Import" and select `file_sf.kml`. Go ahead and upload it and marvel in your new Google Map!

### Extended

#### Real-life Usage

#### Where to go from here








