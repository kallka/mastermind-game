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
        self.assertEqual(type(self.code_maker.answer_code), list,
                         "The function create_random_code did not return a list.")

    # Do zero turns make game return end=True? If all guesses correct, is win=True?
    def test_check_end_of_game(self):
        self.code_maker.turns = 0
        result = self.code_maker.check_end_of_game(0)       # result = (end, win)
        self.assertEqual(result, (True, False), "Zero turns does not trigger game to exit.")
        result = self.code_maker.check_end_of_game(4)
        self.assertEqual(result, (True, True),
                         "Correct code entries matching correct match_val_and_place does not trigger exit.")

    # Does check answer
    def test_check_player_guess(self):
        self.code_maker.answer_code = [1, 2, 3, 4]
        inputs = [[1, 2, 3, 4], [4, 3, 2, 1], [0, 5, 6, 7], [1, 4, 1, 1]]
        answers = [(4, 0), (0, 4), (0, 0), (1, 1)]
        for idx in range(4):
            result = self.code_maker.check_player_guess(inputs[idx])   # (match_val_and_place: int, match_val: int)
            self.assertEqual(result, answers[idx], f"Matches incorrect: guess {inputs[idx]} returns {answers[idx]}.")

    # Check that formats as string.
    def test_int_list_to_string(self):
        result = self.code_maker.int_list_to_string([1, 2, 3, 4])
        self.assertEqual(type(result), str, "Does not return string.")


if __name__ == "__main__":
    unittest.main()
