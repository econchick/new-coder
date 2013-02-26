import random
import argparse

LEVELS = {
    'debug': 1,
    'n00b': 20,
    'l33t': 45,
}


class Sudoku(object):
    def __init__(self, level=None, puzzle=None, solution=None):
        self.level = level
        self.puzzle = puzzle
        self.solution = solution

    def solve(self, temp_solution=None):
        """
        Solves the puzzle.
        Each recursive call fills in a cell,
        until there are no blank cells left.
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
        for j in range(81):
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
        Stops when it reaches the maximum number of blank cells for the
        chosen level.
        """
        temp_puzzle = self.solution if temp_puzzle is None else temp_puzzle
        orig_solution = self.solution if orig_solution is None else orig_solution

        # Pick a random cell and "erase" its contents
        i = random.randint(0, 80)
        new_temp_puzzle = temp_puzzle[:i] + '0' + temp_puzzle[i + 1:]

        # Solve the newly created puzzle
        self.puzzle = new_temp_puzzle
        self.solve()

        # If the solution differs from the original solution, it means that
        # the puzzle does not have a unique solution any longer. Therefore,
        # the puzzle from the previous recursive call is our best puzzle.
        if self.solution != orig_solution:
            self.puzzle = temp_puzzle
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
        choices=range(1, num_solutions + 1)
    )
    args = parser.parse_args()

    if not args.level:
        args.level = random.choice(LEVELS.keys())
    if not args.board:
        args.board = random.randint(1, num_solutions)

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


if __name__ == '__main__':
    solutions = get_solutions('solutions.txt')
    args = parse_args(len(solutions))
    solution = solutions[args.board - 1]
    sudoku = Sudoku(level=args.level, solution=solution)

    print "level: %s, board: %s" % (args.level, args.board)

    sudoku.puzzlefy()
    print sudoku.puzzle
    sudoku.solve()
    print sudoku.solution
