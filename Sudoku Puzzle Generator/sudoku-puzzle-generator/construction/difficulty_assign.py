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

#Difficulties 
# 0 = null
# 1 = Beginner

# 2 = Easy
# 3 = Medium
# 4 = Hard
# 5 = Impossible
class DifficultyAssign:

    @staticmethod
    def assign_board_difficulty(board, candidates):
        score = 0

        # We will loop five times - as we have not implemented super advanced techniuqes any puzzle that cannot be solved in five loops will count as extreme (or maybe impossible...)
        for loop in range(5):

           
            """ 
            SINGLE CHECKS
            """
            change_made = True

            while(change_made):
                change_made = False
                
                for j in range(81):
                    check = hidden_single.hidden_singles(board, candidates, j)
                    if(check):
                        board.score += 100
                        change_made = True

            
            # Have a history of the board breaking - this is due to bad code, mixing different types of arrays, so if it errors assign a difficulty of 0 which will count as null
           
            if(helpers.candidate_board_error(candidates)):
                helpers.print_candidate_board(candidates)
                print("\n\n This happened at loop: ", loop, "\n\n")
                return 0

            # Naked Single - loop as before
            DifficultyAssign.single_check_cleanup(board,candidates)

            # We have done single checks - if it is the first loop set the difficulty
            if(board.empty_slot_count() == 0):  
                return board.score
                    
            """ 
            PAIR CHECKS
            """

            # Hidden Pair Checks
            hidden_pair.hidden_pair(board,candidates)

            # Naked Pair Checks
            naked_pair.naked_pair(board, candidates)

            # All  checks need to then be tested with a naked single to fill out candidates

            DifficultyAssign.single_check_cleanup(board,candidates)

            # We have done single checks - if it is the first loop set the difficulty
            if(board.empty_slot_count() == 0):  
                return board.score

            """ 
            TRIPLE CHECKS
            """
            # Hidden Triple
            hidden_triple.hidden_triple(board, candidates)

            # Hidden Triple
            naked_triple.naked_triple(board, candidates)

            # All   checks need to then be tested with a naked single to fill out candidates
            DifficultyAssign.single_check_cleanup(board,candidates)

            # We have done single checks - if it is the first loop set the difficulty
            if(board.empty_slot_count() == 0):  
                return board.score


            """ 
            POINTING CHECKS
            """
            pointing_solver.pointing_solver(board, candidates)

            # All checks need to then be tested with a naked single to fill out candidates
            DifficultyAssign.single_check_cleanup(board,candidates)
            

            # We have done single checks - if it is the first loop set the difficulty
            if(board.empty_slot_count() == 0):  
                return board.score



        if(board.empty_slot_count() != 0):
            return 15000




    @staticmethod
    def single_check_cleanup(board,candidates):
        change_made = True
            
        while(change_made):
            change_made = False
            for j in range(81):
                check = naked_single.naked_single(board,candidates,j)
                if(check):
                    board.score += 100
                    change_made = True

   

   