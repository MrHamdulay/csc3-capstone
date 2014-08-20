# Author : Rayaan Fakier FKRRAY001
# Date : 28 - 04 - 2014
# util.py

import copy

def create_grid(grid):
    """Creates a 4x4 grid"""
    for i in range(4):
        grid.append([0]*4)
    return grid

def print_grid(grid):
    """Print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    
    grid_form = "{0:<5}" # Formats grid
    # Prints grid block by block
    for rows in range(4):
        print("|",end="")
        for columns in range(4):
            if grid[rows][columns] > 0:
                print(grid_form.format(grid[rows][columns]),end ="")
            else:
                print(grid_form.format(""),end = "")
    
        print("|",end="")
    
        print()
    
    print("+--------------------+")


def check_lost(grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for p in range(4):
        for q in range(4):
            if grid[p][q] == 0: # If any 0's -> return False
                return False
    
    for s in range(4):
        for t in range(4):
            
            # Checks if 4 mid blocks have any possible moves
            if (s == 1 or s == 2) and (t == 1 or t == 2):
                if grid[s][t] == (grid[s-1][t] or grid[s+1][t] or grid[s][t-1] or grid[s][t+1]):
                    return False
                
            # Checks if 2 top mid blocks have any possible moves        
            if (s == 0) and (t == 1 or t == 2):
                if grid[s][t] == (grid[s+1][t] or grid[s][t-1] or grid[s][t+1]):
                    return False
                
             # Checks if 2 bottom mid blocks have any possible moves       
            if (s == 3) and (t == 1 or t == 2):
                if grid[s][t] == (grid[s-1][t] or grid[s][t-1] or grid[s][t+1]):
                    return False
                
            # Checks if 2 left mid blocks have any possible moves        
            if (t == 0) and (s == 1 or s == 2):
                if grid[s][t] == (grid[s-1][t] or grid[s+1][t] or grid[s][t+1]):
                    return False
                
           # Checks if 2 right mid blocks have any possible moves         
            if (t == 3) and (s == 1 or s == 2):
                if grid[s][t] == (grid[s-1][t] or grid[s+1][t] or grid[s][t-1]):
                    return False
                
            # Checks if top left block has any possible moves        
            if (s == 0) and (t == 0):
                if grid[s][t] == (grid[s+1][t] or grid[s][t+1]):
                    return False
                
           # Checks if top right block has any possible moves         
            if (s == 0) and (t == 3):
                if grid[s][t] == (grid[s+1][t] or grid[s][t-1]):
                    return False   
                
            # Checks if bottom left block has any possible moves        
            if (s == 3) and (t == 0):
                if grid[s][t] == (grid[s-1][t] or grid[s][t+1]):
                    return False
                
            # Checks if bottom right block has any possible moves                        
            if (s == 3) and (t == 3):
                if grid[s][t] == (grid[s-1][t] or grid[s][t-1]):
                    return False
    return True
    
def check_won(grid):
    """return True if a value >=32 is found in the grid; otherwise False"""
    for block in range(4):
        for val in range(4):
            if grid[block][val] >= 32:
                return True
    return False
    
def copy_grid(grid):
    """Return a copy of the grid"""
    new_grid = copy.deepcopy(grid)
    return new_grid
    
def grid_equal(grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True
    else:
        return False