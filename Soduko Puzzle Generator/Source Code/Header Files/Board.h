#pragma once
#include <algorithm>
#include <vector>

using namespace std;
#ifndef BOARD_H
#define BOARD_H

class Board
{
private:
    // Methods - Board Initialisation
    void InitialiseBoard(vector<vector<int>>& board);
    void FillInBox(int box_int, vector<vector<int>>& board);


    


    // Valid Spot Methods
    bool CheckValidRow(int num, int row_ind, int col_ind);
    bool CheckValidColumn(int num, int row_ind, int col_ind);
    bool CheckValidBox(int num, int row_ind, int col_ind);


    // Utility Functions
    int GetRandomIntFromVector(vector<int>& vec);



public:
    // Construct
    Board();
    ~Board();

    // Utility
    void PrintBoard();


    // Board
    vector<vector<int>> board = { {0,0,0,0,0,0,0,0,0}
                                ,{0,0,0,0,0,0,0,0,0}
                                ,{0,0,0,0,0,0,0,0,0}
                                ,{0,0,0,0,0,0,0,0,0}
                                ,{0,0,0,0,0,0,0,0,0}
                                ,{0,0,0,0,0,0,0,0,0}
                                ,{0,0,0,0,0,0,0,0,0}
                                ,{0,0,0,0,0,0,0,0,0}
                                ,{0,0,0,0,0,0,0,0,0} };


    // Solving Methods:
    bool FillBoard(vector<vector<int>>& board);

    // Helpers
    bool CheckValidNumber(int num, int row_ind, int col_ind);
    vector<int> FindEmpty(vector<vector<int>>& board);

};
#endif
