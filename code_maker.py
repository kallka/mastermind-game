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
from messages_constants import RANDOMDOTORG_APIKEY


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

    def get_turns(self):
        return self.turns

    def get_min_num(self):
        return self.min_num

    def get_max_num(self):
        return self.max_num

    def get_answer_code(self):
        return self.answer_code

    def decrement_turns(self):
        self.turns -= 1

    def increment_turns(self):
        self.turns += 1

    def create_random_code(self):
        '''
        Connect to random.org API to generate 4 random numbers 0-7 inclusive. Returns a json response that includes
        4 randomly generated numbers in given range.
        :return: a list of 4 random integers
        '''

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

        response = requests.post(
            url='https://api.random.org/json-rpc/2/invoke',
            data=data,
            headers=headers
        )

        json_response = response.json()
        code = json_response['result']['random']['data']
        self.answer_code = code


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
