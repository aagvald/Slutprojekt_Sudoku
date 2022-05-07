from house_list_generator import create_house_list, identify_house_number

numbers = [1,2,3,4,5,6,7,8,9]

def candidates_already_in_column(board,col):
    false_candidates = []
    for other_row in range(9):
        if board[other_row][col] > 0:
            false_candidates.append(board[other_row][col])
    return false_candidates


def candidates_already_in_house(board,row,col):
    house_number = identify_house_number(row,col)
    house = create_house_list(board)[house_number]
    return house


def candidate_removal(board,row,col):
    cell_candidates = numbers
    for num in numbers:
        if num in board[row] or num in candidates_already_in_column(board,col) or num in candidates_already_in_house(board,row,col):
            cell_candidates = [x for x in cell_candidates if x != num]
    return cell_candidates
