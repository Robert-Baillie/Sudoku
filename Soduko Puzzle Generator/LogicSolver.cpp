#include "LogicSolver.h"
#include "MatchCountTable.h"

int LogicSolver::SolveBoard(Board& bo) {
    /// Difficulty point count at end
    int difficulty_score = 0;
        
	/// Initialise an array of potential solutions for each cell
	vector<vector<int>> possible_solutions = InitialisePossibleSolutions();

    /// Set initial values for the grid - print out the possible solutions
    SetInitialValues(bo, possible_solutions);


    // Print board
    


    // Loop through - could do all in an individual loop - looping three times gives a better score accuracy
    

    for (size_t iteration = 0; iteration < 3; iteration++)
    {
        if (bo.EmptySlotCount() == 0) break;

        /// Single Cell Solving
        for (size_t i = 0; i < possible_solutions.size(); i++)
        {
            // Only change solve for unsolved numbers - can be solved after each so check each time
            if (bo.board[i / 9][i % 9] == 0) RowSolver(bo, possible_solutions, difficulty_score, i);
            if (bo.board[i / 9][i % 9] == 0)  ColSolver(bo, possible_solutions, difficulty_score, i);
            if (bo.board[i / 9][i % 9] == 0)  BoxSolver(bo, possible_solutions, difficulty_score, i);
        }



        /// Match Solving

        // Loop over rows
        for (size_t i = 0; i < 81; i += 9)
        {
            RowMatchSolver(bo, possible_solutions, difficulty_score, i);

        }

        // Loop over columns
        for (size_t i = 0; i < 9; i++)
        {
            ColMatchSolver(bo, possible_solutions, difficulty_score, i);

        }

        // Loop over boxes
        for (size_t i = 0; i < 81; i += 27)
        {
            for (size_t j = 0; j < 9; j += 3)
            {
                BoxMatchSolver(bo, possible_solutions, difficulty_score, i + j);
            }

        }
    }
   
   
    
    if (bo.EmptySlotCount() != 0) cout << "We do not have the technique to solve this puzzle (or this puzzle is not valid) in three iterations! " << endl;

    return difficulty_score;
}


void LogicSolver::SetInitialValues(Board& bo, vector<vector<int>>& possible_solutions) {
    // Loop through the board
    /// Rows
    for (size_t i = 0; i < bo.board.size(); i++)
    {
        /// Columns
        for (size_t j = 0; j < bo.board[i].size(); j++)
        {
            /// Get the index for the possible solution
            int indx = 9 * i + j;

            // Test on board number
            int num = bo.board[i][j];

            if (num != 0) {
                possible_solutions[indx] = { num };

                RemoveFromPossibleSolutions(bo, possible_solutions, indx, i, j, num);
                
            }
        }

    }
}

vector<vector<int>> LogicSolver::InitialisePossibleSolutions()
{
    vector<int> one_to_nine = { 1,2,3,4,5,6,7,8,9 };
    vector<vector<int>> possible_solutions = {};

    for (size_t i = 0; i < 81; i++)
    {
        possible_solutions.push_back(one_to_nine);
    }

    return possible_solutions;
}


/// Logic Solvers

// Single Cell

void LogicSolver::RowSolver(Board& bo, vector<vector<int>>& possible_solutions, int& points, int indx)
{
    vector<int> available = possible_solutions[indx];

    if (available.size() == 1) {
        SetAvailable(bo, possible_solutions, indx, available, points);
        return;
    }

    int row_start = (indx / 9) * 9;
    int row_end = row_start + 9;

    for (size_t i = row_start; i < row_end; i++)
    {
        // Dont check this index
        if (i != indx) {
            // Loop over current index in row
            for (size_t j = 0; j < possible_solutions[i].size(); j++)
            {
                /// If the current number we are looping is in the available list
                int num = possible_solutions[i][j];
                if (find(available.begin(), available.end(), num) != available.end()){
                    available.erase(remove(available.begin(), available.end(), num), available.end());
                    
                }
            }
        }
    }

    if (available.size() == 1) {
        SetAvailable(bo, possible_solutions, indx, available, points);
        return;
    }
 

}

void LogicSolver::ColSolver(Board& bo, vector<vector<int>>& possible_solutions, int& points, int indx)
{
    vector<int> available = possible_solutions[indx];

    if (available.size() == 1) {
        SetAvailable(bo, possible_solutions, indx, available, points);
        return;
    }

    int col_start = indx % 9;

    for (size_t i = col_start; i < 81; i+=9)
    {
        // Dont check this index
        if (i != indx) {
            // Loop over current index in row
            for (size_t j = 0; j < possible_solutions[i].size(); j++)
            {
                /// If the current number we are looping is in the available list
                int num = possible_solutions[i][j];
                if (find(available.begin(), available.end(), num) != available.end()) {
                    available.erase(remove(available.begin(), available.end(), num), available.end());

                }
            }
        }
    }

    if (available.size() == 1) {
        SetAvailable(bo, possible_solutions, indx, available, points);
        return ;
    }

    

}

