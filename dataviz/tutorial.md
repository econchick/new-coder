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