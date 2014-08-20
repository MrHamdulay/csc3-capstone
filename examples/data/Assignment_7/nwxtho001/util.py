'''a module of functions to manipulate 2-dimensional arrays of size 4x4
tom new
2014/28/04'''

def create_grid (grid):
    '''Creates a 4x4 grid'''
    for i in range (4):
        grid.append ([0] * 4)
        
def print_grid (grid):
    '''Prints out a 4x4 grid in 5-width columns within a box'''
    for row in range (6):
        for col in range (6):
            
            # creates the border
            if (col == 0 or col == 5) and (row == 0 or row == 5):
                print ('+', end = '')
            elif col == 0 or col == 5:
                print ('|', end = '')
            elif row == 0 or row == 5:
                print ('-'*5, end = '')
            
            # 'escapes' zeroes with spaces
            elif grid [row - 1][col - 1] == 0:
                print (' ' * 5, end = '')
            
            # prints the values in grid
            else:
                print ('{:<5}'.format(grid [row - 1][col - 1]), end = '')
        print ( )
        
def check_zeroes (grid):
    '''Returns True if there are 0 values, otherwise False'''
    for row in range (4):
        for col in range (4):
            if grid [row][col] == 0:
                return True
    return False
            
def check_horz (grid):
    '''Returns True if there are adjacent horizontal values that are equal, otherwise False'''
    for row in range (3):
        for col in range (3):
            if grid [row][col] == grid [row][col + 1]:
                return True
    return False

def check_vert (grid):
    '''Returns True if there are adjacent vertical values that are equal, otherwise False'''
    for row in range (3):
        for col in range (3):
            if grid [row][col] == grid [row + 1][col]:
                return True
    return False    
        
def check_lost (grid):
    '''Returns True if there are no 0 values and no adjacent values that are equal, otherwise False'''
    if check_zeroes (grid) or check_horz (grid) or check_vert (grid):
        return False
    else:
        return True
    
def check_won (grid):
    '''Returns True if a value >= 32 is found in the grid, otherwise False'''
    for row in range (4):
        for col in range (4):
            if grid [row][col] >= 32:
                return True
    return False

def copy_grid (grid):
    '''Returns a copy of the grid'''
    import copy
    return copy.deepcopy (grid)

def grid_equal (grid1, grid2):
    '''Checks if 2 grids are equal - return boolean value'''
    if grid1 == grid2:
        return True
    return False