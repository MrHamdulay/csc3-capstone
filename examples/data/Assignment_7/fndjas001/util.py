"""A module of functions used to manipulate a 4x4 grid
Jason Findlay
30/04/2014"""

"""Create a 4x4 grid"""
def create_grid(grid):
    for i in range(4):
        grid.append([0]*4)

"""Print out a 4x4 grid in 5-width columns within a box"""
def print_grid(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j]==0:
                grid[i][j]=""
    print("+--------------------+")
    for i in range(4):
        print("|{0:<5}{1:<5}{2:<5}{3:<5}|".format(grid[i][0],grid[i][1],grid[i][2],grid[i][3]))
    print("+--------------------+")

"""Returns True if there are no 0 values and there are no adjacent like values.
Otherwise returns False"""
def check_lost(grid):
    lost=True
    for i in range(3):
        for j in range(4):
            if grid[i][j]==grid[i+1][j] or grid[i][j]=="":
                return False
    for i in range(4):
        for j in range(3):
            if grid[i][j]==grid[i][j+1] or grid[i][j]=="":
                return False
    return True

"""Returns True if a value>32 is found in the grid. Otherwise returns False"""
def check_won(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j]>=32:
                return True
    return False

"""Returns a copy of the grid"""
def copy_grid(grid):
    grid2=[]
    create_grid(grid2)
    for i in range(4):
        for j in range(4):
            grid2[i][j]=grid[i][j]
    return grid2

"""Checks if two grids are equal-returns boolean value"""
def grid_equal(grid1,grid2):
    for i in range(4):
        for j in range(4):
            if grid1[i][j]!=grid2[i][j]:
                return False
    return True
