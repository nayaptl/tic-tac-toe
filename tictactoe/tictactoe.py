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
    xs=0
    os=0
    
    for i in board:
        for j in i:
            if j == X:
                xs+=1
            elif j == O:
                os+=1
    if xs == 0:#for initial state X starts first
        return X
    elif xs > os:
        return O
    else:
        return X
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    tupleactions=set()
    for i,row in enumerate(board):
        for j,cell in enumerate(row):
            if  cell == EMPTY:
                tupleactions.add((i,j))
    return tupleactions
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise ValueError()
    memoryboard=copy.deepcopy(board)
    memoryboard[action[0]][action[1]] = player(memoryboard)
    return memoryboard
    
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0]==board[i][1] and board[i][1]==board[i][2] and board[i][2] != EMPTY:
            return board[i][2]#check rows 
        if board[0][i]==board[1][i] and board[1][i]==board[2][i] and board[2][i] != EMPTY:
            return board[2][i]#check cols
    if board[0][0]==board[1][1] and board[0][0]==board[2][2] and board[2][2] != EMPTY:
        return board[1][1] #check diagonals
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1] != EMPTY:
        return board[1][1] #check diagonals
        
    if not actions(board):
        return None#if board is completed and nobody won
    #raise NotImplementedError
    return 2#to continue game


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == 2:
        return False
    else: 
        return True
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    elif winner(board)==None:
        return 0
    
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None#terminal board
    if board == initial_state():
        return 0, 1
    best=math.inf#if player is O we need minimum score
    move=None
    if player(board)==X:
        best=-math.inf#if player is X we need maximum score
        
    #newboard=copy.deepcopy(board)
    for setofactions in actions(board):
        if player(board)==X:
            bestval = minval(result(board, setofactions))
            if bestval>best:
                best=bestval
                move=setofactions
        else:
            bestval = maxval(result(board, setofactions))
            if bestval<best:
                best=bestval
                move=setofactions
    return move


def maxval(board):
    if terminal(board):
        return utility(board)
    best=-math.inf
    for setaction in actions(board):
        best = max(best, minval(result(board, setaction)))
    return best
    
    
    
    
    
def minval(board):
    if terminal(board):
        return utility(board)
    best=math.inf
    for setaction in actions(board):
        best = min(best, maxval(result(board, setaction)))
    return best