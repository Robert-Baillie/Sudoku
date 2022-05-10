#include <iostream>
#include "Board.cpp"

using namespace std;



int main(){
    
    srand (time(NULL));
    for (size_t i = 0; i < 1000; i++)
    {
        Board b = Board();
    
        /// Printing out the board values
        b.PrintBoard();
    }
    
   

     
    // End
    return 0;
}