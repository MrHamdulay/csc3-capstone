"""Luvo Fokazi
02/05/2014
"""
def create_grid(grid): #creates 4 by 4 grid/matrix
    for i in range(4):
        grid.append([0]*4)
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+","-"*20,"+",sep="")
    for row in range(4):
        print("|",end="")
        for col in range(4):
            if grid[row][col]!=0:
                print("{0:<5}".format(grid[row][col]),end="")
            else:
                print("{0:<5}".format(""),end="")
        print("|")
    print("+","-"*20,"+",sep="")
def check_lost (grid):
    flag=True
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for row in range(4):
            for col in range(4):
                if grid[row][col]==0:
                    flag=False
                    break
                else:
                    continue
    for row in range(1,3,1):
        for col in range(1,3,1):
            if grid[row][col]==grid[row-1][col] or grid[row+1][col]==grid[row][col] or grid[row][col]==grid[row][col-1] or grid[row][col]==grid[row][col+1]:
                flag=False
                break
    return flag
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for row in range(4):
            for col in range(4):
                if grid[row][col]>=32:
                    return True
    return False           
def copy_grid (grid):
    """return a copy of the grid"""
    gridCopy=[[0 for x in range(4)] for x in range(4)]
    for i in range(4):
        for j in range(4):
            gridCopy[i][j]=grid[i][j]
    return gridCopy
def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    for row in range(4):
                for col in range(4):
                    if grid1[row][col]!=grid2[row][col]:
                        return False
    return True
    