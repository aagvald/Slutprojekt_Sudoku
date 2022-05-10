from house_list_generator import create_house_list, identify_row, identify_col
from decide_candidates import determine_candidates

numbers = [1,2,3,4,5,6,7,8,9]

def house_list_candidates(board):
    candidate_list = determine_candidates(board)
    house_cand_list = create_house_list(candidate_list)
    return house_cand_list


def find_single_cand_in_house(board):
    house_cand_list = house_list_candidates(board)
    for house in range(9):
        for num in numbers:

            digit_cand_count = 0
            for cell in range(9):
                if num in house_cand_list[house][cell]:
                    digit_cand_count += 1

            if digit_cand_count == 1:
                house_cell_digit = [house, cell, num]
                row = identify_row(house_cell_digit[0],house_cell_digit[1])
                col = identify_col(house_cell_digit[0],house_cell_digit[1])
                row_col_digit = [row, col, num]
                return row_col_digit


def find_single_cand_in_row(board):
    candidate_list = determine_candidates(board)
    for row in range(9):
        for num in numbers:

            digit_cand_count = 0
            for col in range(9):
                if num in candidate_list[row][col]:
                    digit_cand_count += 1
            
            if digit_cand_count == 1:
                row_col_digit = [row, col, num]
                return row_col_digit


def find_single_cand_in_col(board):
    candidate_list = determine_candidates(board)
    for col in range(9):
        for num in numbers:

            digit_cand_count = 0
            for row in range(9):
                if num in candidate_list[row][col]:
                    digit_cand_count += 1
            
            if digit_cand_count == 1:
                row_col_digit = [row, col, num]
                return row_col_digit