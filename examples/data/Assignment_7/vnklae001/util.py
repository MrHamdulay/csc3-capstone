# Assignment 7 - Question 2
# A program containing utility functions that manipulate 2-dimensional arrays of size 4x4
# Written by: Laene van Niekerk
# VNKLAE001

def create_grid(grid):      # Create a 4x4 grid
    for i in range(4):
        grid.append([0]*4)
    return grid

def print_grid (grid):      # Print out a 4x4 grid in 5-width columns within a box
    print("+--------------------+")
    for row in range(4):
        print("|", end="")
        for col in range(4):
            if grid[row][col] == 0:
                print("{0:<5}".format(" "), end="")
            else:
                print("{0:<5}".format(grid[row][col]), end="")
        print("|")
    print("+--------------------+")    

def check_lost (grid):      # Return True if there are no 0 values and no adjacent values that are equal; otherwise False (i.e. the game is lost when the numbers next to each other are not equal to each other)
    for row in range(4):
        for col in range(4):
            if grid[row][col] == 0:
                return False
            elif col+1 < 4 and grid[row][col] == grid[row][col+1]:
                return False
            elif row+1 < 4 and grid[row][col] == grid[row+1][col]:
                return False
    return True

def check_won (grid):       # Return True if a value >= 32 is found in the grid; otherwise False (i.e. game is won when there is a number that is equal to or higher than 32)
    for row in range(4):
        for col in range(4):
            if grid[row][col] >= 32:
                return True
    return False

def copy_grid (grid):       # Return a copy of the grid
    #from copy import deepcopy
    new_grid = []
    for row in range(4):
        temp = []
        for col in range(4):
            temp.append(grid[row][col])
        new_grid.append(temp)
    return new_grid

def grid_equal (grid1, grid2):      # Check if 2 grids are equal - return Boolean value
    if grid1 == grid2:
        return True
    return False