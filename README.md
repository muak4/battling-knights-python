# Battling Knights

## Python Coding Challenge

### Summary
[Challenge.pdf](https://github.com/muak4/battling-knights-python/blob/main/Challenge.pdf) contains all the necessary information to understand the dynamics of this game. It's a simple 
console game that operates based on the contents of the `moves.txt` file. Contents of file is the combination
of knights movements. It is also explained in [Challenge.pdf](https://github.com/muak4/battling-knights-python/blob/main/Challenge.pdf).

Console will be printed with every movement of knight as well as little
explanation of what happened in this step.

To execute this game, you only need a Python interpreter, which is available on almost all operating systems.

### How to run this script?

Clone a repository, change directory to `battling-knights-python/battling-knights` and execute `main.py` script.

**Commands:**

`cd battling-knights-python/battling-knights`

`python3 main.py` 

This script will look for the `moves.txt` in the same directory. If it found the file, script will continue else script
will exit with Exception `FileNotFoundError`.

When the program finishes all the contents of `moves.txt`. It will generate the **JSON** file with name 
`game_board.json`. Which contains the game final score. Final Score will also be displayed on console. 

### Python Code

Although this is a fairly simple console game, its code is distributed among different files to facilitate better
understanding. Documentation has been added for every function to explain its expected behavior. The files included
in this code are as follows:

- **main.py:** This serves as the starting point of the game, bringing together every element required for gameplay.
  Initially, it reads the `moves.txt` file, iterating over each move and calling the corresponding function to handle it.
  Once all moves have been processed, it generates the final result, saving it in the `game_board.json` file, and 
  displays the result on the console.
- **game_init.py.py:** This initializes key elements, namely knights and items, at the beginning of the game. 
  They are initialized globally to maintain their state consistently throughout the application.
- **game_moves.py:** This component manages all operations related to knight movement on the board. It evaluates 
  everything related to knights and items, including the knight's status (Drowned, Dead, or Alive), the item the 
  knight is holding, and the knight's attack and defense stats. It handles all aspects of a specific move from the 
  moves.txt file.
- **game_state.py:** This component is responsible for updating our 8x8 board. It displays the result of every 
  iteration on the board, step by step, and compiles the final state of our game.
- **utils.py:** This is a helper file where I have written helper methods that are needed throughout the application.
  This file keeps our code clean and easy to understand, as it contains all the minor business logic.
  Function like reading/writing files, error handling are part of this file.
