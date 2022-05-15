from fill_single_candidates import fill_single_cand_in_house, fill_single_cand_in_row, fill_single_cand_in_col, only_candidate
from empty_cells import empty_cells_left, first_empty_cell
import copy
import random

def fill_board(board):
    while True:
        if empty_cells_left(board) == 0:
            break

        fill_single_cand_in_house(board)
        fill_single_cand_in_row(board)
        fill_single_cand_in_col(board)
        only_candidate(board)

        if empty_cells_left(board) > 0 and fill_single_cand_in_house(board) == False and fill_single_cand_in_row(board) == False and fill_single_cand_in_col(board) == False:
            return False
    return True
        

def solve_sudoku(board):
    test_board = copy.deepcopy(board)
    if fill_board(board) == True:
        return board

    if fill_board(board) == False:

        cell_info = first_empty_cell(board)
        row = cell_info[0]
        col = cell_info[1]
        candidates = cell_info[2]

        for cand in candidates:
            test_board[row][col] = cand
            if fill_board(test_board) == True:
                board = test_board
                return board
            else:
                test_board = copy.deepcopy(board)

#def try_cands(board):
    #fill_board(board)

    #cell_info = first_empty_cell(board)
    #row = cell_info[0]
    #col = cell_info[1]
    #candidates = cell_info[2]
    #num = random.choice(candidates)

    #board[row][col] = num
    #return num
