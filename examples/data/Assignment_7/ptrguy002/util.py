from operator import *
from functools import *

def create_grid(grid):
    """create a 4x4 grid"""
    for a in range(len(grid)):
        grid.pop()
    for a in range(4):
        grid.append([0,0,0,0])
    return grid

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for y in grid:
        print("|" + reduce(add, map(lambda x: str(x) + " "*(5-len(str(x))) if x > 0 else "     ", y)) + "|")
    print("+--------------------+")

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for p1 in [(a, b) for a in range(4) for b in range(4)]:
        for p2 in [(a, b) for a in range(4) for b in range(4)]:
            dx = abs(p1[0] - p2[0])
            dy = abs(p1[1] - p2[1])
            if (dx == 0 and dy == 0):
                if grid[p1[1]][p1[0]] == 0:
                    return False
            elif ((dx == 1 and dy == 0) or (dy == 1 and dx == 0)):
                if grid[p1[1]][p1[0]] == grid[p2[1]][p2[0]]:
                    return False
    return True

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for y in grid:
        for x in y:
            if x >= 32:
                return True
    return False

#Where's memcpy when you need it XD
def copy_grid (grid):
    """return a copy of the grid"""
    ret = []
    for y in grid:
        tmp = []
        for x in y:
            tmp.append(x)
        ret.append(tmp)
    return ret

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    for x,y in [(a,b) for a in range(4) for b in range(4)]:
        if grid1[y][x] != grid2[y][x]:
            return False
    return True
