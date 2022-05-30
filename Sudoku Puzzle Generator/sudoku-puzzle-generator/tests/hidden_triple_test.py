import logic.helpers as helpers
import logic.hidden_triple as hidden_triple
from board.board import Board
import numpy as np


def hidden_triple_test():
    # From example - https://www.sudokuwiki.org/PuzImages/HT1.png HT of (2,5,6) on 0
    test_board = Board()
    
    test_board.board = np.array( [[0,0,0,0,0,1,0,3,0]
                            ,[2,3,1,0,9,0,0,0,0]
                            ,[0,6,5,0,0,3,1,0,0]
                            ,[6,7,8,9,2,4,3,0,0]
                            ,[1,0,3,0,5,0,0,0,6]
                            ,[0,0,0,1,3,6,7,0,0]
                            ,[0,0,9,3,6,0,5,7,0]
                            ,[0,0,6,0,1,9,8,4,3]
                            ,[3,0,0,0,0,0,0,0,0] ])

    test_candidates = helpers.build_candidate_board(test_board)
    helpers.print_candidate_board(test_candidates)

    # helpers.print_candidate_board(test_candidates) #- visual confirmation
    hidden_triple.hidden_triple_row(test_board, test_candidates, 0)
    helpers.print_candidate_board(test_candidates)

    # Can then use Col test
    hidden_triple.hidden_triple_col(test_board, test_candidates, 8)
    helpers.print_candidate_board(test_candidates)
