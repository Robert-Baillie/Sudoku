import numpy as np
import logic.helpers as helpers


def naked_triple(board, candidates):
    # We are not passed an index - we will loop through homes instead

    #Rows
    for i in range(0,81,9):
        copy = candidates.copy()
        row = naked_triple_row(board, candidates, i)

        if row and helpers.boards_match(candidates,copy) == False:
            #print("Assigning points via naked triple")
            board.score +=1450
            #print(board.score)
                
        

    #Cols
    for i in range(0, 9):
        copy = candidates.copy()
        col = naked_triple_col(board, candidates, i)

        if col and helpers.boards_match(candidates,copy) == False:
            #print("Assigning points via naked triple")
            board.score +=1450
            #print(board.score)

    #Boxes
    for i in range(0, 81, 27):
        for j in range(i, i + 9, 3):
            copy = candidates.copy()
            box = naked_triple_box(board, candidates, j)

            if box and helpers.boards_match(candidates,copy) == False:
                #print("Assigning points via naked triple")
                board.score +=1450
                #print(board.score)




def naked_triple_row(board, candidates, row_start):
    # We are at the starting index of a row
    # Build an array on what we are going to test
    arr = []
    arr_indexs = []
    
    triple_indexs = []
    triple = []
    for i in range(row_start, row_start + 9):
        # Triple - dont care for candidate entries with more than 3 - by definition it would not be a naked pair
        if(len(candidates[i]) < 4 and len(candidates[i]) > 1):
            arr.append(candidates[i])
            arr_indexs.append(i)
    
    #print("\nThe Possiblities are: ", arr)
    #print("\nThe arr indexs are: ", arr_indexs)
    # Array of possiblities has been built - triple loop (three) through the loop and union the set
    # If the set union is length 3, then we have our triple pair values
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            for k in range(j + 1,  len(arr)):
                union = helpers.union_triple(arr[i],arr[j], arr[k])
            
                if(len(union) == 3 and (len(arr[i]) + len(arr[j]) + len(arr[k])  > 3)):
                    triple_indexs = [arr_indexs[i], arr_indexs[j], arr_indexs[k]]
                    triple = union
                    break
            else:
                continue
            break
        else:
            continue
        break

    #print("\nThe Union found is: ", triple)
    #print("\nThe Indexes of these are:", triple_indexs)
    # Loop through the whole row - if if isnt in the pair indexs then remove the two candidates
    for i in range(row_start, row_start + 9):
        if i not in triple_indexs:
            # Loop through the pair and remove from candidates:
            for j in range(len(triple)):
                if triple[j] in candidates[i]:
                    candidates[i] = np.delete(candidates[i], np.where(candidates[i] == triple[j]))


    if(len(triple) > 0): return True
    return False
        



def naked_triple_col(board, candidates, col_start):
    arr = []
    arr_indexs = []
    
    triple_indexs = []
    triple = []
    for i in range(col_start, 81, 9):
        # Triple - dont care for candidate entries with more than 3 - by definition it would not be a naked pair
        if(len(candidates[i]) < 4 and len(candidates[i]) > 1):
            arr.append(candidates[i])
            arr_indexs.append(i)

    #print("\nThe Possiblities are: ", arr)
    #print("\nThe arr indexs are: ", arr_indexs)
    # Array of possiblities has been built - triple loop (three) through the loop and union the set
    # If the set union is length 3, then we have our triple pair values
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            for k in range(j + 1,  len(arr)):
                union = helpers.union_triple(arr[i],arr[j], arr[k])
            
                if(len(union) == 3 and (len(arr[i]) + len(arr[j]) + len(arr[k])  > 3)):
                    triple_indexs = [arr_indexs[i], arr_indexs[j], arr_indexs[k]]
                    triple = union
                    break
            else:
                continue
            break
        else:
            continue
        break
    
    #print("\nThe Union found is: ", triple)
    #print("\nThe Indexes of these are:", triple_indexs)
    # Loop through the whole row - if if isnt in the pair indexs then remove the two candidates
    for i in range(col_start, 81, 9):
        if i not in triple_indexs:
            # Loop through the pair and remove from candidates:
            for j in range(len(triple)):
                if triple[j] in candidates[i]:
                    candidates[i] = np.delete(candidates[i], np.where(candidates[i] == triple[j]))

    if(len(triple) > 0): return True
    return False


def naked_triple_box(board, candidates, box_start):
    arr = []
    arr_indexs = []
    
    triple_indexs = []
    triple = []
    for i in range(box_start, box_start + 3):
        for j in range(i, i + 19, 9):
            # Triple - dont care for candidate entries with more than 3 - by definition it would not be a naked pair
            if(len(candidates[j]) < 4 and len(candidates[j]) > 1):
                arr.append(candidates[j])
                arr_indexs.append(j)

    #print("\nThe Possiblities are: ", arr)
    #print("\nThe arr indexs are: ", arr_indexs)
    # Array of possiblities has been built - triple loop (three) through the loop and union the set
    # If the set union is length 3, then we have our triple pair values
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            for k in range(j + 1,  len(arr)):
                union = helpers.union_triple(arr[i],arr[j], arr[k])
            
                if(len(union) == 3 and (len(arr[i]) + len(arr[j]) + len(arr[k]) > 3)):
                    triple_indexs = [arr_indexs[i], arr_indexs[j], arr_indexs[k]]
                    triple = union
                    break
            else:
                continue
            break
        else:
            continue
        break

    #print("\nThe Union found is: ", triple)
    #print("\nThe Indexes of these are:", triple_indexs)
    # Loop through the whole row - if if isnt in the pair indexs then remove the two candidates
    for i in range(box_start, box_start + 3):
        for j in range(i, i + 19, 9):
            if j not in triple_indexs:
                # Loop through the pair and remove from candidates:
                for k in range(len(triple)):
                    if triple[k] in candidates[j]:
                        candidates[j] = np.delete(candidates[j], np.where(candidates[j] == triple[k]))

    if(len(triple) > 0): return True
    return False
