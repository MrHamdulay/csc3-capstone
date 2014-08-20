#Util
#Richard van Gysen
#29 April 2014

#create grid
import copy
def create_grid(grid):
    """create a 4x4 grid"""
    for i in range (4):
        grid.append ([0]*4)
    return grid
#print grid
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for i in grid:
        print('|', end='')
        for j in i:
            j = str(j)
            if j == '0':
                print(' '.ljust(5), end = '')
            else:
                print(j.ljust(5),end = '')
        print('|')
    print("+--------------------+")
#check if a value in grid is 0 or adjascent values are equal
def check_lost (grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j]==0:
                return False
            else: continue   
    for i in range(4):
        for j in range(3):
            if grid[i][j]==grid[i][j+1]:
                return False 
            else:
                continue
    for i in range(3):
        for j in range(4):
            if grid[i][j]==grid[i+1][j]:
                return False
            else:
                continue
    return True
#check if a value is more than 32
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in range(4):
            for j in range(4):
                if grid[i][j]>= 32:
                    return True
    return False
#return a copy of the grid
def copy_grid (grid):
    """return a copy of the grid"""
    copygrid = copy.deepcopy(grid)
    return copygrid
#check if two grids are equal
def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    for i in range(4):
            for j in range(4):
                if grid1[i][j] != grid2[i][j]:
                    return False
    return True 