
"""util module
Sthabiso Andile Gazu
April 2014"""
import copy
def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0]*4)
        

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+"+"-"*(20)+"+",end="")
    print()
    for i in range(4):
        print("|",end="")
        for j in range(4):
            if grid[i][j] ==0:
                print("{:<5}".format(" "),end="")
            else:    
                print("{:<5}".format(grid[i][j]),end="")   
        print("|",end="")
        print()
    print("+"+"-"*(20)+"+",end="")
    print()
    
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for i in range(4):
        if 0 in grid[i]:
            return False
        else:
            for j in range(4):
                if (j+1)<4 and (i+1)<4 :
                    if grid[i][j]==grid[i][j+1] or grid[i][j]==grid[i+1][j]: 
                        return False
    return True

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in range(4):
        for j in range(4):
            if grid[i][j]>=32:
                return True
    return False
                
            

def copy_grid (grid):
    """return a copy of the grid"""
    copy_grid=copy.deepcopy(grid)
    return copy_grid

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1==grid2:
        return True
    return False    
    