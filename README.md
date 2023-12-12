# Mastermind
A game which can be played by a user "against" the computer. This is a game where a player tries to guess the number combinations. At the end of each attempt to guess the 4 number combinations, the computer will provide feedback whether the player had guess a number correctly, or/and a number and digit correctly. A player must guess the right number combinations within 10 attempts to win the game.

# Rules
1. At the start of the game the computer will randomly select a pattern of four different numbers from a total of 8 different numbers.
2. A player will have 10 attempts to guess the number combinations.
3. At the end of each guess, computer will provide one of the following response as feedback:
     - The player had guess a correct number.
     - The player had guessed a correct number and its correct location.
     - The player’s guess was incorrect.

# RUN
1. This program was built using python3.9.5. Python versions can be found here: https://www.python.org/downloads/.
2. Please review and install requirements.txt. In command line, enter: < pip: -r requirements.txt >
3. To run the program, cd into the main directory and run ui.py. In the command line, enter: < python3 ui.py >
4. Follow command prompts to play mastermind game. 

# File Structure
├── README.md

├── code_breaker.py

├── code_maker.py

├── messages_constants.py

├── requirements.txt

├── tests

│   ├── test_code_breaker.py

│   ├── test_code_maker.py

│   └── test_ui.py

└── ui.py

# Under Construction / TODO
The following are ideas to expand and improve the program.
1. Hints: Implemented in the CodeBreaker. The hints will act like an aide to the player. Hints start broadly and become more direct. The plan is to implement either the Knuth or Swaszek approach to mastermind. Knuth is well documented but requires high space and time complexity as it relies on first creating a list of all possible permutations of the 0-7 numbers selected for the code entries. Swaszek sacrifices a bit of run time efficiency for simplicity and may be a better option.
2. Two Player Game: Currently, the game is configured to allow only one player to compete against a computer. The human player is always the code breaker. A Game Manager class might be implemented to allow either 2 human players or different combinations of human and computer players.
3. UI Class: The ui.py program might benefit from being turned into a class.
4. Try/except for Random.org API should be changed to loop through a few request tries and then exit if API is unreachable.
5. Consider not automatically setting the random number when CodeBreaker establishes an instance of CodeMaker game object. If another human player is going to set the code, this request wastes time.
6. Testing at nominal level. Needs to be more robust.
       
# Sources
1. https://www.random.org/clients/http/api/
2. https://realpython.com/python-pep8/
3. https://peps.python.org/pep-0000/
4. https://mathworld.wolfram.com/Mastermind.html
5. https://stackoverflow.com/questions/53198937/python-api-calling-random-org
6. https://puzzling.stackexchange.com/questions/546/clever-ways-to-solve-mastermind
7. https://www.seas.upenn.edu/~ncollina/Mastermind.pdf
