
def create_grid (grid):
    for i in range(4):
        grid.append([0]*4)
    
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for row in [0,1,2,3]:
        print("|", end="")
        for col in [0,1,2,3]:
            if grid[row][col] == 0:
                print("     ", end="")
            else: print(str(grid[row][col]) + " "*(5-(len(str(grid[row][col])))), end="")
        print("|")
    print("+--------------------+")
    
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    flag = True
    for row in [0,1,2,3]:
        for col in [0,1,2,3]:
            if grid[row][col] == 0: flag = False
            if row != 3:
                if grid[row][col] == grid[row+1][col]: flag = False
            if col != 3:
                if grid[row][col] == grid[row][col+1]: flag = False
    return flag

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    flag = False
    for row in [0,1,2,3]:
        for col in [0,1,2,3]:
            if grid[row][col] >= 32: flag = True
    return flag

def copy_grid (grid):
    """return a copy of the grid"""
    newgrid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for row in [0,1,2,3]:
        for col in [0,1,2,3]:
            newgrid[row][col] = grid[row][col]
    return newgrid

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2: return True
    else:  return False