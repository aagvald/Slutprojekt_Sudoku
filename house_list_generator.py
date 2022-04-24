def create_house_list(board):
    house_list = [[], [], [], [], [], [], [], [], []]
    
    for row in board:
    
        if board.index(row) < 3:
            for col in range(9):
                if col < 3:
                    house_list[0].append(row[col])
                if 2 < col < 6:
                    house_list[1].append(row[col])
                if 5 < col < 9:
                    house_list[2].append(row[col])
    
        if 2 < board.index(row) < 6:
            for col in range(9):  
                if col < 3:
                    house_list[3].append(row[col])
                if 2 < col < 6:
                    house_list[4].append(row[col])
                if 5 < col < 9:
                    house_list[5].append(row[col])
    
        if 5 < board.index(row) < 9:
            for col in range(9):  
                if col < 3:
                    house_list[6].append(row[col])
                if 2 < col < 6:
                    house_list[7].append(row[col])
                if 5 < col < 9:
                    house_list[8].append(row[col])
    
    return house_list
