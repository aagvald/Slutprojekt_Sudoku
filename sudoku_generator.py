import random
from house_list_generator import create_house_list
from row_check_and_shuffle import is_column_unique, is_house_unique, shuffle_rows

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

house_list = create_house_list(board)
print(house_list)
 


for row in board:
    for col in range(9):

        if board.index(row) == 1 or board.index(row) == 4 or board.index(row) == 7:
            row_above = board.index(row) - 1
            for i in range(row_above, board.index(row)):
                
                if col < 3:
                    for k in range(3):
                        if board[row_above][k] == row[col]:
                            print(False)
                            print(board.index(row))
                            print(col)
            
                if 2 < col < 6:
                    for k in range(3, 6):
                        if board[row_above][k] == row[col]:
                            print(False)
                            print(board.index(row))
                            print(col)
            
                if 5 < col < 9:
                    for k in range(6, 9):
                        if board[row_above][k] == row[col]:
                            print(False)
                            print(board.index(row))
                            print(col)
                
        if board.index(row) == 2 or board.index(row) == 5 or board.index(row) == 8:
            row_above = board.index(row) - 2
            for i in range(row_above, board.index(row)):

                if col < 3:
                    for k in range(3):
                        if board[row_above][k] == row[col]:
                            print(False)
                            print(board.index(row))
                            print(col)
            
                if 2 < col < 6:
                    for k in range(3, 6):
                        if board[row_above][k] == row[col]:
                            print(False)
                            print(board.index(row))
                            print(col)
            
                if 5 < col < 9:
                    for k in range(6, 9):
                        if board[row_above][k] == row[col]:
                            print(False)
                            print(board.index(row))
                            print(col)
