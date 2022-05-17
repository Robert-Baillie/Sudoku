#include "MatchCountTable.h"


void MatchCountTable::AddCount(vector<int> value) {
    // If the vector already exists add a count else push back and add a count
    if (find(values.begin(), values.end(), value) != values.end()) {

        ptrdiff_t pos = distance(values.begin(), find(values.begin(), values.end(), value));

        count[pos]++;
    }
    else {
        // Havent found it - add to both lists
        values.push_back(value);
        count.push_back(1);
    }
}

int MatchCountTable::GetCount(vector<int> value  ) {
    ptrdiff_t pos = distance(values.begin(), find(values.begin(), values.end(), value));

    return count[pos];
}