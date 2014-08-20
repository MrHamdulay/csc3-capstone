"""A list of functions to be utilized to create a game replicating 2048
by Jeremy Smith SMTJER002
1 May 2014"""

def create_grid(grid):
    """creates a 4x4 grid"""
    height=4
    for row in range(height):
            grid.append([0]*height)
    return grid

def print_grid (grid):
    """prints out a 4x4 grid in 5-width columns within a box"""
    height=4
    game_grid = grid
    print('+'+'-'*20+'+')
    for row in range(height):
        print('|',end='')
        for col in range(height):
            if game_grid[row][col] == 0:
                print('{0:<5}'.format(" "),end='')
            else:
                print('{0:<5}'.format(game_grid[row][col]),end='')
        print('|')
    print('+'+'-'*20+'+')
    
def check_lost (grid):
    """returns False if there are 0 values in the grid or if any adjacent values are equal, otherwise returns True"""
    height=4
    #check for 0 value in grid    
    for row in range(height):
        for col in range(height):
            if 0 in grid[row]:
                return False
    #check for equal adjacent values horizontally       
    for row in range(height):
        for col in range(height-1):    
            if grid[row][col] == grid[row][col+1]:
                return False
    
    #check for equal adjacent values vertically           
    for row in range(height-1):
        for col in range(height):    
            if grid[row][col] == grid[row+1][col]:
                return False            
    else:
        return True

def check_won (grid):
    """returns True if a value>=32 is found in the grid; otherwise False"""
    height=4
    for row in range(height):
        for col in range(height):
            if grid[row][col] >= 32:
                return True
    else: 
        return False
    
def copy_grid (grid):
    """returns a copy of a grid"""
    height = 4
    copy = []
    for row in range(height):
        row_copy=[]
        for col in range(height):
            row_copy.append(grid[row][col])
        copy.append(row_copy)
    return copy

def grid_equal (grid1, grid2):
    """checks if 2 grids are equal - return boolean value"""
    height = 4
    for row in range(height):
        for col in range(height):
            if grid1[row][col] != grid2[row][col]:
                return False
    else:
        return True