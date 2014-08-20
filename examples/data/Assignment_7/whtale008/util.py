""" util grid program
alexander Whiting
30 april 2014"""


import copy



def create_grid(grid):
    """create a 4x4 grid"""
    
    for i in range(0,4):
        grid.append([0]*4)
    
    
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+","-"*20,"+",sep="")
    for i in grid:
        line = ""
        for x in i:
            if x == 0:
                line = line + " "*5
            else:    
                line =line+ str(x) +" "*(5-len(str(x)))
        print("|",line,"|",sep="")
    print("+","-"*20,"+",sep="")
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    check = True
    for y in range(0,3):
        for x in range(0,3):
            if grid[y][x] == 0 or grid [y][x+1]==0 or grid[y+1][x] == 0:
                check = False
                break
            elif grid[y][x] == grid[y][x+1] or grid[y][x] == grid[y+1][x]:
                check = False
                break
    return check
    
    
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    
    check = False
    for y in grid:
        for x in y:
            if x >= 32:
                check = True
                break
    return check

def copy_grid (grid):
    """return a copy of the grid"""
    
    new_grid = copy.deepcopy(grid) # found a library that deep copies without having to use lists
    return new_grid

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    check =False
    
    if grid1 == grid2:
        check = True
    
    return check