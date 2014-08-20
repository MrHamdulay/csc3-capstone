def create_grid(grid):
    """create a 4x4 grid"""
    for t in range(4):
        grid.append([0,0,0,0])

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    tempGrid = copy_grid(grid)
    print("+--------------------+")
    for x in range(4):
        for y in range(4):
            if grid[x][y] == 0:
                tempGrid[x][y] = ""
    for i in range(4):
        print("|{0:<5}{1:<5}{2:<5}{3:<5}|".format(tempGrid[i][0],tempGrid[i][1],tempGrid[i][2],tempGrid[i][3]))
    print("+--------------------+")

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for x in range(4):
            for y in range(4):
                if grid[x][y] == 0:
                    return False
    for x in range(4):
        for y in range(3):
            if grid[x][y] == grid[x][y+1] or grid[y][x] == grid[y+1][x]:
                return False
    return True

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for x in range(4):
            for y in range(4):
                if grid[x][y]>=32:
                    return True
    return False

def copy_grid (grid):
    """return a copy of the grid"""
    newGrid = []
    for i in range(4):
        newGrid.append([grid[i][0],grid[i][1],grid[i][2],grid[i][3]])
    return newGrid

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    for x in range(4):
            for y in range(4):
                if grid1[x][y]!=grid2[x][y]:
                    return False
    return True
                    