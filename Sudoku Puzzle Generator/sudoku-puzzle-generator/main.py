import numpy as np
from board.board import Board
from construction.number_extractor import Extractor
from construction.uniqueness_solver import UniqueSolver
from construction.difficulty_assign import DifficultyAssign

from logic import hidden_pair
from logic import hidden_single
from logic import hidden_triple
from logic import naked_pair
from logic import naked_single
from logic import naked_triple
from logic import pointing_solver
from logic import helpers



if __name__ == '__main__':

    satisfactory_board = False

    # Step One - Build a board
    board = Board()

    while(satisfactory_board == False):
        board.initialise_board()
        board.fill_board()
    
        board.complete_board = board.board.copy()
        board.print_board()
        #Step Two - Extract until non uniqueness
        Extractor.remove_numbers_until_non_uniqueness(board)

        #Half step - if empty count is less than 20 then do nothing - puzzle quality is not adequet
        satisfactory_board =  (board.empty_slot_count() > 20)

    # Oblt reaches here when true so assign puzzle board
    board.puzzle_board = board.board.copy()   
         
    #Step Three - Build Candidate boards
    candidates = helpers.build_candidate_board(board)

    
    board.print_board()
    #Step Four - Build Strings
    board.puzzle_string = helpers.assign_board_string(board.puzzle_board, board.complete_board)

    #Step Five Add the Difficulty onto the strong
    board.puzzle_string += DifficultyAssign.assign_board_difficulty(board.board, candidates)

    

    

    