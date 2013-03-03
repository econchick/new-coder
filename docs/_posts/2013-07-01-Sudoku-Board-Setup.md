---
layout: post.html
title: "Part 1: Sudoku Board Setup"
tags: [gui]
---

Walkthrough of setting up our Sudoku Board using Tkinter.

### Planning out our Sudoku game

When thinking of Sudoku, we know that we must have some logic to automatically check the math of our input numbers to see if every horizontal row and vertical column, as well 3x3 box, contains all digits from 1 through 9. This is the logic of the game.

When running our Sudoku game, we want to take in arguments of the level of came that we want to play (n00b, l33t, or debug), as well as the board number we wish to play (if any).  We will need to have a function that parses these arguments.

Of course, we'll need a visual interface to play the game - a GUI (Graphical User Interface). We'll need to create a separate class for drawing our Sudoku board, and we will use the Tkinter library.

Last, we'll write some tests to make sure we've covered the initialization of the Sudoku board, the logic of the Sudoku, etc.

### Defining application specific errors

We define our own Exception because we want to create error handling that's specific to our Sudoku applcation, rather than file I/O exceptions, or database exceptions, etc. This is all we need to create our own exception:

```python

class SudokuError(Exception):
    """
    An application specific error.
    """
    pass

```

In the future, we will use this error class and pass our own error message when we try to catch any errors when creating our Sudoku game.

### Parsing Command-line Arguments

Python's standard library has an `argparse` module that will help us capture command-line arguments and assign them to the appropriate variables.

``python
import argparse


def parse_arguments():
    """
    Parses arguments of the form:
        sudoku.py <level name> [board number]
    Where `level name` must be in the LEVELS list and `board number` must be
    a positive integer.
    """
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--level",
                            help="Level name.",
                            type=str,
                            choices=LEVELS,
                            required=True)
    arg_parser.add_argument("--board",
                            help="Board number. Must be a positive integer.",
                            type=check_negative,
                            default=-1)

    # Returns a dictionary of keys = argument flag, and value = argument
    args = vars(arg_parser.parse_args())
    return args['level'], args['board']
```

You can read more about Python's argparse module by working through this [howto](http://docs.python.org/2/howto/argparse.html). Basically, `argparse` allows us to define the usage of arguments for the command line, as well as setting up how many arguments to expect (`add_argument`), the flags for the arguments (`--level`), defaults (`default=-1`), etc, as well as returning the exact parsed argument we want, `args['level']` and `args['board']`.

You'll notice in the second argument, `--board`, callese the `check_negative` function. This is just to check in case a user passes a negative number for a board number (only positive numbers are allowed):

```python
def check_negative(value):
    """
    Checks if value is a positive integer.
    Throws ArgumentTypeError if not.
    """
    ivalue = int(value)
    if ivalue < 0:
        raise argparse.ArgumentTypeError("%s is an invalid positive int value"
                                         % value)
    return ivalue
```

### User Interface Setup

Now we'll actually setup the board that the user will interact with.  Since we are using Tkinter, we'll need to import some objects to help us draw the board:

```python
from Tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM
```

We'll also define some global variables for our UI class beforehand:

```python
import argparse
from Tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM

MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board
```
