"""Module for 2048 game
Dudley Mutero
5/1/14"""

def create_grid(grid):
    """create a 4x4 grid"""
    height = 4
    for i in range (height):
        grid.append ([0] * 4)  
    return grid

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    layout="{lay:<5}" # format of the way the grid is to be printed 
    for x in range (4):
        for y in range(6):
            if y==0 or y == 5:
                print ("|",end ="") #printing 1st postion of the grid its boarders
            elif grid[x][y-1] ==0:
                print (layout.format(lay=" "),end="") #deleting all zero terms in the grid
            else:
                print(layout.format(lay=grid[x][y-1]),end ="")
        print()#new line
    print("+--------------------+")

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for x in range (4):
        for y in range(4):
            if grid[x][y]==0:#Checking for zero term
                return False
    for i in range (1,4):
        for j in range (1,4):
            if (grid[i-1][j-1]==grid[i-1][j]) or (grid[i-1][j-1] ==grid[i][j-1]):#checking adjacent values on grid
                return False
    return True

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for a in range (4):
        for b in range (4):
            if grid[a][b]>=32:
                return True
    return False

def copy_grid (grid):
    """return a copy of the grid"""
    list2=[]
    for i in range(4):
        list2.append([grid[i][0],grid[i][1],grid[i][2],grid[i][3]])
    return list2

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1!=grid2:
        return False
    return True

            