import logic.helpers as helpers
import logic.pointing_solver as pointing_solver
from board.board import Board
import numpy as np

def pointing_pair_whole():
    # From example - https://www.sudokuwiki.org/PuzImages/PP2.png 
    test_board = Board()
    
    test_board.board = np.array( [[0,3,2,0,0,6,1,0,0]
                            ,[4,1,0,0,0,0,0,0,0]
                            ,[0,0,0,9,0,1,0,0,0]
                            ,[5,0,0,0,9,0,0,0,4]
                            ,[0,6,0,0,0,0,0,7,1]
                            ,[3,0,0,0,2,0,0,0,5]
                            ,[0,0,0,5,0,8,0,0,0]
                            ,[0,0,0,0,0,0,5,1,9]
                            ,[0,5,7,0,0,9,8,6,0] ])

    test_candidates = helpers.build_candidate_board(test_board)
    helpers.print_candidate_board(test_candidates)

    #Rows  PPR on 12, Two PPRs on 60, PPR on 63
    
    pointing_solver.pointing_solver_row(test_board, test_candidates, 12) #Works
    helpers.print_candidate_board(test_candidates)

    pointing_solver.pointing_solver_row(test_board, test_candidates, 60) #Works
    helpers.print_candidate_board(test_candidates)

    pointing_solver.pointing_solver_row(test_board, test_candidates, 63)  #Works
    helpers.print_candidate_board(test_candidates)

    # Cols PPC on 28, 29, 30,33,34
    pointing_solver.pointing_solver_col(test_board, test_candidates, 28)   #Works
    helpers.print_candidate_board(test_candidates)

    pointing_solver.pointing_solver_col(test_board, test_candidates, 29)     #Works
    helpers.print_candidate_board(test_candidates)

    pointing_solver.pointing_solver_col(test_board, test_candidates, 30)     #Works
    helpers.print_candidate_board(test_candidates)

    pointing_solver.pointing_solver_col(test_board, test_candidates, 33)     #Works
    helpers.print_candidate_board(test_candidates)

    pointing_solver.pointing_solver_col(test_board, test_candidates, 34)     #Works
    helpers.print_candidate_board(test_candidates)

def pointing_triple_col():
    # https://www.sudokuwiki.org/PuzImages/PP3.png indx 59
    test_board = Board()
    
    test_board.board = np.array( [[9,3,0,0,5,0,0,0,0]
                            ,[2,0,0,6,3,0,0,9,5]
                            ,[8,5,6,0,0,2,0,0,0]
                            ,[0,0,3,1,8,0,5,7,0]
                            ,[0,0,5,0,2,0,9,8,0]
                            ,[0,8,0,0,0,5,0,0,0]
                            ,[0,0,0,8,0,0,1,5,9]
                            ,[5,0,8,2,1,0,0,0,4]
                            ,[0,0,0,5,6,0,0,0,8] ])

    test_candidates = helpers.build_candidate_board(test_board)
    helpers.print_candidate_board(test_candidates)

    #Rows  PPR on 12, Two PPRs on 60, PPR on 63
    
    pointing_solver.pointing_solver_col(test_board, test_candidates, 59) #Works
    helpers.print_candidate_board(test_candidates)