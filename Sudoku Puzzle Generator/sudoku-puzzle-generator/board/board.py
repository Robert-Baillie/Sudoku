import numpy as np


class Board:
    def __init__(self):
        # Initialise the board as a 2D array of zero values
        self.board =np.array([[0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0]])

        self.puzzle_board = None
        self.complete_board = None
        self.puzzle_string = None
        self.puzzle_zero_count = 0
        self.score = 0



    # Initialising the board - Fill the boxes down the diagonals
    def initialise_board(self):
        # Boxes to fill are 0, 3, 6 - start at 0 and increment by 3
        for i in range(0,9,3):
            self.fill_in_box(i)



    # Fill iin box - using the box number passed - find the cell indexs and populate
    def fill_in_box(self, box_num):
        # Temp array that is used to populate box
        tmp = np.array([1,2,3,4,5,6,7,8,9])

        # Loop through the box
        for row in range(3):
            for col in range(3):
                # Grab a number - assign to the board and remove from tmp
                num = np.random.choice((tmp))
                self.board[row + box_num][col + box_num] = num
                tmp = np.delete(tmp, np.argwhere(tmp == num))



    # Fill in the rest of the board
    def fill_board(self):
        row = None
        col = None

        # Step 1 - Find and empty spot - if we do not find one then the board is complete
        # store in a tuple of (i,j)
        find = self.find_empty()

        # if tuple is not size of 2 then we can assign row and col
        if(find is None): 
            return True
        else:
            row = find[0]
            col = find[1]
        
        #Step 2 - Loop through the values of 1 to 9
        for num in range(1,10,1):
            # Step 3 - If the number is valid add it onto the board
            if(self.check_valid_number(num,row,col)):
                self.board[row][col] = num

                # Step 5 - If we can solve this new board, return true
                if(self.fill_board()): 
                    return True

                # Step 6 - other wise return false
                self.board[row][col] = 0
    
        return False
        

    def find_empty(self):
        vec = ()
        
        for i in range(9):
            for j in range(9):
                if(self.board[i, j] == 0):
                    vec = (i, j)
                    return vec



    def check_valid_number(self, num,row,col):
        rows = True
        cols = True
        boxes = True


        # Rows - Loop through rows and on an equal number (or the index) return false
        for i in range(9):
            if(self.board[row, i] == num and i != col): 
                rows = False
                break
        
        # Cols as above
        for i in range(9):
            if(self.board[i, col] == num and i != row):
                cols = False
                break
        
        #Boxes = use integer division to return 0 1 or 2
            # This gives us starting x or y of box which we can then multiply and add to get the end of box

        x = col / 3
        y = row / 3
        x_adj = int(x) * 3
        y_adj = int(y) * 3


        

        for i in range(y_adj, y_adj + 3, 1):
            for j in range(x_adj, x_adj + 3, 1):
                if(self.board[i, j] == num and (i != row and j != col)): 
                    boxes = False
                    break

        
        # Only return true if they are all true
        if(rows and cols and boxes):
            return True

        return False



   # Utilites
    # Print the board in a nice format
    def print_board(self):
        for i in range(9):
            # Row Bars
            if(i % 3 == 0 and i != 0): 
                print("------------")
                
            for j in range(9):
                # Col Bars
        
                if(j % 3 == 0 and j != 0): 
                    print("|", end = "")
                print(self.board[i][j], end = "")
    
            print("\n", end = "")

    # Get the empty slot count of the board
    def empty_slot_count(self):
        count = 0

        for i in range(9):
            for j in range(9):
                if(self.board[i][j] == 0):
                    count += 1

        return count