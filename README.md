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

# Build Approach
     This mastermind game was designed around the idea that 2 players needed to be represented: a code breaker and a code maker. The ui.py currently serves a the main for the project and also handles all user input. CodeBreaker and CodeMaker can print responses but does not take user input. The goal of this design was to make testing easier as input errors could be isolated to one file. 
     The first round of design focused on implementing a working design based on the requirements in the project prompt. CodeMaker is currently a computer only program but can be built to take a random code from a human user. CodeBreaker is configured to simply handle the current game and help process human input. In this way, an additional player class could be implemented to store information about a player's previous games, scores, rank, etc. The next step is to implement hints for CodeBreaker. Hints could be expanded to create a computer player option for CodeBreaker.
     Currently, CodeMaker handles creating the code, verifying the code, providing feedback, tracking turns, and determining when the game has finished. CodeBreaker stores validates the user guess (prior to sending to the CodeMaker) and handles storing guesses and feedback. It can also print previous feedback. The ui.py takes all user input and also allows users to select 'h' for hints or 'p' to print previous feedback. 
     The messages_constants.py is designed to store printed messages. As I find I am often tweaking the wording of printed messages, this alphabetized list makes the print statements easy to find. In addition, when a section of code is under construction, I can include a directly printed string within the function. This helps me identify which functions or methods still need work.
     The time complexity of this project is currently O(n) with constant space complexity. The CodeBreaker stores the longest lists, but these are bound in size by turns and code entry size. Validation of input and verification of guesses is O(n). This may change as hints is implemented. Currently, most algorithms used to solve mastermind rely on forming a list of all possible permutations of the accepted numbers. In the default case of this program, space complexity would be O(n^m) where n is the number of possible numbers and m is the number of code entries.
     
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
