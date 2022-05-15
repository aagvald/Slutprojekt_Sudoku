from fill_single_candidates import fill_single_cand_in_house, fill_single_cand_in_row, fill_single_cand_in_col
from brute_forcing import first_empty_cell

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

