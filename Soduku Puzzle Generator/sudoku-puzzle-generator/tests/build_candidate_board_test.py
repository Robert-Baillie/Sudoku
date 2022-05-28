from cgi import test
import logic.helpers as helpers
from board.board import Board
import numpy as np

def candidate_board_test():
    test_board = Board()
    # the following board should have the following candidate board:
    test_board.board = np.array( [[1,0,0,0,0,4,0,8,0]
                            ,[0,4,0,0,0,0,0,1,0]
                            ,[8,0,6,2,0,0,0,0,0]
                            ,[0,0,0,5,2,0,7,0,0]
                            ,[0,0,7,0,4,0,2,0,0]
                            ,[0,0,1,0,9,3,0,0,0]
                            ,[0,0,4,0,0,2,5,0,3]
                            ,[0,8,0,0,0,0,0,6,0]
                            ,[0,9,0,3,0,0,0,0,4] ])
    test_board.print_board()

    correct_candidate_board = np.array([
        [1]             ,[2,3,5,7]      ,[2,3,5,9]      ,[6,7,9]        ,[3,5,6,7]      ,[4]            ,[3,6,9]        ,[8]            ,[2,5,6,7,9]
        ,[2,3,5,7,9]    ,[4]            ,[2,3,5,9]      ,[6,7,8,9]      ,[3,5,6,7,8]    ,[5,6,7,8,9]    ,[3,6,9]        ,[1]            ,[2,5,6,7,9]
        ,[8]            ,[3,5,7]        ,[6]            ,[2]            ,[1,3,5,7]      ,[1,5,7,9]      ,[3,4,9]        ,[3,4,5,7,9]    ,[5,7,9]
        ,[3,4,6,9]      ,[3,6]          ,[3,8,9]        ,[5]            ,[2]            ,[1,6,8]        ,[7]            ,[3,4,9]        ,[1,6,8,9]
        ,[3,5,6,9]      ,[3,5,6]        ,[7]            ,[1,6,8]        ,[4]            ,[1,6,8]        ,[2]            ,[3,5,9]        ,[1,5,6,8,9]
        ,[2,4,5,6]      ,[2,5,6]        ,[1]            ,[6,7,8]        ,[9]            ,[3]            ,[4,6,8]        ,[4,5]          ,[5,6,8]
        ,[6,7]          ,[1,6,7]        ,[4]            ,[1,6,7,8,9]    ,[1,6,7,8]      ,[2]            ,[5]            ,[7,9]          ,[3]
        ,[2,3,5,7]      ,[8]            ,[2,3,5]        ,[1,4,7,9]      ,[1,5,7]        ,[1,5,7,9]      ,[1,9]          ,[6]            ,[1,2,7,9]
        ,[2,5,6,7]      ,[9]            ,[2,5]            ,[3]            ,[1,5,6,7,8]    ,[1,5,6,7,8]    ,[1,8]          ,[2,7]          ,[4]], dtype=object
    )
    # That was painful to type...

    test_candidate_board = helpers.build_candidate_board(test_board)

    # Loop over both - compare each element - if differ then board is incorrect
    for i in range(len(correct_candidate_board)):
        for j in range(len(correct_candidate_board[i])):
            if(correct_candidate_board[i][j] - test_candidate_board[i][j] != 0):
                raise Exception("The test for building a candidate board is broken.")
    
    


