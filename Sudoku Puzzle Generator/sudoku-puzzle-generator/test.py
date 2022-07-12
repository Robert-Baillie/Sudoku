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
  build_candidate_board_test.candidate_board_test()

  # Hidden
  # Single
  hidden_single_test.hidden_single_row_test()
  hidden_single_test.hidden_single_col_test()
  hidden_single_test.hidden_single_box_test()


  # By visual inspection these tests pass
  # Naked
  naked_pair_test.naked_pair_test_row()
  naked_pair_test.naked_pair_test_col()
  naked_pair_test.naked_pair_test_box()
  naked_triple_test.naked_triple_test_col()
  naked_triple_test.naked_triple_test_row()
  naked_triple_test.naked_triple_test_box()

  # Hidden
  hidden_pair_test.hidden_pair_test_row()
  hidden_pair_test.hidden_pair_test_col()
  hidden_pair_test.hidden_pair_test_box()

  
  hidden_triple_test.hidden_triple_test()


  # Pointing
  pointing_tests.pointing_pair_whole()
  pointing_tests.pointing_triple_col()


    
  

  
