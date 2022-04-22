import random
from house_list_generator import create_house_list
from row_check_and_shuffle import is_unique, shuffle_rows

board = [[],[],[],[],[],[],[],[],[]]

for row in range(len(board)):
    num_list = [1,2,3,4,5,6,7,8,9]

    if row == 0:
        for col in range(9):
            random_num_candidate = random.choice(num_list)
            board[0].append(random_num_candidate)
            num_list.remove(random_num_candidate)
    
    if row > 0:
        for col in range(9):
            random_num_candidate = random.choice(num_list)
            board[row].append(random_num_candidate)
            num_list.remove(random_num_candidate)

        shuffle_rows(board, row)

for row in board:
    print(row)