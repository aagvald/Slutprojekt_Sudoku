import random
from house_list_generator import create_house_list, identify_house_number, identify_cell_in_house, identify_row, identify_col
from decide_candidates import determine_candidates, house_list_candidates

numbers = [1,2,3,4,5,6,7,8,9]

def first_empty_cell(board):
    for row in range(9):
        for col in range(9):
            cell_candidates = determine_candidates(board)[row][col]
            if len(cell_candidates) > 0:
                cell_info = [row, col, cell_candidates]
                return cell_info


#def