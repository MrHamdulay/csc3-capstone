global grid
grid =list()

def create_grid(grid):
    """create a 4x4 grid"""  
    for i in range (4):
        tempgrid=[]
        for j in range(4):
            tempgrid.append(0)
        grid.append(tempgrid)

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for i in range(4):
        print('|',end='')
        for j in grid[i]:
            if j ==0:
                print("{0:<5}".format(" "),end="")
            else:
                print("{0:<5}".format(j),end="")
        print('|')
    print("+--------------------+")

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for i in range (4):
        #Look for zero values in grid and return false if found.
        for num in range(4):
            if grid[i][num] ==0:
                return False
        #Look for equal horizontally adjacent values and return false if found.
        for num in range(3):
            if grid[i][num] ==grid[i][num+1]:
                return False
    #Look for equal vertically 
    for i in range (3):
        for num in range(4):
            if grid[i][num] == grid[i+1][num]:
                return False
    return True
    
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in grid:
        for a in i:
            if a >= 32:
                return True
    return False

def copy_grid (grid):
    """return a copy of the grid"""
    new_grid= []
    for i in grid:
        new_row=[]
        for a in i:
            new_row.append(a)
        new_grid.append(new_row)
    return new_grid

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    for i in range(4):
        for num in range(4):
            if grid1[i][num] != grid2[i][num]:
                return False
    return True
            