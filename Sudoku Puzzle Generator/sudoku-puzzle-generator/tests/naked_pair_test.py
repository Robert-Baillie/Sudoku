import logic.helpers as helpers
import logic.naked_pair as naked_pair
from board.board import Board
import numpy as np



def naked_pair_test_row():
    # Based off of visual testing from https://www.sudokuwiki.org/PuzImages/NP1.png
    test_board = Board()
    
    test_board.board = np.array([[4,0,0,0,0,0,9,3,8]
                            ,[0,3,2,0,9,4,1,0,0]
                            ,[0,9,5,3,0,0,2,4,0]
                            ,[3,7,0,6,0,9,0,0,4]
                            ,[5,2,9,0,0,1,6,7,3]
                            ,[6,0,4,7,0,3,0,9,0]
                            ,[9,5,7,0,0,8,3,0,0]
                            ,[0,0,3,9,0,0,4,0,0]
                            ,[2,4,0,0,3,0,7,0,9]])

    # Build the candidate board
    candidates = helpers.build_candidate_board(test_board)

   # helpers.print_candidate_board(candidates)  - visual confirmation this is correct..
    # From the candidate board we can see there is a naked pair of (1, 6) on the top row - test for this
    naked_pair.naked_pair_row(test_board, candidates, 0)

   #  helpers.print_candidate_board(candidates)

    # Also have the naked pair of 6 and 7 on row 3 )index 18
    naked_pair.naked_pair_row(test_board, candidates, 18)

    # helpers.print_candidate_board(candidates)

    
def naked_pair_test_col():
    # Based off of visual testing from https://www.sudokuwiki.org/PuzImages/NP2.png
    test_board = Board()
    
    test_board.board = np.array([[0,8,0,0,9,0,0,3,0]
                            ,[0,3,0,0,0,0,0,6,9]
                            ,[9,0,2,0,6,3,1,5,8]
                            ,[0,2,0,8,0,4,5,9,0]
                            ,[8,5,1,9,0,7,0,4,6]
                            ,[3,9,4,6,0,5,8,7,0]
                            ,[5,6,3,0,4,0,9,8,7]
                            ,[2,0,0,0,0,0,0,1,5]
                            ,[0,1,0,0,5,0,0,2,0] ])

    # Build the candidate board
    candidates = helpers.build_candidate_board(test_board)

    #helpers.print_candidate_board(candidates) # - visual confirmation this is correct..

    # From the candidate board we can see there is a naked pair of (3,7) on col 4
    naked_pair.naked_pair_col(test_board, candidates, 3)

    helpers.print_candidate_board(candidates)
  
def naked_pair_test_box():
    # Based off of visual testing from https://www.sudokuwiki.org/PuzImages/NP2.png
    test_board = Board()
    
    test_board.board = np.array([[0,8,0,0,9,0,0,3,0]
                            ,[0,3,0,0,0,0,0,6,9]
                            ,[9,0,2,0,6,3,1,5,8]
                            ,[0,2,0,8,0,4,5,9,0]
                            ,[8,5,1,9,0,7,0,4,6]
                            ,[3,9,4,6,0,5,8,7,0]
                            ,[5,6,3,0,4,0,9,8,7]
                            ,[2,0,0,0,0,0,0,1,5]
                            ,[0,1,0,0,5,0,0,2,0] ])

    # Build the candidate board
    candidates = helpers.build_candidate_board(test_board)

    #helpers.print_candidate_board(candidates) # - visual confirmation this is correct..

    # From the candidate board we can see there is a naked pair of (4,7) in BL box
    naked_pair.naked_pair_box(test_board, candidates, 54)

    helpers.print_candidate_board(candidates)

    #Also one of 7,3 in BM
    naked_pair.naked_pair_box(test_board, candidates, 57)

    helpers.print_candidate_board(candidates)
  


   