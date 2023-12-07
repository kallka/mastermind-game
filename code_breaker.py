# Author: Karina Kallas
# Date Last Modified: Dec. 6, 2023
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
from messages_constants import MAKE_A_GUESS


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
    def make_guess(self):
        guess = ""
        valid = False

        # loop until guess is valid
        # TODO: make a way to break out of loop in case user can't make valid guess
        while not valid:
            guess = input(MAKE_A_GUESS)
            valid, guess = self.helper_validate_make_guess(guess)

        self.guesses.append(guess)

        # send guess to code maker to process and get feedback
        feedback = self.current_game.process_guess(guess)
        # save (match_value_and_place, match_value) to self.guess_feedback
        self.guess_feedback.append(feedback)

        # optional - return each guess
        return guess

    def helper_validate_make_guess(self, guess):
        valid = False

        if len(guess) == self.current_game.code_entries:
            guess = list(guess)
            min_num, max_num = self.current_game.min_num, self.current_game.max_num

            for idx, str_num in enumerate(guess):
                int_num = ord(str_num) - 48           # ascii values: 48-57 are 0-9
                if max_num >= int_num >= min_num:
                    guess[idx] = int_num
                    valid = True
                else:
                    valid = False
                    break

        return valid, guess


# #################################################################################################################### #
#                                                                                                                      #
# MAIN                                                                                                                 #
#                                                                                                                      #
#                                                                                                                      #
# #################################################################################################################### #
def main():
    new_player = CodeBreaker()

    turns = new_player.current_game.get_turns()

    while turns > 0:
        guess = new_player.make_guess()
        print(guess)
        # remove as this will be handled by code_maker
        turns -= 1
        print(new_player.guesses)

    return 0


if __name__ == "__main__":
    main()