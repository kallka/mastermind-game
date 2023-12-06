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
# FUNCTIONS                                                                                                            #
#                                                                                                                      #
#                                                                                                                      #
# #################################################################################################################### #
def create_random_code():
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
            "n": 4,
            "min": 0,
            "max": 7,
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
    # example response: {  "jsonrpc":"2.0",
    #                      "result":{"random":{ "data":[3,1,3,3],
    #                                           "completionTime":"2023-12-06 20:35:12Z"},
    #                                           "bitsUsed":12,"bitsLeft":249712,
    #                                           "requestsLeft":976,
    #                                           "advisoryDelay":2000},
    #                       "id":1}

    jsonResponse = response.json()
    code = jsonResponse['result']['random']['data']

    # result, random , data = value
    return code


# #################################################################################################################### #
#                                                                                                                      #
# MAIN                                                                                                                 #
#                                                                                                                      #
#                                                                                                                      #
# #################################################################################################################### #
def main():
    create_random_code()
    return 0


if __name__ == "__main__":
    main()