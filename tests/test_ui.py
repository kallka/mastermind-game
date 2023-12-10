# Author: Karina Kallas
# Date Last Tested: Dec. 6, 2023

import unittest
from unittest.mock import patch
from ui import *

# #################################################################################################################### #
#                                                                                                                      #
# TESTS: ui.py                                                                                                         #
#                                                                                                                      #
#                                                                                                                      #
# #################################################################################################################### #
class TestCodeMaker(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @patch('ui.ask_to_play')
    def test_ask_to_play(self, mock_play_mastermind):
        mock_play_mastermind = 'OK'
        pass

if __name__ == "__main__":
    unittest.main()