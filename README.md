# ai50-Tic-Tac-Toe

#### Implementation of an AI to play Tic-Tac-Toe optimally

This is a Tic-Tac-Toe game that I made for the CS50-AI course. It is a two player game, where the first player is X and the second player is O. The game is played on a 3x3 board. The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner. If all 9 squares are filled and neither player has 3 marks in a row, the game is a draw.

<img src="https://cs50.harvard.edu/ai/2020/projects/0/tictactoe/images/game.png" width="800" />

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

#### Pseudocode for minimax algorithm

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

### Alpha-Beta Pruning (optional, but may make your AI run more efficiently)
Alpha–beta pruning is a search algorithm that seeks to decrease the number of nodes that are evaluated by the minimax algorithm in its search tree. It is an adversarial search algorithm used commonly for machine playing of two-player games (Tic-tac-toe, Chess, Go, etc.). It stops evaluating a move when at least one possibility has been found that proves the move to be worse than a previously examined move. Such moves need not be evaluated further. When applied to a standard minimax tree, it returns the same move as minimax would, but prunes away branches that cannot possibly influence the final decision. Alpha–beta pruning is a kind of minimax algorithm.

> **Alfa-beta pruning is essentially cuts off redundant state calculations.**

##### Vizuallization of alpha-beta pruning

<img src="https://i.imgur.com/RF416mM.png" width="800" />

> images source: https://www.youtube.com/watch?v=D5aJNFWsWew&ab_channel=CS50
