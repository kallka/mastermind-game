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
#           Description: Controls making code, validating answers, and tracking turns.                                 #
#           Methods:    - request_new_game                                                                             #
#                       - make_guess                                                                                   #
#                       - create_random_code                                                                           #
#                                                                                                                      #
# #################################################################################################################### #
class CodeBreaker:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.games_played = 0
        self.current_game = None
        self.current_guesses = []

    ####################################################################################################################
    #                                make_guess and validate_guess_input                                               #
    ####################################################################################################################
    def make_guess(self):
        if self.current_game is None:
            self.set_new_game()

        guess = ""
        valid = False
        while not valid:
            guess = input(MAKE_A_GUESS)
            valid, guess = self.helper_validate_make_guess(guess)

        self.current_guesses.append(guess)

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

    ####################################################################################################################
    #                                SETS:                                                                             #
    #                                   1. set_new_game                                                                #
    ####################################################################################################################
    def set_new_game(self):
        new_game = CodeMaker()
        new_game.create_random_code()
        self.current_game = new_game


# #################################################################################################################### #
#                                                                                                                      #
# MAIN                                                                                                                 #
#                                                                                                                      #
#                                                                                                                      #
# #################################################################################################################### #
def main():
    new_player = CodeBreaker()


    new_player.set_new_game()
    turns = new_player.current_game.get_turns()

    while turns > 0:
        new_player.make_guess()
        # remove as this will be handled by code_maker
        turns -= 1
        print(new_player.current_guesses)

    return 0


if __name__ == "__main__":
    main()
