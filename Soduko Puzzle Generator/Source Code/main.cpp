#include "Board.h"
#include "UniqueSolver.h"
#include "PuzzleExtractor.h"
#include "LogicSolver.h"
#include "MatchCountTable.h"
#include <time.h>   
#include <iostream>

using namespace std;


int main() {

    srand(time(NULL));
  //  srand(1);


    for (size_t i = 0; i < 1000; i++)
    {


        Board b = Board();
        PuzzleExtractor::RemoveNumbersUntilNonUniqueness(b);
        cout << "Board: " << i + 1 << endl;
        cout << "The board has: " << UniqueSolver::GetSolutionCountOfBoard(b) << " solutions!" << endl;




         // b.board = { {1,0,0,0,0,4,0,8,0}
         //                 ,{0,4,0,0,0,0,0,1,0}
         //                 ,{8,0,6,2,0,0,0,0,0}
         //                 ,{0,0,0,5,2,0,7,0,0}
         //                 ,{0,0,7,0,4,0,2,0,0}
         //                 ,{0,0,1,0,9,3,0,0,0}
         //                 ,{0,0,0,0,0,2,5,0,3}
         //                 ,{0,8,0,0,0,0,0,6,0}
         //                 ,{0,9,0,3,0,0,0,0,4} };

        cout << endl << "The number of empty slots is: " << b.EmptySlotCount() << endl;

        cout << "The difficulty score is: " << LogicSolver::SolveBoard(b) << endl;
    }
    
    // End
    return 0;
}

/* TEST CODE*/
// cout << "The Following board should have 1 solution." << endl;
// b.board = { {0,0,0,2,6,0,7,0,1}
//            ,{6,8,0,0,7,0,0,9,0}
//            ,{1,9,0,0,0,4,5,0,0}
//            ,{8,2,0,1,0,0,0,4,0}
//            ,{0,0,4,6,0,2,9,0,0}
//            ,{0,5,0,0,0,3,0,2,8}
//            ,{0,0,9,3,0,0,0,7,4}
//            ,{0,4,0,0,5,0,0,3,6}
//            ,{7,0,3,0,1,8,0,0,0} };
// 
// b.PrintBoard();
// 
// cout << "The board has: " << Solver::GetSolutionCountOfBoard(b) << " solutions!" << endl;
// 
// cout << endl << " FILL BOARD SOLUTION IS (COULD BE WRONG) : " << endl;
// b.FillBoard(b.board);
// 
// b.PrintBoard();
// 
// 
// cout << endl << "The Following board should have 2 solutions." << endl;
// 
// b.board = { {2,9,5,7,4,3,8,6,1}
//           ,{4,3,1,8,6,5,9,0,0}
//           ,{8,7,6,1,9,2,5,4,3}
//           ,{3,8,7,4,5,9,2,1,6}
//           ,{6,1,2,3,8,7,4,9,5}
//           ,{5,4,9,2,1,6,7,3,8}
//           ,{7,6,3,5,3,4,1,8,9}
//           ,{9,2,8,6,7,1,3,5,4}
//           ,{1,5,4,9,3,8,6,0,0} };
// b.PrintBoard();
// cout << "The board has: " << Solver::GetSolutionCountOfBoard(b) << " solutions!" << endl;