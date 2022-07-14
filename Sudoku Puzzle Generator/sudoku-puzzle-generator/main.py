from tkinter import W
import numpy as np
from board.board import Board
from construction.number_extractor import Extractor
from construction.uniqueness_solver import UniqueSolver
from construction.difficulty_assign import DifficultyAssign



from logic import helpers


if __name__ == '__main__':

    beginnner_puzzles = []
    easy_puzzles = []
    med_puzzles = []
    hard_puzzles = []
    impossible_puzzles = []

    for i in range(100000):
        

        # Step One - Build a board
        board = Board()
        board.initialise_board()
        board.fill_board()
        
        board.complete_board = board.board.copy()
            
        #Step Two - Extract until non uniqueness
        Extractor.remove_numbers_until_non_uniqueness(board)

        #Half step - if empty count is less than 25 then do nothing - puzzle quality is not adequet
        if(board.empty_slot_count() > 25):


            # Only reaches here when true so assign puzzle board
            board.puzzle_board = board.board.copy()   
            board.puzzle_zero_count = board.empty_slot_count()

            #Step Three - Build Candidate boards
            candidates = helpers.build_candidate_board(board)
           
           
            #Step Four - Build Strings
            board.puzzle_string = helpers.assign_board_string(board.puzzle_board, board.complete_board)

            #Step Five Add the Difficulty onto the strong
            tmp = DifficultyAssign.assign_board_difficulty(board, candidates)


            if tmp <= 4000:
                #board.puzzle_string += str(1)
                beginnner_puzzles.append(board.puzzle_string)
            elif tmp <= 5000:
                #board.puzzle_string += str(2)
                easy_puzzles.append(board.puzzle_string)
            elif tmp <= 6000:
                #board.puzzle_string += str(3)
                med_puzzles.append(board.puzzle_string)
            elif tmp < 15000:
                #board.puzzle_string += str(4)
                hard_puzzles.append(board.puzzle_string)
            else:
                #board.puzzle_string += str(5)
                impossible_puzzles.append(board.puzzle_string)

        
        print("Generated Puzzle ", i + 1)
        if i % 100 == 0 and i != 0:
            
            # Beginner
            if(len(beginnner_puzzles) > 0):
                f = open("begi.txt", "a")
                f.write("\n")
                f.write("\n".join(beginnner_puzzles))
                f.close()
                beginnner_puzzles = []

            # Easy
            if(len(easy_puzzles) > 0):
                f = open("easy.txt", "a")
                f.write("\n")
                f.write("\n".join(easy_puzzles))
                f.close()
                easy_puzzles = []

            # Medium
            if(len(med_puzzles) > 0):
                f = open("med.txt", "a")
                f.write("\n")
                f.write("\n".join(med_puzzles))
                f.close()
                med_puzzles = []

            # Hard
            if(len(hard_puzzles) > 0):
                f = open("hard.txt", "a")
                f.write("\n")
                f.write("\n".join(hard_puzzles))
                f.close()
                hard_puzzles = []

            # Impossible
            if(len(impossible_puzzles) > 0):
                f = open("impo.txt", "a")
                f.write("\n")
                f.write("\n".join(impossible_puzzles))
                f.close()
                impossible_puzzles = []


            
            

    

    