'''
This is the Sudoku_Set_Up class. This class takes a string representation of the
Sudoku board, re-organises it in a meaningful way, replaces empty spaces with
all possible numbers and set's up the board for the solver.
'''
class Sudoku_Set_Up():
    rows = 'abcdefghi'; columns = '123456789';

    def __init__(self, string_board):
        '''
        Initialises the class.
        Takes in a sudoku board in the form of a String
        For a 9x9 puzzle String length must = 161. 81 elements and 80 commas
        else throws an exception
        '''
        string_board = string_board.replace(',', '');
        if len(string_board) != 81:
            print('The length of the string board is incorrect. Stopping now');
            raise Exception('String must be 161 characters');
        else : #build the game
            self.build_board();
            self.string_board = string_board;
            self.dict_board = str_to_dict(string_board);

    def cross_join(a,b):    #helper for build board
        a = [x+y for x in a for y in b];
        return a;
    
    def build_board(self):
        '''
        Helps build indices in a way to complement the rules of sudoku
        '''
        self.keys = [x+y for x in self.rows for y in self.columns];
        self.row_line = [self.cross_join(x,self.columns) for x in self.rows];
        self.col_line = [self.cross_join(self.rows, x) for x in self.columns];
        self.sub_grid = [self.cross_join(x,y) for x in ('abc','def','ghi')
                         for y in ('123','456','789')];
        self.list_all = self.row_line + self.col_line + self.sub_grid;
        self.blocks = dict((x, [y for y in self.list_all if x in y]) for x in
                           self.keys);
        self.comparers = dict((x, set(sum(self.blocks[x],[]))-set([x]))
                              for x in self.keys);

    def str_to_dict(self, string_board = None):
        '''
        Takes in a sudoku board as a ',' seperated string and converts it into
        a dict with keys as a1, a2...., b1, b2..., i9 and values as strings
        '''
        string_board = self.string_board;
        dict_board = {};
        for key, value in zip(self.keys, string_board):
            if value == '0':
                value = '123456789';
            dict_board[key] = value;
        return dict_board;

    def dict_to_str(self, dict_board = None):
        '''
        Takes a dict of block_number, value_stored and converts it to a string
        '''
        string_board = '';
        dict_board = self.dict_board;
        for key in self.keys:
            value = dict_board[key];
            if len(value) == 1:
                string_board += str(value);
            else: string_board += '0'
        return string_board;

    def remove_elem(self, index, elem):
        '''
        Replaces a digit from the string stored for a particular block.
        '''
        self.dict_board[index] = self.dict_board[index].replace(elem, '');

    def solve_check(self):
        '''
        returns false if board is not solved. else returns true
        '''
        for key in self.keys:
            if len(dict_board(key)) != 1: return False;
        for box in self.list_all:
            required_digits = '123456789';
            for key in box:
                required_digits = required_digits.replace(self.dict_board[key],
                                                          '');
                if len(required_digits) != 0:
                    return False;
        return True;

    '''def disp(self, dict_board = None):
        """
        Converts dict to a 2d array.
        Displays it line by line
        """
        dict_board = self.dict_board;
        to_array = [['0' for x in range(0,9)] for y in range(0,9)];
        count_row = 0; count_col = 0;
        while (count_row < 9):
            for key in dict_board.keys():
                to_array[count_row][count_col] = dict_board(key);
                count_col += 1;
                if (count_col > 8):
                    count_col = 0;
                    count_row += 1;'''
        
