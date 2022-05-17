#pragma once

#include <vector>
#include <string>

#ifndef MATCHCOUNTTABLE_H
#define MATCHCOUNTTABLE_H

using namespace std;

class MatchCountTable
{
public:
    vector<vector<int>> values;
    vector<int> count;

    void AddCount(vector<int> value);

    int GetCount(vector<int> value);
};
#endif
