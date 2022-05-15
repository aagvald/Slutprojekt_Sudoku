from single_candidates import find_single_cand_in_house, find_single_cand_in_row, find_single_cand_in_col

def fill_single_cand_in_house(board):
    while True:
        row_col_num = find_single_cand_in_house(board)
        if row_col_num == False:
            break
        else:
            row = row_col_num[0]
            col = row_col_num[1]
            num = row_col_num[2]
            board[row][col] = num


def fill_single_cand_in_row(board):
    while True:
        row_col_num = find_single_cand_in_row(board)
        if row_col_num == False:
            break
        else:
            row = row_col_num[0]
            col = row_col_num[1]
            num = row_col_num[2]
            board[row][col] = num


def fill_single_cand_in_col(board):
    while True:
        row_col_num = find_single_cand_in_col(board)
        if row_col_num == False:
            break
        else:
            row = row_col_num[0]
            col = row_col_num[1]
            num = row_col_num[2]
            board[row][col] = num


def empty_cells_left(board):
    empty_cells = 0
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                empty_cells += 1
    return empty_cells


def solve_sudoku(board):
    while True:
        if empty_cells_left(board) == 0:
            break
        fill_single_cand_in_house(board)
        fill_single_cand_in_row(board)
        fill_single_cand_in_col(board)
