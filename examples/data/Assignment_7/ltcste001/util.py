#stephanie latchmanan
#utility functions to manipulate 2D arrays
#27 April 2014

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0]*4)
    return grid

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+", "-"*20, "+", sep = "")
    for i in grid:
                print("|", end="")
                for j in i:
                    if j != 0:
                            print("{0:<5}".format(j), end="")
                    else:
                        print("{0:<5}".format(" "), end="")
                print("|")
    print("+", "-"*20, "+", sep = "") 

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for i in range(3):
        for j in range(3):
            if grid[i][j]==grid[i+1][j] or grid[i][j]==grid[i][j+1] or grid[i][j]==0 :
                return False
    else:
        return True

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in grid:
        for j in i:
            if j >= 32:
                return True
    else: 
        return False

def copy_grid (grid):
    """return a copy of the grid"""
    test_grid = []
    for j in range(4):
        grd = []
        for i in range(4):
            grd.append(grid[j][i])
        test_grid.append(grd)
    return test_grid

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1==grid2:
        return True
    else:
        return False