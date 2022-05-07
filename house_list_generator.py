def create_house_list(board):
    house_list = [[], [], [], [], [], [], [], [], []]
    
    for row in board:
        for col in range(9):
    
            if board.index(row) < 3:
                if col < 3:
                    house_list[0].append(row[col])
                if 2 < col < 6:
                    house_list[1].append(row[col])
                if 5 < col < 9:
                    house_list[2].append(row[col])
    
            if 2 < board.index(row) < 6:  
                if col < 3:
                    house_list[3].append(row[col])
                if 2 < col < 6:
                    house_list[4].append(row[col])
                if 5 < col < 9:
                    house_list[5].append(row[col])
    
            if 5 < board.index(row) < 9:
                if col < 3:
                    house_list[6].append(row[col])
                if 2 < col < 6:
                    house_list[7].append(row[col])
                if 5 < col < 9:
                    house_list[8].append(row[col])
    
    return house_list


def identify_house_number(row,col):
    if row < 3:
        if col < 3:
            return 0
        if 2 < col < 6:
            return 1
        if 5 < col < 9:
            return 2
    
    if 2 < row < 6:
        if col < 3:
            return 3
        if 2 < col < 6:
            return 4
        if 5 < col < 9:
            return 5
    
    if 5 < row < 9:
        if col < 3:
            return 6
        if 2 < col < 6:
            return 7
        if 5 < col < 9:
            return 8


def is_house_unique(board, row):
    for col in range(9):

        if board.index(row) == 1 or board.index(row) == 4 or board.index(row) == 7:
            row_above = board.index(row) - 1
            for i in range(row_above, board.index(row)):
                
                if col < 3:
                    for k in range(3):
                        if board[row_above][k] == row[col]:
                            return False
            
                if 2 < col < 6:
                    for k in range(3, 6):
                        if board[row_above][k] == row[col]:
                            return False
            
                if 5 < col < 9:
                    for k in range(6, 9):
                        if board[row_above][k] == row[col]:
                            return False
                
        if board.index(row) == 2 or board.index(row) == 5 or board.index(row) == 8:
            row_above = board.index(row) - 2
            for i in range(row_above, board.index(row)):

                if col < 3:
                    for k in range(3):
                        if board[row_above][k] == row[col]:
                            return False
            
                if 2 < col < 6:
                    for k in range(3, 6):
                        if board[row_above][k] == row[col]:
                            return False
            
                if 5 < col < 9:
                    for k in range(6, 9):
                        if board[row_above][k] == row[col]:
                            return False
    
    return True