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
    @patch('ui.input', create=True)
    def test_get_user_input_yes_no(self, mock_user_response):
        for entry in YES_RESPONSES:
            char = entry[-1].swapcase()
            entry = entry[:-1] + char
            print(entry)
            mock_user_response = entry
            self.assertIsNotNone(get_user_input_yes_no(2), "Is case sensitive: test_get_user_input_yes_no")

    # Test that mixed caps/lowercase accepted
    @patch('ui.input', side_effect=['yEs', 'nO', 'yeS'])
    def test_get_user_input_yes_no(self, mock_input):
        call_1 = mock_input()
        call_2 = mock_input()
        call_3 = mock_input()
        self.assertTrue(call_1 == 'yEs' and call_2 == 'nO' and call_3 == 'yeS')

    # Test that mixed caps/lowercase accepted
    # TODO: Figure out why returning: (.lower() may be culprit) <MagicMock name='input().lower()' id='140476102239040'>
    @patch('ui.input', side_effects='yEs')
    def test_get_user_input_yes_no(self, mock_inputs):
        result = get_user_input_yes_no(2)
        self.assertEqual(result, ('yEs', 2) , "Is case sensitive: test_get_user_input_yes_no")

if __name__ == "__main__":
    unittest.main()