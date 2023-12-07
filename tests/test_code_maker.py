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
    # Is object created by CodeMaker class and can initialized values be updated?
    def test_create_CodeMaker_object(self):
        result = CodeMaker()
        self.assertIsNotNone(result, "CodeMaker object created.")

        result = CodeMaker(1, 1, 1, 1)
        self.assertEqual(result.turns, 1, "CodeMaker.turns are == 1?")
        self.assertEqual(result.min_num, 1, "CodeMaker.turns are == 1?")
        self.assertEqual(result.max_num, 1, "CodeMaker.turns are == 1?")
        self.assertEqual(result.code_entries, 1, "CodeMaker.turns are == 1?")

    # Does decrement_turns work?
    def test_decrement_turns(self):
        result = CodeMaker(1, 1, 1, 1)
        result.decrement_turns()
        self.assertEqual(result.turns, 0, "Turns should decrement to 0.")

    # Does increment_turns work?
    def test_increment_turns(self):
        result = CodeMaker(1, 1, 1, 1)
        result.increment_turns()
        self.assertEqual(result.turns, 2, "Turns should decrement to 0.")

    # Does create_random_code update answer_code?
    def test_create_random_code(self):
        result = CodeMaker()
        result.create_random_code()
        self.assertEqual(len(result.answer_code), result.code_entries,
                         "The answer_code is the same length as the code_entries.")


if __name__ == "__main__":
    unittest.main()
