"""Utility functions to manipulate 2-dimensional arrays of size 4x4"""
"""Brandon Pickup"""
"""Assignment 7 Question 2"""
"""27 April 2014"""

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0]*4)
    
    
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("{0}{1}{0}".format("+","-"*20)) #prints the border for the first row 
    for i in range(4):     
        for j in range(4):
            if j == 0:#prints the left border 
                print("|",end="")
            if grid[i][j] != 0:print("{0:<5}".format(grid[i][j]),end="")#prints the grid values in columns of width 5 if the value is not 0
            else: print("{0:<5}".format(" "),end="")
        print("|")#right hand border
    print("{0}{1}{0}".format("+","-"*20))#bottom border
    
    
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0: #checks whether the value in the grid is 0, if it is, the game is not lost
                return False
            if i<3:
                if grid[i][j] == grid[i+1][j]:
                    return False#check down
            if j<3: 
                if grid[i][j] == grid[i][j+1]:#check right
                    return False
    return True


def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in range(4):
        for j in range(4):
            if grid[i][j] >= 32:
                return True   
    return False


def copy_grid (grid):
    """return a copy of the grid"""
    copy=[]    
    for i in range (4):#creates a a 4x4 grid which is empty - just filled with 0s
        copy.append([0]*4)
    for i in range(4):
        for j in range(4):#for every value in the grid sent as a parameter, a copy of the value is stored in the local grid (copy) of this function
            copy[i][j] = grid[i][j]
    return copy


def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    for i in range(4):
        for j in range(4):
            if grid1[i][j] != grid2[i][j]:#compares each value within each grid sent as parameters, if a duplicate is found, False is sent as the grids are not equal.
                return False   
    return True    