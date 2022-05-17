from house_list_generator import identify_row, identify_col
from decide_candidates import determine_candidates, house_list_candidates

numbers = [1,2,3,4,5,6,7,8,9]

#Hittar en kandidatsiffra som är begränsad till en enda plats i ett hus och placerar den
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
                board[row][col] = num
                return True
    return False

#Hittar en kandidatsiffra som är begränsad till en enda plats i en rad och placerar den
def find_single_cand_in_row(board):
    candidate_list = determine_candidates(board)
    for row in range(9):
        for num in numbers:

            digit_cand_count = []
            for col in range(9):
                if num in candidate_list[row][col]:
                    digit_cand_count.append([row, col, num])
            
            if len(digit_cand_count) == 1:
                row = digit_cand_count[0][0]
                col = digit_cand_count[0][1]
                board[row][col] = num
                return True
    return False

#Hittar en kandidatsiffra som är begränsad till en enda plats i en kolumn och placerar den
def find_single_cand_in_col(board):
    candidate_list = determine_candidates(board)
    for col in range(9):
        for num in numbers:

            digit_cand_count = []
            for row in range(9):
                if num in candidate_list[row][col]:
                    digit_cand_count.append([row, col, num])
            
            if len(digit_cand_count) == 1:
                row = digit_cand_count[0][0]
                col = digit_cand_count[0][1]
                board[row][col] = num
                return True
    return False


#Hittar en plats som har en enda kandidat och placerar den
def only_candidate(board):
    candidate_list = determine_candidates(board)
    for row in range(9):
        for col in range(9):
            if len(candidate_list[row][col]) == 1:
                num = candidate_list[row][col][0]
                board[row][col] = num
                return True
    return False
