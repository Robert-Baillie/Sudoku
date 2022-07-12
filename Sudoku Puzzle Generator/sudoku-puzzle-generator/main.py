import numpy as np
from board.board import Board
from construction.number_extractor import Extractor
from construction.uniqueness_solver import UniqueSolver
from construction.difficulty_assign import DifficultyAssign


from logic import helpers



if __name__ == '__main__':

    for i in range(100000):
        satisfactory_board = False

        # Step One - Build a board
        board = Board()
        board.initialise_board()
        board.fill_board()
        
        board.complete_board = board.board.copy()
            
        #Step Two - Extract until non uniqueness
        Extractor.remove_numbers_until_non_uniqueness(board)

        #Half step - if empty count is less than 20 then do nothing - puzzle quality is not adequet
        if(board.empty_slot_count() > 20):


            # Only reaches here when true so assign puzzle board
            board.puzzle_board = board.board.copy()   
            board.puzzle_zero_count = board.empty_slot_count()

            #Step Three - Build Candidate boards
            candidates = helpers.build_candidate_board(board)
           
           
            #Step Four - Build Strings
            board.puzzle_string = helpers.assign_board_string(board.puzzle_board, board.complete_board)

            #Step Five Add the Difficulty onto the strong
            tmp = DifficultyAssign.assign_board_difficulty(board, candidates)

            board.puzzle_string += str(tmp)
            
            print(board.puzzle_string)

    

    