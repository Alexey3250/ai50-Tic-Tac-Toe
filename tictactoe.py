"""
Tic Tac Toe Player
"""

import math
import copy

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
    # Assigns the board to a new variable - deep copy
    newBoard = copy.deepcopy(board)
    (row, col) = action
    
    # If the action is not valid, raise an exception
    if newBoard[row][col] != EMPTY:
        raise Exception("Invalid action")
    
    # add X or O to the board
    if player(newBoard) == X:
        newBoard[row][col] = X
    else:
        newBoard[row][col] = O
    
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check if X is a winner
    if checkRow(board, X) or checkCol(board, X) or checkDiag(board, X):
        return X
    # Check if O is a winner
    elif checkRow(board, O) or checkCol(board, O) or checkDiag(board, O):
        return O
    # If no one won, return None
    else:
        return None
    
## Helpers for winner function start here
def checkRow(board, player):
    """
    Checks if there is a winner in a row for the given player
    """
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            return True
    return False
    
def checkCol(board, player):
    """
    Checks if there is a winner in a column for the given player
    """
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    return False

def checkDiag(board, player):
    """
    Checks if there is a winner in a diagonal for the given player
    """
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False
## Helpers for winner function end here

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if there is a winner
    if winner(board) != None:
        return True
    
    # Check if there are any empty spaces
    for row in board:
        for col in row:
            if col == EMPTY:
                return False

    # If there is no winner and no empty spaces, the game is over
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Check if X won
    if winner(board) == X:
        return 1
    
    # Check if O won
    if winner(board) == O:
        return -1
    
    # If no one won, return 0
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # If the game is over, return None
    if terminal(board):
        return None
    
    # If it is X's turn
    if player(board) == X:
        # Set the value to negative infinity
        value = -math.inf
        # Set the best action to None
        bestAction = None
        
        # For loop to find the best action
        for action in actions(board):
            # Find the minimum value of the next board
            minVal = min_value(result(board, action))
            # If the minimum value is greater than the current value
            if minVal > value:
                # Set the value to the minimum value
                value = minVal
                # Set the best action to the current action
                bestAction = action
    
    # If it is O's turn
    else:
        # Set the value to positive infinity
        value = math.inf
        # Set the best action to None
        bestAction = None
        
        # For loop to find the best action
        for action in actions(board):
            # Find the maximum value of the next board
            maxVal = max_value(result(board, action))
            # If the maximum value is less than the current value
            if maxVal < value:
                # Set the value to the maximum value
                value = maxVal
                # Set the best action to the current action
                bestAction = action
    
    return bestAction

def max_value(board):
    """
    Returns the maximum value of the board
    """
    # If the game is over, return the utility
    if terminal(board):
        return utility(board)
    
    # Set the value to negative infinity
    value = -math.inf
    
    # For loop to find the maximum value
    for action in actions(board):
        value = max(value, min_value(result(board, action)))
    
    return value

def min_value(board):
    """
    Returns the minimum value of the board
    """
    # If the game is over, return the utility
    if terminal(board):
        return utility(board)
    
    # Set the value to positive infinity
    value = math.inf
    
    # For loop to find the minimum value
    for action in actions(board):
        value = min(value, max_value(result(board, action)))
    
    return value