"""Assignment 7 question 2
Ross van der Heyde VHYROS001
30 April 2014"""

import copy

def create_grid(grid): #works
    """create a 4x4 grid"""
    for i in range (4):
        grid.append([0]*4)
        
def print_grid (grid): #works
    """print out a 4x4 grid in 5-width columns within a box"""
    output = "{:<5}"
    print("+--------------------+")
    for i in range (4):#rows
        print("|",end = "")
        for j in range(4):#columns
            if grid[i][j]!= 0:
                print(output.format(grid[i][j]),end="")
            else:
                print(output.format(""),end="")
        print("|")        
    print("+--------------------+")

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    lost = True
    for i in range (4): # rows
        for j in range(4):#columns
            if grid[i][j] ==0:# check if 0
                lost = False
            
    for i in range (3):
        for j in range (3):
            # check if adjacent values are equal
            if grid[i][j] == grid[i][j+1]:# go through rows, compare to next block
                lost = False
                
            if grid [j][i] == grid[j+1][i]:# go through cols, compare to next one
                lost = False
    return lost

def check_won (grid): #works
    """return True if a value>=32 is found in the grid; otherwise False"""
    won = False
    for i in range(4):
        for j in range(4):    
            if grid [i][j] >= 32:
                won = True
    return won
        
def copy_grid (grid):
    """return a copy of the grid"""
    gridCopy = copy.deepcopy(grid)
    return gridCopy

def grid_equal (grid1, grid2): #Works
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True
    else:
        return False
    
#+--------------------+
#|2         2         |
#|     4         8    |
#|     16        128  |
#|2    2    2    2    |
#+--------------------+    
# 17 
