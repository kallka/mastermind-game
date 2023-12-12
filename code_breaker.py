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
# File Name: code_breaker.py
# File Description: This file servers as player2 (the code breaker). It enables a player to send guesses to player1
#                   (the code maker), which provides feedback to player2. It also can be configured to provide hints.
#                   The 'hints' portion of this module is currently under construction. CodeBreaker stores past guesses,
#                   past feedback and number of hints for the current game.
#
# Sources:  1. https://mathworld.wolfram.com/Mastermind.html

# #################################################################################################################### #
#                                                                                                                      #
# IMPORTS                                                                                                              #
#                                                                                                                      #
#                                                                                                                      #
# #################################################################################################################### #
from code_maker import CodeMaker
from messages_constants import HINT_0, HINT_1


# #################################################################################################################### #
#                                                                                                                      #
# CLASS:    CodeBreaker                                                                                                #
#                                                                                                                      #
#           Description: Controls making guess, validating guess in corrrect parameters, hints,                        #
#           and tracking guesses and feedback.                                                                         #
#                                                                                                                      #
# #################################################################################################################### #
class CodeBreaker:
    def __init__(self):
        self.current_game = self.set_new_game()
        self.guesses = []
        self.guess_feedback = []
        self.hints = 0

    ####################################################################################################################
    #                                 set_new_game                                                                     #
    ####################################################################################################################
    @classmethod
    def set_new_game(cls) -> object:
        '''
        Creates a new game by creating instance of CodeMaker object and generating random code.
        :return: A new game (object).
        '''
        new_game = CodeMaker()
        new_game.create_random_code()
        return new_game

    ####################################################################################################################
    #                                make_guess                                                                        #
    #                                helper_validate_make_guess                                                        #
    ####################################################################################################################
    def make_guess(self, guess: str) -> bool:
        '''
        Takes a user guess (string) and determines if it is valid. If guess is invalid, immediately returns False.
        If guess is valid, guess is appended to self.guesses and sent to CodeMaker to get feedback on
        corrrect/incorrect matches. Feedback from the CodeMaker is appended to self.guess_feedback.
        Returns if guess was valid, returns True.
        :param guess: A string representing player's guess.
        :return: Boolean value of True if guess was valid or False if guess was invalid.
        '''
        valid, guess = self.helper_validate_make_guess(guess)
        if valid is False:
            return valid

        # save guess, get feedback, and save feedback
        self.guesses.append(guess)
        feedback = self.current_game.process_guess(guess)
        self.guess_feedback.append(feedback)

        # returns True for guess is valid
        return valid

    def helper_validate_make_guess(self, guess: str) -> tuple[bool, list[int]]:
        '''
        Takes the player's guess (string), if length of guess matches code entries,
        turns into a list of integers by converting to ascii values. (*Note int() does not work well
        as certain string values do not convert smoothly to ints.) Confirms that each guess digit is within
        specified parameters and then returns a tuple representing (valid, converted guess).
        If guess was valid, valid = True.
        :param guess: A string representing the player's guess.
        :return: A tuple (valid, guess) where valid is True if the guess was valid and guess is now a list of integers.
        '''
        valid = False

        if guess:
            if len(guess) == self.current_game.get_code_entries():
                guess = list(guess)
                min_num, max_num = self.current_game.get_min_num(), self.current_game.get_max_num()

                for idx, str_num in enumerate(guess):
                    # Convert to ascii values (48-57 are 0-9) as directly converting to integer value causes problems
                    # with some non-integer values.
                    int_num = ord(str_num) - 48
                    if max_num >= int_num >= min_num:
                        guess[idx] = int_num
                        valid = True
                    else:
                        valid = False
                        break

        return valid, guess

    ####################################################################################################################
    #                                 HINTS:    - hints_manager                                                        #
    #                                           - hints_educated_guess                                                 #
    ####################################################################################################################
    def hints_manager(self) -> str:
        '''
        Calculates how many guesses a player has made and makes a determination about what hint is appropriate
        Increments self.hints to track hints. Self.hints can later be used to deduct turns or calculate score.
        :return: A string response to be printed by the UI.
        '''
        min_num = self.current_game.get_min_num()
        max_num = self.current_game.get_max_num()
        if len(self.guesses) == 0:
            return HINT_0.format(min_num=min_num, max_num=max_num)
        else:
            total = 0
            for feedback in self.guess_feedback:
                total += feedback[0] + feedback[1]

            if len(self.guesses) > 0 and self.hints == 0:
                self.hints += 1
                return HINT_1.format(min_num=min_num, max_num=max_num, total=total)
            else:
                self.hints += 1
                return self.hint_educated_guess()

    def hint_educated_guess(self):
        # Knuth algorithm
            # 1. Create the set S of 1296 possible codes, 0000,1112,.., 7777. (8^4 possibilites)
            # 2. Start with initial guess 0011.
            # 3. Play the guess to get a response.
            # 4. If the response is four colored pegs the game is won, the algorithm terminates.
            # 5. Otherwise, remove from S any code that would not give the same response if it (the guess) were the code.
            # 6. Apply minimax technique: For each unused code in S, calculate how many possibilities in S
            #    code of the 1296 not just those in S, calculate how many possibilities in S would be eliminated for
            #    each possible colored/white peg score. The score of a guess is the minimum number of possibilities it
            #    might eliminate from S. From the set of guesses with the maximum score select one as the next guess,
            #    choosing a member of S whenever possible. (Knuth follows the convention of choosing the guess with the
            #    least numeric value e.g. 2345 is lower than 3456. Knuth also gives an example showing that in some
            #    cases no member of S will be among the highest scoring guesses and thus the guess cannot win on the
            #    next turn yet will be necessary to assure a win in five.)
            # 7. Repeat from step 3.

        # Personal observations about solving mastermind
            # 1. Guess 0011
            # 2. Play guess to get response.
            # 3. Review complete match to value only match. Take total, T, of correct answers and create a new guess
            #    selecting at least T numbers from previous solution. Ex. If 2 were complete match and 1 value only,
            #    that means T =3. Pick 2 numbers to stay same and 1 number to change value. 1 new number is selected for
            #    remaining place.
            # 4. If previous guesses exist, compare each selected number to previous T. It should never be lower.
            #    Compare all assumed complete matches to past complete matches. Compare all value only matches to
            #    to past value only matches. T should stay consistent or higher than previous guesses. Lower T helps
            #    elimiate possible number solutions as much as higher T helps find correct solutions.
            # 5. Repeat from 2.

        return "<<< placeholder - under construction >>>"

    ####################################################################################################################
    #                                 remaining_turns                                                                  #
    ####################################################################################################################
    def remaining_turns(self):
        return self.current_game.get_turns()


# #################################################################################################################### #
#                                                                                                                      #
# MAIN                                                                                                                 #
#                                                                                                                      #
#                                                                                                                      #
# #################################################################################################################### #
def main():
    new_player = CodeBreaker()

    while new_player.current_game.get_turns() > 0:
        guess = input(f"Input {new_player.current_game.get_code_entries()} integers "
                      f"between {new_player.current_game.get_min_num()} and {new_player.current_game.get_max_num()}: ")
        new_player.make_guess(guess)

    return 0


if __name__ == "__main__":
    main()
