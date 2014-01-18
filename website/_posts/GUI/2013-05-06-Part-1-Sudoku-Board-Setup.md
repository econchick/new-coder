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

You'll notice in the second argument, `--board`, calls the `check_negative` function. This is just to check in case a user passes a negative number for a board number (only positive numbers are allowed):

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

We'll now define a class for our UI, `SudokuUI(Frame)`, and go through each function.

```python
class SudokuUI(Frame):
    """
    The Tkinter UI, responsible for drawing the board and accepting user input.
    """
    def __init__(self, parent, game):
        self.game = game
        Frame.__init__(self, parent)
        self.parent = parent

        self.row, self.col = -1, -1

        self.__initUI()
```

We inherit from Tkinter's `Frame` class, and initiallize the board. 


```python
    def __initUI(self):
        self.parent.title("Sudoku")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(
            self, width=WIDTH, height=HEIGHT,
            highlightthickness=0
        )
        self.canvas.pack(fill=BOTH, side=TOP)
        clear_button = Button(
            self, text="Clear answers",
            command=self.__clear_answers
        )
        clear_button.pack(fill=BOTH, side=BOTTOM)

        self.__draw_grid()
        self.__draw_puzzle()

        self.canvas.bind("<Button-1>", self.__cell_clicked)
        self.canvas.bind("<Key>", self.__key_pressed)
```

We give our GUI the title Sudoku. 

The packer allows you to specify the relative positioning of widgets within their container. To make our lives easier it takes a qualitative relationship specification and determines the exact placement coordinates for us. A widget will appear only after its geometry is specified. In this case, when the packer’s `pack()` method is applied to it. We use the packer options fill, expand and side. You can learn more about the packer options [here](http://effbot.org/tkinterbook/pack.htm).

We first create the `Canvas` widget, a rectangular area intended for drawing pictures or other complex layouts. On it we can place graphics, text, widgets, or frames. We then create a `Button` widget with the text Clear Answers. When it is clicked, `clear_answers()` is called. We then call `draw_grid()` and `draw_puzzle()`.

The last two lines use the concepts of bindings and events. We specify an event like `"<Button-1>"` that always triggers a certain function.`<Button-1>` corresponds to clicking on the mouse. Functions called in this way are commonly known as callbacks. You can learn more about bindings and events by reading the [documentation](http://docs.python.org/2/library/tkinter.html#bindings-and-events). 

```python
def __draw_grid(self):
        """
        Draws grid divided with blue lines into squares 3x3
        """
        for i in xrange(10):
            color = "blue" if i % 3 == 0 else "gray"

            x0 = MARGIN + i * SIDE
            y0 = MARGIN
            x1 = MARGIN + i * SIDE
            y1 = HEIGHT - MARGIN
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

            x0 = MARGIN
            y0 = MARGIN + i * SIDE
            x1 = WIDTH - MARGIN
            y1 = MARGIN + i * SIDE
            self.canvas.create_line(x0, y0, x1, y1, fill=color)
```
We draw the Sudoku grid. The method `create_line(x0, y0, x1, y1, ..., xn, yn, option, ...)` creates a line object that goes through a series of points on the Canvas.  You can read more about the different Canvas objects [here](http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/canvas.html)

```python
def __draw_puzzle(self):
        self.canvas.delete("numbers")
        for i in xrange(9):
            for j in xrange(9):
                answer = self.game.answer[i][j]
                if answer != 0:
                    x = MARGIN + j * SIDE + SIDE / 2
                    y = MARGIN + i * SIDE + SIDE / 2
                    original = self.game.puzzle[i][j]
                    color = "black" if answer == original else "slate gray"
                    self.canvas.create_text(
                        x, y, text=answer, tags="numbers", fill=color
                    )
```

We first delete all existing numbers on the board. We then iterate through all the cells in the board and find the ones whose value in the answer list is nonzero. You will find out later that the board files have zeros in the cells that are empty when the game starts. That is why the cell with nonzero values `black` text while the remaining cells have `slate gray` text. A `tag` is a string you can associate with objects on the `Canvas`. `Tags` are useful because they allow you to perform operations on all the objects with the same tag, such as changing their color or deleting them.

`draw_puzzle()` is called when the board is initialized, when a key is pressed and when the user clears their answers. 

```python
def __draw_cursor(self):
        self.canvas.delete("cursor")
        if self.row >= 0 and self.col >= 0:
            x0 = MARGIN + self.col * SIDE + 1
            y0 = MARGIN + self.row * SIDE + 1
            x1 = MARGIN + (self.col + 1) * SIDE - 1
            y1 = MARGIN + (self.row + 1) * SIDE - 1
            self.canvas.create_rectangle(
                x0, y0, x1, y1,
                outline="red", tags="cursor"
            )
```

We highlight the curently selected box in red. 

```python
 def __draw_victory(self):
        # create oval
        x0 = y0 = MARGIN + SIDE * 2
        x1 = y1 = MARGIN + SIDE * 7
        self.canvas.create_oval(
            x0, y0, x1, y1,
            tags="victory", fill="dark orange", outline="orange"
        )
        # create text
        x = y = MARGIN + 4 * SIDE + SIDE / 2
        self.canvas.create_text(
            x, y,
            text="You win!", tags="victory",
            fill="white", font=("Arial", 32)
        )
```

When the user solves the puzzle an orange oval appears on the puzzle with the text "You win!".

```python
def __cell_clicked(self, event):
        if self.game.game_over:
            return
        x, y = event.x, event.y
        if (MARGIN < x < WIDTH - MARGIN and
            MARGIN < y < HEIGHT - MARGIN):
            self.canvas.focus_set()

            # get row and col numbers from x,y coordinates
            row, col = (y - MARGIN) / SIDE, (x - MARGIN) / SIDE

            # if cell was selected already - deselect it
            if (row, col) == (self.row, self.col):
                self.row, self.col = -1, -1
            elif self.game.puzzle[row][col] == 0:
                self.row, self.col = row, col
        else:
            self.row, self.col = -1, -1

        self.__draw_cursor()
```

We identify which cell the user clicks on and select the cell if it was not already selected. Otherwise we unselect the cell. 

```python
    def __key_pressed(self, event):
        if self.game.game_over:
            return
        if self.row >= 0 and self.col >= 0 and event.char in "1234567890":
            self.game.answer[self.row][self.col] = int(event.char)
            self.col, self.row = -1, -1
            self.__draw_puzzle()
            self.__draw_cursor()
            if self.game.check_win():
                self.__draw_victory()
```

We set the cell value equal to what the user inputs only when they type an integer 1-9. We then check to see if the user has solved the puzzle. If so, we call `draw_victory()`. 

```python
    def __clear_answers(self):
        self.game.set_answer_to_puzzle()
        self.canvas.delete("victory")
        self.__draw_puzzle()
```

We call `set_answer_to_puzzle()` which creates a two dimensional array of the correct answers for all the cells in the board. We then deletes all objects on the canvas with the tag victory. In our case it's just the happy orange oval with the text "You win!". We then draw the puzzle. 