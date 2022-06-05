import numpy as np
from board.board import Board
from construction.number_extractor import Extractor
from construction.uniqueness_solver import UniqueSolver

from logic import hidden_pair
from logic import hidden_single
from logic import hidden_triple
from logic import naked_pair
from logic import naked_single
from logic import naked_triple
from logic import pointing_solver
from logic import helpers


# Buidling Board
from tests import build_candidate_board_test

# Hidden Tests
from tests import hidden_single_test
from tests import hidden_pair_test
from tests import hidden_triple_test


# Naked Tests
from tests import naked_pair_test
from tests import naked_triple_test

# Pointing Tests 
from tests import pointing_tests


if __name__ == '__main__':
  # The following are all working
  # Building
  # build_candidate_board_test.candidate_board_test()

  # Hidden
  # Single
  # hidden_single_test.hidden_single_row_test()
  # hidden_single_test.hidden_single_col_test()
  # hidden_single_test.hidden_single_box_test()


  # By visual inspection these tests pass
  # Naked
  # naked_pair_test.naked_pair_test_row()
  # naked_pair_test.naked_pair_test_col()
  # naked_pair_test.naked_pair_test_box()
  #  naked_triple_test.naked_triple_test_col()
  # naked_triple_test.naked_triple_test_row()
   # naked_triple_test.naked_triple_test_box()

  # Hidden
  #hidden_pair_test.hidden_pair_test_row()
  #hidden_pair_test.hidden_pair_test_col()
  #hidden_pair_test.hidden_pair_test_box()
  #hidden_triple_test.hidden_triple_test()
  # pointing_tests.pointing_pair_whole()
  #pointing_tests.pointing_triple_col()

  for i in range(10):

    b = Board()
    b.initialise_board()
    b.fill_board()

    print("\nThe full Board: \n")
    b.print_board()

    Extractor.remove_numbers_until_non_uniqueness(b)
    print("\nThe extracted Board: \n")
    
    b.print_board()
    print("\nThe board has: ", UniqueSolver.get_solution_count(b), " solutions!\n")
    print("\nThe board has: ", b.empty_slot_count(), " empty slots!\n")

    candidates = helpers.build_candidate_board(b)
    print("\nThe candidate Board: \n")
    helpers.print_candidate_board(candidates)

    for loop in range(5):

      
      # Single Checks
      for j in range(81):
          hidden_single.hidden_singles(b, candidates, j)
          naked_single.naked_single(b,candidates,j)

      print("\nThe candidate Board after single checks: \n")
      helpers.print_candidate_board(candidates)

      print("\nThe  Board after single checks: \n")
      b.print_board()

      if(b.empty_slot_count() == 0):
        print("\nThe Board has been completed, breaking the loop. Stage: Single Checks, Loop: ", loop)
        break
        

      # Naked Pair Check
      naked_pair.naked_pair(b, candidates)
      


      # Naked Single Check to fill in blanks
      for j in range(81):
          naked_single.naked_single(b,candidates,j)


      print("\nThe Board after naked pair checks")
      b.print_board()

      print("\nThe candidate Board after naked single checks: \n")
      helpers.print_candidate_board(candidates)

      # Hidden Pair Check
      hidden_pair.hidden_pair(b,candidates)

      
      # Naked Single Check to fill in blanks
      for j in range(81):
          naked_single.naked_single(b,candidates,j)

      print("\nThe Board after hidden pair checks")
      b.print_board()

      print("\nThe candidate Board after hidden pair: \n")
      helpers.print_candidate_board(candidates)

      
        
      if(b.empty_slot_count() == 0):
        print("\nThe Board has been completed, breaking the loop. Stage: Naked/Hidden Pair Checks, Loop: ", loop)
        break

    
    # Naked Triple Check
      naked_triple.naked_triple(b, candidates)

      # Naked Single Check to fill in blanks
      for j in range(81):
          naked_single.naked_single(b,candidates,j)

          
      print("\nThe Board after naked triple checks")
      b.print_board()

      print("\nThe candidate Board after naked triple checks: \n")
      helpers.print_candidate_board(candidates)

      # Hidden Triple Check
      hidden_triple.hidden_triple(b,candidates)


      # Naked Single Check to fill in blanks
      for j in range(81):
          naked_single.naked_single(b,candidates,j)

      print("\nThe Board after hidden Triple checks")
      b.print_board()

      print("\nThe candidate Board after hidden Triple: \n")
      helpers.print_candidate_board(candidates)

      


      if(b.empty_slot_count() == 0):
        print("\nThe Board has been completed, breaking the loop. Stage: Naked/Hidden Triple Checks, Loop: ", loop)
        break


    # Pointing Tests
      pointing_solver.pointing_solver(b,candidates)

      # Naked Single Check to fill in blanks
      for j in range(81):
          naked_single.naked_single(b,candidates,j)

      if(b.empty_slot_count() == 0):
        print("\nThe Board has been completed, breaking the loop. Stage: Pointing Checks, Loop: ", loop)
        break
    
  

  
