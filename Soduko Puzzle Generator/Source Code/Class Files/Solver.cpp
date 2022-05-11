#include "Solver.h"


int Solver::GetSolutionCountOfBoard(Board& bo) {
    int solution_count = 0;
    SolveBoardUnique(bo, solution_count);
    return solution_count;
}

bool Solver::SolveBoardUnique(Board& bo, int& solution_count) {
    int row;
    int col;
    // Step 1 (Base case)- Find an empty spot. If we do not find one, then the board is complete!
    // Store the found in a vector - 0 = i, 1 = j;
    vector<int> find = bo.FindEmpty(bo.board);

    if (find.size() != 2) {
        /// We have a solution
        solution_count++;
        // Stop if we get to 10
        // if(solution_count == 10) return true;

        // Remove the alst number - start loop from penultamite
        row = 8;
        col = 7;

        int last_num = bo.board[row][col];
        for (size_t num = last_num + 1; num < 10; num++)
        {

            if (bo.CheckValidNumber(num, row, col)) {
                bo.board[row][col] = num;


                if (SolveBoardUnique(bo, solution_count)) return true;


                bo.board[row][col] = 0;
            }
            return false;


        }

    }
    // Step 2 - Assign Row and col
    else {
        row = find[0];
        col = find[1];
    }

    // Step 3 - Loop through the values of 1 - 9
    for (size_t num = 1; num < 10; num++)
    {
        // Step 4 - If valid then add it into the board
        if (bo.CheckValidNumber(num, row, col)) {
            bo.board[row][col] = num;

            // Step 5 - If we can solve this new board - return true
            if (SolveBoardUnique(bo, solution_count)) return true;

            // Step 6 - otherwise return
            bo.board[row][col] = 0;
        }


    }
    return false;

}
