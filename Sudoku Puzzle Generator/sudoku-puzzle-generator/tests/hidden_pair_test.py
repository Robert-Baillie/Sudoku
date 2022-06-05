import logic.helpers as helpers
import logic.hidden_pair as hidden_pair
from board.board import Board
import numpy as np


def hidden_pair_test_row():
    # From example - https://www.sudokuwiki.org/PuzImages/HP1.png HP of (6,7)
    test_board = Board()
    
    test_board.board = np.array( [[0,0,0,0,0,0,0,0,0]
                            ,[9,0,4,6,0,7,0,0,0]
                            ,[0,7,6,8,0,4,1,0,0]
                            ,[3,0,9,7,0,1,0,8,0]
                            ,[7,0,8,0,0,0,3,0,1]
                            ,[0,5,1,3,0,8,7,0,2]
                            ,[0,0,7,5,0,2,6,1,0]
                            ,[0,0,5,4,0,3,2,0,8]
                            ,[0,0,0,0,0,0,0,0,0] ])

    test_candidates = helpers.build_candidate_board(test_board)

    # helpers.print_candidate_board(test_candidates) #- visual confirmation
    hidden_pair.hidden_pair_row(test_board, test_candidates, 0)
    helpers.print_candidate_board(test_candidates)


def hidden_pair_test_col():
    # From example - https://www.sudokuwiki.org/PuzImages/HP2.png
    test_board = Board()
    
    test_board.board = np.array( [[7,2,0,4,0,8,0,3,0]
                            ,[0,8,0,0,0,0,0,4,7]
                            ,[4,0,1,0,7,6,8,0,2]
                            ,[8,1,0,7,3,9,0,0,0]
                            ,[0,0,0,8,5,1,0,0,0]
                            ,[0,0,0,2,6,4,0,8,0]
                            ,[2,0,9,6,8,0,4,1,3]
                            ,[3,4,0,0,0,0,0,0,8]
                            ,[1,6,8,9,4,3,2,7,5] ])

    test_candidates = helpers.build_candidate_board(test_board)

    # helpers.print_candidate_board(test_candidates) #- visual confirmation
    hidden_pair.hidden_pair_col(test_board, test_candidates, 6)
    helpers.print_candidate_board(test_candidates)



def hidden_pair_test_box():
    # From example - https://www.sudokuwiki.org/PuzImages/HP2.png
    test_board = Board()
    
    test_board.board = np.array( [[7,2,0,4,0,8,0,3,0]
                            ,[0,8,0,0,0,0,0,4,7]
                            ,[4,0,1,0,7,6,8,0,2]
                            ,[8,1,0,7,3,9,0,0,0]
                            ,[0,0,0,8,5,1,0,0,0]
                            ,[0,0,0,2,6,4,0,8,0]
                            ,[2,0,9,6,8,0,4,1,3]
                            ,[3,4,0,0,0,0,0,0,8]
                            ,[1,6,8,9,4,3,2,7,5] ])

    test_candidates = helpers.build_candidate_board(test_board)

    # helpers.print_candidate_board(test_candidates) #- visual confirmation
    hidden_pair.hidden_pair_box(test_board, test_candidates, 27)
    #hidden_pair.hidden_pair_row(test_board, test_candidates, 36)
    helpers.print_candidate_board(test_candidates)