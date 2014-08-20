# A module of utility functions that manipulate 2D arrays of size 4x4
# Martin Batek
# 30 April 2014

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0]*4)
    return grid
        
def print_grid(grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+"+("-"*20)+"+")
    for row in range(len(grid)):
        print("|",end="")
        for column in range(len(grid[row])):
            if grid[row][column]==0:
                print("     ",end="")
            else:
                numstring = str(grid[row][column])
                print(numstring+((5-len(numstring))*" "),end="")
        print("|")
    print("+"+("-"*20)+"+")
    
def check_lost(grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    x = True
    for row in range(len(grid)-1):
        for column in range(len(grid[row])-1):
            if grid[row][column]==0 or grid[row][column+1]==0 or grid[row+1][column]==0: # Testing for zeros
                x = False
            elif grid[row][column] == grid[row][column+1] or grid[row+1][column] == grid[row+1][column+1]: # Testing for equal adjacent numbers
                x = False
            elif grid[row][column] == grid[row+1][column] or grid[row][column+1] == grid[row+1][column+1]: # Testing for equal numbers on top of one another
                x = False
    return x
            
def check_won(grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    x = False
    for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] >= 32:
                    x = True
    return x

def copy_grid (grid):
    """return a copy of the grid"""
    gridcopy = []
    for row in range(len(grid)):
        gridrow = []
        for column in range(len(grid[row])):
            gridrow.append(grid[row][column])
        gridcopy.append(gridrow)
    return gridcopy

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True
    else:
        return False


     
