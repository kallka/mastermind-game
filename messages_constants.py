# Author: Karina Kallas
# Date Last Modified: Dec. 11, 2023
#
# Project Name: Master Mind
# Project Description:  A game which can be played by a user "against" the computer.
#                       This is a game where a player tries to guess the number combinations in a random code
#                       set by the computer. At the end of each attempt to guess the number combinations,
#                       the computer will provide feedback whether the player had guessed a number correctly,
#                       or/and a number and digit correctly. A player must guess the right
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

GET_PRINT = "*** Type 'p' to print previous feedback and guesses!"

GUESS_FEEDBACK = "You guessed: {guess} ... " \
                 "\t-> {match_value_place} matched value and place. " \
                 "\t-> {match_value} matched value, invalid place."

HINT_0 = "**HINT: Try two pairs of random numbers between {min_num} and {max_num}. The minimum and " \
         "maximum number may be included in your guess. Example: 0011.\n"

HINT_1 = "**HINT: Look at your last entry. You had a total of {total} correct. That means of those numbers, " \
         "{total} need to be in your next guess. \nIf you need more help, ask for another hint and I will provide " \
         "an educated guess. \n"

INSTRUCTIONS = "\n\tINSTRUCTIONS\n" \
               "1.) At the start of the game the computer will randomly select a pattern of {code_entries} different " \
               "numbers between the range of {min_num} and {max_num}, inclusive. " \
               "\n2.) A player will have {turns} attempts to guess the number combinations." \
               "\n3.) At the end of each guess, computer will provide feedback that tells the player " \
               "how many guesses matched correct value and place, and how many guesses matched only value." \
               "\n* EXAMPLE: (Assume secret code answer is: 1234 and accepted values are between 0-7.)" \
               "\n\t- You guessed: < 0000 >... 0 matched value and place. 0 matched value, invalid place." \
               "\n\t- You guessed: < 4321 >... 0 matched value and place. 4 matched value, invalid place." \
               "\n\t- You guessed: < 1122 >... 1 matched value and place. 1 matched value, invalid place." \
               "\n\t- You guessed: < 1234 >... 4 matched value and place. 0 matched value, invalid place." \
               "\n**The game is won when a player guesses all correct integers in the correct order. " \
               "The game is lost if the player runs out of turns.\n"

INVALID_RESPONSE = "That was not a valid response. Please try again."

INVALID_RESPONSE_AND_EXIT = "I am sorry. Your input does not match a valid yes or no response. " \
                            "\n The program will now exit. Please try again later."

LOST_GAME = "Game lost. The correct answer was {answer}. :( Better luck next time!"

NO_RESPONSES = {"N", "NO", "n", "no"}

PLAY_GAME = "Would you like to play mastermind? Y/N? "

RANDOMDOTORG_APIKEY = "475df9e9-d3d0-4bcd-a0c8-5db30b110daf"

REMAINING_TURNS = "You have {turns} turns remaining."

WELCOME = "WELCOME TO MASTERMIND."

WON_GAME = "Congratulations! You won! {guess} matches {answer}."

YES_RESPONSES = {"Y", "YES", "y", "yes"}
