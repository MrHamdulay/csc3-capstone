'''module of utility functions to manipulate 
2-dimensional arrays of size 4x4
Michele Balestra  BLSMIC004
1 March 2014'''

def create_grid(grid):
    """create a 4x4 grid"""
    height = 4
    for i in range (height):
        grid.append ([0] * 4)
        
        
def print_grid(grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print('+--------------------+')
    for i in range(4):
        print('|',end='')
        for j in range(4):
            if grid[i][j]==0:
                grid[i][j] = ' '
            print('{:<5}'.format(grid[i][j]),end='')
        print('|',end='')
        print()
    print('+--------------------+')
    
def check_lost(grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    if 0 in grid:
        return True
    else: return False
    
def check_won(grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in range(4):
        for j in range(4):
            if (grid[i][j])>=32:
                return True
    else: return False

def copy_grid(grid):
    """return a copy of the grid"""
    new_grid = grid[:]
    return new_grid
    
def grid_equal(grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True
    else: return False