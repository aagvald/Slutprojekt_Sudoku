import random
from house_list_generator import create_house_list, identify_house_number, is_house_unique

def is_column_unique(row, row_above):
    for col in range(len(row)):
        if row_above[col] == row[col]:
            return False
    return True

def shuffle_rows(board, row):
    i = 1
    while i == 1:
        count = 0
        for row_above in range(row):
            if is_column_unique(board[row], board[row_above]) == True:
                count += 1
                if count == row: 
                    i = 2
            else:
                random.shuffle(board[row])
    return row
