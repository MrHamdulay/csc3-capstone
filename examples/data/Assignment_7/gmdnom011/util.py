# Module of utility functions to manipulate 2-D arrays of size 4x4
# Nomsa Gamedze
# 28 April 2014

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([])
    for i in range(4):
        while len(grid[i]) < 4:
               grid[i].append(0)
    return grid

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    result = ""
    result += "+--------------------+" + '\n'
    for i in range(len(grid)):
        result += "|"
        for c in grid[i]:
            if c != 0:
                c =  str(c)
                result += c.ljust(5)
            else:
                result += " ".ljust(5)
        result += "|" + '\n'
    result += "+--------------------+"
    print(result)
    

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for i in range(4):
        boolean = True
        if 0 in grid[i]:
            boolean = False
            return boolean
        for c in range(3):
            if grid[i][c] == grid[i][c+1]:
                boolean = False
                return boolean
    for v in range(3):
        for c in range(4):
            if grid[v][c] == grid[v+1][c]:
                boolean = False
                return boolean
    else: 
        return boolean

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in range(4):
        for c in range(4):
            if grid[i][c] >= 32:
                return True
    else:
        return False

def copy_grid (grid):
    """return a copy of the grid"""
    grid_copy = [[], [], [], []]
    for i in range(len(grid)):
        for c in grid[i]:
            grid_copy[i].append(c)
    return grid_copy

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    for i in range(4):
        for c in range(4):
            if grid1[i][c] != grid2[i][c]:
                return False
    else:
        return True