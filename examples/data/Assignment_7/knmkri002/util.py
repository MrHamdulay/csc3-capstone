"""module of utility functions
Kristin Kinmont
27 April 2014"""

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0]*4)

def print_grid(grid):
    """ print out a 4x4 grid in 5-width columns within a box"""
    print("+"+"-"*20+"+") #print top of box
    print("|", end = "")
    count = 1 # to count the number of rows and determine when the | at the front ust be printed
    for row in grid:
        for col in row:
            if col == 0:
                col = " "
            col = '{0:<5}'.format(col) # print out values in a column width of 5
            print(col, end = "")
        count += 1
        print("|")
        if count <= 4:
            print("|",end = "")
    print("+"+"-"*20+"+")

def check_lost(grid):
    for row in range(4):
        for col in range(4):
            if grid[row][col] == 0:
                return False
            if row > 0:
                if grid[row][col] == grid[row - 1][col]: 
                    return False
            if col > 0:
                if grid[row][col] == grid[row][col - 1]:
                    return False
            if row == 0:
                if col > 0:
                    if grid[row][col] == grid[row][col - 1]:
                        return False 
            if col == 0:
                if row > 0:
                    if grid[row][col] == grid[row - 1][col]: 
                        return False 
    return True
    
def check_won(grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for row in grid:
        for col in row:
            if col >= 32:
                return True
    else:
        return False

def copy_grid(grid):
    """return a copy of the grid"""
    grid1 = []
    for i in range(4):
        grid1.append([0]*4)
    for row in range(4):
        for col in range(4):
            grid1[row][col] = grid[row][col]
    return grid1

def grid_equal(grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    count = 0
    for row in range(4):
        for col in range(4):
            if grid1[row][col] != grid2[row][col]:
                count += 1
    if count == 0:
        return True
    else:
        return False
            