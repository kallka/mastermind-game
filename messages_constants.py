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
# File Name: messages_constants.py
# File Description: An alphabetized list of all messages that are used as constants in the program.

# #################################################################################################################### #
#                                                                                                                      #
# CONSTANTS                                                                                                            #
# Alphabetized list of all messages that are used as constants.                                                        #
#                                                                                                                      #
# #################################################################################################################### #

GOODBYE = "Thank you for stopping by. " \
          "\nGoodbye!"

GET_CODEBREAKER_GUESS = "Please input {code_entries} integers between {min_num} and {max_num}: "

GET_HINT = "** Type 'h' to get a hint!"

GUESS_FEEDBACK = "You guessed: {guess} ... " \
                 "\t-> {match_value_place} matched value and place. " \
                 "\t-> {match_value} matched value, invalid place."

HINT_0 = "Try at least one guess before asking for a hint..."

HINT_1 = "Try two pairs of random numbers between {min_num} and {max_num}. The minimum and" \
         "maximum number may be included in your guess."

INSTRUCTIONS = ""

INVALID_RESPONSE = "That was not a valid response. Please try again."

INVALID_RESPONSE_AND_EXIT = "I am sorry. Your input does not match a valid yes or no response. " \
                            "\n The program will now exit. Please try again later."

LOST_GAME = "Game lost. The correct answer was {answer}. :( Better luck next time!"

NO_RESPONSES = {"N", "NO", "n", "no"}

PLAY_GAME = "Would you like to play mastermind? Y/N? "

RANDOMDOTORG_APIKEY = "475df9e9-d3d0-4bcd-a0c8-5db30b110daf"

REMAINING_TURNS = "You have {turns} turns remaining."

TRY_AGAIN = "Good guess! Please try again."

WELCOME = "WELCOME TO MASTERMIND."

WON_GAME = "Congratulations! You won! {guess} matches {answer}."

YES_RESPONSES = {"Y", "YES", "y", "yes"}
