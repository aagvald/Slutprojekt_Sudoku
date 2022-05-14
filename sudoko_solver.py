import random
from decide_candidates import determine_candidates
from single_candidates import house_list_candidates, find_single_cand_in_house, find_single_cand_in_row, find_single_cand_in_col
from house_list_generator import identify_row, identify_col
from solve_board import fill_single_cand_in_house, fill_single_cand_in_row, fill_single_cand_in_col, fill_board

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

for row in board:
    print(row)

print("")
board = [
    [5, 9, 7, 2, 6, 8, 3, 4, 1],
    [2, 8, 1, 4, 3, 7, 5, 0, 0],
    [4, 3, 6, 9, 1, 5, 2, 7, 8],
    [0, 6, 2, 3, 8, 4, 1, 5, 7],
    [0, 1, 4, 7, 5, 0, 0, 2, 0],
    [0, 7, 5, 1, 2, 0, 0, 0, 4],
    [7, 5, 0, 8, 9, 1, 4, 0, 2],
    [6, 4, 0, 5, 7, 2, 0, 1, 0],
    [1, 2, 0, 6, 4, 3, 7, 0, 5],
]

for row in board:
    print(row)
print("")

fill_single_cand_in_house(board)
#print(house_list_candidates(board)[8][1])
#print(find_single_cand_in_house(board))
#fill_single_cand_in_row(board)
for row in board:
    print(row)