# Util module for 2048 game
# James Behr
# 2014-04-30

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0,0,0,0])
    
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""  
    print('+', '-' * 20, '+', sep = '')
    for y in range(4):
        print('|', end = '')
        for x in range(4):
            # Print nothing if value is 0, else print the value
            if grid[y][x]:
                print('{:<5}'.format(grid[y][x]), end = '')
            else:
                print(' ' * 5, end = '')
        print('|')
    print('+', '-' * 20, '+', sep = '')
    
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for i in range(4):
        # Check for 0s in the grid
        if 0 in grid[i]:
            return False
    
    for y in range(4):
        for x in range(4):
            # Check if each adjacent square is equal. If any square is return False
            if y - 1 > 0:
                if grid[y][x] == grid[y - 1][x]:
                    return False
                
            if y + 1 < 4:
                if grid[y][x] == grid[y + 1][x]:
                    return False     
                
            if x - 1 > 0:
                if grid[y][x] == grid[y][x - 1]:
                    return False 
                
            if x + 1 < 4:
                if grid[y][x] == grid[y][x + 1]:
                    return False   
        
    # Return true if all checks fail
    return True
            
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    # Loop through to check for values >= 32
    for y in range(4):
        for x in range(4):
            if grid[y][x] >= 32:
                return True
    return False

def copy_grid (grid):
    # Use slicing and a list comprehension to create a copy, rather than a reference
    """return a copy of the grid"""
    return [grid[i][:] for i in range(4)]

def grid_equal (grid1, grid2):
    # Compare each sub-list using python's list comparing
    """check if 2 grids are equal - return boolean value"""
    for i in range(4):
        if grid1[i] != grid2[i]:
                return False
    return True
            