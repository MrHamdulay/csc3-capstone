# module of utility functions (called util.py) to manipulate 2-dimensional arrays of size 4x4.
# Mulisa Badugela
# 1 May 2014
import copy
def create_grid(grid): # create a 4x4 grid
    height=4
    
    for i in range(height):
        grid.append([0]*4)
    return grid

def print_grid (grid): # print out a 4x4 grid in 5-width columns within a box
    width=5
    print("+"+"-"*(4*width)+"+")
    
    for i in range(4):
        print("|",end='')
        for j in range(4):
            if grid[i][j] == 0:
                print("{0:<5}".format(" "),end="")
            else:
                print("{0:<5}".format(grid[i][j]),end="")
                
        print("|")
        
    print("+"+"-"*(4*width)+"+")
    
def check_lost (grid): # return True if there are no 0 values and no adjacent values that are equal; otherwise False
    for i in range(4):
	    for j in range(4):
		    if grid[i][j] == 0:
			    return False
		    if j>0:
			    if grid[i][j] == grid[i][j-1]:
				    return False
		    if i>0:
			    if grid[i][j] == grid[i-1][j]:
				    return False
    return True

def check_won (grid): # return True if a value>=32 is found in the grid; otherwise False
    for i in range(4):
        for j in range(4):
            if grid[i][j] >= 32:
                return True
    else:
        return False
    
def copy_grid (grid): # return a copy of the grid
    grid_copy=copy.deepcopy(grid)
    return grid_copy

def grid_equal (grid1, grid2): # check if 2 grids are equal - return boolean value
    if grid1 == grid2:
        return True
    else:
        return False    
