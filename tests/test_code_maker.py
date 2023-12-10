# Author: Karina Kallas
# Date Last Tested: Dec. 6, 2023

import unittest
from code_maker import *


# #################################################################################################################### #
#                                                                                                                      #
# TESTS                                                                                                                #
#                                                                                                                      #
#                                                                                                                      #
# #################################################################################################################### #
class TestCodeMaker(unittest.TestCase):
    def setUp(self) -> None:
        self.code_maker = CodeMaker()
        self.code_maker_ones = CodeMaker(1, 1, 1, 1)

    def tearDown(self) -> None:
        pass

    # Is object created by CodeMaker class and can initialized values be updated?
    def test_create_CodeMaker_object(self):
        self.assertIsNotNone(self.code_maker, "CodeMaker object created.")
        self.assertEqual(self.code_maker_ones.turns, 1, "CodeMaker.turns are == 1?")
        self.assertEqual(self.code_maker_ones.min_num, 1, "CodeMaker.turns are == 1?")
        self.assertEqual(self.code_maker_ones.max_num, 1, "CodeMaker.turns are == 1?")
        self.assertEqual(self.code_maker_ones.code_entries, 1, "CodeMaker.turns are == 1?")

    # Does decrement_turns work?
    def test_decrement_turns(self):
        self.code_maker_ones.decrement_turns()
        self.assertEqual(self.code_maker_ones.turns, 0, "Turns should decrement to 0.")

    # Does increment_turns work?
    def test_increment_turns(self):
        self.code_maker_ones.increment_turns()
        self.assertEqual(self.code_maker_ones.turns, 2, "Turns should decrement to 0.")

    # Does create_random_code update answer_code?
    def test_create_random_code(self):
        self.code_maker.create_random_code()
        self.assertEqual(len(self.code_maker.answer_code), self.code_maker.code_entries,
                         "The answer_code is the same length as the code_entries.")


if __name__ == "__main__":
    unittest.main()
