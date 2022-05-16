#pragma once

#include <vector>
#include <iostream>
#include <algorithm>
#include "Board.h" 

#ifndef LOGICSOLVER_H
#define LOGICSOLVER_H

using namespace std;

class LogicSolver
{
public:
    // static int GetCellIndex(Board& bo, int num);
    
    //Start
    static void SetInitialValues(Board& bo, vector<vector<int>>& possible_solutions);
    static vector<vector<int>> InitialisePossibleSolutions();


    // Logic Solving Methods - https://medium.com/@eneko/solving-sudoku-puzzles-programmatically-with-logic-and-without-brute-force-b4e8b837d796
    static bool RowSolver(Board& bo, vector<vector<int>>& possible_solutions, int& points, int indx);
    static bool ColSolver(Board& bo, vector<vector<int>>& possible_solutions, int& points, int indx);
    static bool BoxSolver(Board& bo, vector<vector<int>>& possible_solutions, int& points, int indx);

    // Main method
    static int SolveBoard(Board& bo);


    // Utility
    static void PrintSolutionBoard(vector<vector<int>> possible_solutions);
    static void RemoveFromPossibleSolutions(Board& bo, vector<vector<int>>& possible_solutions, int indx, int row_ind, int col_ind, int num);
    static void SetAvailable(Board& bo, vector<vector<int>>& possible_solutions, int indx, vector<int>& available, int& points);
};

#endif

