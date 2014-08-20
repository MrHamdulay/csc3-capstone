""" Utility program to create, and manipulate 4x4 array grids
 Author: Julius Stopforth (STPJUL004)
 Date: 2014-04-29 """

def create_grid(grid):
    """ create a 4x4 grid """
    for i in range(4):
        grid.append([0]*4)
    return grid

def print_grid(grid):
    """ print out 4x4 grid with 5-width columns within a box """
    print("+",'-'*len(grid[0]*5),'+',sep='')# top line of box
    for i in range(len(grid)):
        grid_str = ''
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                grid_str += "{:<5}".format(' ')
            else:
                grid_str += "{:<5}".format(grid[i][j])#append a 5-width column
        print('|',grid_str,'|',sep='')
    print("+",'-'*len(grid[0]*5),'+',sep='')# bottom line of box

def check_lost(grid):
    """ Return True if there are no 0 values and no adjacent values that are equal; otherwise False """
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                return False
            elif i+1 < len(grid):
                if grid[i][j] == grid[i+1][j]:
                    return False
            elif j+1 < len(grid[i]):
                if grid[i][j] == grid[i][j+1]:
                    return False            
    return True

def check_won(grid):
    """ Return True if a value>=32 is found in the grid; otherwise False """
    for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] >= 32:
                    return True    
    return False

def copy_grid(grid):
    """ Return a copy of the grid """
    new_grid = []
    new_grid = create_grid(new_grid)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            new_grid[i][j] = grid[i][j]
    return new_grid

def grid_equal(grid1, grid2):
    """ Check if 2 grids are equal - return boolean value """
    for i in range(len(grid1)):
            for j in range(len(grid1[i])):
                if grid1[i][j] != grid2[i][j]:
                    return False
    return True