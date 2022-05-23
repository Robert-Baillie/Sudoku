from board.board import Board
import numpy as np
from construction.number_extractor import Extractor
from construction.uniqueness_solver import UniqueSolver

# boardd = Board()

# boardd.board= np.array([ [2,9,5,7,4,3,8,6,1]
#            ,[4,3,1,8,6,5,9,0,0]
#            ,[8,7,6,1,9,2,5,4,3]
#            ,[3,8,7,4,5,9,2,1,6]
#            ,[6,1,2,3,8,7,4,9,5]
#            ,[5,4,9,2,1,6,7,3,8]
#            ,[7,6,3,5,3,4,1,8,9]
#            ,[9,2,8,6,7,1,3,5,4]
#            ,[1,5,4,9,3,8,6,0,0] ])

# boardd.print_board()

# print(UniqueSolver.get_solution_count(boardd))
for i in range(10000):
    if(i % 100 == 0):
        print(i)
    board_test = Board()

    #board_test.print_board()

    Extractor.remove_numbers_until_non_uniqueness( board_test)
   # board_test.print_board()
    if(board_test.empty_slot_count() == 0):
        
        print("Puzzle Board: ")
        board_test.print_board()
        board_test.print_board()
        print("The board has: ", board_test.empty_slot_count(), " empty slots")

print("Done!")