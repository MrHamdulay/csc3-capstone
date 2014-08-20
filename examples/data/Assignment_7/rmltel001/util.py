"""Module to manipulate 2-dimensional arrays of size 4x4
Telisha Ramlall
27 April 2014"""

import copy

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range (4):
        grid.append([0,0,0,0]) #append an empty 4x4 list to the grid
    
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for i in range(len(grid)):
        print("|", end = "")
        for j in range(len(grid)):
            if (grid[i][j] == 0):
                grid[i][j] = "" #convert 0 in grid to empty string to print neater grid
            print ("{0: <5}".format(grid[i][j]), end = "")
            if (grid[i][j] == ""):
                grid[i][j] = 0 #convert empty string back to 0 for easier manipulation of grid           
        print("|", end = "")
        print()
    print("+--------------------+")
    
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    lost = True
    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j+1]: #check if numbers on either side of a number is equal to number
                lost = False

    for i in range(3):
        for j in range(4):
            if grid[i][j] == grid[i+1][j]: #check if number below a number is equal
                lost = False    
              
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0: #check if the grid contains any 0s
                lost = False
            
    return lost
    
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    won = False
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] >= 32: #check if any number in the grid is equal to 32
                won = True
    return won    


def copy_grid(grid):
    """return a copy of the grid"""
    return copy.deepcopy(grid) #deep copy is a function in the class copy that returns an original copy

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2: #checks each element in a grid to the corresponding element in another
        return True
    else:
        return False