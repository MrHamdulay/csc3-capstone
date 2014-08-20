#VRMNIC005
#assignment 7, question 2
#2048 is ruining my life

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0, 0, 0, 0])

def print_grid(grid):
    """Print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for row in grid:
        print("|", end = "")
        for num in row:
            if num == 0:
                print(" " * 5, end="")
            else:
                print("{:<5}".format(num), end="")
        print("|")
    print("+--------------------+")

def check_lost(grid):
    """return True if there are no 0 values and no adjacent values that are equal"""
    #check 0s
    for row in grid:
        if 0 in row:
            return False
    
    #check adjacent values

    for y in range(3):
        for x in range(4):
            if grid[y][x] == grid[y+1][x]:
                return False
            if grid[x][y] == grid[x][y+1]:
                return False

    return True #game is lost

def check_won(grid):
    """return True if a value >= 32 is found in grid"""
    for row in grid:
        for num in row:
            if num >= 32:
                return True

    return False
    
def copy_grid(grid):
    """return a copy of the grid"""
    new_grid = []
    for row in grid:
        new_grid.append(row[:])

    return new_grid

def grid_equal(grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    return grid1 == grid2
        
