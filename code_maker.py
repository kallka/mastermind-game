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
# File Name: code_maker.py
# File Description: This file servers as player1 (the code maker). It is responsible for creating a random code,
#                   validating responses from player2 (the code breaker), and keeping track of remaining turns.
#                   It also checks whether a game has been won or lost.
#
# Sources:  1. https://www.random.org/clients/http/api/
#           2. https://stackoverflow.com/questions/53198937/python-api-calling-random-org


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
#           Description: Controls making code, validating answers, tracking turns, and checking end of game.           #
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
    def get_turns(self) -> int:
        return self.turns

    def get_min_num(self) -> int:
        return self.min_num

    def get_max_num(self) -> int:
        return self.max_num

    def get_code_entries(self) -> int:
        return self.code_entries

    def get_answer_code(self) -> list[int]:
        return self.answer_code

    ####################################################################################################################
    #                                       decrement_turns / increment_turns                                          #
    ####################################################################################################################
    def decrement_turns(self) -> None:
        '''Can be used to decrement turns if a user gets a hint.'''
        self.turns -= 1

    def increment_turns(self) -> None:
        '''Can be used to increment turns if user wants one more try.'''
        self.turns += 1

    ####################################################################################################################
    #                                       create_random_code                                                         #
    ####################################################################################################################
    def create_random_code(self) -> None:
        '''
        Connect to random.org API to generate 4 random numbers 0-7 inclusive. Returns a json response that includes
        4 randomly generated numbers in given range. If an error occurs connecting to random.org the HTTP status
        code will be 503.
        :return: Modifies self.answer_code with a list of 4 random integers.
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

        try:
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
        except requests.exceptions.HTTPError as e:
            # TODO: Create loop in order to try again and then exit in event API unreachable.
            if e.response.status_code == 503:
                print("Random.org API unavailable. Please try again.")

    ####################################################################################################################
    #                               PROCESS GUESSES:  - process_guess                                                  #
    #                                                 - check_end_of_game                                              #
    #                                                 - check_player_guess                                             #
    ####################################################################################################################
    def process_guess(self, guess: str) -> tuple[int, int]:
        '''
        Takes a pre-validated guess(string) from the user, checks the guess against the answer, decrements turns,
        provides feedback, and checks if the game has ended. If game has not ended, returns matches tuple
        (matched_value_and_place, matched_value).
        :param guess: A validated string provided by the player representing current guess.
        :return: A tuple of 2 ints representing (matched_value_and_place, matched_value).
        '''
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

    def check_end_of_game(self, num_correct_guesses: int) -> tuple[bool, bool]:
        '''
        Checks if the game has ended by checking if turns are used up and/or if the player's correct
        matched_value_and_place guesses equal the number of code entries.
        :param num_correct_guesses: int representing number of guesses that matched value and place.
        :return: tuple(bool, bool) representing end (to signal end game) and win result.
        '''
        end = False
        win = False

        # number_correct_guesses corresponds to matched value - if this matches code_entries, game is won
        if self.turns < 1 or num_correct_guesses == self.code_entries:
            end = True
            if num_correct_guesses == self.code_entries:
                win = True

        return end, win

    def check_player_guess(self, guess: list[int]) -> tuple[int, int]:
        '''
        Checks the current guess from the code breaker for matches of index and value as well as matches of value only.
        :param guess: The current guess from the code breaker. A list of ints.
        :return: A tuple representing (match_value_and_place, match_value_only).
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
    def int_list_to_string(self, int_list: list[int]) -> str:
        '''
        Takes a list of integers and returns a printable string.
        :param int_list: List of integers
        :return: String
        '''
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