void LogicSolver::BoxSolver(Board& bo, vector<vector<int>>& possible_solutions, int& points, int indx)
{

    vector<int> available = possible_solutions[indx];

    if (available.size() == 1) {
        SetAvailable(bo, possible_solutions, indx, available, points);
        return;
    }

    int box_row_start = (indx / 9) /3 * 3;
    int col_box_start = (indx % 9) / 3 * 3;
    int start = box_row_start * 9 + col_box_start;

    for (size_t i = start; i < (start+3); i++)
    {
        for (size_t k = i; k < (i+19); k+=9)
        {
            // Dont check this index
            if (k != indx) {
                // Loop over current index in row
                for (size_t j = 0; j < possible_solutions[k].size(); j++)
                {
                    /// If the current number we are looping is in the available list
                    int num = possible_solutions[k][j];
                    if (find(available.begin(), available.end(), num) != available.end()) {
                        available.erase(remove(available.begin(), available.end(), num), available.end());

                    }
                }
            }
        }
        
       
    }

    if (available.size() == 1) {
        SetAvailable(bo, possible_solutions, indx, available, points);
        return;
    }

}

// Match Cell
void LogicSolver::RowMatchSolver(Board& bo, vector<vector<int>>& possible_solutions, int& points, int indx) {
    MatchCountTable count_table;

    vector<int> nums_to_remove;

    /// Given i - starting index of a row - loop through the row ( + 1)
    for (size_t i = indx; i < 9; i++)
    {
        // If there is a solution - do not add to the count table
        if (possible_solutions[i].size() != 1) count_table.AddCount(possible_solutions[i]);

    }

    // Loop through the count table - if the size is the same as the count then it must be in there - so remove those numbers from the rest of the row.
    for (size_t i = 0; i < count_table.values.size(); i++)
    {
        if (count_table.values[i].size() == count_table.count[i]) {
            nums_to_remove = count_table.values[i];
        }
    }

     
    /// Loop through row and remvoe
    for (size_t i = indx; i < 9; i++)
    {
        // If there is a solution - do not add to the count table
        if (possible_solutions[i] != nums_to_remove && nums_to_remove.size() != 0 && possible_solutions[i].size() != 1) {

            
             
            for (size_t j= 0; j < nums_to_remove.size(); j++)
            {
                int size = possible_solutions[i].size();

                /// below does not necessarily erase a number - if it does then we can add points :)
                possible_solutions[i].erase(remove(possible_solutions[i].begin(), possible_solutions[i].end(), nums_to_remove[j]), possible_solutions[i].end());

                if (size != possible_solutions[i].size()) points += 250;
                if (possible_solutions[i].size() == 1) {
                    int row = i / 9;
                    int col = i % 9;

                    bo.board[row][col] = possible_solutions[i][0];
                    points += 50;
                    RemoveFromPossibleSolutions(bo, possible_solutions, i, row, col, possible_solutions[i][0]);
                    
                }
            }
            

        }

    }
}

void LogicSolver::ColMatchSolver(Board& bo, vector<vector<int>>& possible_solutions, int& points, int indx) {
    MatchCountTable count_table;

    vector<int> nums_to_remove;

    /// Given i - starting index of a column - loop through the row ( + 1)
    for (size_t i = indx; i < 81; i+=9)
    {
        // If there is a solution - do not add to the count table
        if (possible_solutions[i].size() != 1) count_table.AddCount(possible_solutions[i]);

    }

    // Loop through the count table - if the size is the same as the count then it must be in there - so remove those numbers from the rest of the row.
    for (size_t i = 0; i < count_table.values.size(); i++)
    {
        if (count_table.values[i].size() == count_table.count[i]) {
            nums_to_remove = count_table.values[i];
        }
    }

   
    /// Loop through column and remvoe
    for (size_t i = indx; i < 81; i+=9)
    {
        // If there is a solution - do not add to the count table
        if (possible_solutions[i] != nums_to_remove && nums_to_remove.size() != 0 && possible_solutions[i].size() != 1) {
            int size = possible_solutions[i].size();

            for (size_t j = 0; j < nums_to_remove.size(); j++)
            {

                /// below does not necessarily erase a number - if it does then we can add points :)
                possible_solutions[i].erase(remove(possible_solutions[i].begin(), possible_solutions[i].end(), nums_to_remove[j]), possible_solutions[i].end());

                if (possible_solutions[i].size() == 1) {
                    int row = i / 9;
                    int col = i % 9;

                    bo.board[row][col] = possible_solutions[i][0];
                    points += 50;
                    RemoveFromPossibleSolutions(bo, possible_solutions, i, row, col, possible_solutions[i][0]);

                }
            }
            if (size != possible_solutions[i].size()) points += 250;


        }

    }



    
}

