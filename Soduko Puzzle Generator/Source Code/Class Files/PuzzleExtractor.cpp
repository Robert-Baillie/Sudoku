#include "PuzzleExtractor.h"


vector<int> PuzzleExtractor::InitialiseIndexList() {
	vector<int> vec;

	for (size_t i = 0; i < 81; i++)
	{
		vec.push_back(i);
	}

	return vec;
}
void PuzzleExtractor::RemoveNumbersUntilNonUniqueness(Board& bo) {
	/// Reset List
	vector<int> slots_remaining = InitialiseIndexList();
	vector<vector<int>> board;
	board = bo.board;


	// Remove a slot whilst the solution count is 1	
	while (Solver::GetSolutionCountOfBoard(bo) == 1) {
		board = bo.board;
		/// Get slot and remove it
		
		int rnd_ind = rand() % slots_remaining.size();
		RemoveNumber(bo, rnd_ind, slots_remaining);

	}
	// Last Remove Number will give multiple solutions, so set to the one defined at the start of the loop
	bo.board = board;

}

void PuzzleExtractor::RemoveNumber(Board& bo, int indx, vector<int>& slots_remaining) {
	int slot_to_remove = slots_remaining[indx];

	/// Get the row and column of index - index and index entry are identical
	int row = slot_to_remove / 9;
	int col = slot_to_remove % 9;


	// cout << "The slot to remove is: " << slot_to_remove << " this corresponds to row " << row << " and col " << col << endl;

	bo.board[row][col] = 0;

	slots_remaining.erase(remove(slots_remaining.begin(), slots_remaining.end(), slot_to_remove), slots_remaining.end());
}