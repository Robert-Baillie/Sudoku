import numpy as np
from board.board import Board
from construction.uniqueness_solver import UniqueSolver

class Extractor:
    slots_remaining = None

    @classmethod
    def remove_numbers_until_non_uniqueness(cls, bo):
        # Reset the remaining slots list
        slots_remaining = cls.initialise_index_list()
        
        board = bo.board

        slot_to_remove = np.random.choice(slots_remaining)
        # Forty (middle) causes an error which will return a null board on first selction - make sure we dont start with this
        while(slot_to_remove == 40):
            slot_to_remove = np.random.choice(slots_remaining)
        
        # Remove the first set of numbers before starting the loop
        cls.remove_numbers(bo, slot_to_remove)

        #Remove a slot whilst the uniqueness count of the board is 1 - do five attempts to create consistently better puzzles
        for attempt in range(5):

            while(UniqueSolver.get_solution_count(bo) == 1):
                board = bo.board.copy()
                
                # Get a slot from the board and remove it
                slot_to_remove = np.random.choice(slots_remaining)
                cls.remove_numbers(bo, slot_to_remove)
            
            bo.board = board
                
        bo.puzzle_board = board
        


    @classmethod
    def remove_numbers(cls, bo, slot_to_remove):
        
        # The slot to remove is an index on the board with a number active - get the row and column for it
        row = int(slot_to_remove) / 9
        col = int(slot_to_remove) % 9

        row = int(row)
        col = int(col)
        # get the opposite - want to remove two at a time - leads to better puzzles
        opp_row = 8 - row
        opp_col = 8 - col
        # Set both to zero
        bo.board[row, col] = 0
        bo.board[opp_row, opp_col] = 0

        # Remove the slot and the opposite slot from the slots remaining
        opp_slot = opp_row * 9 + opp_col    
        cls.slots_remaining = np.delete(cls.slots_remaining, np.where(cls.slots_remaining == slot_to_remove))
        cls.slots_remaining = np.delete(cls.slots_remaining, np.where(cls.slots_remaining == opp_slot))



    @staticmethod
    def initialise_index_list():
        return np.arange(0,81,1)