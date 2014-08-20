#Assignment 7,Question 2
#Avreyna Kistensamy
#27 April 2014

import copy
grid= []
def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0] * 4)
        
def print_grid(grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    pr_grid = copy.deepcopy(grid)
    print("+--------------------+")
    for row in range(4):
        print("|",end="")
        for col in range(4):
            if pr_grid[row][col] == 0:
                pr_grid[row][col] = " "
            print("{0:<5}".format(pr_grid[row][col]),end="") #5 width 
        print("|")
    print("+--------------------+")
    
def check_lost(grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for row in range(4):
        for col in range(4):
            #Multiple ifs to check all sides
            if col > 0: #to avoid out of range index
                if grid[row][col] == grid[row][col-1]:
                    return False 
            if row >0:
                if grid[row][col] == grid[row-1][col]:
                    return False
            if col < 3:
                    if grid[row][col] == grid[row][col+1]:
                        return False
            if row < 3:
                if grid[row][col] == grid[row+1][col]:
                    return False
            else: 
                return True

   
            
def check_won(grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for row in range(4):
        for col in range(4):
            if type(grid[row][col]) == int:
                if grid[row][col] >= 32:
                    return True
    else:
        return False #indent with 1st loop
    
def copy_grid(grid):
    """return a copy of the grid"""
    return copy.deepcopy(grid)    #checked online for this
    
def grid_equal(grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True
    else:
        return False