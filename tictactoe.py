"""
Tic Tac Toe Player
"""

import math
import sys
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

    """
    myList = []
    #list of X on the board
    listX = []
    #list of O on the board
    listO = []

    # Transform the board to a simple list
    for row in board:
        for element in row:
            myList.append(element)

    # return the player who should play
    if EMPTY in myList:
  
        for element in myList:
            if element==X:
                listX.append(element)
            elif element==O:
                listO.append(element)

        if len(listX) == len(listO):
            return X
        else:
            return O
    else:
        return"""

    if any(None in row for row in board):
        numX = sum(row.count(X) for row in board)
        numO = sum(row.count(O) for row in board)

        if numX == numO:
            return X
        else:
            return O
    else:
        return


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    """for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    choices.add((i, j))
        return choices"""
    # store the set of actions
    choices = set()

    for i, row in enumerate(board):
        for j, cel in enumerate(row):
            if cel == EMPTY:
                choices.add((i, j))
    return choices


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # a copy of board

    # indexes
    i, j = action
    if i < 3 and j < 3 and board[i][j] is EMPTY:
        newplayer = player(board)
        new_board = copy.deepcopy(board)
        new_board[i][j] = newplayer
        return new_board
    else:
        raise Exception("Invalid action!")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2]) and (board[i][0] != EMPTY):
            return board[i][0]
    for i in range(3):
        if (board[0][i] == board[1][i] == board[2][i]) and (board[0][i] != EMPTY):
            return board[0][i]
    if ((board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0])) and (
            board[1][1] != EMPTY):
        return board[1][1]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    mylist = []
    for row in board:
        for element in row:
            mylist.append(element)

    if winner(board) is not None:
        return True
    if EMPTY not in mylist:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    while terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0


def max_value(board):
    if terminal(board):
        return utility(board)
    value = -1
    for action in actions(board):
        value = max(value, min_value(result(board, action)))
        if value == 1:
            break
    return value


def min_value(board):
    if terminal(board):
        return utility(board)
    value = 1
    for action in actions(board):
        value = min(value, max_value(result(board, action)))
        if value == -1:
            break
    return value


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) == X:
        best_value = -1
        best_move = (-1, -1)
        c = sum(row.count(EMPTY) for row in board)
        if c == 9:
            return best_move
        for action in actions(board):
            move_value = min_value(result(board, action))
            if move_value == 1:
                best_move = action
                break
            if move_value > best_value:
                best_move = action
        return best_move
    if player(board) == O:
        best_value = 1
        best_move = (-1, -1)
        for action in actions(board):
            move_value = max_value(result(board, action))
            if move_value == -1:
                best_move = action
                break
            if move_value < best_value:
                best_move = action
        return best_move
