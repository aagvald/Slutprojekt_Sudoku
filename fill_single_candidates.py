from find_single_candidates import find_single_cand_in_house, find_single_cand_in_row, find_single_cand_in_col

def fill_single_cand_in_house(board):
    row_col_num = find_single_cand_in_house(board)
    if row_col_num == False:
        return False
    else:
        row = row_col_num[0]
        col = row_col_num[1]
        num = row_col_num[2]
        board[row][col] = num
        return True


def fill_single_cand_in_row(board):
    row_col_num = find_single_cand_in_row(board)
    if row_col_num == False:
        return False
    else:
        row = row_col_num[0]
        col = row_col_num[1]
        num = row_col_num[2]
        board[row][col] = num
        return True


def fill_single_cand_in_col(board):
    row_col_num = find_single_cand_in_col(board)
    if row_col_num == False:
        return False
    else:
        row = row_col_num[0]
        col = row_col_num[1]
        num = row_col_num[2]
        board[row][col] = num
        return True
