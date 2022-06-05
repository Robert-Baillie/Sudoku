from operator import index
import numpy as np
import logic.helpers as helpers

# This will also catch naked pairs - as of now there is no solution for this specific case

def hidden_pair(board, candidates):
    # We are not passed an index - we will loop through homes instead

    #Rows
    for i in range(0,81,9):
        hidden_pair_row(board, candidates, i)
            
        

    #Cols
    for i in range(0, 9):
        hidden_pair_col(board, candidates, i)

    #Boxes
    for i in range(0, 81, 27):
        for j in range(i, i + 9, 3):
            hidden_pair_box(board, candidates, j)


def hidden_pair_row(board, candidates, row_start):
    # Given a row start
    # Initialise a list of arrays - 2D
    # Loop over each candidate (non len 1) and add each index to the count list - i.e a 1 at cell 50 - add 50 to arr[0]
    index_array = [[],[],[],[],[],[],[],[],[]]

    
    for i in range(row_start, row_start + 9):
        # If solution already found, we can ignore
        if(len(candidates[i]) > 1):
            # Loop over this candidate
            for j in range(len(candidates[i])):
                # Push each number into -1 index array
                num = candidates[i][j]
                index_array[num - 1].append(i)

    #print("The index array is: ", index_array)
    # We are testing pairs - do not need arrays longer than 2
    index_to_compare = []
    number_index = []

    for i in range(len(index_array)):
        if(len(index_array[i]) > 1 and len(index_array[i]) < 3):
            # Suitable - push to comparison list
            index_to_compare.append(index_array[i])
            number_index.append(i)

    #print("\nThe passing index arrays are: ", index_to_compare)
    #print("\nThe number indexes are: ", number_index)
    # Double (pair) loop through the index to compare loop - if the union is length 2 then we have found the indexs which contain our hidden double
    index_pair = []
    numbers = []

    for i in range(len(index_to_compare) - 1):
        for j in range(i + 1, len(index_to_compare)):
            union = helpers.union_pair(index_to_compare[i],index_to_compare[j])
            
            if(len(union) == 2 and ((len(index_to_compare[i]) + len(index_to_compare[j])) > 2)):
                numbers.append(number_index[i] + 1)
                numbers.append(number_index[j] + 1)
                index_pair = union
                break
        else:
            continue
        break

    #print("\nThe Index pair is: ", index_pair)
    #print("\nThe numbers are: ", numbers)
    # Remove the numbers
    # Loop through the whole row - if if isnt in the pair indexs then remove the two candidates
    for i in range(row_start, row_start + 9):
        if i in index_pair:
            # Loop through the row - for the indexs we have numbers set them as the candidate
            candidates[i] = numbers
            # for j in range(len(numbers)):
            #     if numbers[j] in candidates[i]:
            #         candidates[i] = np.delete(candidates[i], np.where(candidates[i] == numbers[j]))



def hidden_pair_col(board, candidates, col_start):
   
    index_array = [[],[],[],[],[],[],[],[],[]]

    
    for i in range(col_start, 81, 9):
        
        if(len(candidates[i]) > 1):
           
            for j in range(len(candidates[i])):
                
                num = candidates[i][j]
                index_array[num - 1].append(i)

    #print("The index array is: ", index_array)
    index_to_compare = []
    number_index = []

    for i in range(len(index_array)):
        if(len(index_array[i]) > 1 and len(index_array[i]) < 3):
            index_to_compare.append(index_array[i])
            number_index.append(i)

    #print("\nThe passing index arrays are: ", index_to_compare)
    #print("\nThe number indexes are: ", number_index)
    index_pair = []
    numbers = []

    for i in range(len(index_to_compare) - 1):
        for j in range(i + 1, len(index_to_compare)):
            union = helpers.union_pair(index_to_compare[i],index_to_compare[j])
            
            if(len(union) == 2 and (len(index_to_compare[i]) + len(index_to_compare[j]) > 2)):
                numbers.append(number_index[i] + 1)
                numbers.append(number_index[j] + 1)
                index_pair = union
                break
        else:
            continue
        break

    #print("\nThe Index pair is: ", index_pair)
    #print("\nThe numbers are: ", numbers)
   
    for i in range(col_start, 81, 9):
        if i in index_pair:
          
            candidates[i] = numbers
            



def hidden_pair_box(board, candidates, box_start):
   
    index_array = [[],[],[],[],[],[],[],[],[]]

    
    for i in range(box_start, box_start + 3):
        for j in range(i, i + 19, 9):
        
            if(len(candidates[j]) > 1):
           
                for k in range(len(candidates[j])):
                
                    num = candidates[j][k]
                    index_array[num - 1].append(j)

    #print("The index array is: ", index_array)
    index_to_compare = []
    number_index = []

    for i in range(len(index_array)):
        if(len(index_array[i]) > 1 and len(index_array[i]) < 3):
            index_to_compare.append(index_array[i])
            number_index.append(i)

    ##print("\nThe passing index arrays are: ", index_to_compare)
    #print("\nThe number indexes are: ", number_index)
    index_pair = []
    numbers = []

    for i in range(len(index_to_compare) - 1):
        for j in range(i + 1, len(index_to_compare)):
            union = helpers.union_pair(index_to_compare[i],index_to_compare[j])
            
            if(len(union) == 2 and (len(index_to_compare[i]) + len(index_to_compare[j]) > 2)):
                numbers.append(number_index[i] + 1)
                numbers.append(number_index[j] + 1)
                index_pair = union
                break
        else:
            continue
        break

    #print("\nThe Index pair is: ", index_pair)
    #print("\nThe numbers are: ", numbers)
   
    for i in range(box_start, box_start + 3):
        for j in range(i, i + 19, 9):
            if j in index_pair:
          
                candidates[j] = numbers