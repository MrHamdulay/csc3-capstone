8#29/04/2014
#ASSIGNMENT 7
#QUESTION 2 - util function to be run by question2.py
#WHTBAS001
#THOMAS WHITEHEAD

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0,0,0,0])

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                grid[i][j] = ' '
        print("|",'{0:<4} {1:<4} {2:<4} {3:<5}'.format(grid[i][0], grid[i][1], grid[i][2], grid[i][3]),"|",sep="")            
    print("+--------------------+")

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                return False
    for i in range(3):
        for j in range(3):
            if grid[i][j] == grid[i][j+1]:
                return False
            if grid[i][j] == grid[i+1][j]:
                return False
            if grid[i][j+1] == grid[i+1][j+1]:
                return False
            if grid[i+1][j] == grid[i+1][j+1]:
                return False
    else:
        return True

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in range(4):
        for j in range(4):
            if grid[i][j] >= 32:
                return True
    else:
        return False

def copy_grid (grid):
    """return a copy of the grid"""
    newgrid = []
    for i in range(4):
        newgrid.append([0,0,0,0])
    for j in range(4):
        for k in range(4):
            newgrid[j][k] = grid[j][k]
    return newgrid

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    for i in range(4):
        for j in range(4):
            if grid1[i][j] != grid2[i][j]:
                return False
    else:
        return True