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

#for row in board:
    #for col in range(len(row)):
        
        #while True:
            #random_num_candidate = random.randint(1, 9)

            #if random_num_candidate not in row:
                 #row[col] = random_num_candidate
                 #column_list[col].append(row[col])
                 #break

    #print(row)



for row in board:

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for col in range(len(row)):
        
        while True:
            random_num_candidate = random.choice(numbers)
            
            if random_num_candidate not in column_list[col]:
                row[col] = random_num_candidate
                break
            
        column_list[col].append(row[col])
        numbers.remove(random_num_candidate)

    print(row)


#print( )

#print(column_list)


#for row in range(len(board)):
    #for col in range(9):

        #for i in range(row):

            #if board[row][col] == board[i][col] != 0 and row != i:

                #print(True)
                #print(board[row][col])
                #print(row)
