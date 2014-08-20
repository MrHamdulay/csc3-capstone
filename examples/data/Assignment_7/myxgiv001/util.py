def create_grid(grid):
    """create a 4x4 grid"""
    #grid = [[0]*4,[0]*4,[0]*4,[0]*4]
    grid.append([0]*4)
    grid.append([0]*4)
    grid.append([0]*4)
    grid.append([0]*4)
    #return grid

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for i in grid:
        print("|",end="")
        for j in i:
            if j == 0:
                print("{:<5}".format(" "),end="")
            else:
                print("{:<5}".format(j),end="")
        print("|")
    print("+--------------------+")   
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                return False
            if j+1<4 and grid[i][j] == grid[i][j+1]:
                return False
            if i+1<4 and grid[i][j] == grid[i+1][j]:
                return False
            if j-1>=0 and grid[i][j] == grid[i][j-1]:
                return False
            if i-1>=0 and grid[i][j] == grid[i-1][j]:
                return False
    return True
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in grid:
        for j in i:
            if j>=32:
                return True
    return False
    pass
def copy_grid (grid):
    """return a copy of the grid"""
    newGrid = []
    create_grid(newGrid)
    for i in range(4):
        for j in range(4):
            newGrid[i][j] = int(grid[i][j])
    return newGrid
def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    for i in range(4):
        for j in range(4):
            if grid1[i][j] != grid2[i][j]:
                return False
    return True
