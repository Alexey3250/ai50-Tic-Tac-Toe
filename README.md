# ai50-Tic-Tac-Toe

#### Implementation of an AI to play Tic-Tac-Toe optimally

This is a Tic-Tac-Toe game that I made for the CS50-AI course.
To Play the game, run the following command in the terminal:
>python3 runner.py


<img src="https://i.imgur.com/FSZiCva.gif" width="800" />

https://cs50.harvard.edu/ai/2020/projects/0/tictactoe/

## Algorithm

### Adversarial Search
In artificial intelligence, deep learning, machine learning, and computer vision, adversarial search is basically a kind of search in which one can trace the movement of an enemy or opponent. The step which arises the problem for the user or the user or the agent doesn't want that specific step task to be carried out.

### Minimax
Minimax is a decision rule used in artificial intelligence, decision theory, game theory, statistics, and philosophy for minimizing the possible loss for a worst case (maximum loss) scenario. When dealing with gains, it is referred to as "maximin"—to maximize the minimum gain. Originally formulated for two-player zero-sum game theory, covering both the cases where players take alternate moves and those where they make simultaneous moves, it has also been extended to more complex games and to general decision-making in the presence of uncertainty.

#### Functions
MAX (X) aims to maximise score.
MIN (O) aims to minimise score.

- $So$: initial state
- **Player**($s$): represents the player who is to move on a given state $s$.
- **Actions**($s$): represents the set of actions that can be executed in a given state $s$.
- **Result**($s$, $a$): represents the state that results from executing action $a$ in state $s$. 
  - represents new state - $s$ of the board after implementing the action $a$.
- **Terminal-Test**($s$): returns true if $s$ is a terminal state (or the end of the game).
  - game continues if ***false***.
  - game ends if ***true***.
- **Utility**($s$, $p$): returns the utility of state $s$ to player $p$.
  -  If $p$ wins, return **1**.
  -  If $p$ loses, return **-1**.

##### Algorithm visualization

<img src="https://i.imgur.com/UXGArzz.png" width="800" />

##### Decision tree diagram for minimizing player (O)

<img src="https://i.imgur.com/PGTABN6.png" width="800" />

##### Decision tree diagram for maximizing player (X)

<img src="https://i.imgur.com/8iyG6hQ.png" width="800" />

> images source: https://www.youtube.com/watch?v=D5aJNFWsWew&ab_channel=CS50



### Alpha-Beta Pruning (optional, but may make your AI run more efficiently)
Alpha–beta pruning is a search algorithm that seeks to decrease the number of nodes that are evaluated by the minimax algorithm in its search tree. It is an adversarial search algorithm used commonly for machine playing of two-player games (Tic-tac-toe, Chess, Go, etc.). It stops evaluating a move when at least one possibility has been found that proves the move to be worse than a previously examined move. Such moves need not be evaluated further. When applied to a standard minimax tree, it returns the same move as minimax would, but prunes away branches that cannot possibly influence the final decision. Alpha–beta pruning is a kind of minimax algorithm.

> **Alfa-beta pruning essentially cuts off redundant state calculations.**

##### Vizuallization of alpha-beta pruning

<img src="https://i.imgur.com/RF416mM.png" width="800" />

> images source: https://www.youtube.com/watch?v=D5aJNFWsWew&ab_channel=CS50


## Pseudocode

#### Pseudocode for minimax main algorithm



## Functions for Tic-Tac-Toe in runner.py

#### Player
In the initial state, the player is X. The player is switched after each move.
The function returns the player who is to move next (either X or O).
> We don't need to check initial state because the player is always X in the initial state.

- Starting count of turns for player X: 0
- Starting count of turns for player O: 0

- For loop to count X and O on the board:
    - If the board has X:
        - Add 1 to the count of X
    - If the board has O:
        - Add 1 to the count of O
- Return the player with the most turns **IF** the count of X = the count of O **then** it's O's turn.
  - >Any return value is acceptable if a terminal state is reached.
  
