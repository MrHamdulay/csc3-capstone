# util.py
# a module utility function to manipulate 2-D arrays of size 4x4
# these functions will be used in question 3
# Thomas Konigkramer
# 27 April 2014

def create_grid(grid):
    """create a 4x4 grid"""
    height = 4
    for i in range(height):
        grid.append([0] * height)    
    
def print_grid(grid):
    """print out a 4x4 grid in 5-width columns without a box"""
    
    print("+--------------------+")
    
    for row in range(4):
        print("|", end = "")
        for column in range(4):
            if grid[row][column] == 0:
                print("{0:<5}".format(""), end = "") # so that 0 doesn't get printed
            else:
                print("{0:<5}".format(grid[row][column]), end = "")
        print("|")
    
    print("+--------------------+")
        
   
def check_lost(grid):
    """ return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for row in range(4):
        for column in range(4):
            if grid[row][column] == 0:
                return False
            elif column == 3: # to prevent out of range index - checking horizontals
                if grid[row][column] == grid[row][column-1]:
                    return False
            elif grid[row][column] == grid[row][column+1]:
                return False 
    
    for row in range(4):
        for column in range(4):
            if row == 3: # to prevent out of range index - checking verticals
                if grid[row][column] == grid[row-1][column]:
                    return False
            elif grid[row][column] == grid[row+1][column]:
                return False
    
    return True

def check_won(grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for row in range(4):
        for column in range(4):
            if grid[row][column] >= 32:
                return True        
    return False
    
def copy_grid(grid):
    """return a copy of the grid"""
    import copy
    
    grid_copy = copy.deepcopy(grid)
    return grid_copy

def grid_equal(grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True
    else:
        return False