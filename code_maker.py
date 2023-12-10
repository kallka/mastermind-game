# Author: Karina Kallas
# Date Last Modified: Dec. 8, 2023
#
# Project Name: Master Mind
# Project Description:  A game which can be played by a user "against" the computer.
#                       This is a game where a player tries to guess the number combinations. At the end of each attempt
#                       to guess the 4 number combinations, the computer will provide feedback whether the player had
#                       guess a number correctly, or/and a number and digit correctly. A player must guess the right
#                       number combinations within 10 attempts to win the game.
#
# File Name: code_maker.py
# File Description: This file servers as player1 (the code maker). It is responsible for creating a random code,
#                   validating responses from player2 (the code breaker), and keeping track of remaining turns.
# Sources: https://stackoverflow.com/questions/53198937/python-api-calling-random-org


# #################################################################################################################### #
#                                                                                                                      #
# IMPORTS                                                                                                              #
#                                                                                                                      #
#                                                                                                                      #
# #################################################################################################################### #
import requests
import json
from collections import defaultdict
from messages_constants import RANDOMDOTORG_APIKEY, LOST_GAME, WON_GAME, GUESS_FEEDBACK


# #################################################################################################################### #
#                                                                                                                      #
# CLASS:    CodeMaker                                                                                                  #
#                                                                                                                      #
#           Description: Controls making code, validating answers, and tracking turns.                                 #
#           Methods:    - decrement_turns                                                                              #
#                       - increment_turns                                                                              #
#                       - create_random_code                                                                           #
#                                                                                                                      #
# #################################################################################################################### #
class CodeMaker:
    def __init__(self, turns=10, min_num=0, max_num=7, code_entries=4):
        self.turns = turns
        self.min_num = min_num
        self.max_num = max_num
        self.code_entries = code_entries
        self.answer_code = []               # change this to automatic create_random_code ?

    ####################################################################################################################
    #                                 GETS: - get_turns                                                                #
    #                                       - get_min_num                                                              #
    #                                       - get_max_num                                                              #
    #                                       - get_answer_code                                                          #
    ####################################################################################################################
    def get_turns(self):
        return self.turns

    def get_min_num(self):
        return self.min_num

    def get_max_num(self):
        return self.max_num

    def get_code_entries(self):
        return self.code_entries

    def get_answer_code(self):
        return self.answer_code

    ####################################################################################################################
    #                                       decrement_turns / increment_turns                                          #
    ####################################################################################################################
    def decrement_turns(self):
        '''Can be used to decrement turns if a user gets a hint.'''
        self.turns -= 1

    def increment_turns(self):
        '''Can be used to increment turns if user wants one more try.'''
        self.turns += 1

    ####################################################################################################################
    #                                       create_random_code                                                         #
    ####################################################################################################################
    def create_random_code(self):
        '''
        Connect to random.org API to generate 4 random numbers 0-7 inclusive. Returns a json response that includes
        4 randomly generated numbers in given range. If an error occurs connecting to random.org the HTTP status
        code will be 503.
        :return: a list of 4 random integers
        '''
        # set up data for json request
        raw_data = {
            "jsonrpc": "2.0",
            "method": "generateIntegers",
            "params": {
                "apiKey": RANDOMDOTORG_APIKEY,
                "n": self.code_entries,
                "min": self.min_num,
                "max": self.max_num,
                "replacement": True
            },
            'id': 1
        }
        headers = {'Content-type': 'application/json', 'Content-Length': '200', 'Accept': 'application/json'}
        data = json.dumps(raw_data)

        # TODO: Find an exception to raise for 503 Service Unavailable Error to use try/except
        # send request and receive response
        response = requests.post(
            url='https://api.random.org/json-rpc/2/invoke',
            data=data,
            headers=headers
        )

        # pull random code, list of integers, from response
        json_response = response.json()
        code = json_response['result']['random']['data']
        self.answer_code = code

    ####################################################################################################################
    #                               PROCESS GUESSES:  - process_guess                                                  #
    #                                                 - check_player_guess                                             #
    ####################################################################################################################
    def process_guess(self, guess):
        # check valid guess
        matches = self.check_player_guess(guess)
        # remove a turn
        self.decrement_turns()

        # print result
        format_guess = self.int_list_to_string(guess)
        print(f"{GUESS_FEEDBACK.format(guess=format_guess, match_value_place=matches[0], match_value=matches[1])}")

        # check end of game
        end_game, win = self.check_end_of_game(matches[0])
        if end_game is True:
            format_guess, format_answer = self.int_list_to_string(guess), self.int_list_to_string(self.answer_code)
            if win:
                print(f"{WON_GAME.format(guess=format_guess, answer=format_answer)}")
                # must change turns to 0 to trigger end of loop in ui.py
                self.turns = 0
            else:
                print(f"{LOST_GAME.format(answer=format_answer)}")
        return matches

    def check_end_of_game(self, num_correct_guesses):
        end = False
        win = False

        if self.turns < 1 or num_correct_guesses == self.code_entries:
            end = True
            if num_correct_guesses == self.code_entries:
                win = True

        return end, win

    def check_player_guess(self, guess):
        '''
        Checks the current guess from the code breaker for matches of index and value as well as matches of value only.
        :param guess: The current guess from the code breaker. A list of ints.
        :return: match_value_and_place, match_value_only
        '''
        # create a list to store index of items that did not match and result
        guess_idx_not_matched = []
        answer_not_matched = defaultdict(int)
        match_value_and_place = 0
        match_value_only = 0

        # check for matched value and place
        for idx, num in enumerate(guess):
            if num == self.answer_code[idx]:
                match_value_and_place += 1
            else:
                guess_idx_not_matched.append(idx)
                answer_not_matched[self.answer_code[idx]] += 1

        # check for matched value from remaining
        for idx in guess_idx_not_matched:
            if guess[idx] in answer_not_matched and answer_not_matched[guess[idx]] > 0:
                answer_not_matched[guess[idx]] -= 1
                match_value_only += 1

        return match_value_and_place, match_value_only

    ####################################################################################################################
    #                       PROCESS FOR PRINTING:  - int_list_to_string                                                #
    #                                                                                                                  #
    ####################################################################################################################
    def int_list_to_string(self, int_list):
        return ''.join(map(str, int_list))


# #################################################################################################################### #
#                                                                                                                      #
# MAIN                                                                                                                 #
#                                                                                                                      #
#                                                                                                                      #
# #################################################################################################################### #
def main():
    game = CodeMaker()
    game.create_random_code()
    print(game.answer_code)
    while game.turns > 0:
        print(game.turns)
        game.decrement_turns()
    return 0


if __name__ == "__main__":
    main()
