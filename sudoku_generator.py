import random
from house_list_generator import create_house_list

board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

for row in board:
    for col in range(len(row)):
        
        while True:
            random_num_candidate = random.randint(1, 9)

            if random_num_candidate not in row:
                 row[col] = random_num_candidate
                 break

    print(row)

for i in range(9):
    for j in range(i):
        if board[i][0] == board[j][0] and i != j:
            print(True)
            print(board[i][0])

#print(create_house_list(board))