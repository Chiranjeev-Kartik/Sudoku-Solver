"""
Author: Kartikay Chiranjeev Gupta.
Last Modified: 8/1/2021
"""
element_path = []


def board_rep(board, row, col):
    """
    Represents the board in pretty format.
    :param board: 2-D list.
    :param row: Number of rows.
    :param col: Number of columns.
    :return: None.
    """
    for i in range(col):
        print("")
        for j in range(row):
            if (j + 1) % 3 == 0 and (j + 1) != row:
                print(f" {board[i][j]} |", end="")
                continue
            print(f" {board[i][j]} ", end="")
        if (i + 1) % 3 == 0 and (i + 1) != col:
            print("\n- - - - - - - - - - - - - - -", end="")


def take_dim():
    """
    Asks the user for Sudoku board dimension.
    [Note: The Dimension of board must be multiple of 3.]
    :return: row x column.
    """
    [row, col] = list(map(int, input('Enter board dimension (row x column): ').strip().split(' ')))
    if row % 3 != 0 and col % 3 != 0:
        print('Invalid Dimensions!')
        return take_dim()
    else:
        return row, col


def take_board(row, col):
    """
    Asks user to enter board elements.
    [Note: elements must be in range 0-9, Where 0 represents missing value.]
    :param row: Number of rows.
    :param col: Number of columns.
    :return: 2-D list. Representing board elements.
    """
    board = [[] for _ in range(row)]
    for r in range(row):
        for c in range(col):
            e = int(input(f'Element {r + 1}th row and {c + 1}th column: '))
            while not 0 <= e <= 9:
                print('Invalid number!')
                e = int(input(f'Element {r + 1}th row and {c + 1}th column: '))
            board[r].append(e)
    return board


def row_check(board, row, col):
    """
    Returns False if element repeat in row.
    :param board: 2-D list.
    :param row: Number of rows.
    :param col: Number of columns.
    :return: Bool.
    """
    for r in range(row):
        row_element = []
        for c in range(col):
            if board[r][c] == 0:
                continue
            if board[r][c] in row_element:
                return False
            else:
                row_element.append(board[r][c])
    return True


def col_check(board, row, col):
    """
    Returns False if element repeat in column.
    :param board: 2-D list.
    :param row: Number of rows.
    :param col: Number of columns.
    :return: Bool.
    """
    for c in range(col):
        col_element = []
        for r in range(row):
            if board[r][c] == 0:
                continue
            if board[r][c] in col_element:
                return False
            else:
                col_element.append(board[r][c])
    return True


def box_check(board, row, col):
    """
    Returns False if any element is repeated in 3 x 3 box.
    :param board: 2-D list.
    :param row: Number of rows.
    :param col: Number of columns.
    :return: Bool.
    """
    for r in range(row // 3):
        for c in range(col // 3):
            elements = []
            for j in range(c * 3, c * 3 + 3):
                for k in range(r * 3, r * 3 + 3):
                    if board[j][k] == 0:
                        continue
                    if board[j][k] in elements:
                        return False
                    else:
                        elements.append(board[j][k])
    return True


def valid_no(board, row, col):
    """
    Returns False if any element is more than 9.
    :param board: 2-D list.
    :param row: Number of rows.
    :param col: Number of columns.
    :return: Bool.
    """
    for i in range(row):
        for j in range(col):
            if board[i][j] > 9:
                return False
    return True


def solve_for_one(board, row, col, i=0, j=0):
    """
    Update value of only one element specified by i and j. And moves backward if no value satisfy at i, j.
    :param board: 2-D list.
    :param row: Number of rows.
    :param col: Number of columns.
    :param i: ith row.
    :param j: jth column.
    :return: updated board and i, j
    """
    global element_path
    if board[i][j] == 0:
        element_path.append((i, j))
        board[i][j] += 1
        while not (row_check(board, row, col) and col_check(board, row, col) and box_check(board, row, col)
                   and valid_no(board, row, col)):
            if board[i][j] < 9:
                board[i][j] += 1
            else:
                board[i][j] = 0
                element_path.pop(-1)
                i, j = element_path[-1]
                board[i][j] += 1
                continue
    return board, i, j


def solver(board, row, col):
    """
    Moves to all position until the board is solved.
    :param board: 2-D list.
    :param row: Number of rows.
    :param col: Number of columns.
    :return: Final solved board.
    """
    i = 0
    j = 0
    while i < row:
        while j < col:
            board, i, j = solve_for_one(board, row, col, i, j)
            j += 1
        i += 1
        j = 0
    return board


row_, col_ = take_dim()
board_ = take_board(row_, col_)
# row, col = 9, 9
# board = [
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9]
# ]  # Test board. (Zero represent missing values)


board_rep(board_, row_, col_)
print("\n\nSolving board...")
board_rep(solver(board_, row_, col_), row_, col_)
