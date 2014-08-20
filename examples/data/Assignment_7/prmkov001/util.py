#Kovlin Perumal
#PRMKOV001
#30/04/2014
#Question 2 - 2D Array Question

import copy
def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0,] * 4)

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for i in range (4) :
        print("|",end = '')
        for j in range (4) :
            if grid[i][j] != 0 :
                print(str(grid[i][j]) + (5 - len(str(grid[i][j]))) * " ",end = '')
            else :
                print( 5 * " ",end = '')
        print("|")
    print("+--------------------+")

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for i in range (4) :
        for j in range (4) :
            if(grid[i][j] == 0) :
                return False 
            elif i != 3:
                if grid[i][j] == grid[i + 1][j] :
                    return False
            elif j != 3:
                if grid[i][j] == grid[i][j + 1] :
                    return False            
    return True

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    check = False    
    for i in range (4) :
        for j in range (4) :
            if(grid[i][j]>=32) :
                check = True    
    return check

def copy_grid (grid):
    """return a copy of the grid"""
    return copy.deepcopy(grid)
    
def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2 :
        return True
    else :
        return False
    
