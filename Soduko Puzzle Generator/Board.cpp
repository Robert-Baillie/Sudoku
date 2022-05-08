#include "Cell.cpp"
#include <vector>
#include <algorithm>
#include "BoardProperties.cpp"

using namespace std;


class Board
{
private:
    // Methods
    void InitialiseBoard(vector<vector<Cell>>& board);
    void InitialiseRow(vector<Cell>& row, int row_num);


    
    // void FillInBoxRandom(vector<vector<Cell>>& board, int box);
    void FillCell(Cell& cell);
    int GetRandomNumber(vector<int> vector);


    // Variables
    BoardProperties board_properties;
    
public:
    // Construct
    Board(/* args */);
    ~Board();

    // Rows
    vector<Cell> row_one;
    vector<Cell> row_two;
    vector<Cell> row_three;
    vector<Cell> row_four;
    vector<Cell> row_five;
    vector<Cell> row_six;
    vector<Cell> row_seven;
    vector<Cell> row_eight;
    vector<Cell> row_nine;
    
    // Board
    vector<vector<Cell>> board;


    
};


Board::Board(/* args */)
{
    board_properties = BoardProperties();

    /// Initialise Board - Fill Diagonal Boxes
    InitialiseBoard(board);


    //
}

Board::~Board()
{
}


void Board::InitialiseBoard(vector<vector<Cell>>& board){
    /// Insert rows
    board = {row_one,
            row_two,
            row_three,
            row_four,
            row_five,
            row_six,
            row_seven,
            row_eight,
            row_nine};
    
    // Row Set Up
    for (size_t i = 0; i < board.size(); i++)
    {
        InitialiseRow(board[i], i);
    }
    
}

void Board::InitialiseRow(vector<Cell>& row, int row_num){
    row_num++;

    int box_num_start = 1;
    if(row_num > 6) box_num_start =7; 
    else if(row_num >3) box_num_start = 4;

    for (size_t i = 0; i < 9; i++)
    {
        int box_num = box_num_start;
        if(i > 5) box_num = box_num_start +2;
        else if(i > 2) box_num = box_num_start +1;


        Cell cell;
        cell.row_number = row_num;
        cell.column_number = (i+1);
        cell.box_number = box_num;

        cell.cell_number =0;

        if(box_num ==1) FillCell(cell);
        if(box_num ==5){};
        if(box_num ==9){};


        row.push_back(cell);
    }
    
}


int Board::GetRandomNumber(vector<int> vector){
    int rnd = rand() % vector.size();
    return vector[rnd];
}


void Board::FillCell(Cell &cell){
    
}


/// OLD LOGIC
/*
void Board::FillInBoxRandom(vector<vector<Cell>>& board, const int box){
    int column_addition =0;
    int row_addition = 0;
    vector<int> one_to_nine_tmp = one_to_nine;

    /// TEST
    if(box == 0){
        column_addition = 0;
        row_addition = 0;
    }
    else if(box == 4){
        column_addition = 3;
        row_addition = 3;
    } 
    else if(box == 8){
        column_addition = 6;
        row_addition = 6;
    } 

    for (size_t i = 0; i < 3; i++)
    {
        for (size_t j = 0; j < 3; j++)
        {
            Cell cell = board[i + row_addition][j+column_addition];

            int num = GetRandomNumber(one_to_nine_tmp);
            cout << "Inserting " << num << endl;
            cell.cell_number = num;

            board[i + row_addition][j+column_addition] = cell;

            one_to_nine_tmp.erase(std::remove(one_to_nine_tmp.begin(), one_to_nine_tmp.end(), num), one_to_nine_tmp.end());
        }
    }
    


}
*/