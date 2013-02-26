import unittest
from sudoku import Sudoku, LEVELS

PUZZLE = '056807900900024815008010600090073001000000502000081000002100307600740050741300206'
SOLUTION = '156837924973624815428915673895273461317496582264581739582169347639742158741358296'
MAX_EMPTY_CELLS_DEBUG = LEVELS['debug']
MAX_EMPTY_CELLS_N00B = LEVELS['n00b']
MAX_EMPTY_CELLS_L33T = LEVELS['l33t']


class TestSudoku(unittest.TestCase):
    def test_solve(self):
        # Setup
        sudoku = Sudoku(puzzle=PUZZLE)

        # Run
        sudoku.solve()

        # Verify
        self.assertEqual(sudoku.puzzle, PUZZLE)
        self.assertEqual(sudoku.solution, SOLUTION)

    def test_puzzlefy_debug(self):
        # Setup
        sudoku = Sudoku(solution=SOLUTION, level='debug')

        # Run
        sudoku.puzzlefy()

        # Verify
        empty_cells = sudoku.puzzle.count('0')
        self.assertLessEqual(empty_cells, MAX_EMPTY_CELLS_DEBUG)
        self.assertEqual(sudoku.solution, SOLUTION)

        # Run
        sudoku.solve()

        # Verify
        self.assertEqual(sudoku.solution, SOLUTION)

    def test_puzzlefy_n00b(self):
        # Setup
        sudoku = Sudoku(solution=SOLUTION, level='n00b')

        # Run
        sudoku.puzzlefy()

        # Verify
        empty_cells = sudoku.puzzle.count('0')
        self.assertLessEqual(empty_cells, MAX_EMPTY_CELLS_N00B)
        self.assertEqual(sudoku.solution, SOLUTION)

        # Run
        sudoku.solve()

        # Verify
        self.assertEqual(sudoku.solution, SOLUTION)

    def test_puzzlefy_l33t(self):
        # Setup
        sudoku = Sudoku(solution=SOLUTION, level='l33t')

        # Run
        sudoku.puzzlefy()

        # Verify
        empty_cells = sudoku.puzzle.count('0')
        self.assertLessEqual(empty_cells, MAX_EMPTY_CELLS_L33T)
        self.assertEqual(sudoku.solution, SOLUTION)

        # Run
        sudoku.solve()

        # Verify
        self.assertEqual(sudoku.solution, SOLUTION)


if __name__ == '__main__':
    unittest.main()
