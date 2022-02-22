"""
Tic Tac Toe Player
"""

from copy import deepcopy

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
    x = 0
    o = 0
    for i in board:
        for j in i:
            if j == "X":
                x += 1
            elif j == "O":
                o += 1
    if x == o:
        return X
    if x > o:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action.add((i, j))
    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = deepcopy(board)
    i, j = action
    if i > 2 or i < 0 or j > 2 or j < 0 or type(i) == float or type(j) == float:
        raise Exception("Action not valid")
    if new_board[i][j] != EMPTY:
        raise Exception("Action not valid")
    new_board[i][j] = player(new_board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in range(0, 3):
        if ((board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None)):
            return board[row][0]
    for col in range(0, 3):
        if (board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None):
            return board[0][col]
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
        return board[0][0]
    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
        return board[0][2]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    for i in board:
        if EMPTY in i:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == "X":
        return 1
    if win == "O":
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def maxv(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            v = -5
            for action in actions(board):
                if v == 1:
                    return v, optimal_move
                min_value = minv(result(board, action))[0]
                if min_value > v:
                    v = min_value
                    optimal_move = action
            return v, optimal_move

    def minv(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            v = 5
            for action in actions(board):
                if v == -1:
                    return v, optimal_move
                max_value = maxv(result(board, action))[0]
                if max_value < v:
                    v = max_value
                    optimal_move = action
            return v, optimal_move
    player_turn = player(board)
    if terminal(board):
        return None
    if player_turn == "X":
        return maxv(board)[1]
    else:
        return minv(board)[1]
