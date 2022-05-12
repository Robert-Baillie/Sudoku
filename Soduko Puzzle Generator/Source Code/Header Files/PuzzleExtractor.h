#pragma once

#include <vector>
#include <iostream>
#include <algorithm>

#include "Solver.h"
#include "Board.h" 

#ifndef PUZZLEEXTRACTOR_H
#define PUZZLEEXTRACTOR_H

using namespace std;

class PuzzleExtractor
{
public: 
    static void RemoveNumbersUntilNonUniqueness(Board& bo);
    static void RemoveNumber(Board& bo, int slot_to_remove, vector<int>& slots_remaining);

private:
     vector<int> slots_remaining = {};

    static vector<int> InitialiseIndexList();
};

#endif
