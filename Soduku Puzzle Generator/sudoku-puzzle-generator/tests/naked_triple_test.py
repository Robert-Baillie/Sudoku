import logic.helpers as helpers
import logic.naked_triple as naked_triple
from board.board import Board
import numpy as np

def naked_triple_test_row():
    # Based off of visual testing from https://www.sudokuwiki.org/PuzImages/NT1.png
    test_board = Board()
    
    test_board.board = np.array( [[0,7,0,4,0,8,0,2,9]
                            ,[0,0,2,0,0,0,0,0,4]
                            ,[8,5,4,0,2,0,0,0,7]
                            ,[0,0,8,3,7,4,2,0,0]
                            ,[0,2,0,0,0,0,0,0,0]
                            ,[0,0,3,2,6,1,7,0,0]
                            ,[0,0,0,0,9,3,6,1,2]
                            ,[2,0,0,0,0,0,4,0,3]
                            ,[1,3,0,6,4,2,0,7,0] ])

    # Build the candidate board
    candidates = helpers.build_candidate_board(test_board)

    #helpers.print_candidate_board(candidates)  #- visual confirmation this is correct..
    # From the candidate board we can see there is a naked pair of (1, 6) on the top row - test for this
    naked_triple.naked_triple_row(test_board, candidates, 36)

    helpers.print_candidate_board(candidates)

def naked_triple_test_col():
    # Based off of visual testing from http://hodoku.sourceforge.net/examples/n301.png
    test_board = Board()
    
    test_board.board = np.array( [[0,0,0,2,9,4,3,8,0]
                            ,[0,0,0,1,7,8,6,4,0]
                            ,[4,8,0,3,5,6,1,0,0]
                            ,[0,0,4,8,3,7,5,0,1]
                            ,[0,0,0,4,1,5,7,0,0]
                            ,[5,0,0,6,2,9,8,3,4]
                            ,[9,5,3,7,8,2,4,1,6]
                            ,[1,2,6,5,4,3,9,7,8]
                            ,[0,4,0,9,6,1,2,5,3] ])

    # Build the candidate board
    candidates = helpers.build_candidate_board(test_board)

    #helpers.print_candidate_board(candidates)  #- visual confirmation this is correct..
    # From the candidate board we can see there is a naked pair of (1, 6) on the top row - test for this
    naked_triple.naked_triple_col(test_board, candidates, 1)

    helpers.print_candidate_board(candidates)


def naked_triple_test_box():
    # Based off of visual testing from https://www.sudokuwiki.org/PuzImages/N21.png
    test_board = Board()
    
    test_board.board = np.array( [[2,9,4,5,1,3,0,0,6]
                            ,[6,0,0,8,4,2,3,1,9]
                            ,[3,0,0,6,9,7,2,5,4]
                            ,[0,0,0,0,5,6,0,0,0]
                            ,[0,4,0,0,8,0,0,6,0]
                            ,[0,0,0,4,7,0,0,0,0]
                            ,[7,3,0,1,6,4,0,0,5]
                            ,[9,0,0,7,3,5,0,0,1]
                            ,[4,0,0,9,2,8,6,3,7] ])

    # Build the candidate board
    candidates = helpers.build_candidate_board(test_board)

    #helpers.print_candidate_board(candidates)  #- visual confirmation this is correct..
    
    naked_triple.naked_triple_box(test_board, candidates, 27)
    naked_triple.naked_triple_box(test_board, candidates, 33)


    helpers.print_candidate_board(candidates)