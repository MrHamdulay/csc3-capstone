#Assignment 7
#Question 2
#Barry Su
#30 April 2014
#Module of utility functions to manipulate 2D arrays

def create_grid(grid):
    #create a 2D array of 4x4 grid
    for i in range(4):
        grid.append([0]*4)
    
def print_grid(grid):   
    #create grid inside a box with width 5 for each column
    print("+" + "-"*20 + "+")
    for row in range(4):
        print("|", end="")
        for col in range(4):
            if grid[row][col] == 0:
                grid[row][col] = " "
            print(grid[row][col],sep="",end=" "*(5-len(str(grid[row][col]))))           
        print("|")
    print("+" + "-"*20 + "+")
    
def check_lost(grid):
    #check to see if there are 0 values and adjacent values that are equal
    for row in range(4):
        for col in range(3):
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
            elif grid[row+1][col] == grid[row][col]:
                return False  
    return True

#Check to see if the value is >= 32
def check_won(grid):
    for row in range(4):
        for col in range(4):
            if grid[row][col] == " ":
                grid[row][col] = 0
            if (grid[row][col]) >= 32:
                return True
    return False

import copy    
def copy_grid(grid):
    #return a copy of the grid
    copyGrid = copy.deepcopy(grid)
    return copyGrid    

def grid_equal(grid1, grid2):
    #check to see if the two grids equal using Boolean
    if grid1 == grid2:
        return True
    else:
        return False
    