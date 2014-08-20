#Dhriven Hamlall

import copy

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range (4):
        grid.append([0]*4)
        
#===============================================================================================

def print_grid(grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    
    pr_grid = copy.deepcopy(grid)#=================================grid manipulation using deep copy
    print("+--------------------+")
    for row in range(4):
        print("|",end="")
        for col in range(4):
            if pr_grid[row][col] == 0:#================================grid manipulation using deep copy
                pr_grid[row][col] = " "#=======================================grid manipulation using deep copy
            print("{0:<5}".format(pr_grid[row][col]),end="") 
        print("|")
    print("+--------------------+")
#=============================================================================================================


def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j+1]: #check if numbers next to each other are equal
                return False

    for i in range(3):
        for j in range(4):
            if grid[i][j] == grid[i+1][j]: #check if number below a number is equal
                return False    
              
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0: #check if the grid contains any 0
                return False
            
    return True
#==============================================================================================================================
def check_won(grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for row in range(4):
        for col in range(4):
            if grid[row][col] >=32:
                return True
    else:
        return False 
#=================================================================================================================================

def copy_grid(grid):
    """return a copy of the grid"""
    return copy.deepcopy(grid)  #basically makes a copy of the original grid
#=====================================================================================================================================


def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True
    else:
        return False