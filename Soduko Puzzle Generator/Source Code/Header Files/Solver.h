#pragma once

#include <vector>
#include "Board.h" 

#ifndef SOLVER_H
#define SOLVER_H

using namespace std;

class Solver
{
public: /// Cannot create an instance
    static int GetSolutionCountOfBoard(Board& bo);
    static bool SolveBoardUnique(Board& bo, int& solution_count);
};

#endif
