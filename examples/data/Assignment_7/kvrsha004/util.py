""" Q2 of Assignment 7: Utility functions for 2D arrays
Shaheel Kooverjee
1st May 2014 """

grid = []
gridcopy = []

def create_grid(grid):
    """create a 4x4 grid"""
    
    for i in range(4):
        grid.append([0] * 4) #list with 4 0-entries

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    
    print("+--------------------+")
    for row in range(4): #print rows
        print("|", end="")
        for col in range(4): #print columns
            if grid[row][col] == 0:
                grid[row][col] = " "
            print("{0:<5}".format(grid[row][col]), end="") #5-width formatting for columns
        print("|", end="")
        print()    
    print("+--------------------+")

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    
    for row in range(4):
        for col in range(3):
            if grid[row][col] == " ":
                grid[row][col] = 0            
            if grid[row][col] == 0: #false if 0 anywhere in grid
                return False
            elif grid[row][col] == grid[row][col+1]: #to compare values to the right/left of each other
                return False
    for row in range(3):
        for col in range(4):
            if grid[row][col] == " ":
                grid[row][col] = 0
            if grid[row][col] == 0: #false if 0 anywhere in grid
                return False
            elif grid[row+1][col] == grid[row][col]: #to compare values to the top/bottom of each other
                return False
    return True #if not false from any of previous loops
    
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    
    for row in range(4):
        for col in range(4):
            if grid[row][col] == " ":
                grid[row][col] = 0
            if grid[row][col] == 32 or grid[row][col] >= 32:
                return True
    return False
    
def copy_grid (grid):
    """return a copy of the grid"""
    
    for i in range(4):
            gridcopy.append([" "] * 4) #blank new 4x4 grid    
    for row in range(4):
        for col in range(4):
            gridcopy[row][col] = grid[row][col] #copy corresponding entries from original grid to blank grid 
    return gridcopy
        
    
def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    
    for row in range (4):
        for col in range(4):
            if grid1[row][col] != grid2[row][col]: #check that all corresponding entries in the two grids are identical
                return False
    return True