"""Utility functions  to manipulate 2-dimensional arrays of size 4x4
Paul Freund
01/05/14"""

def create_grid(grid):
    """create a 4x4 grid"""
    for y in range(4):
        grid.append([0] * 4)
    return grid

def print_grid(grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for y in grid:
        print("|", end = "")
        for x in y:
            if x == 0:
                print(" " * 5, end = "")
            else:
                print("{:<5}".format(x), end = "")
        print("|")
    print("+--------------------+")
    
    
def check_lost(grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    if grid == []:
        return True
    else:
        if (no_zero_1d(grid[0]) == True) and (no_horizontal_adj_eq(grid[0]) == True) and (no_vertical_adj_eq(grid) == True):
            x = check_lost(grid[1:])
            return x
        else:
            return False

def no_zero_1d(grid):
    """returns True if there are no zeros in a 1d grid; otherwise False"""
    if grid == []:
        return True
    else:
        if grid[0] == 0:
            return False
        else:
            x = no_zero_1d(grid[1:])
            return x

def no_horizontal_adj_eq(grid):
    """returns True if there are no horizantal equal adjacent numbers grid; otherwise False"""
    if len(grid) < 2:
        return True
    else:
        if grid[0] == grid[1]:
            return False
        else:
            x = no_horizontal_adj_eq(grid[1:])
            return x

def no_vertical_adj_eq(grid):
    """returns True there are no vertically equal adjacent numbers in a 2xn grid; otherwise False"""
    grid = grid[:2]
    if len(grid) < 2:
        return True
    else:
        if grid[0] == []:
            return True
        else:
            if grid[0][0] == grid[1][0]:
                return False
            else:
                y = []
                for i in range(2):
                    y.append(grid[i - 1][1:])
                x = no_vertical_adj_eq(y)
                return x
            
def check_won(grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    if grid == []:
        return False
    else:
        if check_won_1d(grid[0]) == True:
            return True
        else:
            x = check_won(grid[1:])
            return x

def check_won_1d(grid):
    """return True if a value>=32 is found in a 1d grid; otherwise False"""
    if grid ==[]:
        return False
    else:
        if grid[0] >= 32:
            return True
        else:
            x = check_won_1d(grid[1:])
            return x

def copy_grid(grid):
    """returns a copy of the grid"""
    from copy import deepcopy
    copy_grid = deepcopy(grid)
    return copy_grid

def grid_equal(grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True
    else:
        return False