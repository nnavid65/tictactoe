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
    countX = 0
    countO = 0
    
    
    for row in range (len(board)):
        for col in range (len(board[row])):
            if board [row][col] == X:
                countX += 1
            if board [row][col] == O:
                countO +=1
    
    if countX > countO:
        return O
    else:
        return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    allPossibleActions = set()
    
    for row in range (len(board)):
        for col in range (len(board[0])): #instead of 0 I put row
            if [row][col] == EMPTY:
                allPossibleActions.add((row,col))
    
    return allPossibleActions
    


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    if actions in action.board:
        raise Exception ("It is not Valid Actions!!!")
    
    
    row , col = action
    board_copy = copy.deepcopy(board)
    board_copy [row][col] = player(board)
    return board_copy


def checkRow (board, player):
    
        
    for row in range (len(board)):
        if board [row][0] == player and board [row][1] == player and board [row][2] == player:
            return True
        return False

def checkCol (board, player):
    for col in range (len(board)):
        if board [col][0] == player and board [col][1] == player and board [col][1] == player: 
            return True
        return False
    
def checkFirstDig (board, player):
    count = 0
    for row in range (len(board)):
        for col in range (len(board[row])):
            if row == col and board [row][col] == player:
                count += 1
    if count == 3:
        return True
    else: 
        return False
    
def checkSecondDig (board, player):
    count = 0
    for row in range (len(board)):
        for col in range (len(board[row])):
            if (len(board) - row -1) == col and board [row][col] == player:
                count +=1 
    if count == 3:
        return True
    else:
        return False


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checkRow (board, X) or checkCol (board, X) or checkFirstDig (board, X) or checkSecondDig (board, X):
        return X
    elif checkRow (board, O) or checkCol (board, O) or checkFirstDig (board, O) or checkSecondDig (board, 0):
        return O
    else: 
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    if winner == X:
        return True
    if winner == O:
        return True
    for row in range (len(board)):
        for col in range (len(board[row])):
            if board [row][col] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner == X:
        return 1
    if winner == O:
        return -1
    else:
        return 0
    
def max_value(board):
    v = -math.inf
    if terminal.board:
        return utility(board)
    
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v
        
def min_value(board):
    v = math.inf
    if terminal.board:
        return utility(board)
    
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v        


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    # Case of player is X (max player)
    elif player(board) == X:
         plays = []
         # Loop over the possible action 
         for action in actions(board):
             # Add in plays list of tupple with the min value and the action that to its value
             plays.append([min_value(result(board, action)), action])
        # Reverse sort for plays list and get the action that should take 
         return sorted(plays, key = lambda  x: x[0], reverse = True)[0][1]
     
     
        # Case of player is O (max player)
    elif player(board) == O:
         plays = []
         # Loop over the possible action 
         for action in actions(board):
             # Add in plays list of tupple with the min value and the action that to its value
             plays.append([max_value(result(board, action)), action])
        # Reverse sort for plays list and get the action that should take 
         return sorted(plays, key = lambda  x: x[0])[0][1]
     
     
    
