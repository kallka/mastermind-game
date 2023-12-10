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
from code_breaker import CodeBreaker
from messages_constants import WELCOME, PLAY_GAME, INSTRUCTIONS, GOODBYE, YES_RESPONSES, NO_RESPONSES, \
    INVALID_RESPONSE, INVALID_RESPONSE_AND_EXIT, REMAINING_TURNS, GET_HINT, GET_CODEBREAKER_GUESS


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
    Player needs to return a valid yes/no response from get_user_input_yes_no in order for loop to continue.
    If break_loop return from get_user_input_yes_no function is equal to the break_loop_max (number of tries
    given to a playerr to attempt correct input), the program returns.
    Returns when player declines to play another game or break_loop_max reached.
    '''
    play = True

    while play:
        # include a break_loop_max to specify how many turns a player can attempt to enter yes/no
        break_loop_max = 5
        user_response, break_loop = get_user_input_yes_no(break_loop_max)

        if break_loop == break_loop_max:
            print(f"{INVALID_RESPONSE_AND_EXIT}")
            return

        if user_response in YES_RESPONSES:
            play_mastermind()

        else:
            play = False


def get_user_input_yes_no(break_loop_max):
    '''
    Gets a yes or no user response. Loops through request to get input until a user either
    returns a valid yes/no (ex. 'YES, yES, y, No, N, no') or until the break_loop_max is reached.
    If the user can't return a valid response in this many times, the program returns.
    Returns: user_response, break_loop so that another function knows valid response or if max was reached.
    '''
    user_response = ''
    break_loop = 0

    while (user_response not in YES_RESPONSES) and (user_response not in NO_RESPONSES) and break_loop < 5:
        if break_loop > 0:
            print(f"\n{INVALID_RESPONSE}")
        user_response = input(f"\n{PLAY_GAME}").lower()
        break_loop += 1

    return user_response, break_loop


def get_user_guess(game):
    print(f"{REMAINING_TURNS.format(turns=game.remaining_turns())}\t{GET_HINT}")

    entries, min_num, max_num = game.current_game.get_code_entries(), \
                                game.current_game.get_min_num(), \
                                game.current_game.get_max_num()
    guess = input(f"{GET_CODEBREAKER_GUESS.format(code_entries=entries, min_num=min_num, max_num=max_num)}")

    if guess == 'h' or guess == 'H':
        guess = get_hints(game)

    return guess


def get_hints(game):
    # TODO: Implement hints of various levels.
    print("\nYOU want a hint.\n")
    guess = get_user_guess(game)
    return guess


def play_mastermind():
    # print instructions and check turns
    print(INSTRUCTIONS)

    # TODO: This where the game could include more than 1 user.
    # A GameManager class might help control play as users increase.
    game = CodeBreaker()

    while game.remaining_turns() > 0:
        guess = get_user_guess(game)
        valid_guess = game.make_guess(guess)
        if not valid_guess:
            print(INVALID_RESPONSE)


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
