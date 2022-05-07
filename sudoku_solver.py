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

def determine_candidates(board,row):
    candidate_list = [[],[],[],[],[],[],[],[],[]]
    for col in range(9):
        
        if board[row][col] > 0:
            cell_candidates = []
        
        else:
            cell_candidates = numbers
            for num in numbers:
                if num in board[row]:
                    cell_candidates = [x for x in cell_candidates if x != num]
    
        candidate_list[row].append(cell_candidates)

    return candidate_list

print(determine_candidates(board,1))
