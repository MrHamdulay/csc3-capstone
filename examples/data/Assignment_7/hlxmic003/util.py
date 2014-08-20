# Michaela Heale
# Assignment 7 Question 2

def create_grid(grid):
    """create a 4x4 grid"""
    if not grid:
        for d in range(0,4):
            grid.append([0,0,0,0])
    box = "+--------------------+"
    for no in grid:
        box += "\n|"
        for val in no:
            if val == 0:
                box += "     "
            else:
                box += str(val) + (" "*(5 - len(str(val))))
        box += "|"
    box += "\n+--------------------+"
    return box
        

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    tote = create_grid(grid)
    print(tote)
    

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    zeroes = True
    for no in grid:
        for val in no:
            if val == 0:
                zeroes = False
                break
    for z in range(1,4):
        for x in range(0,4):
            if grid[z-1][x] == grid[z][x]:
                zeroes = False
                break
    return zeroes
                

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    boole = False
    for no in grid:
        for val in no:
            if val >= 32:
                boole = True
                break
    return boole

def copy_grid (grid):
    """return a copy of the grid"""
    return grid    
    

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    equal = False
    if grid1 == grid2:
        equal = True
    return equal