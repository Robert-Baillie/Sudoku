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
	while (UniqueSolver::GetSolutionCountOfBoard(bo) == 1) {
		board = bo.board;
		/// Get slot and remove it
		
		int rnd_ind = rand() % slots_remaining.size();
		int slot_to_remove = slots_remaining[rnd_ind];
		RemoveNumbers(bo, slot_to_remove, slots_remaining);

	}
	// Last Remove Number will give multiple solutions, so set to the one defined at the start of the loop
	bo.board = board;

}


/// Remove Opposite  Numbers
void PuzzleExtractor::RemoveNumbers(Board& bo, int slot_to_remove, vector<int>& slots_remaining) {
	
	/// Get the row and column of index - index and index entry are identical
	int row = slot_to_remove / 9;
	int col = slot_to_remove % 9;

	bo.board[row][col] = 0;

	int opposite_row = 8 - row;
	int opposite_col = 8 - col;

	bo.board[opposite_row][opposite_col] = 0;

	int opposite_slot_num = opposite_row * 9 + (opposite_col);

	
	slots_remaining.erase(remove(slots_remaining.begin(), slots_remaining.end(), slot_to_remove), slots_remaining.end());
	slots_remaining.erase(remove(slots_remaining.begin(), slots_remaining.end(), opposite_slot_num), slots_remaining.end());

}