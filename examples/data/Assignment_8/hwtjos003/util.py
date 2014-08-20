#util module
#Joshua Hewitson
#2/5/2014

import math

def create_grid(grid):
    """create a 4x4 grid"""
    grid1 = [0,0,0,0]
    grid2 = [0,0,0,0]
    grid3 = [0,0,0,0]
    grid4 = [0,0,0,0]
    
    grid.append(grid1)
    grid.append(grid2)
    grid.append(grid3)
    grid.append(grid4)

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    x = ""
    for i in range(4):
        x += "|"
        
        for j in range(4):
            if grid[i][j] == 0:
                x += '     '
            else :
                x += '{:<5}'.format(str(grid[i][j]))
        x += "|\n"
    print (x, end = "")
    print ("+--------------------+")    

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    # check for any 0 values:
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                return False
    
    # compare all the values in the list and use the distance formula to check for equal values with distance of 1 (square root in formula is not needed as we are looking for values of 1)    
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if grid[i][j] == grid[k][l]:
                        if math.pow(i-k, 2)+math.pow(j-l, 2) == 1:
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
    grid2 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(4):
        for j in range(4):
            grid2[i][j] = grid[i][j]
    return grid2

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True
    return False