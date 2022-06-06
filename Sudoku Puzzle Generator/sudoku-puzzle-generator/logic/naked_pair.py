import numpy as np
import logic.helpers as helpers
import logic.naked_single as naked_single

def naked_pair(board, candidates):
    # We are not passed an index - we will loop through homes instead

    #Rows
    for i in range(0,81,9):
        naked_pair_row(board, candidates, i)
            
        

    #Cols
    for i in range(0, 9):
        naked_pair_col(board, candidates, i)

    #Boxes
    for i in range(0, 81, 27):
        for j in range(i, i + 9, 3):
            #print("Box Index checking: ", j)
            naked_pair_box(board, candidates, j)



def naked_pair_row(board, candidates, row_start):
    # We are at the starting index of a row
    # Build an array on what we are going to test
    arr = []
    arr_indexs = []
    
    pair_indexs = []
    pair = []
    for i in range(row_start, row_start + 9):
        # Pair - dont care for candidate entries with more than 2 - by definition it would not be a naked pair
        if(len(candidates[i]) == 2):
            arr.append(candidates[i])
            arr_indexs.append(i)

    #print("\nThe Possiblities are: ", arr)
    #print("\nThe arr indexs are: ", arr_indexs)
    # Array of possiblities has been built - double loop (pair) through the loop and union the set
    # If the set union is length 2, then we have our naked pair values
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            union = helpers.union_pair(arr[i],arr[j])
            # Disregard any unions where both sets are length of 1 - this is not desired
            if(len(union) == 2 and (len(arr[i]) + len(arr[j]) > 2)):
                #print(arr[i], arr[j])
                pair_indexs = [arr_indexs[i], arr_indexs[j]]
                pair = union
                break
        else:
            continue
        break

    #print("\nThe Union found is: ", pair)
    #print("\nThe Indexes of these are:", pair_indexs)
    # Loop through the whole row - if if isnt in the pair indexs then remove the two candidates
    for i in range(row_start, row_start + 9):
        if i not in pair_indexs:
            # Loop through the pair and remove from candidates:
            for j in range(len(pair)):
                #if j in candidates[i]:
                if pair[j] in candidates[i]:
                    candidates[i] = np.delete(candidates[i], np.where(candidates[i] == pair[j]))
                    if(len(candidates[i]) == 1):
                        naked_single.naked_single(board,candidates,i)

                    
                
def naked_pair_col(board, candidates, col_start):
    # We are at the starting index of a col
    # Build an array on what we are going to test
    arr = []
    arr_indexs = []
    
    pair_indexs = []
    pair = []
    for i in range(col_start, 81, 9):
        # Pair - dont care for candidate entries with more than 2 - by definition it would not be a naked pair
        # if(len(candidates[i]) < 3):
        if(len(candidates[i]) == 2):
            arr.append(candidates[i])
            arr_indexs.append(i)

    #print("\nThe Possiblities are: ", arr)
    #print("\nThe arr indexs are: ", arr_indexs)
    # Array of possiblities has been built - double loop (pair) through the loop and union the set
    # If the set union is length 2, then we have our naked pair values
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            union = helpers.union_pair(arr[i],arr[j])
            
            if(len(union) == 2 and (len(arr[i]) + len(arr[j]) > 2)):
                #print(arr[i], arr[j])
                pair_indexs = [arr_indexs[i], arr_indexs[j]]
                pair = union
                break
        else:
            continue
        break

    #print("\nThe Union found is: ", pair)
    #print("\nThe Indexes of these are:", pair_indexs)
    # Loop through the whole row - if if isnt in the pair indexs then remove the two candidates
    for i in range(col_start, 81, 9):
        if i not in pair_indexs:
            # Loop through the pair and remove from candidates:
            for j in range(len(pair)):
                if pair[j] in candidates[i]:
                    candidates[i] = np.delete(candidates[i], np.where(candidates[i] == pair[j]))
                    if(len(candidates[i]) == 1):
                        naked_single.naked_single(board,candidates,i)


def naked_pair_box(board, candidates, box_start):
    # We are at the starting index of a box (TL)
    # Build an array on what we are going to test
    arr = []
    arr_indexs = []
    
    pair_indexs = []
    pair = []
    for i in range(box_start, box_start + 3):
        for j in range(i, i + 19, 9):

            # Pair - dont care for candidate entries with more than 2 - by definition it would not be a naked pair
            if(len(candidates[j]) == 2):
                arr.append(candidates[j])
                arr_indexs.append(j)

    #print("\nThe Possiblities are: ", arr)
    #print("\nThe arr indexs are: ", arr_indexs)
    # Array of possiblities has been built - double loop (pair) through the loop and union the set
    # If the set union is length 2, then we have our naked pair values
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            union = helpers.union_pair(arr[i],arr[j])
            
            if(len(union) == 2 and (len(arr[i]) + len(arr[j]) > 2)):
                #print(arr[i], arr[j])
                pair_indexs = [arr_indexs[i], arr_indexs[j]]
                pair = union
                break
        else:
            continue
        break

    # Loop through the whole row - if if isnt in the pair indexs then remove the two candidates
    for i in range(box_start, box_start + 3):
        for j in range(i, i + 19, 9):
            if j not in pair_indexs:
                # Loop through the pair and remove from candidates:
                for k in range(len(pair)):
                    if pair[k] in candidates[j]:
                        candidates[j] = np.delete(candidates[j], np.where(candidates[j] == pair[k]))
                        if(len(candidates[j]) == 1):
                            naked_single.naked_single(board,candidates,j)