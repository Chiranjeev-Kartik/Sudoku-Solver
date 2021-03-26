#!/usr/bin/env python3
# Example board
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
# New Board <- Fill the values to prepare a new board.
# board = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]

row_len = len(board[0])
column_len = len(board)
element_path = []


def board_rep(board_):  # To represent board in a pretty format.
    for i in range(0, column_len):
        print("")
        for j in range(0, row_len):
            if (j + 1) % 3 == 0 and (j + 1) != row_len:
                print(f" {board_[i][j]} |", end="")
                continue
            print(f" {board_[i][j]} ", end="")
        if (i + 1) % 3 == 0 and (i + 1) != column_len:
            print("\n- - - - - - - - - - - - - - -", end="")


def row_check(board_):  # To check that No number repeat in a row.
    for row in board_:
        row_elements = []
        for element in row:
            if element == 0:
                continue
            if element in row_elements:
                return False
            else:
                row_elements.append(element)
    return True


def column_check(board_):  # To check No number repeat in a column.
    for i in range(0, column_len):
        column_elements = []
        for j in range(0, row_len):
            if board_[j][i] == 0:
                continue
            if board_[j][i] in column_elements:
                return False
            else:
                column_elements.append(board_[j][i])
    return True


def valid_no(board_):  # To check No number is more than 9.
    for i in range(0, 9):
        for j in range(0, 9):
            if board_[i][j] > 9:
                return False
    return True


def box_checker(board_):  # To check No number repeat in a Box.
    for x in [0, 1, 2]:
        for i in [0, 1, 2]:
            elements = []
            for j in range(i * 3, i * 3 + 3):
                for k in range(x * 3, x * 3 + 3):
                    if board_[j][k] == 0:
                        continue
                    if board_[j][k] in elements:
                        return False
                    else:
                        elements.append(board_[j][k])
    return True


def solver(board_, i=0, j=0):  # To Fill number according to rows, columns, and boxes.
    # ( Using the back tracking algorithm)
    global element_path
    if board_[i][j] == 0:
        element_path.append((i, j))
        board_[i][j] += 1
        while not (row_check(board_) and column_check(board_) and box_checker(board_) and valid_no(board_)):
            if board_[i][j] < 9:
                board_[i][j] += 1
            else:
                board_[i][j] = 0
                element_path.pop(-1)
                i, j = element_path[-1]
                board_[i][j] += 1
                continue
    return board_, i, j


def result(board_):  # To Move in each column and row.
    i = 0
    j = 0
    while i < 9:
        while j < 9:
            board_, i, j = solver(board_, i, j)
            j += 1
        i += 1
        j = 0
    return board_


board_rep(result(board))
