import numpy as np

# Board Building
def build_candidate_board(board):
    # one_to_nine = [1,2,3,4,5,6,7,8,9]
    one_to_nine = np.arange(1,10)

    candidates = [None] * 81
    


    for i in range(81):
        candidates[i] = one_to_nine
        
    
    # Loop through
    for i in range(len(board.board)):
        for j in range(len(board.board[i])):
            indx = 9 * int(i) + int(j)

            num = board.board[i][j]
            
            if(num != 0):
                candidates[indx] = [num]
                remove_from_candidates(board, candidates, indx, i, j, num)

    return candidates


def set_available(board, candidates, indx, available):
    row =int( indx / 9)
    col = int(indx % 9)
    num = available[0]

    board.board[row][col] = num
    candidates[indx] = available

    remove_from_candidates(board, candidates, indx, row, col, num)

    

def remove_from_candidates(board, candidates, indx, row, col, num):
    #Remove number from row
    for row_ind in range(9 * row, 9 * row +9):
        if(row_ind != indx):
            candidates[row_ind] = np.delete(candidates[row_ind], np.where(candidates[row_ind] == num))

            if(len(candidates[row_ind]) == 1 and board.board[int( indx / 9)][int(indx % 9)] == 0):
                print("\n We should set: ", candidates[row_ind], " at index: ", row_ind)
                #set_available(board,candidates,row_ind,candidates[row_ind])
            
            
           

    # Remove from col
    for col_ind in range(col, 81, 9):
        if(col_ind != indx):
            candidates[col_ind] = np.delete(candidates[col_ind], np.where(candidates[col_ind] == num))
            
            

    # Remove from box
    box_row_start = int((row / 3)) * 3
    col_row_start = int((col / 3)) *3
    start = 9 * int(box_row_start) + int(col_row_start)
    end = int(start) + 3

    for box_ind in range(start, end):
        if(box_ind != indx):
            candidates[box_ind] = np.delete(candidates[box_ind], np.where(candidates[box_ind] == num))
            

        if(box_ind + 9 != indx):
            candidates[box_ind + 9] = np.delete(candidates[box_ind + 9], np.where(candidates[box_ind + 9] == num))
            
            
        if(box_ind + 18 != indx):
            candidates[box_ind + 18] = np.delete(candidates[box_ind + 18], np.where(candidates[box_ind + 18] == num))
            



def print_candidate_board(candidates):
    for i in range(len(candidates)):
        if(i % 27 == 0 and i != 0): 
            print("\n-----------------------------------------------------------------------------")
        elif(i % 9 == 0 and i != 0): 
            print("\n", end = "")
        elif(i % 3 == 0 and i != 0 ):
            print (" | ", end = "")
        
        count = 0
        for j in range(len(candidates[i])):
            count = count + 1
            print(candidates[i][j], end = "")
        
        print((8 - count) * " ", end = "")
        
        
def candidate_board_error(candidates):
    for i in range(len(candidates)):
        if(len(candidates[i]) == 0):
            return True
    return False
        


def union_pair(arr1,arr2):
    return list(set().union(arr1,arr2))

def union_triple(arr1,arr2,arr3):
    return list(set().union(arr1,arr2, arr3))

def intersection(arr1,arr2) :
    return  [ e for e in arr1 if e in arr2 ]

def calculate_box_start(indx):  
    row = int(indx / 27) * 27
    col = int((indx % 9) / 3) * 3

    return  row + col



def assign_board_string(puzzle_board, complete_board):
    board = ''

    for i in range(9):
        for j in range(9):
            num = puzzle_board[i][j]
            board += get_number_letter(num)

    for i in range(9):
        for j in range(9):
            num = complete_board[i][j]
            board += get_number_letter(num)

    return board


def boards_match(candidates, copy):
    for i in range(len(candidates)):
        for j in range(len(candidates[i])):
            if candidates[i][j] != copy[i][j]:
                return False

    return True
    

def get_number_letter(num):
    char = chr(num + 96)
    if(num == 0): 
        char = 'x'
    return char