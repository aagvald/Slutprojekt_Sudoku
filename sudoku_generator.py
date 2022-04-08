import random

grid = [[row, column] for row in range(9) for column in range(9)]

print(grid)

row_list = []
column_list = []
house_list = []

row = []
for i in range(9):
    for i in grid:
        if len(row) < 9:
            row.append(i)
    row_list.append(row)
    row = []
    del grid[0:9]
