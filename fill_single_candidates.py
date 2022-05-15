from find_single_candidates import find_single_cand_in_house, find_single_cand_in_row, find_single_cand_in_col

def fill_single_cand_in_house(board):
    while True:
        row_col_num = find_single_cand_in_house(board)
        if row_col_num == False:
            break
        else:
            row = row_col_num[0]
            col = row_col_num[1]
            num = row_col_num[2]
            board[row][col] = num
            return True
    return False


def fill_single_cand_in_row(board):
    while True:
        row_col_num = find_single_cand_in_row(board)
        if row_col_num == False:
            break
        else:
            row = row_col_num[0]
            col = row_col_num[1]
            num = row_col_num[2]
            board[row][col] = num
            return True
    return False


def fill_single_cand_in_col(board):
    while True:
        row_col_num = find_single_cand_in_col(board)
        if row_col_num == False:
            break
        else:
            row = row_col_num[0]
            col = row_col_num[1]
            num = row_col_num[2]
            board[row][col] = num
            return True
    return False
