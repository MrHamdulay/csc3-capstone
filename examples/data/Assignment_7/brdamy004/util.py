# Assignment 7 question 2
# Amy Brodie
# 1/05/2014

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0,0,0,0])
    
    
def print_grid(grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+","-"*20,"+",sep="")
    for r in range(4):
        print("|",end="")
        for c in range(4):
            if grid[r][c] == 0:
                print("{0:<5}".format(" "),end="")
            else:
                print("{0:<5}".format(grid[r][c]),end="")
        print("|","\n",sep="",end="")
    print("+","-"*20,"+",sep="")
    
    
def check_lost(grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    flag_0 = True
    flag_a = True
    # check if there are zeros in grid
    for r in range(4):
        for c in range(4):
            if grid[r][c] == 0:
                flag_0 = False
                break
    # check for adjacent values that are equal
    for r in range(3):
        for c in range(3):
            if grid[r][c] == grid[r+1][c]:
                flag_a = False
                break
            if grid[r][c] == grid[r][c+1]:
                flag_a = False
                break
    if flag_a and flag_0:
        return True
    else:
        return False
            

def check_won(grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for r in range(4):
        for c in range(4):
            if grid[r][c] >= 32:
                return True
    return False

    
def copy_grid(grid):
    """return a copy of the grid"""
    copygrid = []
    create_grid(copygrid)
    for r in range(4):
        for c in range(4):
            copygrid[r][c] = grid[r][c]
    return copygrid


def grid_equal(grid1,grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True
    else:
        return False