"""A7Q2 - 2d array manipulation for 2048 game
27/04/2014
CRNKEE002"""

import copy

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0,0,0,0])

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print('+--------------------+')   
    for i in range(4):
        toprint = ''
        for j in range(4):
            if grid[i][j] == 0:
                toprint = toprint + '{:<5}'.format("")
            else:    
                toprint = toprint + '{:<5}'.format(str(grid[i][j]))
        print('|' + toprint + '|')      
    print('+--------------------+')

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for x in range(4):
        for y in range(4):
            if grid[x][y] == 0:
                return False   
            
    for x in range(4):
        for y in range(4):
            for x2 in range(x-1, x+2):
                for y2 in range(y-1, y+2):
                    if (x == x2 and y == y2) or (y2>3) or (x2>3):
                        pass
                    elif (x2 == x-1 and y2 == y-1) or (x2 == x-1 and y2 == y+1) or (x2 == x+1 and y2 == y-1) or (x2 == x+1 and y2 == y+1) or (x2==x and y2 ==y)  or (x2 == -1) or (y2 == -1):
                        pass
                    elif (grid[x][y] == grid[x2][y2]):
                        return False
    else:
        return True
    

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for x in range(4):
        for y in range(4):
            if grid[x][y] >= 32:
                return True
    else:
        return False

def copy_grid (grid):
    """return a copy of the grid"""
    return copy.deepcopy(grid)

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    for x in range(4):
        for y in range(4):
            if grid1[x][y] != grid2[x][y]:
                return False
    else:
        return True