"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Start count of turns
    turnX = 0
    turnO = 0
    
    # For loop to count turns of X and O
    for row in board:
        for col in row:
            if col == X:
                turnX += 1
            elif col == O:
                turnO += 1
    
    # Returns who's turn it is
    return X if turnX == turnO else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Create a set of all possible actions
    possibilities = set()
    
    # For loop to add all possible actions to the set
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                possibilities.add((row, col))

    # Return the set of all possible actions
    return possibilities


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    # dont forget to do a deep copy
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

# New implemented functions for a cleaner code

#