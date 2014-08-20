def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0,0,0,0])

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for i in range(4):
        print("|",end='')
        for j in range(4):
            if(grid[i][j]==0):
                print("{:<5}".format(" "),end='')
            else:
                print("{:<5}".format(grid[i][j]),end='')
        print("|",end='')
        print()
    print("+--------------------+")

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for i in range(4):
        for j in range(4):
            if(grid[i][j]==0):
                return False
            if(j<3 and grid[i][j]==grid[i][j+1]):
                return False
            if(i<3 and grid[i][j]==grid[i+1][j]):
                return False
    return True
            
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in range(4):
        for j in range(4):
            if(grid[i][j]>=32):
                return True
    return False

def copy_grid (grid):
    """return a copy of the grid"""
    a=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(4):
        for j in range(4):
            a[i][j]=grid[i][j]
    return a

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if(grid1==grid2):
        return True
    else:
        return False


                