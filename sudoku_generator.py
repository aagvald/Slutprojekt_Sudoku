import random

#grid = [[row, column] for row in range(9) for column in range(9)]

#row_list = []
#column_list = []
#house_list = []

#row = []
#for i in range(9):
    #for j in grid:
        #if len(row) < 9:
            #row.append(j)
    #row_list.append(row)
    #row = []
    #del grid[0:9]

#for i in range(9):
    #for j in row_list:
        #column_list.append(j[i])

#house = []
#for i in row_list:
    #for j in range(3):
        #if len(house) < 9:
            #house.append(i[j])
    #house_list.append(house)

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

house = []
for row in board:
    if board.index(row) < 3:
        for i in range(3):
            house.append(row[i])

print(house)