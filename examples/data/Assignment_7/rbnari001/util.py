"""2 may 2014
Ariel Rubin
manipulate 2-dimensional arrays of size 4x"""

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0]*4)
    return grid

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for i in range(4):
        print('|',end='')
        for j in range(4):
            if grid[i][j]==0:
                print("{:5}".format(' '),sep='',end='')
            else:
                print('{:<5}'.format(grid[i][j]),sep='',end='')
        print('|')
        
    print("+--------------------+")

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
   
    if not 0 in grid:
        for i in range(3):
            for j in range(3):
                    if grid[i][j]==grid[i+1][j] or grid[i][j]==grid[i][j+1]:
                        return False
        
        return True
    else:
        return False
    
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in range(4):
        for j in range(4):
            if grid[i][j]>=32:
                return True           
    return False
            
def copy_grid (grid):
    """return a copy of the grid"""
    newgrid=[]
    newgrid=create_grid(newgrid)
    for i in range(4):
        for j in range(4):
            newgrid[i][j]=grid[i][j]
    return newgrid

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    for i in range(4):
        for j in range(4):
            if not grid1[i][j] == grid2[i][j]:
                return False
    return True