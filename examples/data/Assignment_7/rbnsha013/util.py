"""Utility functions
Shane Robinson
27 April 2014"""

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0]*4)

def print_grid(grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for i in grid:
        for j in range(4):
            if i[j]!=0:
                if j==0:
                    print("|", "{:" "<5}".format(i[j]), sep="", end="")
                elif j<3 and j>0:
                    print("{:" "<5}".format(i[j]), sep="", end="")
                elif j==3:
                    print("{:" "<5}".format(i[j]), "|", sep="", end="")
            elif i[j]==0:
                if j==0:
                    print("|", "{:" "<5}".format(" "), sep="", end="")
                elif j<3 and j>0:
                    print("{:" "<5}".format(" "), sep="", end="")
                elif j==3:
                    print("{:" "<5}".format(" "), "|", sep="", end="")
        print()
    print("+--------------------+")

def check_lost(grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    #use index of arrays to check if values are equal surrounding a value
    for i in range(4):
        for j in range(4):
            if grid[i][j]==0:
                return False
            elif i==0 or i==1 or i==2:
                if j==0 or j==1 or j==2:
                    if grid[i][j]==grid[i][j+1] or grid[i][j]==grid[i+1][j]: #check on right and below
                        return False
                elif j==3:
                    if grid[i][j]==grid[i+1][j]: #check below
                        return False
            elif i==3:
                if j==0 or j==1 or j==2:
                    if grid[i][j]==grid[i][j+1]: #check on right
                        return False
                if j==3:
                    continue
    else:
        return True

def check_won(grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in range(4):
        for j in range(4):
            check = grid[i][j]
            if check>=32:
                return True
    else:
        return False

def copy_grid(grid):
    """return a copy of the grid"""
    new_grid = []
    for k in range(4):
        new_grid.append([0]*4)
    for i in range(4):
        for n in range(4):
            j = grid[i]
            l = j[n]
            new_grid[i][n] = l
    return new_grid

def grid_equal(grid1, grid2):
    for i in range(4):
        for j in range(4):
            if grid1[i][j]==grid2[i][j]:
                continue
            else:
                return False
    else:
        return True