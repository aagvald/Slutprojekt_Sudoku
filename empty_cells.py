from decide_candidates import determine_candidates

numbers = [1,2,3,4,5,6,7,8,9]

#Returnerar hur många tomma platser som återstår
def empty_cells_left(board):
    empty_cells = 0
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                empty_cells += 1
    return empty_cells

#Bestämmer första tomma plats med kandidater
def first_empty_cell(board):
    for row in range(9):
        for col in range(9):
            cell_candidates = determine_candidates(board)[row][col]
            if len(cell_candidates) > 0:
                cell_info = [row, col, cell_candidates]
                return cell_info
