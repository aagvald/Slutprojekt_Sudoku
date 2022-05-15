def create_house_list(board):
    house_list = [[], [], [], [], [], [], [], [], []]
    
    for row in range(9):
        for col in range(9):
    
            if row < 3:
                if col < 3:
                    house_list[0].append(board[row][col])
                if 2 < col < 6:
                    house_list[1].append(board[row][col])
                if 5 < col < 9:
                    house_list[2].append(board[row][col])
    
            if 2 < row < 6:  
                if col < 3:
                    house_list[3].append(board[row][col])
                if 2 < col < 6:
                    house_list[4].append(board[row][col])
                if 5 < col < 9:
                    house_list[5].append(board[row][col])
    
            if 5 < row < 9:
                if col < 3:
                    house_list[6].append(board[row][col])
                if 2 < col < 6:
                    house_list[7].append(board[row][col])
                if 5 < col < 9:
                    house_list[8].append(board[row][col])
    
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


def identify_row(house_number,cell_number):
    if house_number < 3:
        if cell_number < 3:
            return 0
        if 2 < cell_number < 6:
            return 1
        if 5 < cell_number < 9:
            return 2
    
    if 2 < house_number < 6:
        if cell_number < 3:
            return 3
        if 2 < cell_number < 6:
            return 4
        if 5 < cell_number < 9:
            return 5
    
    if 5 < house_number < 9:
        if cell_number < 3:
            return 6
        if 2 < cell_number < 6:
            return 7
        if 5 < cell_number < 9:
            return 8


def identify_col(house_number,cell_number):
    if house_number == 0 or house_number == 3 or house_number == 6:
        if cell_number < 3:
            return cell_number
        if 2 < cell_number < 6:
            return cell_number - 3
        if 5 < cell_number < 9:
            return cell_number - 6
    
    if house_number == 1 or house_number == 4 or house_number == 7:
        if cell_number < 3:
            return cell_number + 3
        if 2 < cell_number < 6:
            return cell_number
        if 5 < cell_number < 9:
            return cell_number - 3
        
    if house_number == 2 or house_number == 5 or house_number == 8:
        if cell_number < 3:
            return cell_number + 6
        if 2 < cell_number < 6:
            return cell_number + 3
        if 5 < cell_number < 9:
            return cell_number