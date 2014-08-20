# util.py
# Name: Buhlebezwe
# Student Number: MBLBUH001
# Date: 30 April 2014

def create_grid(grid):
    """create a 4x4 grid"""
    height = 4
    for i in range (height):
        grid.append ([0] * 4)                                       #fill entries of grid with 0
        
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+"+"-"*20+"+")                                           #print top of border

    for i in range(4):
        print("|",end="")                                           #print left side of border
        for j in range(4):
            if grid[i][j] == 0:
                print("{:<5}".format(" "), end="")                  #print space character justified left in a column width of 5
            else:
                print("{:<5}".format(grid[i][j]),end="")            #print entry in grid justified right in a column width of 5
        print("|",end="")                                           #print right side of border
        print()
    print("+"+"-"*20+"+")                                           #print bottom of border
    
    
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:                                     
                return False                                        #return False if gird has entries with value 0
        for k in range(3):   
            if grid[i][k] == grid[i][k+1]:
                return False                                        #return False if grid has adjacent values equal
            elif grid[k][i] == grid[k+1][i]:
                return False                                        #return False if grid has adjacent values equal
    return True

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in range(4):
        for j in range(4):
            if grid[i][j]>=32:
                return True                                         #return True if a value>=32 is found in the grid; otherwise False
    return False

def copy_grid (grid):
    """return a copy of the grid"""
    import copy
    
    new_grid = copy.deepcopy(grid)
    return new_grid                                                 #return new_grid, a copy of grid

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True                                                 #return True if two grids are equal
    return False