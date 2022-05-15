from house_list_generator import create_house_list, identify_row, identify_col
from decide_candidates import determine_candidates, house_list_candidates

numbers = [1,2,3,4,5,6,7,8,9]

def find_single_cand_in_house(board):
    house_cand_list = house_list_candidates(board)
    for house in range(9):
        for num in numbers:

            digit_cand_count = []
            for cell in range(9):
                if num in house_cand_list[house][cell]:
                    digit_cand_count.append([house, cell, num])

            if len(digit_cand_count) == 1:
                house_cell_digit = digit_cand_count[0]
                row = identify_row(house_cell_digit[0],house_cell_digit[1])
                col = identify_col(house_cell_digit[0],house_cell_digit[1])
                row_col_num = [row, col, num]
                return row_col_num
    return False


def find_single_cand_in_row(board):
    candidate_list = determine_candidates(board)
    for row in range(9):
        for num in numbers:

            digit_cand_count = []
            for col in range(9):
                if num in candidate_list[row][col]:
                    digit_cand_count.append([row, col, num])
            
            if len(digit_cand_count) == 1:
                row_col_num = digit_cand_count[0]
                return row_col_num
    return False


def find_single_cand_in_col(board):
    candidate_list = determine_candidates(board)
    for col in range(9):
        for num in numbers:

            digit_cand_count = []
            for row in range(9):
                if num in candidate_list[row][col]:
                    digit_cand_count.append([row, col, num])
            
            if len(digit_cand_count) == 1:
                row_col_num = digit_cand_count[0]
                return row_col_num
    return False
