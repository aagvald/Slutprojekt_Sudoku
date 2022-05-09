import random
from decide_candidates import determine_candidates
from scout_candidates import house_list_candidates, find_single_cand_in_house
from house_list_generator import identify_row, identify_col

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

cell_info = find_single_cand_in_house(board)
single_cand_row = (identify_row(cell_info[0],cell_info[1]))
single_cand_col = (identify_col(cell_info[0],cell_info[1]))
