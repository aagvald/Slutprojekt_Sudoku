import random

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
    for i in range(len(row)):
        row[i] = random.randint(1,9)
    print(row)

def create_house_list(board):
    house_list = [[], [], [], [], [], [], [], [], []]
    
    for row in board:
    
        if board.index(row) < 3:  
            for i in range(9):  
                if i < 3:
                    house_list[0].append(row[i])
                if 2 < i < 6:
                    house_list[1].append(row[i])
                if 5 < i < 9:
                    house_list[2].append(row[i])
    
        if 2 < board.index(row) < 6:
            for i in range(9):  
                if i < 3:
                    house_list[3].append(row[i])
                if 2 < i < 6:
                    house_list[4].append(row[i])
                if 5 < i < 9:
                    house_list[5].append(row[i])
    
        if 5 < board.index(row) < 9:
            for i in range(9):  
                if i < 3:
                    house_list[6].append(row[i])
                if 2 < i < 6:
                    house_list[7].append(row[i])
                if 5 < i < 9:
                    house_list[8].append(row[i])
    
    return house_list

print(create_house_list(board))