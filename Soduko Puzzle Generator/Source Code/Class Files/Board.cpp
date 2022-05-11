#include "Board.h"  
#include <iostream>

Board::Board()
{
    /// Initialise Board 
    InitialiseBoard(board);


    /// Fill
    FillBoard(board);

}

Board::~Board()
{
}


/* Fill In Boxes down the diagonals */
void Board::InitialiseBoard(vector<vector<int>>& board) {
    /// Boxes 0, 3, 6
    for (size_t i = 0; i < 9; i += 3)
    {
        FillInBox(i, board);
    }


}

/* Using the box number passed - find the squares to populate */
void Board::FillInBox(int box_int, vector<vector<int>>& board) {
    // Create a temporary vector that will be used to populate data
    vector<int> one_to_nine_tmp = { 1,2,3,4,5,6,7,8,9 };

    for (size_t row = 0; row < 3; row++)
    {
        for (size_t col = 0; col < 3; col++)
        {
            int num = GetRandomIntFromVector(one_to_nine_tmp);
            board[row + box_int][col + box_int] = num;
            one_to_nine_tmp.erase(remove(one_to_nine_tmp.begin(), one_to_nine_tmp.end(), num), one_to_nine_tmp.end());

        }

    }


}

/* Validation Methods*/

// Check if number is valid in the row, column and the box, any that return false makes whole loop false
bool Board::CheckValidNumber(int num, int row_ind, int col_ind) {
    return (CheckValidRow(num, row_ind, col_ind)
        && CheckValidColumn(num, row_ind, col_ind)
        && CheckValidBox(num, row_ind, col_ind));
}


/// Row
bool Board::CheckValidRow(int num, int row_ind, int col_ind) {
    int size = 9;   /// Hard coded for now - could change to SQRT board

    // Loop through the row
    for (size_t i = 0; i < size; i++)
    {
        // If the column we are on is equal to the number (and it isnt the column we passed) then it is not valid
        if (board[row_ind][i] == num && i != col_ind) return false;

    }

    // Passed so valid
    return true;
}

// Column
bool Board::CheckValidColumn(int num, int row_ind, int col_ind) {
    int size = 9;   /// Hard coded for now - could change to SQRT board

    // Loop through the column
    for (size_t i = 0; i < size; i++)
    {
        // If the row we are on is equal to the number (and it isnt the column we passed) then it is not valid
        if (board[i][col_ind] == num && i != row_ind) return false;

    }

    // Passed so valid
    return true;
}

// Box
bool Board::CheckValidBox(int num, int row_ind, int col_ind) {
    /// Using interger division - return 0, 1 ,2
    /// This gives us the starting x and y of the box
    // x and y as in normal cartesian
    int x = col_ind / 3;
    int y = row_ind / 3;

    // Multiply by 3 to get the end of box
    int x_adj = x * 3;
    int y_adj = y * 3;

    for (size_t i = y_adj; i < y_adj + 3; i++)
    {
        for (size_t j = x_adj; j < x_adj + 3; j++)
        {
            // cout << "Now Checking Row: " << i << " and Column " << j << endl;
            if (board[i][j] == num && (i != row_ind && j != col_ind)) {
                // cout << num << " is not valid for: " << i << " " << j << endl;

                return false;
            }
        }

    }

    return true;
}

/* Board Solivng Methods */
bool Board::FillBoard(vector<vector<int>>& board) {
    int row;
    int col;

    // Step 1 (Base case)- Find an empty spot. If we do not find one, then the board is complete!
    // Store the found in a vector - 0 = i, 1 = j;
    vector<int> find = FindEmpty(board);

    if (find.size() != 2) return true;
    // Step 2 - Assign Row and col
    else {
        row = find[0];
        col = find[1];
    }

    // Step 3 - Loop through the values of 1 - 9
    for (size_t num = 1; num < 10; num++)
    {
        // Step 4 - If valid then add it into the board
        if (CheckValidNumber(num, row, col)) {
            board[row][col] = num;

            // Step 5 - If we can solve this new board - return true
            if (FillBoard(board)) return true;

            // Step 6 - otherwise return
            board[row][col] = 0;
        }


    }
    return false;
}


vector<int> Board::FindEmpty(vector<vector<int>>& board) {
    vector<int> vec = {};
    int size = 9;

    for (size_t i = 0; i < size; i++)
    {
        for (size_t j = 0; j < size; j++)
        {
            if (board[i][j] == 0) {
                vec.push_back(i);
                vec.push_back(j);
                return vec;
            }
        }

    }


    return vec;
}




/* Helper Methods*/

/* Utility Method to Print the board */
void Board::PrintBoard() {

    for (size_t i = 0; i < board.size(); i++)
    {
        vector<int> row = board[i];
        int size = row.size();


        // Print row bars
        if (i % 3 == 0 && i != 0) cout << "------------" << endl;


        for (size_t j = 0; j < size; j++)
        {
            if (j % 3 == 0 && j != 0) cout << "|";
            cout << board[i][j];

        }
        cout << endl;
    }
    cout << endl;
}


/* Utility Function as named*/
int Board::GetRandomIntFromVector(vector<int>& vec) {
    // Generate Random Integer
    int rnd_ind = rand() % vec.size();
    int num = vec[rnd_ind];

    // Return
    return num;
}