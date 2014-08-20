"""Module for manipulating 4x4 arrays
Julian Albert
ALBJUL005
29 April 2014"""

def create_grid(grid):
    '''create a 4x4 grid'''
    for i in range(4):                          
        grid.append([0,0,0,0])                  
    return grid                                 

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")             
    for i in range(4):                          
        string = '|'                              
        for j in range(4):                      
            value = str(grid[i][j])               
            if value == '0':
                value = ' '                       
            string += value + ' ' * (5-(len(value)))  
        string += '|'                            
        print(string)                           
    print("+--------------------+") 
    
def check_lost(grid):
    """Return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                return False
            elif i+1 < len(grid):
                if grid[i][j] == grid[i+1][j]:
                    return False
            elif j+1 < len(grid[i]):
                if grid[i][j] == grid[i][j+1]:
                    return False            
    return True

def check_won(grid):
    """Return True if a value>=32 is found in the grid; otherwise False"""
    for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] >= 32:
                    return True    
    return False

def copy_grid(grid):
    """ Return a copy of the grid """
    new_grid = []
    new_grid = create_grid(new_grid)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            new_grid[i][j] = grid[i][j]
    return new_grid

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:                            #check if two grids are identical
        return True
    else:
        return False