"""Assignment 7 Question 2 utility functions to manipulate a 2-d array
joshua wort
29 april 2014"""

def create_grid(grid):
    """create a 4x4 grid"""
    
    for i in range(4):
        grid.append([0]*4)
    return grid

def print_grid(grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    #print first row
    print("+--------------------+")
    #print middle 4 rows with inputted numbers
    for row in range(4):
        print("|", end="")
        for col in range(4):
            gap=len(str(grid[row][col]))
            if grid[row][col]==0: #checks if any zeros and replaces them with empty strings 
                grid[row][col]=" "
            print(grid[row][col],end=" "* (5-gap))
        print("|")
    #print last row
    print("+--------------------+")

def check_lost(grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    #checks if there are any zeros or adjacent values equal on the left or right and returns False
    for col in range(3):
        for row in range(4):
            if grid[row][col]==" ":
                grid[row][col]=0
            if grid[row][col]==0:
                return False
            elif grid[row][col]==grid[row][col+1]:
                return False
    #checks if there are any zeros or adjacent values up or down equal and returns False
    for row in range(3):
        for col in range(4):
            if grid[row][col]==" ":
                grid[row][col]=0
            if grid[row][col]==0:
                return False
            elif grid[row][col]==grid[row+1][col]:
                return False
    
    return True
        
    

def check_won(grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for row in range(4):
        for col in range(4):
            if grid[row][col]==" ":
                grid[row][col]=0
            if grid[row][col]>=32:
                    return True
    return False

def copy_grid(grid):
    """return a copy of the grid"""
    #create a new empty grid
    copied_grid=[]
    #copies the values of the other grid into the new grid
    for row in range(4):
            copied_grid.append(grid[row][:])
    
    return copied_grid

def grid_equal(grid1,grid2):
    """check if 2 grids are equal - return boolean value"""
    for row in range(4):
        for col in range(4):
            if grid1[row][col]!=grid2[row][col]:
                return False
    return True
            
    
    