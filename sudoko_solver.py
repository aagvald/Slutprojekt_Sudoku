from decide_candidates import determine_candidates, house_list_candidates
from find_single_candidates import find_single_cand_in_house, find_single_cand_in_row, find_single_cand_in_col
from fill_single_candidates import only_candidate
from solve_board import fill_single_cand_in_house, fill_single_cand_in_row, fill_single_cand_in_col, fill_board, solve_sudoku
from empty_cells import first_empty_cell

board = [
    [5,0,0,0,0,0,3,4,0],
    [2,0,0,0,0,7,0,0,0],
    [0,0,0,0,1,0,0,0,0],
    [0,0,0,3,0,0,0,5,0],
    [0,1,4,0,0,0,0,0,0],
    [0,7,0,0,0,0,0,0,0],
    [0,0,0,8,0,0,0,0,2],
    [6,0,0,5,0,0,0,0,0],
    [0,2,0,0,0,0,7,0,0],
]

board_1 = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
]
for row in board:
    print(row)

print("")

board_1 = solve_sudoku(board)

for row in board:
    print(row)
