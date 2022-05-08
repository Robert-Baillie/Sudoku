#include <iostream>
#include "Board.cpp"

using namespace std;



int main(){
    Board b = Board();
    






    /// Printing out the board values
    cout << "BOARD VALUES" << endl;
    cout << "--------------------------------------------" << endl;
    for (size_t i = 0; i < b.board.size(); i++)
    {
        vector<Cell> row = b.board[i];
        int size = row.size();

        for (size_t j = 0; j < size; j++)
        {
            cout << b.board[i][j].cell_number;
        
        }
        cout << endl;
    }

     /// Printing out the board values
    cout << "COLUMN VALUES" << endl;
    cout << "--------------------------------------------" << endl;
    for (size_t i = 0; i < b.board.size(); i++)
    {
        vector<Cell> row = b.board[i];
        int size = row.size();

        for (size_t j = 0; j < size; j++)
        {
            cout << b.board[i][j].column_number;
        
        }
        cout << endl;
    }

     /// Printing out the board values
    cout << "Row VALUES" << endl;
    cout << "--------------------------------------------" << endl;
    for (size_t i = 0; i < b.board.size(); i++)
    {
        vector<Cell> row = b.board[i];
        int size = row.size();

        for (size_t j = 0; j < size; j++)
        {
            cout << b.board[i][j].row_number;
        
        }
        cout << endl;
    }

     /// Printing out the board values
    cout << "BOX VALUES" << endl;
    cout << "--------------------------------------------" << endl;
    for (size_t i = 0; i < b.board.size(); i++)
    {
        vector<Cell> row = b.board[i];
        int size = row.size();

        for (size_t j = 0; j < size; j++)
        {
            cout << b.board[i][j].box_number;
            cout<< ".";
        
        }
        cout << endl;
    }

    // End
    return 0;
}