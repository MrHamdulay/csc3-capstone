# a module of utility functions (called util.py) to manipulate 2-dimensional arrays of size 4x4
# Budeli Rendani
# BDLREN001
# 29/04/2014

import copy
# A function to create a 4x4 grid
def create_grid(grid): # defining funtion
    height=4 # Setting the height of the grid to be 4
    for i in range(height):
        grid.append([0]*4) # appending the 0 values into the grid
    return grid

# print out a 4x4 grid in 5-width columns within a box
def print_grid(grid):
    breadth=20 # Setting the the variable breadth to be 20
    height=4 # Setting the variable of height to be 4 
    c=' ' # Creating a variable of an empty string for the location of a zero
    print('+','-'*breadth,'+', sep='') # printing the borders of the grid
    for i in range(height):
        print('|', end="")
        for j in range(height): # looping through the grid to check the presence of 0 and either print a 0 or the equavalent value
            if grid[i][j] == 0:
                print("{:<5}".format(c), end="") # printing out spaces left aligned with a spacing of 5
            else:
                print("{:<5}".format(grid[i][j]), end="") # printing out values left aligned with a spacing of 5
        print('|', end="")
        print()
    print('+','-'*breadth,'+', sep='') # Printing the border of the grid

# return True if there are no 0 values and no adjacent values that are equal; otherwise False
def check_lost (grid):
    for i in range(3): # Using nested loop to loop also within the list inside the list
        for j in range(3):
            if grid[i][j] == 0: #if the number in the position of the grid is 0 it must return falls
                return False
            elif grid[i][j] == grid[i][j+1]: #if the value in the next position is equal to the value in the current position it must return false
                return False
            elif grid[i][j] == grid[i+1][j]: #if the value in the position belowa is equal to the value in the current position it must return false
                return False
    return True # return true when either of the conditions is met

# return True if a value>=32 is found in the grid; otherwise False
def check_won(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j]>=32: # return true when the value in the grid is greater or equal to 32
                return True
    return False # return false if condition not met

# return a copy of the grid
def copy_grid (grid):
    new_copy=[] # Creating an empty string for a copy of a new grid
    height=4
    for i in range(height): # creating a copy of the current grid
        new_copy.append([" "]*4)
        for j in range(height):
            new_copy[i][j]=grid[i][j]
    return new_copy # return the new grid
    
# check if 2 grids are equal - return boolean value
def grid_equal(grid1,grid2):
    height=4 # setting height of grid to be 4
    for i in range(height):
        for j in range(height): 
            if grid1[i][j] != grid2[i][j]: # return false if grid 1 is not equal to grid 2
                return False
    return True # if condition not met, return true

