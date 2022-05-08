#include <vector>
using namespace std;

class BoardProperties
{
private:
    // Board connected_board;
public:
    BoardProperties(/*Board board*/);
    ~BoardProperties();

    vector<int> one_to_nine = {1,2,3,4,5,6,7,8,9};


    // Rows
    vector<vector<int>> row_numbers_remaining = {
                                            one_to_nine,
                                            one_to_nine,
                                            one_to_nine,
                                            one_to_nine,
                                            one_to_nine,
                                            one_to_nine,
                                            one_to_nine,
                                            one_to_nine,
                                            one_to_nine,
                                            };

    // Column
    vector<vector<int>> col_numbers_remaining = {
                                            one_to_nine,
                                            one_to_nine,
                                            one_to_nine,
                                            one_to_nine,
                                            one_to_nine,
                                            one_to_nine,
                                            one_to_nine,
                                            one_to_nine,
                                            one_to_nine,
                                            };
                    
    // Boxes
    vector<vector<int>> box_numbers_remaining = {
                                            one_to_nine,
                                            one_to_nine,
                                            one_to_nine,
                                            one_to_nine,
                                            one_to_nine,
                                            one_to_nine,
                                            one_to_nine,
                                            one_to_nine,
                                            one_to_nine,
                                            };


};

BoardProperties::BoardProperties(/*Board board*/)
{
    // connected_board = board;

}

BoardProperties::~BoardProperties()
{
}
