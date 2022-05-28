import stat
from board.board import Board
import numpy as np

class UniqueSolver:
    solution_count = 0
    
    @classmethod
    def get_solution_count(cls, bo):
        cls.solution_count = 0
        cls.solve_board_unique(bo, None)
        return cls.solution_count

    
    @classmethod
    def solve_board_unique(cls,bo, last_slot_checked):
        row, col = None, None

        if(last_slot_checked != None):
            row = last_slot_checked[0]
            col = last_slot_checked[1]
        
        # Works very similar to the fill board method in board (Needs to fill board recursively)

        #  Find an empty spot - if we do not find one then the board is complete
        find = bo.find_empty()

        

        if(find is None): 
            # We have a solution - can add limitations here
            cls.solution_count = cls.solution_count + 1
            
            #Remove the last number on the board
            
            last_num = bo.board[row][col]
            start = None

            # If the last number is 9 then we dont want to change the last num to one above - this will cause a call stack errors (10 is never found, hence we always set as 10)
            if(last_num == 9):
                start = last_num - 1
            else:
                start = last_num + 1

            # Loop through the values and try to solve for uniquness again
            for num in range(int(start),10,1):
           
                if(bo.check_valid_number(num,row,col)):
                    bo.board[row][col] = num

                    
                    if(cls.solve_board_unique(bo, last_slot_checked)): 
                        return True

                    
                    bo.board[row][col] = 0
                return False
        else:
            # Assign the row and col - and do as we normally do
            row = find[0]
            col = find[1]

        for num in range(1,10,1):
           
                if(bo.check_valid_number(num,row,col)):
                    bo.board[row][col] = num

                    
                    if(cls.solve_board_unique(bo, find)): 
                        return True

                    
                    bo.board[row][col] = 0

        return False