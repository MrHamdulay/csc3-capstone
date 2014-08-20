""" module of utility functions to manipulate 2-dimensional arrays of size 4x4
Author: Dominic Manthoko
01 March 2014
"""

# throught this program, y represents the row number in a grid and x represents 
# the column number in a grid

def create_grid(grid):
    """create a 4x4 grid"""
    
    # adds four list to and empty array
    for i in range(4):
        grid.append([0]*4)  
    
    return grid

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    
    # prints the upper part of the box
    print("+" + "-"*20 + "+")
    
    for y in range(4):
        for x in range(4):
            # handles the left side of the grid
            if (y == 0 and x==0) or (y==1 and x==0) or (y==2 and x==0) or (y==3 and x==0):
                if grid[y][x] == 0:
                    print("|{:<5}".format(''), end = '') 
                else:    
                    print("|{:<5}".format(grid[y][x]), end = '')
                    
            # handles the right side of the grid        
            elif (y==0 and x==3) or (y==1 and x==3) or (y==2 and x==3) or (y==3 and x==3):
                if grid[y][x] == 0:
                    print("{:<5}|".format(''), end = '') 
                else:    
                    print("{:<5}|".format(grid[y][x]), end = '')                
            
            # if a zero value is found, print a space instead of a zero
            elif grid[y][x] == 0:
                print("{:<5}".format(''), end = '')
                
            # handle the middle part of the grid    
            else:
                print("{:<5}".format(grid[y][x]), end = '')
        print()
    
    # prints the lower part of the box    
    print("+" + "-"*20 + "+")
    
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""

    for y in range(4):
        for x in range(4):
            
            if grid[y][x] == 0:
                return False
            
            ## the rest of the code tests if there are any adjacent values that
            ## are equal
            
            elif y==0:           # first line of the grid
                if x == 0:       # top left corner of the grid
                    if (grid[y][x] == grid[y][x+1]) or (grid[y][x] == grid[y+1][x]):
                        return False
                    
                elif x == 3:     # top right corner of the grid
                    if (grid[y][x] == grid[y][x-1]) or (grid[y][x] == grid[y+1][x]):
                        return False
                    
                else:            # upper middle part of the grid
                    if (grid[y][x] == grid[y][x-1]) or (grid[y][x] == grid[y][x+1]) or (grid[y][x] == grid[y+1][x]):
                        return False
            
            elif y == 1 or y == 2:          # checks the values in rows 2 and 3 or the grid
                if x == 0:                  # checks the values on the left side in rows 2 and 3
                    if (grid[y][x] == grid[y-1]) or (grid[y][x] == grid[y+1][x]) or (grid[y][x] == grid[y][x+1]):
                        return False
                    
                if x == 3:                  # checks the values on the right side in rows 2 and 3
                    if  (grid[y][x] == grid[y-1]) or (grid[y][x] == grid[y+1][x]) or (grid[y][x] == grid[y][x-1]):
                        return False
                      
                else:                       # checks the values in the middle part of the grid          
                    if (grid[y][x] == grid[y-1]) or (grid[y][x] == grid[y+1][x]) or (grid[y][x] == grid[y][x+1]) or (grid[y][x] == grid[y][x-1]):
                        return False
                    
            else:                           # checks the values in the last row of the grid
                if x == 0:                  # checks the value at the bottom left of the grid
                    if (grid[y][x] == grid[y-1][x]) or (grid[y][x] == grid[y][x+1]):
                        return False
                    
                elif x == 3:                # checks the value at the bottom right of the grid
                    if (grid[y][x] == grid[y-1][x]) or (grid[y][x] == grid[y][x-1]):
                        return False
                    
                else:                       # checks the values inbetween the bottom left and right of the grid
                    if (grid[y][x] == grid[y-1][x]) or (grid[y][x] == grid[y][x+1]) or (grid[y][x] == grid[y][x-1]):
                        return False
   
    return True

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    
    for y in range(4):
        for x in range(4):
            
            if grid[y][x] >= 32:
                return True
    
    return False

def copy_grid (grid):
    """return a copy of the grid"""
    
    from copy import deepcopy
    
    # create a copy of the grid
    
    grid_copy = deepcopy(grid)
    
    return grid_copy

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    
    for y in range(4):
        for x in range(4):
            # find a value in grid1 that is not equal to another value in grid2 
            # at the same index, then the grids are not the same
            if grid1[y][x] != grid2[y][x]: 
                return False
    return True
