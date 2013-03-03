import argparse
import unittest
import sys

import sudoku


class TestParseArguments(unittest.TestCase):
    def test_it_parses_arguments(self):
        sys.argv = ['sudoku.py', '--level', 'l33t', '--board', '5']
        level_name, board_number = sudoku.parse_arguments()
        self.assertEqual(level_name, 'l33t')
        self.assertEqual(board_number, 5)

    def test_it_works_when_missing_board_number(self):
        sys.argv = ['sudoku.py', '--level', 'l33t']
        level_name, board_number = sudoku.parse_arguments()
        self.assertEqual(level_name, 'l33t')
        self.assertEqual(board_number, -1)

    def test_it_doesnt_work_when_missing_level_name(self):
        sys.argv = ['sudoku.py']
        try:
            self.assertRaises(
                argparse.ArgumentError,
                sudoku.parse_arguments
            )
        except SystemExit:  # argparse performs sys.exit with error
            pass

    def test_it_doesnt_work_for_invalid_level_names(self):
        for invalid_name in ['l00t', 'n33b', '']:
            sys.argv = ['sudoku.py', '--level', invalid_name]
            try:
                self.assertRaises(
                    argparse.ArgumentError,
                    sudoku.parse_arguments
                )
            except SystemExit:  # argparse performs sys.exit with error
                pass

    def test_it_doesnt_work_for_invalid_board_numbers(self):
        for invalid_board_number in ['-1', 'x']:
            sys.argv = ['sudoku.py', '--level', 'n00b',
                        '--board', invalid_board_number]
            try:
                self.assertRaises(
                    argparse.ArgumentError,
                    sudoku.parse_arguments
                )
            except SystemExit:  # argparse performs sys.exit with error
                pass


class TestSudokuGameInit(unittest.TestCase):
    def test_it_creates_board_from_file(self):
        boards_file = ("123456789\n" * 9).strip().split('\n')
        game = sudoku.SudokuGame(boards_file)
        self.assertEqual(game.boards, [[range(1, 10)] * 9])

    def test_it_creates_multiple_boards_from_file(self):
        boards_file = ("012345678\n" * 18).strip().split('\n')
        game = sudoku.SudokuGame(boards_file)
        self.assertEqual(game.boards, [[range(0, 9)] * 9] * 2)

    def test_it_doesnt_work_with_wrong_number_of_chars_per_line(self):
        boards_file = ("1234567890\n" * 18).strip().split('\n')
        self.assertRaises(sudoku.SudokuError, sudoku.SudokuGame, boards_file)

    def test_it_doesnt_work_with_wrong_number_of_lines_per_file(self):
        boards_file = ("123456789\n" * 19).strip().split('\n')
        self.assertRaises(sudoku.SudokuError, sudoku.SudokuGame, boards_file)

    def test_it_doesnt_work_with_invalid_chars(self):
        boards_file = ("12345678x\n" * 9).strip().split('\n')
        self.assertRaises(sudoku.SudokuError, sudoku.SudokuGame, boards_file)


class TestSudokuGameStart(unittest.TestCase):
    boards_file = ("012345678\n" * 9 + "123456789\n" * 9).strip().split('\n')

    def test_it_starts_game_with_specific_board_number(self):
        game = sudoku.SudokuGame(self.boards_file)
        game.start(0)
        self.assertEqual(game.puzzle, [range(0, 9)] * 9)
        game.start(1)
        self.assertEqual(game.puzzle, [range(1, 10)] * 9)

    def test_it_starts_game_with_random_board_number(self):
        game = sudoku.SudokuGame(self.boards_file)
        game.start(-1)
        self.assertEqual(len(game.puzzle), 9)

    def test_it_doesnt_start_game_with_wrong_board_number(self):
        for wrong_board_number in [-2, 3, 9]:
            game = sudoku.SudokuGame(self.boards_file)
            self.assertRaises(
                sudoku.SudokuError, game.start, wrong_board_number
            )


class TestSudokuGameCheckers(unittest.TestCase):
    boards_file = (
        "012345678\n123456789\n" * 4 + "012345678\n" +
        "\n".join(
            [(a + b) * 4 + a for a, b in zip("012345678", "123456789")]
        ) + "\n" +
        ("123" * 2 + "012\n" + "456" * 2 + "345\n" + "789" * 2 + "678\n") * 3
    ).strip().split('\n')

    def test_check_block_accepts_correct_sequences(self):
        game = sudoku.SudokuGame(self.boards_file)
        game.start(-1)

        for p in [xrange(1, 10), reversed(xrange(1, 10))]:
            self.assertTrue(game._SudokuGame__check_block(p))

    def test_check_block_doesnt_accept_incorrect_sequences(self):
        game = sudoku.SudokuGame(self.boards_file)
        game.start(-1)
        for p in [xrange(0, 9), reversed(xrange(0, 9))]:
            self.assertFalse(game._SudokuGame__check_block(p))

    def test_check_row_only_accepts_correct_rows(self):
        game = sudoku.SudokuGame(self.boards_file)
        game.start(0)
        for row in xrange(9):
            self.assertEqual(game._SudokuGame__check_row(row), row % 2 != 0)

    def test_check_column_only_accepts_correct_columns(self):
        game = sudoku.SudokuGame(self.boards_file)
        game.start(1)
        for column in xrange(9):
            self.assertEqual(game._SudokuGame__check_column(column), column % 2 != 0)

    def test_check_square_only_accepts_correct_squares(self):
        game = sudoku.SudokuGame(self.boards_file)
        game.start(2)
        for row in xrange(3):
            for column in xrange(3):
                self.assertEqual(
                    game._SudokuGame__check_square(row, column), column != 2
                )


class TestSudokuGameSetAnswerToPuzzle(unittest.TestCase):
    def test_it_resets_the_game(self):
        boards_file = ("012345678\n" * 9).strip().split('\n')
        game = sudoku.SudokuGame(boards_file)
        game.game_over = True
        game.answer = [range(1, 10)] * 9
        game.start(-1)

        game.set_answer_to_puzzle()
        self.assertFalse(game.game_over)
        self.assertEqual(game.puzzle, game.answer)


if __name__ == '__main__':
    unittest.main()
