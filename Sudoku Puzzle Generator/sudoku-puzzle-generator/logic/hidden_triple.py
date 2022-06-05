import numpy as np
import logic.helpers as helpers

# This will also catch naked pairs - as of now there is no solution for this specific case

def hidden_triple(board, candidates):
    # We are not passed an index - we will loop through homes instead

    #Rows
    for i in range(0,81,9):
        hidden_triple_row(board, candidates, i)
            
        

    #Cols
    for i in range(0, 9):
        hidden_triple_col(board, candidates, i)

    #Boxes
    for i in range(0, 81, 27):
        for j in range(i, i + 9, 3):
            hidden_triple_box(board, candidates, j)


def hidden_triple_row(board, candidates, row_start):
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

    ##print("The index array is: ", index_array)
    # We are testing triple - do not need arrays longer than 3
    index_to_compare = []
    number_index = []

    for i in range(len(index_array)):
        if(len(index_array[i]) > 1 and len(index_array[i]) < 4):
            # Suitable - push to comparison list
            index_to_compare.append(index_array[i])
            number_index.append(i)

    #print("\nThe passing index arrays are: ", index_to_compare)
    #print("\nThe number indexes are: ", number_index)
    # Double (pair) loop through the index to compare loop - if the union is length 2 then we have found the indexs which contain our hidden double
    index_triple = []
    numbers = []

    for i in range(len(index_to_compare) - 2):
        for j in range(i + 1, len(index_to_compare) - 1):
            for k in range(j + 1,  len(index_to_compare)):
                union = helpers.union_triple(index_to_compare[i],index_to_compare[j],index_to_compare[k])
            
                if(len(union) == 3 and (len(index_to_compare[i]) + len(index_to_compare[j]) + len(index_to_compare[k])> 3)):
                    numbers.append(number_index[i] + 1)
                    numbers.append(number_index[j] + 1)
                    numbers.append(number_index[k] + 1)
                    index_triple = union
                    break
            else:
                continue
            break
        else:
            continue
        break

    #print("\nThe Index triple is: ", index_triple)
    #print("\nThe numbers are: ", numbers)
    # Remove the numbers
    # Loop through the whole row - if if isnt in the triple indexs then remove the candidates
    for i in range(row_start, row_start + 9):
        if i in index_triple:
            # Loop through the row - for the indexs we have numbers set them as the candidate
            #print("The intersection is: ", helpers.intersection(numbers,candidates[i]))
            candidates[i] = helpers.intersection(numbers,candidates[i])


def hidden_triple_col(board, candidates, col_start):
    # Given a row start
    # Initialise a list of arrays - 2D
    # Loop over each candidate (non len 1) and add each index to the count list - i.e a 1 at cell 50 - add 50 to arr[0]
    index_array = [[],[],[],[],[],[],[],[],[]]

    
    for i in range(col_start, 81, 9):
        # If solution already found, we can ignore
        if(len(candidates[i]) > 1):
            # Loop over this candidate
            for j in range(len(candidates[i])):
                # Push each number into -1 index array
                num = candidates[i][j]
                index_array[num - 1].append(i)

    #print("The index array is: ", index_array)
    # We are testing triple - do not need arrays longer than 3
    index_to_compare = []
    number_index = []

    for i in range(len(index_array)):
        if(len(index_array[i]) > 1 and len(index_array[i]) < 4):
            # Suitable - push to comparison list
            index_to_compare.append(index_array[i])
            number_index.append(i)

    #print("\nThe passing index arrays are: ", index_to_compare)
    #print("\nThe number indexes are: ", number_index)
    # Double (pair) loop through the index to compare loop - if the union is length 2 then we have found the indexs which contain our hidden double
    index_triple = []
    numbers = []

    for i in range(len(index_to_compare) - 2):
        for j in range(i + 1, len(index_to_compare) - 1):
            for k in range(j + 1,  len(index_to_compare)):
                union = helpers.union_triple(index_to_compare[i],index_to_compare[j],index_to_compare[k])
            
                if(len(union) == 3 and (len(index_to_compare[i]) + len(index_to_compare[j]) + len(index_to_compare[k])> 3)):
                    numbers.append(number_index[i] + 1)
                    numbers.append(number_index[j] + 1)
                    numbers.append(number_index[k] + 1)
                    index_triple = union
                    break
            else:
                continue
            break
        else:
            continue
        break

    #print("\nThe Index triple is: ", index_triple)
    #print("\nThe numbers are: ", numbers)
    # Remove the numbers
    # Loop through the whole row - if if isnt in the triple indexs then remove the candidates
    for i in range(col_start, 81, 9):
        if i in index_triple:
            # Loop through the row - for the indexs we have numbers set them as the candidate
            #print("The intersection is: ", helpers.intersection(numbers,candidates[i]))
            candidates[i] = helpers.intersection(numbers,candidates[i])


def hidden_triple_box(board, candidates, box_start):
    # Given a row start
    # Initialise a list of arrays - 2D
    # Loop over each candidate (non len 1) and add each index to the count list - i.e a 1 at cell 50 - add 50 to arr[0]
    index_array = [[],[],[],[],[],[],[],[],[]]

    
    for i in range(box_start, box_start + 3):
        for j in range(i, i + 19, 9):
            # If solution already found, we can ignore
            if(len(candidates[j]) > 1):
                # Loop over this candidate
                for k in range(len(candidates[j])):
                    # Push each number into -1 index array
                    num = candidates[j][k]
                    index_array[num - 1].append(j)

    #print("The index array is: ", index_array)
    # We are testing triple - do not need arrays longer than 3
    index_to_compare = []
    number_index = []

    for i in range(len(index_array)):
        if(len(index_array[i]) > 1 and len(index_array[i]) < 4):
            # Suitable - push to comparison list
            index_to_compare.append(index_array[i])
            number_index.append(i)

    #print("\nThe passing index arrays are: ", index_to_compare)
    #print("\nThe number indexes are: ", number_index)
    # Double (pair) loop through the index to compare loop - if the union is length 2 then we have found the indexs which contain our hidden double
    index_triple = []
    numbers = []

    for i in range(len(index_to_compare) - 2):
        for j in range(i + 1, len(index_to_compare) - 1):
            for k in range(j + 1,  len(index_to_compare)):
                union = helpers.union_triple(index_to_compare[i],index_to_compare[j],index_to_compare[k])
            
                if(len(union) == 3 and (len(index_to_compare[i]) + len(index_to_compare[j]) + len(index_to_compare[k])> 3)):
                    numbers.append(number_index[i] + 1)
                    numbers.append(number_index[j] + 1)
                    numbers.append(number_index[k] + 1)
                    index_triple = union
                    break
            else:
                continue
            break
        else:
            continue
        break

    #print("\nThe Index triple is: ", index_triple)
    #print("\nThe numbers are: ", numbers)
    # Remove the numbers
    # Loop through the whole row - if if isnt in the triple indexs then remove the candidates
    for i in range(box_start, box_start + 3):
        for j in range(i, i + 19, 9):
            if j in index_triple:
                # Loop through the row - for the indexs we have numbers set them as the candidate
                #print("The intersection is: ", helpers.intersection(numbers,candidates[j]))
                candidates[j] = helpers.intersection(numbers,candidates[j])
            