If X has more turns, then it is O's turn, otherwise game is finished.

##### Implemented code
<img src="https://i.imgur.com/Ukpl3Vu.png" width="400">

#### Actions

The actions function returns a set of all possible actions (row, col) available on the board for the given player.
Possible actions are all empty squares.

- Starting set of actions: empty set
- For loop to check all the cells on the board:
    - If the cell is empty:
        - Add the cell to the set of actions
- Return the set of actions

##### Implemented code
<img src="https://i.imgur.com/ydKWUlh.png" width="533">

#### Result
The result function takes a *board* and an *action* as input and returns the board that results from making that move **without modifying the original board** (using <href="https://docs.python.org/3/library/copy.html#copy.deepcopy">deep copy</href>).
- Assign a deep copy of  the new board to a variable
- Assign row and column of the action to variables
- If the action is not in the set of actions:
    - Raise an exception
- Add X or O to the board depending on the player. **IF** the player is X 
  - **then** add X to the board
  - otherwise add O to the board.
- Return the new board

##### Implemented code
<img src="https://i.imgur.com/1KpU8Qf.png" width="566">

#### Winner
The winner function returns the winner of the game, if there is one.
##### Implemented code
<img src="https://i.imgur.com/FoQoFpd.png" width="500">

> The code can be improved by using the loop only once. In this case, the code will be more efficient but will require more time to write.

#### Helpers for winner function

All functions are taking **board** and **player** as arguments.
Retruns **True** if the player has won the game, **False** otherwise.
#### Check rows
Check if there is a winner in the rows.
##### Implemented code
<img src="https://i.imgur.com/HDLEhKk.png" width="500">
#### Check columns
Check if there is a winner in the columns.
##### Implemented code
<img src="https://i.imgur.com/zdGUzDQ.png" width="500">
#### Check diagonals
Check if there is a winner in the diagonals.
##### Implemented code
<img src="https://i.imgur.com/qSKohDp.png" width="500">

#### Terminal-Test
The terminal test function returns **True** if the game is over (win, loss or draw), **False** otherwise.
> I.e. the function returns **False** if the game is still in progress.

- **IF** the board has a winner **then** the game is over > return **True**
- **IF** the board has empty cells **then** the game is not over > return **False**
- **IF** there is no winner and no empty spaces, the game is over > return **True**
##### Implemented code
<img src="https://i.imgur.com/FbRKhvY.png" width="566">

#### Utility
The utility function returns the utility of the board. 
1 if X has won the game, -1 if O has won, 0 otherwise.
##### Implemented code
<img src="https://i.imgur.com/wSOvZuL.png" width="500">

#### Minimax
The minimax function returns the optimal action for the current player on the board.
- Given *state* $s$:
    - **MAX** picks action $a$ that produces highest value of **Min-Value**(Result($s, a$))
    - **MIN** picks action $a$ that produces lowest value of **Max-Value**(Result($s, a$))

##### Implemented code
<img src="https://i.imgur.com/G1o8kid.png" width="500">
<br>
<br>

#### Max-Value
- Function **MAX-VALUE**(*state*):
  - if **Terminal-Test**(*state*):
    - return **Utility**(*state*)
  - $v$ = -$\infty$
  - for each *action* in **Actions**(*state*) do:
      - $v$ = max($v$, **MIN-VALUE**(**Result**(*state*, *action*)))
  - return $v$

##### Implemented code
<img src="https://i.imgur.com/bVrSL7g.png" width="500">
<br>

#### Min-Value
- Function **MIN-VALUE**(*state*):
  - if **Terminal-Test**(*state*):
    - return **Utility**(*state*)
  - $v$ = $\infty$
  - for each *action* in **Actions**(*state*) do:
      - $v$ = min($v$, **MAX-VALUE**(**Result**(*state*, *action*)))
      - 
##### Implemented code
<img src="https://i.imgur.com/KNbU2QI.png" width="500">

