#Description: Functions used for question 2 and the 2048 game
#Name: Paul Roux RXXPAU008
#Date: 01 May 2014

import copy

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0,0,0,0])
    

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for i in grid:
        print("|",end='')
        for j in i:
            if j == 0: print("     ",end = '')
            else:print(str(j)+(" "*(5-len(str(j)))),end = '')
        print("|")
    print("+--------------------+")
            

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for i in grid:
        for j in i:
            if j == 0: return False
    
    #Checks each adjacent value next to the specified entry    
    for i in range(4):
        for j in range(4):
                try: 
                    if grid[i][j]==grid[i+1][j]:return False
                except:
                    try:
                        if grid[i][j]==grid[i-1][j]:return False
                    except:
                        try:
                            if grid[i][j]==grid[i][j+1]:return False
                        except:
                            try:
                                if grid[i][j]==grid[i][j-1]:return False
                            except:m=1
       
    return True

def check_won (grid):
    """returns True if a value>=32 is found in the grid; otherwise False"""
    for i in grid:
        for j in i:
            if j >= 32:
                return True
    return False

def copy_grid (grid):
    """returns a copy of the grid"""
    grid_copy = copy.deepcopy(grid)
    return grid_copy

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    #Checks the values to see if a value in one list is the same in a corresponding index of another list
    for i in range(4):
        for j in range(4):
            if grid1[i][j]!=grid2[i][j]: return False
    return True
