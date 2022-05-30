import numpy as np
import logic.helpers as helpers

def hidden_singles(board, candidates, indx):
    
    hidden_singles_row(board, candidates, indx)
    hidden_singles_col(board, candidates, indx)
    hidden_singles_box(board, candidates, indx)
    
                
def hidden_singles_row(board, candidates, indx):
     # Copy the candidates
    available = candidates[indx]

    row_start = int(indx / 9) * 9
    row_end = row_start + 9


    for i in range(row_start, row_end):
        # Do not check the indx we are on
        if i != indx:
            # Loop over the index in the row
            for j in range(len(candidates[i])):
                # If the member we are looking for is in the available list - then remove it
                    if(candidates[i][j] in available):
                        available = np.delete(available, np.where(available == candidates[i][j]))

    # Loop over row is done - if the size is one then we can assign the number
    if(len(available) == 1):
        # print("Removing via row hidden single")
        helpers.set_available(board, candidates, indx, available)
        return True


def hidden_singles_col(board, candidates, indx):
    # Col
    available = candidates[indx]

    col_start = int(indx) % 9

    for i in range(col_start, 81, 9):
        if(i != indx):
            for j in range(len(candidates[i])):
                if(candidates[i][j] in available):
                        available = np.delete(available, np.where(available == candidates[i][j]))
    
  
    if(len(available) == 1):
        # print("Removing via column hidden single")
        helpers.set_available(board, candidates, indx, available)
        return True


def hidden_singles_box(board, candidates, indx):
    # Box
    available = candidates[indx]

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
                        available = np.delete(available, np.where(available == candidates[k][j]))

    if(len(available) == 1):
        # print("Removing via box hidden single")
        helpers.set_available(board, candidates, indx, available)
        return True