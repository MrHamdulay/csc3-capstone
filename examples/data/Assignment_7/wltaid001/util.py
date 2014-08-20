"""Aiden Walton
WLTAID001
Question 2 - Assignment 7"""
def create_grid (grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0]*4)

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+","-"*20,"+",sep="")
    for row in range(4):
        print("|",end="")
        for col in range(4):
            if grid[row][col]==0:
                print("{0:<5}".format(""),end="")
            else:
                print("{0:<5}".format(grid[row][col]),end="")
        print("|")
    print("+","-"*20,"+",sep="")
    

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    x=0.1
    x1=0.1
    y=True
    for row in range(4):
        x=0.1
        x1=0.1
        for col in range(4):
            if row<=2:
                if grid[row][col]==grid[row+1][col]:
                    y=False
            if grid[row][col]==x or grid[row][col]==0:
                y=False
            elif x!=grid[row][col]:
                x=grid[row][col]
                continue
            
            
    return y
            
            

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    x=False
    for row in range(4):
        for col in range(4):
            if grid[row][col]>=32:
                x=True
    return x
            

def copy_grid (grid):
    """return a copy of the grid"""
    new_grid=[]
    for row in range(4):
        new_grid.append([0]*4)
    for row in range(4):
        for col in range(4):
            new_grid[row][col]=grid[row][col]
    return new_grid

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    x=True
    for row in range(4):
        for col in range(4):
            if grid1[row][col]==grid2[row][col]:
                continue
            elif not grid1[row][col]==grid2[row][col]:
                x=False
                break
    return x