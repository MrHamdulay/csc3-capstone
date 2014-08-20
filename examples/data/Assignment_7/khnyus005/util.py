'''
Created on 01 May 2014
module of utilities
@author: Yusuf Khan
KHNYUS005
'''
global grid
grid = []

def create_grid(grid):
    """create a 4x4 grid"""
    for c in range(4):
        x = []
        for t in range(4):
            x.append(0)
        grid.append(x)#uses nested loop to create array

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for h in range(4):
        print('|',end='')
        for v in grid[h]:
            if v == 0:
                print(' '*5,end='')#5 blanks if 0
            else:#format in columns of width 5
                print("{0:<5}".format(v),end='')
        print('|')
    print("+--------------------+")

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    lost = True
    for h in range(4):
        for v in grid[h]:
            if v == 0:
                lost = False
                break#checks for 0 values
            
    for r in range (3):
        for c in range (3):
            if grid[r][c]==grid[r+1][c]:
                lost = False
                break
            if grid[r][c]==grid[r][c+1]:
                lost = False
                break#checks for equal adjacent values
    
    return lost

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    won = False
    for h in range(4):
        for v in grid[h]:
            if v >= 32:
                won = True
                break
    return won

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1==grid2:
        return True
    else:
        return False
    
'''def copy_grid (grid):
    """return a copy of the grid"""
    new_grid = grid
    return new_grid'''#why doesn't this work?!

def copy_grid(grid):
    """Program that returns a copy of the grid."""
    new_grid = []
    for i in grid:
        new_row = []
        for c in i:#iterate through grid to manually copy each variable
            new_row.append(c)
        new_grid.append(new_row)
    return new_grid