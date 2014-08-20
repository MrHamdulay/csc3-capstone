# question3.py
# Name: Buhlebezwe
# Student Number: MBLBUH001
# Date: 13 May 2014

sudoku_grid = []                                                #initialize sudoku_grid to empty list, []
def create_grid(grid):                                          #define function create_grid(grid)
    for i in range (9):
        grid.append ([0] * 9)                                   #create 9x9 grid filled with 0 entries
    return grid                                                 #returns 9x9 grid filled with 0 entries

create_grid(sudoku_grid)

for row in range(9):
    x = input()                                                 #gets input from the user
    for column in range(9):
        sudoku_grid[row][column] = x[column]                    #fills the sudoku_grid with the input entered by the user

def check_row():                                                #define function check_row()
    counters = {}                                               #initialize counters to empty dictionary, {}
    for i in range(9):
        for j in sudoku_grid[i]:                                #for each element in row i
            if not (j in counters):                             #checks if any number along any row does repeat
                counters[j]=1                                   #adds number in each row to dictionary
                pass
            else:
                return False                                    #return False if a number happens to be repeated in any row
        counters = {}                                           #initialize counters to an empty dictionary, {}, after checking each row
    return True                                                 #return True if each row has non-repeating numbers in it

def check_column():                                             #define function check_column()
    counters = {}                                               #initialize counters to empty dictionary, {}
    for i in range(9):
        for j in range(9):
            for k in sudoku_grid[j][i]:                         #for each element in a column j
                if not (k in counters):                         #checks if any number along any column does repeat
                    counters[k]=1                               #adds number in each column to dictionary
                    pass
                else:
                    return False                                #return false if a number happens to be repeated in any column
        counters = {}                                           #initialize counters to an empty dictionary, {}, after checking each row
    return True                                                 #return True if each column has non-repeating numbers in it

def check_3x3_grid():                                           #define function check_3x3_grid()
    counters = {}                                               #initialize counters to empty dictionary, {}
    for l in range(3):
        for n in range(3):
            for i in range(3*l,3*l+3):
                for j in range(3*n,3*n+3):
                    for k in sudoku_grid[i][j]:                 #for each element in each of the 3x3 smaller grids
                        if not (k in counters):                 #checks if any number in any 3x3 grid repeats
                            counters[k]=1                       #adds number in each 3x3 grid to dictionary
                            pass
                        else:
                            return False                        #return False if a number happens to be repeated in any 3x3 grid
            counters = {}                                       #initialize counters to an empty dictionary, {}, after checking each 3x3 grid
    return True                                                 #return True if each 3x3 grid has non-repeating numbers in it

if check_row() and check_column() and check_3x3_grid():         #checks if all the conditions of a valid Soduku grid are met
    print("Sudoku grid is valid")                               #print statement executed if Soduku grid is valid
else:
    print("Sudoku grid is not valid")                           #print statement executed if Sudoku grid is not valid