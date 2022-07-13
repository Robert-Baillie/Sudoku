from operator import index
import numpy as np
import logic.helpers as helpers

def pointing_solver(board, candidates):

    #Rows
    #print("\nROW\n")
    for i in range(0,81,3):
        pointing_solver_row(board, candidates, i)
            
        
    #print("\nCOL\n")
    #Cols
    for i in range(0, 9):
        pointing_solver_col(board, candidates, i)
        pointing_solver_col(board, candidates, i+27)
        pointing_solver_col(board, candidates, i+54)


def pointing_solver_row(board, candidates, indx):
    #Index passed in is the far left of each box home - (0,9,18,27...), (3,12,21,30...) etc
    row_index = [indx, indx+1, indx+2]
    #Loop through the rest of the box row:
    candidate_count = [0,0,0,0,0,0,0,0,0]
    for i in range(indx, indx + 3):
        # Loop through the candidates and add to count
        for j in range(len(candidates[i])):
            num = candidates[i][j]
            candidate_count[num - 1] = candidate_count[num - 1] + 1

    # Loop through the candidate count board and add any to check
    pair_to_check = []
    triple_to_check = []

    for i in range(len(candidate_count)):
        if(candidate_count[i] == 2):
            pair_to_check.append(i + 1)
        if(candidate_count[i] == 3):
            triple_to_check.append(i + 1)
        
    # Loop through the rest of the board and grab the candidates
    other_candidates = []

    box_start = helpers.calculate_box_start(indx)

    for i in range(box_start, box_start + 3):
        for j in range(i, i + 27, 9):
            if ((j not in row_index) and len(candidates[j]) > 1):
                other_candidates.append(candidates[j])

    ##print("\nOther candidates: ", other_candidates)
    # Pair check - loop through the other candidates - if we find it in any list
    pairs = pair_to_check.copy()
    triples = triple_to_check.copy()

    for i in range(len(pair_to_check)):
        for j in range(len(other_candidates)):
            if pair_to_check[i] in other_candidates[j]:
                pairs.remove(pair_to_check[i])
                break
            

     # triple check - loop through the other candidates - if we find it in any list
    for i in range(len(triple_to_check)):
        for j in range(len(other_candidates)):
            
            if triple_to_check[i] in other_candidates[j]:
                triples.remove(triple_to_check[i])
                
                break
            

    # Have our pair and triple
    if(len(pairs) > 0):
        #print("\nOur pair is: ", pairs)
        #Loop over the whole row
        #print("Index is: ", indx)
        row_start = int((indx / 9)) * 9
        #print("Row Start is: ", row_start)

        board.score += 1000
        print("Assigning points via pointing pair")
        print(board.score)

        for i in range(row_start, row_start + 9):
            if((i not in row_index)):
                for j in range(len(pairs)):
                    candidates[i] = np.delete(candidates[i], np.where(candidates[i] == pairs[j]))

    if(len(triples) > 0):
        #print("\nOur triple is: ", triples)
        #Loop over the whole row
        row_start = int((indx / 9)) * 9
        board.score += 1500
        print("Assigning points via pointing triple")
        print(board.score)
        for i in range(row_start, row_start + 9):
            if((i not in row_index)):
                for j in range(len(triples)):
                    candidates[i] = np.delete(candidates[i], np.where(candidates[i] == triples[j]))


def pointing_solver_col(board, candidates, indx):
    #Index passed in is the top of each box home - (0-9)...
    col_index = [indx, indx+9, indx+18]
    #Loop through the rest of the box row:
    candidate_count = [0,0,0,0,0,0,0,0,0]
    for i in range(indx, indx + 19, 9):
        # Loop through the candidates and add to count
        for j in range(len(candidates[i])):
            num = candidates[i][j]
            candidate_count[num - 1] = candidate_count[num - 1] + 1

    # Loop through the candidate count board and add any to check
    pair_to_check = []
    triple_to_check = []

    for i in range(len(candidate_count)):
        if(candidate_count[i] == 2):
            pair_to_check.append(i + 1)
        if(candidate_count[i] == 3):
            triple_to_check.append(i + 1)
        
    # Loop through the rest of the board and grab the candidates
    other_candidates = []

    box_start = helpers.calculate_box_start(indx)

    for i in range(box_start, box_start + 3):
        for j in range(i, i + 27, 9):
            if ((j not in col_index) and len(candidates[j]) > 1):
                other_candidates.append(candidates[j])

    #print("\nOther candidates: ", other_candidates)
    ##print("\nTriples to check before: ", triple_to_check)
    # Pair check - loop through the other candidates - if we find it in any list
    pairs = pair_to_check.copy()
    triples = triple_to_check.copy()

    for i in range(len(pair_to_check)):
        for j in range(len(other_candidates)):
            if pair_to_check[i] in other_candidates[j]:
                pairs.remove(pair_to_check[i])
                break
            

     # triple check - loop through the other candidates - if we find it in any list
    for i in range(len(triple_to_check)):
        for j in range(len(other_candidates)):
            
            if triple_to_check[i] in other_candidates[j]:
                triples.remove(triple_to_check[i])
                break
            

    # Have our pair and triple
    if(len(pairs) > 0):
        #print("\nOur pair is: ", pairs)
        #Loop over the whole row
        #print("Index is: ", indx)
        col_start = int((indx % 9))
        #print("Col Start is: ", col_start)
        print("Assigning points via pointing pair")
        board.score += 1000
        print(board.score)

        for i in range(col_start,81, 9):
            if((i not in col_index)):
                for j in range(len(pairs)):
                    candidates[i] = np.delete(candidates[i], np.where(candidates[i] == pairs[j]))

    if(len(triples) > 0):
        #print("\nOur triple is: ", triples)
        #Loop over the whole row
        col_start = int((indx % 9))
        print("Assigning points via pointing triple")
        board.score += 1500
        print(board.score)

        for i in range(col_start,81, 9):
            if((i not in col_index)):
                for j in range(len(triples)):
                    candidates[i] = np.delete(candidates[i], np.where(candidates[i] == triples[j]))