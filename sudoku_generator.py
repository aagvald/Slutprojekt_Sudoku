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

column_list = [[], [], [], [], [], [], [], [], []]

for row in board:
    for col in range(len(row)):
        
        while True:
            random_num_candidate = random.randint(1, 9)

            if random_num_candidate not in row:
                 row[col] = random_num_candidate
                 column_list[col].append(row[col])
                 break

    print(row)

print( )

print(column_list)


#for row in range(len(board)):
    #for col in range(9):

        #for i in range(row):

            #if board[row][col] == board[i][col] != 0 and row != i:

                #print(True)
                #print(board[row][col])
                #print(row)
            


print( )

for row in board:
    print(row)

#print(create_house_list(board))