void LogicSolver::BoxMatchSolver(Board& bo, vector<vector<int>>& possible_solutions, int& points, int indx) {

    MatchCountTable count_table;

    vector<int> nums_to_remove;

    /// Given i - starting index of a box (tl) 
    for (size_t i = indx; i < (indx + 3); i++)
    {
        for (size_t k = i; k < (i + 19); k += 9)
        {
            // If there is a solution - do not add to the count table
            if (possible_solutions[k].size() != 1) count_table.AddCount(possible_solutions[k]);
        }
    }

    // Loop through the count table - if the size is the same as the count then it must be in there - so remove those numbers from the rest of the row.
    for (size_t i = 0; i < count_table.values.size(); i++)
    {
        if (count_table.values[i].size() == count_table.count[i]) {
            nums_to_remove = count_table.values[i];
        }
    }


    /// Loop through box and remvoe
    for (size_t i = indx; i < (indx + 3); i++)
    {
        for (size_t k = i; k < (i + 19); k += 9)
        {

            // If there is a solution - do not add to the count table
            if (possible_solutions[k] != nums_to_remove && nums_to_remove.size() != 0 && possible_solutions[k].size() != 1) {
                int size = possible_solutions[k].size();

                for (size_t j = 0; j < nums_to_remove.size(); j++)
                {

                    /// below does not necessarily erase a number - if it does then we can add points :)
                    possible_solutions[k].erase(remove(possible_solutions[k].begin(), possible_solutions[k].end(), nums_to_remove[j]), possible_solutions[k].end());

                    if (possible_solutions[k].size() == 1) {
                        int row = k / 9;
                        int col = k % 9;

                        bo.board[row][col] = possible_solutions[k][0];
                        points += 50;
                        RemoveFromPossibleSolutions(bo, possible_solutions, k, row, col, possible_solutions[k][0]);

                    }
                }
                if (size != possible_solutions[k].size()) points += 250;


            }
        }
    }

    



   
}


/// Utility

void LogicSolver::PrintSolutionBoard(vector<vector<int>> possible_solutions) {
   
    for (size_t i = 0; i < possible_solutions.size(); i++)
    {
        if (i % 27 == 0 && i != 0) cout <<endl << "----------------------------------------------------" << endl;
        else if (i % 9 == 0 && i != 0) cout << endl;
        else if (i % 3 == 0 && i != 0) cout << "  |  ";
        else if (i!= 0) cout << "     ";

        for (size_t j = 0; j < possible_solutions[i].size(); j++)
        {
            cout << possible_solutions[i][j];
        } 
    }
}

void LogicSolver::RemoveFromPossibleSolutions(Board& bo, vector<vector<int>>& possible_solutions,int indx, int i, int j, int num) { /// i and j for row and col
    // Remove num from row
    for (size_t row_ind = 9 * i; row_ind < 9 * i + 9; row_ind++)
    {
        if (row_ind != indx) {
            possible_solutions[row_ind].erase(remove(possible_solutions[row_ind].begin(), possible_solutions[row_ind].end(), num), possible_solutions[row_ind].end());
        }
    }
    // Remove each solution from column
    for (size_t col_ind = j; col_ind < 81; col_ind += 9)
    {
        if (col_ind != indx) {
            possible_solutions[col_ind].erase(remove(possible_solutions[col_ind].begin(), possible_solutions[col_ind].end(), num), possible_solutions[col_ind].end());
        }
    }
    // Remove each solution from box
    int box_row_start = (i / 3) * 3;
    int box_col_start = (j / 3) * 3;
    int start = 9 * box_row_start + box_col_start;
    int end = start + 3;
    // cout << "The row col is " << i << " " << j << endl;
    // cout << "The box row start is: " << box_row_start << endl;
    // cout << "The box col start is: " << box_col_start << endl;
    // cout << "The current index is: " << indx << endl;
    // cout << "The start index is: " << start << endl;
    // cout << "The end index is: " << end << endl;
    // 
    // cout << "The first 3 indexes hit are " << start << ", " << start + 9  << " & " << start + 18  << endl;
    // cout << "The second 3 indexes hit are " << start+1 << ", " << start+10 << " & " << start + 19 << endl;
    // cout << "The last 3 indexes hit are " << start+2 << ", " << start + 11 << " & " << start + 20 << endl;

    for (size_t box_row = start; box_row < end; box_row++)
    {
        if (box_row != indx) possible_solutions[box_row].erase(remove(possible_solutions[box_row].begin(), possible_solutions[box_row].end(), num), possible_solutions[box_row].end());
        if (box_row + 9 != indx) possible_solutions[box_row + 9].erase(remove(possible_solutions[box_row + 9].begin(), possible_solutions[box_row + 9].end(), num), possible_solutions[box_row + 9].end());
        if (box_row + 18 != indx) possible_solutions[box_row + 18].erase(remove(possible_solutions[box_row + 18].begin(), possible_solutions[box_row + 18].end(), num), possible_solutions[box_row + 18].end());

    }
}

void LogicSolver::SetAvailable(Board& bo, vector<vector<int>>& possible_solutions, int indx, vector<int>& available, int& points) {
    int row = indx / 9;
    int col = indx % 9;

    bo.board[row][col] = available[0];
    possible_solutions[indx] = available;

    points += 100;
    RemoveFromPossibleSolutions(bo, possible_solutions, indx, row, col, available[0]);
 }

