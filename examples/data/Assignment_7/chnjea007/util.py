# assignment 7 question 2
import copy
grid = []
def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0,0,0,0])
    return grid 

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for row in range(4):
        print("|", end = "")
        for col in range(4):
            num = grid[row][col]
            if num == 0:
                num = ""
            print(num, " " * (5 - len(str(num))), sep = "", end = "")
        print("|")
    print("+--------------------+")

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for row in range(4):
        for col in range(4):
            num = grid[row][col]
            if num == 0:
                return False
    for row in range(4):
        for col in range(3):
            if grid[row][col] == grid[row][col+1] or grid[col][row] == grid[col+1][row]:
                return False
    return True

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for row in range(4):
        for col in range(4):
            if grid[row][col] >= 32:
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