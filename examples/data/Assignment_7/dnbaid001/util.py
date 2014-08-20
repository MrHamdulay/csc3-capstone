#Assignment 7 - Question 2
#Module of utility functions to manipulate 2D array
#Aidan de Nobrega
#27/04/2014

#used in copy_grid function
import copy

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range (4):
        grid.append([0] * 4) #appends [0,0,0,0] 4 times

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for row in range(4):
        print("|", end = "")
        #inside box
        for col in range(4):
            if grid[row][col] == 0: #print zeroes and white space
                print("{:<5}".format(" "), end= "")#left justified, width = 5
            else:
                print("{:<5}".format(grid[row][col]), end= "")
        print("|", end = "")
        print()
    print("+--------------------+")

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    lost = True #flag
    for row in grid:
        #if there's a zero anywhere, game is not lost
        if 0 in row:
            lost = False
    for row in range(4):
        #checks right adjacent
        for col in range(3):
            if grid[row][col] == grid[row][col + 1]:
                lost = False
        #checks left adjacent
        for col in range(1, 3):
            if grid[row][col] == grid[row][col - 1]:
                lost = False
    #checks lower adjacent
    for row in range(3):
        for col in range(4):
            if grid[row][col] == grid[row + 1][col]:
                lost = False
    #checks upper adjacent
    for row in range(1, 3):
        for col in range(4):
            if grid[row][col] == grid[row - 1][col]:
                lost = False
    return lost

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    won = False #flag
    for row in grid:
        for col in row:
            if col >= 32: # win if any tile is equal to or greater than 32
                won = True
    return won                

def copy_grid (grid):
    """return a copy of the grid"""
    #need to be able to edit copy independently
    grid_copy = copy.deepcopy(grid) #copies without reference
    return grid_copy

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    equal = True #flag
    for row in range(4):
        for col in range(4):
            #if even one coord differs, grids are not equal
            if grid1[row][col] != grid2[row][col]:
                equal = False
    return equal
                