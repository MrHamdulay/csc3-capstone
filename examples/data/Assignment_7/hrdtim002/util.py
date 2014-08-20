"""module of utility functions to manipulate 4x4 array
Tim Hardie
1/5/14"""

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range (4):
        grid.append ([])
        for j in range (4):
            grid[i].append (0)

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    f = '{:<5}'
    print("+--------------------+")
    print('|', f.format(grid[0][0]), f.format(grid[0][1]), f.format(grid[0][2]), f.format(grid[0][3]), '|',sep='')
    print('|', f.format(grid[1][0]), f.format(grid[1][1]), f.format(grid[1][2]), f.format(grid[1][3]), '|',sep='')
    print('|', f.format(grid[2][0]), f.format(grid[2][1]), f.format(grid[2][2]), f.format(grid[2][3]), '|',sep='')
    print('|', f.format(grid[3][0]), f.format(grid[3][1]), f.format(grid[3][2]), f.format(grid[3][3]), '|',sep='')
    print("+--------------------+")

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    is_lost = True
    
    #check for zeroes
    for i in range (4):
        for j in range (4):
            if grid[i][j] == 0:
                is_lost = False
    
    #check corners
    if (grid[0][0] == grid[0][1]) or (grid[0][0] == grid[1][0]): is_lost = False
    if (grid[0][3] == grid[0][2]) or (grid[0][3] == grid[1][3]): is_lost = False
    if (grid[3][0] == grid[3][1]) or (grid[3][0] == grid[2][0]): is_lost = False
    if (grid[3][3] == grid[3][2]) or (grid[3][3] == grid[2][3]): is_lost = False
    
    #check rest
    for i in (1,2):
        for j in (1,2):
            if (grid[i][j] == grid[i-1][j]) or (grid[i+1][j] == grid[i][j]) or (grid[i][j-1] == grid[i][j+1]): is_lost = False
    
    return is_lost

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in range (4):
        for j in range (4):
            if grid[i][j] >= 32:
                return True
    return False

def copy_grid (grid):
    """return a copy of the grid"""
    new_grid = []
    for i in range (4):
        new_grid.append ([])
        for j in range (4):
            new_grid[i].append (grid[i][j])
    return new_grid

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    for i in range (4):
        for j in range (4):
            if grid1[i][j] != grid2[i][j]:
                return False
    return True