from decide_candidates import determine_candidates
from single_candidates import find_single_cand_in_house, find_single_cand_in_row, find_single_cand_in_col
from solve_board import fill_single_cand_in_house, fill_single_cand_in_row, fill_single_cand_in_col, solve_sudoku

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
    [0,0,7,0,0,0,0,4,0],
    [5,0,0,0,0,0,0,9,3],
    [0,4,0,0,6,2,0,0,1],
    [0,0,0,2,0,7,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,1,2,0,0,9,0,8,0],
    [0,0,9,6,0,0,0,3,0],
    [7,0,0,0,4,1,0,0,6],
    [0,0,0,3,0,0,7,0,0],
]
for row in board_1:
    print(row)

print("")
#solve_sudoku(board_1)

fill_single_cand_in_house(board_1)
fill_single_cand_in_col(board_1)
fill_single_cand_in_row(board_1)
for row in board_1:
    print(row)


print("")
print(find_single_cand_in_col(board_1))
fill_single_cand_in_col(board_1)






for row in board_1:
    print(row)
