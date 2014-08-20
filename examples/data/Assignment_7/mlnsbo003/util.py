'''Module of utility functions
Sbongakonke Mlangeni
29 April 2014'''

def create_grid(grid):
    """create a 4x4 grid"""
    for i in grid:
        for j in i:
            return(eval(j))
        
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print('+--------------------+')
    for i in grid:
        print('|',end='')
        for j in i:
            print('{0:<5}'.format(eval(j)),end='')
        print('|')
    print('+--------------------+')    
    
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j+1]:
                return False
            elif grid[i][j] == 0 or grid[i][j+1] == 0:
                return False
            else:
                return True
    for i in range(4):
        for j in grid:
            if j[i] == j[i+1]:
                return False
            
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in grid:
        for j in i:
            if j >= 32:
                return True
            else:
                return False
def copy_grid (grid):
    """return a copy of the grid"""
    return grid

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True
    else:
        return False