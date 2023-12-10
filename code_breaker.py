# Author: Karina Kallas
# Date Last Modified: Dec. 10, 2023
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
from messages_constants import HINT_1


# #################################################################################################################### #
#                                                                                                                      #
# CLASS:    CodeBreaker                                                                                                #
#                                                                                                                      #
#           Description: Controls making guess, validating guess, and tracking guesses and feedback.                   #
#           Methods:    - set_new_game                                                                                 #
#                       - make_guess                                                                                   #
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
    def set_new_game(cls):
        new_game = CodeMaker()
        new_game.create_random_code()
        return new_game

    ####################################################################################################################
    #                                make_guess                                                                        #
    #                                helper_validate_make_guess                                                        #
    ####################################################################################################################
    def make_guess(self, guess):
        valid, guess = self.helper_validate_make_guess(guess)
        if valid is False:
            return valid

        # save guess, get feedback, and save feedback
        self.guesses.append(guess)
        feedback = self.current_game.process_guess(guess)
        self.guess_feedback.append(feedback)

        # returns True for guess is valid
        return valid

    def helper_validate_make_guess(self, guess):
        valid = False

        if len(guess) == self.current_game.code_entries:
            guess = list(guess)
            min_num, max_num = self.current_game.min_num, self.current_game.max_num

            for idx, str_num in enumerate(guess):
                # Convert to ascii values (48-57 are 0-9) as directly converting to integer value causes problems
                # with some noninteger values.
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
    def hints(self):
        if self.hints == 0:
            print(HINT_1)
        elif self.hints == 1:
            print(self.hints_matches_place_and_value())
            self.hints += 1
        return

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
                # do depth first search to determine which numbers are the same?

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
