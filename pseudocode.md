## Pseudocode

#### Pseudocode for minimax main algorithm

- Given *state* $s$:
    - **MAX** picks action $a$ that produces highest value of **Min-Value**(Result($s, a$))
    - **MIN** picks action $a$ that produces lowest value of **Max-Value**(Result($s, a$))
<br>

- Function **MAX-VALUE**(*state*):
  - if **Terminal-Test**(*state*):
    - return **Utility**(*state*)
  - $v$ = -$\infty$
  - for each *action* in **Actions**(*state*) do:
      - $v$ = max($v$, **MIN-VALUE**(**Result**(*state*, *action*)))
  - return $v$
<br>

- Function **MIN-VALUE**(*state*):
  - if **Terminal-Test**(*state*):
    - return **Utility**(*state*)
  - $v$ = $\infty$
  - for each *action* in **Actions**(*state*) do:
      - $v$ = min($v$, **MAX-VALUE**(**Result**(*state*, *action*)))

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
The result function returns the board that results from making move (i, j) on the board for the given player.

#### Winner
The winner function returns the winner of the game, if there is one.

#### Terminal-Test
The terminal test function returns **True** if the game is over (win, loss or draw), **False** otherwise.
I.e. the function returns **False** if the game is still in progress.

#### Utility
The utility function returns the utility of the board. 
1 if X has won the game, -1 if O has won, 0 otherwise.

#### Minimax
The minimax function returns the optimal action for the current player on the board.

## Additioanl functions