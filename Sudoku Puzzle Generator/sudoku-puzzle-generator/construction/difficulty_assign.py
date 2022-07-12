import numpy as np
from board.board import Board
from construction.uniqueness_solver import UniqueSolver


from logic import hidden_pair
from logic import hidden_single
from logic import hidden_triple
from logic import naked_pair
from logic import naked_single
from logic import naked_triple
from logic import pointing_solver
from logic import helpers


class DifficultyAssign:
    slots_remaining = None

    @classmethod
    def assign_board_difficulty(board, candidates):
        
        # We will loop five times - as we have not implemented super advanced techniuqes any puzzle that cannot be solved in five loops will count as extreme (or maybe impossible...)
        for loop in range(5):

           
            # Hidden Single - Loop everytime a change is made
            change_made = True

            while(change_made):
                change_made = False
                
                for j in range(81):
                    check = hidden_single.hidden_singles(board, candidates, j)
                    if(check):
                        change_made = True

            
            # Have a history of the board breaking - this is due to bad code, mixing different types of arrays, so if it errors assign a difficulty of 0 which will count as null
            if(helpers.candidate_board_error(candidates)):
                return 0

            # Naked Single 
