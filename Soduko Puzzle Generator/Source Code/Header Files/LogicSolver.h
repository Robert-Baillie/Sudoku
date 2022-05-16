#pragma once

#include <vector>
#include "Board.h" 

#ifndef LOGICSOLVER_H
#define LOGICSOLVER_H

using namespace std;

class LogicSolver
{
public:
    static int GetCellIndex(Board& bo, int num);
    static void SetInitialValues(Board& bo);

    static int SolveBoard(Board& bo);

};

#endif
