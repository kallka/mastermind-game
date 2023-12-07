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
# File Name: ui.py
# File Description: A user interface for the program that calls functions and organizes actions.

# #################################################################################################################### #
#                                                                                                                      #
# IMPORTS                                                                                                              #
#                                                                                                                      #
#                                                                                                                      #
# #################################################################################################################### #
from messages_constants import WELCOME, PLAY_GAME, INSTRUCTIONS, GOODBYE
from messages_constants import YES_RESPONSES, NO_RESPONSES, INVALID_RESPONSE
from code_breaker import CodeBreaker
from code_maker import CodeMaker


# #################################################################################################################### #
#                                                                                                                      #
# FUNCTIONS                                                                                                            #
#      - ask_to_play()                                                                                                 #
#      - play_mastermind()                                                                                             #
#                                                                                                                      #
# #################################################################################################################### #
def ask_to_play():
    '''
    Sets up loop that asks player if they would like to play the game(s).
    Returns when player declines to play another game.
    '''
    play = True

    while play:
        user_response = ""
        break_loop = 0

        while (user_response not in YES_RESPONSES) and (user_response not in NO_RESPONSES) and break_loop < 5:
            if break_loop > 0:
                print(f"\n{INVALID_RESPONSE}")
            user_response = input(f"\n{PLAY_GAME}").lower()
            break_loop += 1

        if user_response in YES_RESPONSES:
            play_mastermind()

        else:
            play = False


def play_mastermind():
    # play game
    print(INSTRUCTIONS)
    new_game = CodeBreaker()

    while new_game.remaining_turns() > 0:
        new_game.make_guess()


# #################################################################################################################### #
#                                                                                                                      #
# MAIN                                                                                                                 #
#                                                                                                                      #
#                                                                                                                      #
# #################################################################################################################### #
def main():
    '''
    Welcomes user(s), asks if users want to play, and says goodbye.
    :return: 0
    '''

    print(WELCOME)
    ask_to_play()
    print(f"\n{GOODBYE}")

    return 0


if __name__ == "__main__":
    main()
