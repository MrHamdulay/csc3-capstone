"""Name: Sibulele Hlongwane
Date: 30 April 2014
Assignment: Module of utility functions"""
import copy
def create_grid(grid):
    """create a 4x4 grid"""
    #appends 0's into an empty grid to create it
    for j in range(4):
        grid.append([0,0,0,0])
    return grid

def print_grid(grid):
    """print out a 4X4 grid in 5 width columns within a box"""
    print("+--------------------+")
    for row in range(4):
        print("|",end="")
        for col in range(4):
            #change [row][column] value into a string
            temp=str(grid[row][col])
            #determine length of string value, and subtract 5 from it, to determine spacing values
            length=5-(len(temp))    
            #if element equals 0, print with certain spacing amount
            if grid[row][col]==0:
                print(" "*5,end="")
            else:
                #else print element within 5 column spacing
                print(grid[row][col],end=" "*length)
            if col==3:
                print("|",end="")
        print()
    print("+--------------------+")
def check_lost(grid):
    """return true if there are no 0 values and no adjacent values that are equal: otherwise false"""
    #boolean value is automatically set to true until a condition is met proving it to be false
    result=True
    #for every row and each column in that row, check if the [row][column] value equals 0 or check if the block next to it is the same value if so, then return false
    for row in range(4):
        for col in range(4):
            if (grid[row][col]==0) or (grid[row][col-1]==grid[row][col]):
                result=False
                
            if col!=3:
                if (grid[row][col+1]==grid[row][col]):
                    result=False
    return result 

def check_won(grid):
    """return true if a value>=32 is found in the grid; otherwise false"""
    #boolean value is automatically set as false, that the user has won, until proven to be true if a value which is greater than 32 is found
    result=False
    for row in range(4):
        for col in range(4):
            if grid[row][col]>=32:
                result=True
    return result
            
def copy_grid(grid):
    #makes a copy of the grid, which doesnt change if the orginal is changed
    test_grid=copy.deepcopy(grid)
    
    return test_grid
    
   # """return a copy of the grid"""
def grid_equal (grid1, grid2):
        """check if 2 grids are equal - return boolean value"""   
        #sets boolean to automatically be true, as it assumes two grids are equal until proven to be false and returns result.
        result=True
        for row in range(4):
            for col in range(4):
                if grid1[row][col]!=grid2[row][col]:
                    result=False
        return result        

