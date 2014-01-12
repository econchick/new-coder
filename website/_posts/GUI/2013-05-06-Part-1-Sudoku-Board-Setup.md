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
Why is parent an argument? What does it represent?
We set self.row and self.col equal to -1 because initially no cell is selected. 


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

Sudoku is the title of the GUI. It appears on the grey top part
The packer allows you to specify the appearance of your GUI. For example, where the elements are placed.
The Canvas widget is a rectangular area intended for drawing pictures or other complex layouts. On it you can place graphics, text, widgets, or frames.
    What is a widget?
We create a button widget with the text Clear Answers. When it is clicked, self.__clear_answers is called.
We then call self.__draw_grid() and self.__draw_puzzle().
You can learn more about bindings and events by reading this [howto](http://docs.python.org/2/library/tkinter.html#bindings-and-events). Basically....

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

We draw Sudoku grid.

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

We add the provided numbers in black to the grid. The numbers the user inpus will be in grey.


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

When the user solves the puzzle....

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

This ascertains which cell the user clicks on and calls self.__draw_cursor() if the cell was not already selected. It unselects the row if it was already selected. 

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

This sets the cell value equal to what the user types only when they type an integer 1-9. It also sets the user input to self.game.answer[self.row][self.col] and redraws the puzzle with the selected curser. Now the Sudoku grid shows the new user input. Finally it checks to see if the user has now solved the puzzle. 

```python
    def __clear_answers(self):
        self.game.set_answer_to_puzzle()
        self.canvas.delete("victory")
        self.__draw_puzzle()
```

This deletes all user submitted answers....
Uses set_answer_to_puzzle() from SudokuGame
Deletes everything on the canvas with tag="victory" ????
And then dras the puzzle