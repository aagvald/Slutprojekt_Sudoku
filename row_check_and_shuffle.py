import random
from house_list_generator import create_house_list

def is_unique(row_above, row):
    for col in range(len(row_above)):
        if row_above[col] == row[col]:
            return False
    return True

def shuffle_rows(board, row):
    i = 1
    while i == 1:
        count = 0
        for row_above in range(row):
            if is_unique(board[row_above], board[row]) == True:
                count += 1
                if count == row: 
                    i = 2
            else:
                random.shuffle(board[row])
    return row