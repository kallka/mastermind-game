# Author: Karina Kallas
# Date Last Modified: Dec. 6, 2023
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
    # Is object created by CodeBreaker class?
    def test_create_CodeBreaker_object(self):
        result = CodeBreaker()
        self.assertIsNotNone(result)

    # Is a new game stored in self.current_game?
    def test_request_new_game(self):
        result = CodeBreaker()
        result.set_new_game()
        self.assertIsNotNone(result.current_game)

    # Valid entries for helper_validate_make_guess?
    def test_make_guess(self):
        result = CodeBreaker()          #turns = 10, min_num = 0, max_num = 7, code_entries = 4
        result.set_new_game()
        guesses = [['12345678', False], ['1111', True], ['2222', True], ['9999', False],
                   ['-1-1', False], ['7070', True]]
        for entry in guesses:
            valid, guess = result.helper_validate_make_guess(entry[0])
            self.assertIs(valid, entry[1], "Input should be same length as code_entries.")


if __name__ == "__main__":
    unittest.main()
