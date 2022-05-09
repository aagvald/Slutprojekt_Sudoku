from house_list_generator import create_house_list
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
                return house_cell_digit

