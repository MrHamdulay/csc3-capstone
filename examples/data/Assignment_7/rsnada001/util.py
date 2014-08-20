"""question 2 assignment 7
2048 game utility
Adam Rosendorff
02 May 2014"""
import copy
def create_grid(grid):
    """create a 4x4 grid"""
    inner = [0]*4
    for i in range(4):
        grid.append(inner[:])

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print('+--------------------+')
    for i in range(4):
        print('|',end='')
        for j in range(4):
            if grid[i][j] == 0:
                print(' '*5,end='')
            else:
                print('{:<5}'.format(grid[i][j]),end='')
        print('|')     
    print('+--------------------+')  
        
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    adjacent = False
    zero_value = False
    for i in range(4):       
        for j in range(4):
            if grid[i][j] == 0:
                zero_value = True
                break
    for i in range(3):
        for j in range(3):
            if grid[i][j] == grid[i][j+1]:
                adjacent = True
                break
            if grid[i][j] == grid[i+1][j]:
                adjacent = True
                break
    if not adjacent and not zero_value:
        return True
    return False

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in range(4):       
        for j in range(4):
            if grid[i][j] >= 32:
                return True
    return False

def copy_grid (grid):
    """return a copy of the grid"""
    return copy.deepcopy(grid)

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True
    return False
