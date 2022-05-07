import random

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

numbers = [1,2,3,4,5,6,7,8,9]


def candidates_already_in_column(board,col):
    false_candidates = []
    for other_row in range(9):
        if board[other_row][col] > 0:
            false_candidates.append(board[other_row][col])
    return false_candidates


def candidate_requirements(board,row,col):
    cell_candidates = numbers
    for num in numbers:
        if num in board[row] or num in candidates_already_in_column(board,col):
            cell_candidates = [x for x in cell_candidates if x != num]
    return cell_candidates


def determine_candidates(board,row):
    candidate_list = []
    for col in range(9):
        
        if board[row][col] > 0:
            cell_candidates = []
        else:
            cell_candidates = candidate_requirements(board,row,col)

        candidate_list.append(cell_candidates)

    return candidate_list


for row in board:
    print(row)
print(determine_candidates(board,0))