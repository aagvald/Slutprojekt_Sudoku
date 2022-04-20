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
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for row in board:
    for col in range(len(row)):
        
        while True:
            random_num_candidate = random.randint(1, 9)

            if random_num_candidate not in row:
                 row[col] = random_num_candidate
                 column_list[col].append(row[col])
                 break

    print(row)

def request():
    false_value = []

    for col in range(9):
        if column_list[col][0] == board[1][col]:
            false_value.append(board[1][col])
    
    return len(false_value)


while True:
    
    if request() > 0:
        random.shuffle(board[1])
    else:
        break

print( )
for row in board:
    print(row)


#for col in range(len(board[0])):

    #while True:
        #random_num_candidate = random.choice(numbers)

        #if random_num_candidate not in board[0]:
            #board[0][col] = random_num_candidate
            #break

    #numbers.remove(random_num_candidate)
    #column_list[col].append(random_num_candidate)

#for row in board:
    #print(row)



#def determine_candidates(row):
    
    #numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #candidates_list = []

    #for col in range(9):
        #candidates = []

        #for num in numbers:
            #if num not in column_list[col] and num not in row:
                #candidates.append(num)
        #candidates_list.append(candidates)
            
    #return candidates_list
