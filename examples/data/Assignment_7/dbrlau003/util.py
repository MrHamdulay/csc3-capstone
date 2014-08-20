#Lauren de Bruyn
#Module of utility functions
#30 April 2014

import copy

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range (4):
        grid.append ([0] * 4)    
    

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for row in range(4):
        print("|",end="")
        for column in range(4):
            if grid[row][column]== 0:
                print("{0:<5}".format(" "),end="")
            else:
                print("{0:<5}".format(grid[row][column]),end="")
        print("|")
    print("+--------------------+")
    
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for i in range(4):
        for t in range(4):
            if grid[i][t] == 0:
                return False
            
    for i in range(3):
        for t in range(3):
            if grid[i][t] == grid[i][t+1]:
                return False
            
    for i in range(3):
        for t in range(3):
            if grid[i][t] == grid[i+1][t]:
                return False
                
    return True
    
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    winningnumber=0
    for i in range(4):
        for t in range(4):
            if grid[i][t]>=32:
                winningnumber=-1
                
    if winningnumber==-1:
        return True
    else:
        return False

def copy_grid (grid):
    """return a copy of the grid"""
    newgrid=copy.deepcopy(grid)
    return newgrid

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True
    else:
        return False

    
    
            

    
    