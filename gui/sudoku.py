import random
import argparse
import tkMessageBox
from Tkinter import Tk, Frame, Canvas, Button, BOTH, LEFT, RIGHT

LEVELS = {
    'debug': 1,
    'n00b': 20,
    'l33t': 45,
}

FRAME_WIDTH = 440
FRAME_HEIGHT = 400
BUTTON_WIDTH = 20
BUTTON_HEIGHT = 20
CELL_WIDTH = 40
PADDING = 20

DEBUG = False


class Sudoku(object):
    def __init__(self, level=None, puzzle=None, solution=None):
        self.level = level
        self.puzzle = puzzle
        self.answer = puzzle
        self.solution = solution

    def solve(self, temp_solution=None):
        """
        Solves the puzzle.
        Each recursive call fills in a cell, until there are no blank cells left.
        """
        def same_row(i, j):
            return i / 9 == j / 9

        def same_col(i, j):
            return (i - j) % 9 == 0

        def same_block(i, j):
            return i / 27 == j / 27 and i % 9 / 3 == j % 9 / 3

        temp_solution = self.puzzle if temp_solution is None else temp_solution

        # Find an empty cell
        i = temp_solution.find('0')

        # If there are no empty cells, we have solved the puzzle
        if i == -1:
            self.solution = temp_solution
            return

        # Exclude the numbers from same row, column and block
        excluded_numbers = set()
        for j in xrange(81):
            if same_row(i, j) or same_col(i, j) or same_block(i, j):
                excluded_numbers.add(temp_solution[j])

        # Find a legal answer, fill it in the cell and recurse
        for m in '123456789':
            if m not in excluded_numbers:
                temp_solution = temp_solution[:i] + m + temp_solution[i + 1:]
                self.solve(temp_solution)

    def puzzlefy(self, temp_puzzle=None, orig_solution=None):
        """
        Creates a puzzle from the solution.
        Each recursive call removes a cell from the solution.
        Makes sure that the puzzle has a unique solution.
        Stops when it reaches the maximum number of blank cells for the chosen level.
        """
        temp_puzzle = self.solution if temp_puzzle is None else temp_puzzle
        orig_solution = self.solution if orig_solution is None else orig_solution

        # Pick a random cell and "erase" its contents
        i = random.randint(0, 80)
        new_temp_puzzle = temp_puzzle[:i] + '0' + temp_puzzle[i + 1:]

        # Solve the newly created puzzle
        self.puzzle = self.answer = new_temp_puzzle
        self.solve()

        # If the solution differs from the original solution, it means that
        # the puzzle does not have a unique solution any longer. Therefore,
        # the puzzle from the previous recursive call is our best puzzle.
        if self.solution != orig_solution:
            self.puzzle = self.answer = temp_puzzle
            self.solution = orig_solution
            return

        # If we have reached the maximum number of empty cells for our chosen
        # level, the puzzle is done
        max_unknowns = LEVELS[self.level]
        cur_unknowns = new_temp_puzzle.count('0')
        if cur_unknowns == max_unknowns:
            return

        # Else, we recurse
        self.puzzlefy(temp_puzzle=new_temp_puzzle, orig_solution=orig_solution)

    def check_solution(self):
        """
        Checks if the current answer matches the solutions.
        Returns True/False.
        """
        return self.answer == self.solution

    def is_in_puzzle(self, i):
        """
        Checks if the i-th cell is present in the original puzzle.
        Returns True/False.
        """
        return self.solution[i] == self.puzzle[i]

    def set_answer_to_puzzle(self):
        self.answer = self.puzzle


