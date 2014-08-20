# Kate Bell
# BLLKAT005
# 28 April 2014 

def create_grid(grid):
    """create a 4x4 grid"""
    height = 4
    width = 4
    for i in range (height):
        grid.append ([0] * width)    

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for row in range (4):
        print("|",end="")
        for column in range (4):
            if grid[row][column] == 0:
                print("     ",end="")
            else:
                print(grid[row][column],end=" "*(5-len(str(grid[row][column]))))
        print("|",end="\n")  
    print("+--------------------+") 

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    # Loop through to see if any horizontally adjacent values are equal and no 0 values
    for row in range (4):
        for column in range (3):
            # If there's a 0 value, return False
            if grid[row][column]== 0:    
                return False
            # if the value is equal to the value to its right, return False
            if grid [row][column] == grid[row][column+1]:
                return False
    # Loop through to see if any vertically adjacent values are equal     
    for row in range (3):
        for column in range (4):
            # if the value is equal to the vlaue beneath it, check = False
            if grid[row][column] == grid[row+1][column]:
                return False        
    return True

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    check = False
    for row in range (4):
        for column in range (4):
            if grid[row][column] >= 32:
                check = True
    return check

def copy_grid (grid):
    """return a copy of the grid"""
    #Create empty grid
    test_grid = []
    for i in range (4):
        test_grid.append ([0] * 4)    
    # Populate grid with values from grid passed to function    
    for row in range (4):
        for column in range (4):
            test_grid[row][column]=grid[row][column]
    return test_grid

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    for row in range (4):
        for column in range (4):
            if not grid1[row][column]==grid2[row][column]:
                return False
    return True