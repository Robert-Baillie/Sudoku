import numpy as np
import logic.helpers as helpers

def naked_single(board, candidates, indx):
    row = int(indx / 9)
    col = int(indx % 9)

    if(len(candidates[indx]) == 1 and board.board[row][col] == 0):
        helpers.set_available(board, candidates, indx, candidates[indx])