class SudokuGUI(object):
    def __init__(self, sudoku):
        """
        Creates a GUI.
        """
        self.sudoku = sudoku

        self.row = self.col = -1
        self.tk = Tk()
        self.tk.title('Sudoku')
        self.frame = Frame(self.tk)

        self.frame.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self.frame, width=FRAME_WIDTH, height=FRAME_HEIGHT)
        self.canvas.pack()

        button_clear = Button(
            self.frame,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            text='Clear board',
            command=self.clear_board
        )
        button_clear.pack(side=LEFT)
        button_check = Button(
            self.frame,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            text='Check answers',
            command=self.check_answers
        )
        button_check.pack(side=RIGHT)

        for i in xrange(10):
            self.canvas.create_line(
                PADDING + i * CELL_WIDTH,
                PADDING,
                PADDING + i * CELL_WIDTH,
                FRAME_WIDTH - 3 * PADDING,
                fill='gray' if i % 3 else 'black'
            )
            self.canvas.create_line(
                PADDING,
                PADDING + i * CELL_WIDTH,
                FRAME_HEIGHT - PADDING,
                PADDING + i * CELL_WIDTH,
                fill='gray' if i % 3 else 'black'
            )

        self.canvas.bind('<Button-1>', self.mouse_click)
        self.canvas.bind('<Key>', self.key_press)

    def set_answer_to_board(self):
        """
        Populates GUI board with the current value of sudoku.answer.
        """
        if DEBUG:
            print 'setting answer: %s' % self.sudoku.answer

        self.canvas.delete('input')

        for i in xrange(81):
            if self.sudoku.answer[i] != '0':
                self.canvas.create_text(
                    PADDING + i % 9 * CELL_WIDTH + CELL_WIDTH / 2,
                    PADDING + i / 9 * CELL_WIDTH + CELL_WIDTH / 2,
                    text=self.sudoku.answer[i],
                    tags='input',
                    fill='black' if self.sudoku.is_in_puzzle(i) else 'blue'
                )

    def clear_board(self):
        """
        Clears the board of user input, setting it to the value of original puzzle.
        """
        self.sudoku.set_answer_to_puzzle()
        self.set_answer_to_board()

    def check_answers(self):
        """
        Checks user input and displays appropriate message.
        """
        if self.sudoku.check_solution():
            tkMessageBox.showinfo(title='You Win!', message='Congratulations! You Won!', parent=self.tk)
        else:
            tkMessageBox.showinfo(title='Sorry!', message='Your solution is not correct!', parent=self.tk)

    def mouse_click(self, event):
        """
        Handles mouse click event.
        Selects a cell by drawing a blue rectangle around it.
        """
        x, y = event.x, event.y
        if PADDING < x < FRAME_WIDTH - PADDING and PADDING < y < FRAME_HEIGHT - PADDING:
            self.canvas.focus_set()
            row, col = (y - PADDING) / CELL_WIDTH, (x - PADDING) / CELL_WIDTH

            if DEBUG:
                print 'cell clicked: (%s, %s)' % (row, col)

            if not (0 <= row <= 8 and 0 <= col <= 8):
                return

            if (row, col) == (self.row, self.col):
                self.row = self.col = -1
            elif self.sudoku.puzzle[row * 9 + col] == '0':
                self.row, self.col = row, col
        else:
            self.row = self.col = -1

        self.canvas.delete('select')
        if self.row >= 0 and self.col >= 0:
            self.canvas.create_rectangle(
                PADDING + self.col * CELL_WIDTH + 1,
                PADDING + self.row * CELL_WIDTH + 1,
                PADDING + (self.col + 1) * CELL_WIDTH - 1,
                PADDING + (self.row + 1) * CELL_WIDTH - 1,
                outline='blue', tags='select'
            )

    def key_press(self, event):
        """
        Handles key press event.
        If the key pressed is a number, fill it in the answer board.
        """
        key = event.char

        if DEBUG:
            print 'key pressed', key

        if not key.isdigit():
            return

        if self.row >= 0 and self.col >= 0:
            i = self.row * 9 + self.col
            self.sudoku.answer = self.sudoku.answer[:i] + key + self.sudoku.answer[i + 1:]
            self.set_answer_to_board()

    def start(self):
        """
        Puts the GUI in motion.
        """
        self.tk.geometry('%dx%d' % (FRAME_HEIGHT, FRAME_WIDTH))
        self.tk.mainloop()


def parse_args(num_solutions):
    """
    Parses command line arguments,
    defaulting to a random value for both arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--level',
        help='Difficulty level',
        type=str,
        choices=LEVELS
    )
    parser.add_argument(
        '--board',
        help='Board number',
        type=int,
        choices=xrange(1, num_solutions + 1)
    )
    parser.add_argument(
        '--debug',
        help='Print debug messages to standard output',
        action='store_true'
    )
    args = parser.parse_args()

    if not args.level:
        args.level = random.choice(LEVELS.keys())
    if not args.board:
        args.board = random.randint(1, num_solutions)
    if args.debug:
        global DEBUG
        DEBUG = True

    return args


def get_solutions(filename):
    """
    Returns the list of solutions.
    Verifies that the file containing the solutions is in the correct format.
    We expect every line to contain a string of 81 digits
    representing the solution to the puzzle.
    """
    with open(filename) as f:
        solutions = f.read().split('\n')
        for solution in solutions:
            assert len(solution) == 81
            assert solution.isdigit()

    return solutions


def make_sudoku():
    solutions = get_solutions('solutions.txt')
    args = parse_args(len(solutions))
    solution = solutions[args.board - 1]
    sudoku = Sudoku(level=args.level, solution=solution)
    sudoku.puzzlefy()

    if DEBUG:
        print "level: %s, board: %s" % (args.level, args.board)
        print "puzzle:   %s" % sudoku.puzzle
        print "solution: %s" % sudoku.solution

    return sudoku


def make_gui(sudoku):
    gui = SudokuGUI(sudoku)
    gui.set_answer_to_board()
    gui.start()


def main():
    sudoku = make_sudoku()
    make_gui(sudoku)


if __name__ == '__main__':
    main()
