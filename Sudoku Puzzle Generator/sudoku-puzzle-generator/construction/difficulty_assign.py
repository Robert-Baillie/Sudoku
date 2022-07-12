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
                return DifficultyAssign.assign_difficulty(0, loop, board)
                    
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
                return DifficultyAssign.assign_difficulty(1, loop, board)

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
                return DifficultyAssign.assign_difficulty(2, loop, board)


            """ 
            POINTING CHECKS
            """
            pointing_solver.pointing_solver(board, candidates)

            # All checks need to then be tested with a naked single to fill out candidates
            DifficultyAssign.single_check_cleanup(board,candidates)
            

            # We have done single checks - if it is the first loop set the difficulty
            if(board.empty_slot_count() == 0):  
                return DifficultyAssign.assign_difficulty(3, loop, board)



        if(board.empty_slot_count() != 0):
            return 5




    @staticmethod
    def single_check_cleanup(board,candidates):
        change_made = True
            
        while(change_made):
            change_made = False
            for j in range(81):
                check = naked_single.naked_single(board,candidates,j)
                if(check):
                    change_made = True

    @staticmethod
    def assign_difficulty(stage, loop, board):
        # Could probably do a switch statement

        # Stage 0 - singles. For the first loop assign Easy difficulty, if second assign medium, anymore assign hard
        if(stage == 0):
            if(loop == 0):
                if board.puzzle_zero_count < 35:
                    return 1
                else:
                    return 2
            elif loop == 1:
                return 3
            else:
                return 4

        # Stage 2 - pairs. if first loop assign as easy/medium depending on the zero count, anymore set as hard
        if(stage == 1):
            if(loop == 0):
                if board.puzzle_zero_count < 35:
                    return 2
                else:
                    return 3
            else:
                return 4
            
        if(stage ==2):
            if(loop == 0):
                if board.puzzle_zero_count < 35:
                    return 2
                else:
                    return 3
            else:
                return 4

        if(stage == 3):
            if(loop == 0):
                return 3
            else:
                return 4