# Author: Karina Kallas
# Date Last Tested: Dec. 10, 2023

import unittest
from unittest.mock import patch, MagicMock
from ui import *


# #################################################################################################################### #
#                                                                                                                      #
# TESTS: ui.py                                                                                                         #
#                                                                                                                      #
#                                                                                                                      #
# #################################################################################################################### #
class TestUI(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_game = MagicMock()
        self.mock_game.get_code_entries = 4
        self.mock_game.min_num = 0
        self.mock_game.max_num = 7
        pass

    def tearDown(self) -> None:
        pass

    # Test break_loop triggered with valid response
    @patch('ui.get_user_input_yes_no')
    def test_ask_to_play(self, mock_get_user_input_yes_no):
        mock_user_response = 'n'
        mock_break_loop = 5
        mock_get_user_input_yes_no.return_value = mock_user_response, mock_break_loop  # user_response, break_loop

        self.assertEqual(ask_to_play(), INVALID_RESPONSE_AND_EXIT, "Return not triggered by break_loop_max")

    # Test that mixed caps/lowercase accepted
    @patch('builtins.input', lambda *args: 'yEs')
    def test_get_user_input_yes_no(self):
        result = get_user_input_yes_no(2)
        self.assertEqual(result, ('yes', 1), "Is case sensitive: test_get_user_input_yes_no")

    # Confirm returns tuple
    @patch('builtins.input', lambda *args: 'no')
    def test_get_user_input_yes_no(self):
        result = get_user_input_yes_no(2)
        self.assertEqual(tuple, type('yes', 1), "Is case sensitive: test_get_user_input_yes_no")

    # Test '/0'
    @patch('builtins.input', lambda *args: '\0')
    def test_get_user_input_yes_no(self):
        result = get_user_input_yes_no(2)
        # Will loop twice as input invalid and record hex 00 as string
        self.assertEqual(result, ('\x00', 2), "Unexpected input of '\0' does not work.")

    # Test None
    @patch('builtins.input', lambda *args: None)
    def test_get_user_input_yes_no(self):
        result = get_user_input_yes_no(2)
        # Will loop twice as input invalid (None)
        self.assertEqual(result, (None, 2), "None crashes program")

    # Test None
    @patch('builtins.input', lambda *args: chr(27))
    def test_get_user_input_yes_no(self):
        result = get_user_input_yes_no(2)
        # Will loop twice as input invalid (esc)
        self.assertEqual(result, (chr(27), 2), "None crashes program")

    # Test valid input is returned
    @patch('builtins.input', lambda *args: '0123')
    def test_get_user_guess(self):
        result = get_user_guess(self.mock_game)
        # Will loop twice as input invalid (esc)
        self.assertEqual(result, '0123', "The function 'get_user_guess' does not return expected input of '0123'.")

    # Test valid input is returned
    @patch('builtins.input', lambda *args: '0123')
    def test_get_user_guess(self):
        result = get_user_guess(self.mock_game)
        # Will loop twice as input invalid (esc)
        self.assertEqual(result, '0123', "The function 'get_user_guess' does not return expected input of '0123'.")


if __name__ == "__main__":
    unittest.main()