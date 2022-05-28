
import numpy as np
import tests
# Buidling Board
from tests import build_candidate_board_test

# Hidden Tests
from tests import hidden_single_test

# Naked Tests
from tests import naked_pair_test

# Pointing Tests 

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

  # To Confirm working
  # Naked
  # naked_pair_test.naked_pair_test_row()
  # naked_pair_test.naked_pair_test_col()
  naked_pair_test.naked_pair_test_box()

  
