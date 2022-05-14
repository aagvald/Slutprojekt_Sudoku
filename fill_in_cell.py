from single_candidates import find_single_cand_in_house, find_single_cand_in_row, find_single_cand_in_col

def fill_single_cand_in_house(board):
    while find_single_cand_in_house(board) != False:
        row_col_num = find_single_cand_in_house(board)
        row = row_col_num[0]
        col = row_col_num[1]
        num = row_col_num[2]
        board[row][col] = num


def fill_single_cand_in_row(board):
    while find_single_cand_in_row(board) != False:
        row_col_num = find_single_cand_in_row(board)
        row = row_col_num[0]
        col = row_col_num[1]
        num = row_col_num[2]
        board[row][col] = num


def fill_single_cand_in_col(board):
    while find_single_cand_in_col(board) != False:
        row_col_num = find_single_cand_in_col(board)
        row = row_col_num[0]
        col = row_col_num[1]
        num = row_col_num[2]
        board[row][col] = num


def fill_board(board):
    x = False
    while x == False:
        find_single_cand_in_house
        find_single_cand_in_row
        find_single_cand_in_col

        empty_cells = 0
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    empty_cells += 1
        
        if empty_cells == 0:
            x = True
    return True
