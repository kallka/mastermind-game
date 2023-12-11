# Author: Karina Kallas
# Date Last Tested: Dec. 11, 2023

import unittest
from code_breaker import *


# #################################################################################################################### #
#                                                                                                                      #
# TESTS                                                                                                                #
#                                                                                                                      #
#                                                                                                                      #
# #################################################################################################################### #
class TestCodeBreaker(unittest.TestCase):
    def setUp(self) -> None:
        self.code_breaker = CodeBreaker()   # turns = 10, min_num = 0, max_num = 7, code_entries = 4

    def tearDown(self) -> None:
        pass

    # Is object created by CodeBreaker class?
    def test_create_CodeBreaker_object(self):
        self.assertIsNotNone(self.code_breaker)

    # Is a new game stored in self.current_game?
    def test_request_new_game(self):
        self.assertIsNotNone(self.code_breaker.current_game)

    # Valid return from make_guess based on valid or invalid guesses?
    def test_make_guess(self):
        guesses = [['12345678', False], ['1111', True], ['2222', True], ['9999', False],
                   ['-1-1', False], ['7070', True]]
        for entry in guesses:
            valid, guess = self.code_breaker.helper_validate_make_guess(entry[0])
            self.assertIs(valid, entry[1], "Input should be same length as code_entries.")

    # Is helper function correctly turning guess into list of ints?
    def helper_validate_make_guess(self):
        guess = ['1234']
        valid, guess_list = self.code_breaker.helper_validate_make_guess(guess)
        self.assertEqual(guess_list, [1, 2, 3, 4], "Needs to turn string into valid list of integers.")

    # Does helper function properly handle valid and invalid guesses>
    def helper_validate_make_guess(self):
        guesses_false = ['\0', None, 'hhhh', 'None', 'NULL', '1234\n']
        guesses_true = ['0011', '2233', '4455', '6677', '1111', '7654']
        for idx in range(len(guesses_false)):
            valid, guess_list = self.code_breaker.helper_validate_make_guess(guesses_false[idx])
            self.assertIsNot(valid, "Odd input not handled properly.")
        for idx in range(len(guesses_true)):
            valid, guess_list = self.code_breaker.helper_validate_make_guess(guesses_true[idx])
            self.assertIs(valid, "Valid entries rejected.")


if __name__ == "__main__":
    unittest.main()
