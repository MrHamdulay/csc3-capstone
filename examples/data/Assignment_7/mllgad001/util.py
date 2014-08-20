# module of utility functions to manipulate 2-D arrays
# mllgad001
# 02 May 2014


def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0]*4)  # adds an array of four zeros to the list four times

def print_grid(grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+" + "-"*20 + "+")
    
    for j in range(4):        # loops through the entire area of the grid
        for k in range(4):
            if k == 0:
                print("|", end = "") # prints this at position 0
            if grid[j][k] == 0:
                print("{0:<5}".format(" "), end = "") # prints empty spaces (formatted) for the middle space of the grid
            else:                                           
                print("{0:<5}".format(grid[j][k]), end = "")
            if k == 3:
                print("|") # prints this when the last position is reached
                
    print("+" + "-"*20 + "+")         
            
def check_won(grid):
    """return True if a value>=32 is found in the grid; otherwise False"""    
    
    for item in grid:              # loops through everything in the grid
        for j in range(len(grid[0])): 
            if item[j] >= 32:
                return True         # if item more than or equal o 32 is found, return true
                  
    return False  # returns false if there's no item more than or equal to 32
                

def check_lost(grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for item in range(4):      # loops through entire area of graph
        for j in range(4):   
            if grid[item][j] == 0:       # if there is empty spaces found return false
                return False
            
        for j in range(3):      
                if grid[item][j] == grid[item][j+1]:
                    return False                
          # if two adjacet values that are equal is found, return false
    for item in range(3):
        for j in range(4):
            if grid[item][j] == grid[item+1][j]:
                return False
            
    return True       # otherwise, if there no zero values and two adjacent values are equal, return true

def copy_grid(grid):
    """return a copy of the grid"""    
    for i in range(4):
            copy = []
            copy.append([0]*4)  # create a new grid which is a copy of the old one
    for i in range(4):
        for j in range(4):
            copy[i][j] = grid[i][j]  # the new grid's values must be the same as the old grid
    return copy

def grid_equal(grid1,grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return_ = True   # returns true if 2 grids are equal
    return False  # if not, returns false

