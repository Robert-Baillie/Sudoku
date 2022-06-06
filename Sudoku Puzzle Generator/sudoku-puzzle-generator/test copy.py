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

  for i in range(100000):

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
      print("\n\n--------------------------------------------------------------------------------\nStep 1 : Hidden Single Checks\n\n")

      print("\nThe candidate Board before hidden single checks: \n")
      helpers.print_candidate_board(candidates)


      change_made = True
      # Hidden
      while(change_made):
        change_made = False
        for j in range(81):
          check = hidden_single.hidden_singles(b, candidates, j)
          if(check):
            change_made = True

      print("\nThe candidate Board after hidden single checks: \n")
      helpers.print_candidate_board(candidates)
            
      print("\nThe  Board after hidden single checks: \n")
      b.print_board()
      
      if(helpers.candidate_board_error(candidates)):
        raise Exception("The candidate board is broken.")

      print("\n\n--------------------------------------------------------------------------------\nStep 2 : Naked Single Checks\n\n")
      change_made = True
      # Single
      while(change_made):
        change_made = False
        for j in range(81):
          check = naked_single.naked_single(b,candidates,j)
          if(check):
            change_made = True


      print("\nThe candidate Board after naked single checks: \n")
      helpers.print_candidate_board(candidates)
            
      print("\nThe  Board after naked single checks: \n")
      b.print_board()


      if(b.empty_slot_count() == 0):
        print("\nThe Board has been completed, breaking the loop. Stage: Single Checks, Loop: ", loop)
        break
        

      # Hidden Pair Checks
      print("\n\n--------------------------------------------------------------------------------\nStep 3 : Hidden Pair Checks\n\n")

      hidden_pair.hidden_pair(b,candidates)

      print("\nThe candidate Board after hidden pair checks: \n")
      helpers.print_candidate_board(candidates)
            
      print("\nThe  Board after hidden pair checkss: \n")
      b.print_board()

      # Naked Pair Checks
      print("\n\n--------------------------------------------------------------------------------\nStep 4 : Naked Pair Checks\n\n")

      naked_pair.naked_pair(b, candidates)

      print("\nThe candidate Board after naked pair checks: \n")
      helpers.print_candidate_board(candidates)
            
      print("\nThe  Board after naked pair checks: \n")
      b.print_board()

    #   # All Naked pair checks need to then be tested with a naked single to fill out candidates

      change_made = True
      # Single
      while(change_made):
        change_made = False
        for j in range(81):
          check = naked_single.naked_single(b,candidates,j)
          if(check):
            change_made = True

      print("\nThe candidate Board after naked pair checks - single fillout: \n")
      helpers.print_candidate_board(candidates)
            
      print("\nThe  Board after naked pair checks - single fillout:: \n")
      b.print_board()

      if(b.empty_slot_count() == 0):
        print("\nThe Board has been completed, breaking the loop. Stage: Pair Checks, Loop: ", loop)
        break

      
      print("\n\n--------------------------------------------------------------------------------\nStep 5 : Hidden Triple Checks\n\n")

      hidden_triple.hidden_triple(b, candidates)

      print("\nThe candidate Board after hidden triple checks: \n")
      helpers.print_candidate_board(candidates)
                
      print("\nThe  Board after hidden triple checks: \n")
      b.print_board()

      print("\n\n--------------------------------------------------------------------------------\nStep 6 : Naked Triple Checks\n\n")

      naked_triple.naked_triple(b, candidates)

      print("\nThe candidate Board after hidden triple checks: \n")
      helpers.print_candidate_board(candidates)
                
      print("\nThe  Board after hidden triple checks: \n")
      b.print_board()

     # All Naked pair checks need to then be tested with a naked single to fill out candidates

      change_made = True
      # Single
      while(change_made):
        change_made = False
        for j in range(81):
          check = naked_single.naked_single(b,candidates,j)
          if(check):
            change_made = True

      print("\nThe candidate Board after naked pair checks - single fillout: \n")
      helpers.print_candidate_board(candidates)
            
      print("\nThe  Board after naked pair checks - single fillout:: \n")
      b.print_board()

      if(b.empty_slot_count() == 0):
        print("\nThe Board has been completed, breaking the loop. Stage: Triple Checks, Loop: ", loop)
        break

      

      print("\n\n--------------------------------------------------------------------------------\nStep 7 : Pointing Checks\n\n")

      pointing_solver.pointing_solver(b, candidates)

      print("\nThe candidate Board after pointing checks: \n")
      helpers.print_candidate_board(candidates)
                
      print("\nThe  Board after pointing checks: \n")
      b.print_board()
      
      # All Naked pair checks need to then be tested with a naked single to fill out candidates

      change_made = True
      
      while(change_made):
        change_made = False
        for j in range(81):
          check = naked_single.naked_single(b,candidates,j)
          if(check):
            change_made = True

      print("\nThe candidate Board after Pointing Checks - single fillout: \n")
      helpers.print_candidate_board(candidates)
            
      print("\nThe  Board after Pointing Checks - single fillout:: \n")
      b.print_board()

      if(b.empty_slot_count() == 0):
        print("\nThe Board has been completed, breaking the loop. Stage: Pointing Checks, Loop: ", loop)
        break


    if(b.empty_slot_count() != 0):
      print("\nThe board could not be completed in 5 iterations.")
   
    
  

  
