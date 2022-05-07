import random
from candidate_check import candidates_already_in_column, candidates_already_in_house, candidate_removal
from house_list_generator import create_house_list, identify_house_number

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

def determine_candidates(board,row):
    candidate_list = []
    for col in range(9):
        if board[row][col] > 0:
            cell_candidates = []
        else:
            cell_candidates = candidate_removal(board,row,col)
        candidate_list.append(cell_candidates)
    return candidate_list


for row in board:
    print(row)
print(determine_candidates(board,0))
