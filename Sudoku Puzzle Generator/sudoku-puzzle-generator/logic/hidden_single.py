import numpy as np
import logic.helpers as helpers

def hidden_singles(board, candidates, indx):
    
    row = hidden_singles_row(board, candidates, indx)
    col = hidden_singles_col(board, candidates, indx)
    box = hidden_singles_box(board, candidates, indx)

    if(row or col or box):
        return True
    return False


    
                
def hidden_singles_row(board, candidates, indx):

     # Copy the candidates
    available = candidates[indx].copy()

    row = int(indx / 9)
    col = int(indx % 9)



    row_start = int(indx / 9) * 9
    row_end = row_start + 9


    for i in range(row_start, row_end):
        # Do not check the indx we are on
        if i != indx:
            # Loop over the index in the row
            for j in range(len(candidates[i])):
                # If the member we are looking for is in the available list - then remove it
                    if(candidates[i][j] in available):
                        num = candidates[i][j]
                        print("Available before: ", available, " we are deleting: ", num)
                        available = np.delete(available, np.where(available == num))
                        print("Available after: ", available)

    # Loop over row is done - if the size is one then we can assign the number
    if(len(available) == 1 and board.board[row][col] == 0):
        print("Removing via row hidden single: ", available[0], " at index: ", indx)
        helpers.set_available(board, candidates, indx, available)
        return True

    return False


def hidden_singles_col(board, candidates, indx):
    # Col
    available = candidates[indx].copy()

    row = int(indx / 9)
    col = int(indx % 9)



    col_start = int(indx) % 9

    for i in range(col_start, 81, 9):
        if(i != indx):
            for j in range(len(candidates[i])):
                if(candidates[i][j] in available):
                        num = candidates[i][j]
                        print("Available before: ", available, " we are deleting: ", num)
                        available = np.delete(available, np.where(available == num))
                        print("Available after: ", available)
    
  
    if(len(available) == 1 and board.board[row][col] == 0):
        print("Removing via column hidden single: ", available[0], " at index: ", indx)
        helpers.set_available(board, candidates, indx, available)
        return True

    return False


def hidden_singles_box(board, candidates, indx):
    # Box
    available = candidates[indx].copy()

    row = int(indx / 9)
    col = int(indx % 9)



    row_start = int(indx / 9)
    col_start = int(indx) % 9

    box_row_start = int(row_start / 3) * 3
    box_col_start = int(col_start / 3) * 3
    start = box_row_start * 9 + box_col_start

    for i in range(start, start + 3):
        for k in range(i, i + 19, 9):
            if k != indx:

                for j in range(len(candidates[k])):
                    if(candidates[k][j] in available):
                        num = candidates[k][j]
                        print("Available before: ", available, " we are deleting: ", num)
                        available = np.delete(available, np.where(available == num))
                        print("Available after: ", available)

    if(len(available) == 1 and board.board[row][col] == 0):
        print("Removing via box hidden single: ", available[0], " at index: ", indx)
        helpers.set_available(board, candidates, indx, available)
        return True

    return False