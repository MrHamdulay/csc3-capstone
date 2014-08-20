#Programme to create functions
#Joe Sutton
#28 April 2014

def create_grid (grid):
    """create a 4x4 grid"""
    for i in range (4):
        grid.append([0,0,0,0])
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for row in grid:
        print("|", end="")
        for cell in row:
            newcell="{0:<5}".format(cell)
            if cell==0:
                print("     ", end="")
            else:
                print(newcell, end="")
        print("|")
    print("+--------------------+")
    
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    checkspace=0 #create variable
    for row in grid:
        for value in row:
            if value==0:
                checkspace+=1
    
    checkadjacent=0 #create variable to see if a move is availible
    
    for row in range(3):
        for collumn in range(4):
            if grid[row][collumn]==grid[row+1][collumn]:
                checkadjacent+=1
    
    for row in range(4):
        for collumn in range(3):
            if grid[row][collumn]==grid[row][collumn+1]:
                checkadjacent+=1    
    
    if checkspace==0:
        if checkadjacent==0:
            return True
        else:
            return False
    else:
        return False
        
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    checkwon=0 #create variable
    for row in grid:
        for value in row:
            if value>=32:
                checkwon+=1
                
    if checkwon>0:
        return True
    else:
        return False

import copy

def copy_grid (grid):
    """return a copy of the grid"""
    copygrid=copy.deepcopy(grid)
    return copygrid

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    return grid1==grid2