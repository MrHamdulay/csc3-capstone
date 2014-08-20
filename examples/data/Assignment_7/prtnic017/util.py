# PRTNIC017
# 28 April 2014

import copy


def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0] * 4)


def print_grid(grid: list):
    """print out a 4x4 grid in 5-width columns within a box"""
    print('+', '-' * 20, '+', sep='')
    for y in range(len(grid)):
        print('|', end='')
        for x in range(len(grid[y])):
            if grid[y][x] != 0:
                print("{0:<5}".format(str(grid[y][x])), end='')
            else:
                print("{0:<5}".format(''), end='')
        print('|')
    print('+', '-' * 20, '+', sep='')


def check_lost(grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    # Check for 0 values
    for y in range(len(grid)):
        if 0 in grid[y]:
            return False
    # Check horizontal adjacent
    for y in range(len(grid)):
        for x in range(len(grid[y]) - 1):
            if grid[y][x] == grid[y][x + 1]:
                return False
    #Check vertical adjacent
    for y in range(len(grid) - 1):
        for x in range(len(grid[y])):
            if grid[y][x] == grid[y + 1][x]:
                return False
    return True


def check_won(grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for y in range(len(grid)):
        for x in range(len(grid)):
            if type(grid[y][x]) == int:
                if int(grid[y][x]) >= 32:
                    return True
    return False


def copy_grid(grid):
    """return a copy of the grid"""
    return copy.deepcopy(grid)


def grid_equal(grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    return grid1 == grid2