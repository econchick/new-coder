import argparse
import sys
import random

from Tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM

DEBUG = True  # Exceptions are raised for debugging purposes
LEVELS = ['debug', 'n00b', 'l33t']  # Available levels
MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board


class SudokuError(Exception):
    """
    An application specific error.
    """
    pass


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


def parse_arguments():
    """
    Parses arguments of the form:
        sudoku.py <level name> [board number]
    Where `level name` must be in the LEVELS list and `board number` must be
    a positive integer.
    """
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("level",
                            help="Level name.",
                            type=str,
                            choices=LEVELS,
                            nargs='?')
    arg_parser.add_argument("--board",
                            help="Board number. Must be a positive integer.",
                            type=check_negative,
                            default=-1)

    # Returns a dictionary of keys = argument flag, and value = argument
    args = vars(arg_parser.parse_args())
    return args['level'], args['board']


class SudokuUI(Frame):
    """
    The Tkinter UI, responsible for drawing the board and accepting user input.
    """
    def __init__(self, parent, game):
        self.game = game
        Frame.__init__(self, parent)
        self.parent = parent

        self.row, self.col = -1, -1

        self.initUI()

    def initUI(self):
        self.parent.title("Sudoku")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(
            self, width=WIDTH, height=HEIGHT,
            highlightthickness=0
        )
        self.canvas.pack(fill=BOTH, side=TOP)
        clear_button = Button(
            self, text="Clear answers",
            command=self.clear_answers
        )
        clear_button.pack(fill=BOTH, side=BOTTOM)

        self.draw_grid()
        self.draw_puzzle()

        self.canvas.bind("<Button-1>", self.cell_clicked)
        self.canvas.bind("<Key>", self.key_pressed)

    def draw_grid(self):
        for i in xrange(10):
            self.canvas.create_line(
                MARGIN + i * SIDE, MARGIN,
                MARGIN + i * SIDE, HEIGHT - MARGIN,
                fill="blue" if i % 3 == 0 else "gray"
            )

            self.canvas.create_line(
                MARGIN, MARGIN + i * SIDE,
                WIDTH - MARGIN, MARGIN + i * SIDE,
                fill="blue" if i % 3 == 0 else "gray"
            )

    def draw_puzzle(self):
        self.canvas.delete("numbers")
        for i in xrange(9):
            for j in xrange(9):
                answer = self.game.answer[i][j]
                original = self.game.puzzle[i][j]
                if answer != 0:
                    self.canvas.create_text(
                        MARGIN + j * SIDE + SIDE / 2,
                        MARGIN + i * SIDE + SIDE / 2,
                        text=answer, tags="numbers",
                        fill="black" if answer == original else "slate gray"
                    )

    def draw_cursor(self):
        self.canvas.delete("cursor")
        if self.row >= 0 and self.col >= 0:
            self.canvas.create_rectangle(
                MARGIN + self.col * SIDE + 1,
                MARGIN + self.row * SIDE + 1,
                MARGIN + (self.col + 1) * SIDE - 1,
                MARGIN + (self.row + 1) * SIDE - 1,
                outline="red", tags="cursor"
            )

    def draw_victory(self):
        self.canvas.create_oval(
            MARGIN + SIDE * 2, MARGIN + SIDE * 2,
            MARGIN + SIDE * 7, MARGIN + SIDE * 7,
            tags="victory", fill="dark orange", outline="orange"
        )
        self.canvas.create_text(
            MARGIN + 4 * SIDE + SIDE / 2,
            MARGIN + 4 * SIDE + SIDE / 2,
            text="You win!", tags="victory",
            fill="white", font=("Arial", 32)
        )

    def cell_clicked(self, event):
        if self.game.game_over:
            return
        x, y = event.x, event.y
        if (MARGIN < x < WIDTH - MARGIN and
            MARGIN < y < HEIGHT - MARGIN):
            self.canvas.focus_set()
            row, col = (y - MARGIN) / SIDE, (x - MARGIN) / SIDE
            if (row, col) == (self.row, self.col):
                self.row, self.col = -1, -1
            elif self.game.puzzle[row][col] == 0:
                self.row, self.col = row, col
        else:
            self.row, self.col = -1, -1

        self.draw_cursor()

    def key_pressed(self, event):
        if self.game.game_over:
            return
        if self.row >= 0 and self.col >= 0 and event.char in "1234567890":
            self.game.answer[self.row][self.col] = int(event.char)
            self.col, self.row = -1, -1
            self.draw_puzzle()
            self.draw_cursor()
            if self.game.check_win():
                self.draw_victory()

    def clear_answers(self):
        self.game.set_answer_to_puzzle()
        self.canvas.delete("victory")
        self.draw_puzzle()


class SudokuGame(object):
    """
    A Sudoku game, in charge of storing the state of the board and checking
    wether the puzzle is completed.
    """
    def __init__(self, boards_file):
        self.boards = [[]]
        for line in boards_file:
            line = line.strip()
            if len(line) != 9:
                self.boards = []
                raise SudokuError(
                    "Each line in the sudoku puzzle must be 9 chars long."
                )
            if len(self.boards[-1]) == 9:
                self.boards.append([])

            self.boards[-1].append([])

            for c in line.strip():
                if c not in "1234567890":
                    raise SudokuError(
                        "Valid characters for a sudoku puzzle must be in 0-9"
                    )
                self.boards[-1][-1].append(int(c))

        if len(self.boards[-1]) != 9:
            self.boards = []
            raise SudokuError(
                "Each sudoku puzzle must be 9 lines long"
            )

        self.puzzle = self.boards[random.randrange(len(self.boards))]
        self.set_answer_to_puzzle()

    def set_answer_to_puzzle(self):
        self.game_over = False
        self.answer = []
        for i in xrange(9):
            self.answer.append([])
            for j in xrange(9):
                self.answer[i].append(self.puzzle[i][j])

    def start(self, board_number):
        if board_number == -1:
            board_number = random.randrange(len(self.boards))
        elif board_number < 0 or board_number >= len(self.boards):
            raise SudokuError(
                "Can't find board number %d" % board_number
            )
        self.puzzle = self.boards[board_number]
        self.set_answer_to_puzzle()

    def check_block(self, block):
        return set(block) == set(range(1, 10))

    def check_row(self, row):
        return self.check_block(self.answer[row])

    def check_column(self, column):
        return self.check_block(
            [self.answer[row][column] for row in xrange(9)]
        )

    def check_square(self, row, column):
        return self.check_block(
            [
                self.answer[r][c]
                for r in xrange(row * 3, (row + 1) * 3)
                for c in xrange(column * 3, (column + 1) * 3)
            ]
        )

    def check_win(self):
        for row in xrange(9):
            if not self.check_row(row):
                return False
        for column in xrange(9):
            if not self.check_column(column):
                return False
        for row in xrange(3):
            for column in xrange(3):
                if not self.check_square(row, column):
                    return False
        self.game_over = True
        return True


if __name__ == '__main__':
    level_name, board_number = parse_arguments()

    try:
        with open('%s.sudoku' % level_name, 'r') as boards_file:
            game = SudokuGame(boards_file)
            game.start(board_number)

            root = Tk()
            ui = SudokuUI(root, game)
            root.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
            root.mainloop()
    except SudokuError, e:
        print "Puzzles file is invalid."
        if DEBUG:
            raise e
        else:
            sys.exit(1)
