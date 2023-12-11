# Author: Karina Kallas
# Date Last Modified: Dec. 11, 2023
#
# Project Name: Master Mind
# Project Description:  A game which can be played by a user "against" the computer.
#                       This is a game where a player tries to guess the number combinations. At the end of each attempt
#                       to guess the 4 number combinations, the computer will provide feedback whether the player had
#                       guess a number correctly, or/and a number and digit correctly. A player must guess the right
#                       number combinations within 10 attempts to win the game.
#
# File Name: code_breaker.py
# File Description: This file servers as player2 (the code breaker). It is enables a player to send guesses to player1
#                   (the code breaker) and provides feedback to player2.


# #################################################################################################################### #
#                                                                                                                      #
# IMPORTS                                                                                                              #
#                                                                                                                      #
#                                                                                                                      #
# #################################################################################################################### #
from code_maker import CodeMaker
from messages_constants import HINT_0, HINT_1


# #################################################################################################################### #
#                                                                                                                      #
# CLASS:    CodeBreaker                                                                                                #
#                                                                                                                      #
#           Description: Controls making guess, validating guess in corrrect parameters, hints,                        #
#           and tracking guesses and feedback.                                                                         #
#                                                                                                                      #
# #################################################################################################################### #
class CodeBreaker:
    def __init__(self):
        self.current_game = self.set_new_game()
        self.guesses = []
        self.guess_feedback = []
        self.hints = 0

    ####################################################################################################################
    #                                 set_new_game                                                                     #
    ####################################################################################################################
    @classmethod
    def set_new_game(cls) -> object:
        '''
        Creates a new game by creating instance of CodeMaker object and generating random code.
        :return: A new game (object).
        '''
        new_game = CodeMaker()
        new_game.create_random_code()
        return new_game

    ####################################################################################################################
    #                                make_guess                                                                        #
    #                                helper_validate_make_guess                                                        #
    ####################################################################################################################
    def make_guess(self, guess: str) -> bool:
        '''
        Takes a user guess (string) and determines if it is valid. If guess is invalid, immediately returns False.
        If guess is valid, guess is appended to self.guesses and sent to CodeMaker to get feedback on
        corrrect/incorrect matches. Feedback from the CodeMaker is appended to self.guess_feedback.
        Returns if guess was valid, returns True.
        :param guess: A string representing player's guess.
        :return: Boolean value of True if guess was valid or False if guess was invalid.
        '''
        valid, guess = self.helper_validate_make_guess(guess)
        if valid is False:
            return valid

        # save guess, get feedback, and save feedback
        self.guesses.append(guess)
        feedback = self.current_game.process_guess(guess)
        self.guess_feedback.append(feedback)

        # returns True for guess is valid
        return valid

    def helper_validate_make_guess(self, guess: str) -> tuple[bool, list[int]]:
        '''
        Takes the player's guess (string), if length of guess matches code entries,
        turns into a list of integers by converting to ascii values. (*Note int() does not work well
        as certain string values do not convert smoothly to ints.) Confirms that each guess digit is within
        specified parameters and then returns a tuple representing (valid, converted guess).
        If guess was valid, valid = True.
        :param guess: A string representing the player's guess.
        :return: A tuple (valid, guess) where valid is True if the guess was valid and guess is now a list of integers.
        '''
        valid = False

        if guess:
            if len(guess) == self.current_game.code_entries:
                guess = list(guess)
                min_num, max_num = self.current_game.min_num, self.current_game.max_num

                for idx, str_num in enumerate(guess):
                    # Convert to ascii values (48-57 are 0-9) as directly converting to integer value causes problems
                    # with some non-integer values.
                    int_num = ord(str_num) - 48
                    if max_num >= int_num >= min_num:
                        guess[idx] = int_num
                        valid = True
                    else:
                        valid = False
                        break

        return valid, guess

    ####################################################################################################################
    #                                 hints                                                                            #
    ####################################################################################################################
    def hints_manager(self) -> str:
        '''
        Calculates how many guesses a player has made and makes a determination about what hint is appropriate
        Increments self.hints to track hints. Self.hints can later be used to deduct turns or calculate score.
        :return: A string response to be printed by the UI.
        '''
        min_num = self.current_game.get_min_num()
        max_num = self.current_game.get_max_num()
        if len(self.guesses) == 0:
            return HINT_0.format(min_num=min_num, max_num=max_num)
        else:
            total = 0
            for feedback in self.guess_feedback:
                total += feedback[0] + feedback[1]

            if len(self.guesses) > 0 and self.hints == 0:
                self.hints += 1
                return HINT_1.format(min_num=min_num, max_num=max_num, total=total)
            else:
                self.hints += 1
                return self.hint_educated_guess()

    def hint_educated_guess(self):
        # Steps
            # 1. Is total number of matches (all kinds) == code_entries?
            #       - if yes, move around entries based on last guesses
            # 2. Is total matches == 0:
            #       - if yes, return not yet guessed nums list
            # 3. Matches < code_entries?
            #       - review past entries and select at least as many in correct place
        return "placeholder"

    def hints_all_possible_values(self):
        return

    def hints_matches_value_only(self):
        return

    def hints_matches_place_and_value(self):
        hint = "placeholder"
        place_and_value_guesses = []
        for idx, match in enumerate(self.guess_feedback):
            # find all guesses where match and place ok
            if match[0] != 0:
                place_and_value_guesses.append([self.guesses[idx]])
                # Can we do a depth first search comparing all matched value/place
                # to all matched value?

        return hint

    ####################################################################################################################
    #                                 remaining_turns                                                                  #
    ####################################################################################################################
    def remaining_turns(self):
        return self.current_game.get_turns()


# #################################################################################################################### #
#                                                                                                                      #
# MAIN                                                                                                                 #
#                                                                                                                      #
#                                                                                                                      #
# #################################################################################################################### #
def main():
    new_player = CodeBreaker()

    while new_player.current_game.get_turns() > 0:
        guess = input(f"Input {new_player.current_game.get_code_entries()} integers "
                      f"between {new_player.current_game.get_min_num()} and {new_player.current_game.get_max_num()}: ")
        new_player.make_guess(guess)

    return 0


if __name__ == "__main__":
    main()
