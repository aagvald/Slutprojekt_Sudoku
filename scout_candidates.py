from house_list_generator import create_house_list
from candidate_check import determine_candidates

def house_list_candidates(board):
    candidate_list = determine_candidates(board)
    house_list_candidates = create_house_list(candidate_list)
    return house_list_candidates

