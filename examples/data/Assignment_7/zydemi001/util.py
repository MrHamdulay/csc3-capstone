#A module of utility functions to manipulate 2-dimensional arrays of size 4x4
#Author: Emiel Zyde
#Date: 27 April 2014

def create_grid(grid):
    """ create a 4x4 grid """
    
    #make a 4x4 grid
    for i in range(4):
        grid.append([0] * 4)
    return grid 


def print_grid(grid):
    """ print out a 4x4 grid in 5-width columns within a box"""
    
    #print the first row
    print("+", "-" * 20, "+", sep = "")
    
    #print out the grid 
    for i in range(4):
        print("|", end = "")
        for j in range(4):
            gap = len(str(grid[i][j])) 
            if grid[i][j] == 0:   #this ensures than any 0s are replaced by spaces 
                grid[i][j] = " "
            print(grid[i][j], end = " "*(5-gap))
        print("|")
        
    #print the last row
    print("+", "-" * 20, "+", sep = "")

def check_lost(grid):
    """ return True if there are no 0 values and no adjacent values that are equal, otherwise False """ 
    
    for col in range(3):
        for row in range(4):
            if grid[row][col] == " ":
                grid[row][col] = 0
            if grid[row][col] == 0:
                return False
            elif grid[row][col] == grid[row][col+1]:
                return False 
    
    for row in range(3):
        for col in range(4):
            if grid[row][col] == " ":
                grid[row][col] = 0
            if grid[row][col] == 0:
                return False
            elif grid[row][col] == grid[row+1][col]:
                return False
    
    return True

def check_won(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] == " ":
                grid[i][j] = 0
            if grid[i][j] >= 32:
                return True
            
    return False 


def copy_grid(grid):
    """ return a copy of the grid """
    #initalize a copy of the grid that is empty
    copied_grid = []
    
    #loop to the grid and add values to the copy of the grid 
    for i in range(4):
        copied_grid.append(grid[i][:])

    return copied_grid
   

def grid_equal(grid1,grid2):
    """chick if 2 grids are equal - return boolean value"""
    for i in range(4):
        for j in range(4):
            if not grid1[i][j] == grid2[i][j]:
                return False
    return True 