# Author: Karina Kallas
# Date Last Tested: Dec. 6, 2023


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

    # Valid entries for helper_validate_make_guess?
    def test_make_guess(self):
        guesses = [['12345678', False], ['1111', True], ['2222', True], ['9999', False],
                   ['-1-1', False], ['7070', True]]
        for entry in guesses:
            valid, guess = self.code_breaker.helper_validate_make_guess(entry[0])
            self.assertIs(valid, entry[1], "Input should be same length as code_entries.")


if __name__ == "__main__":
    unittest.main()
