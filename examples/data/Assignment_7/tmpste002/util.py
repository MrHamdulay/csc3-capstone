""" Utility functions to manipulate 2-dimensional arrays of size 4x4 used in question3.py """
__author__ = 'Stephen Temple'
__date__ = '2014/04/29'


def create_grid(grid):
    """ Create a 4x4 grid """
    grid.append([0, 0, 0, 0])
    grid.append([0, 0, 0, 0])
    grid.append([0, 0, 0, 0])
    grid.append([0, 0, 0, 0])


def print_grid(grid):
    """ Print out a 4x4 grid in 5-width columns within a box """
    print("+--------------------+")
    for row in range(4):
        print("|", end='')
        for col in range(4):
            print("{0: <5}".format(grid[row][col] if grid[row][col] != 0 else ''), end='')
        print("|")
    print("+--------------------+")


def check_lost(grid):
    """ Return True if there are no 0 values and no adjacent values that are equal otherwise False """
    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[row][col] == 0:
                return False
            elif row > 0 and grid[row][col] == grid[row - 1][col]:
                return False
            elif row < 3 and grid[row][col] == grid[row + 1][col]:
                return False
            elif col > 0 and grid[row][col] == grid[row][col - 1]:
                return False
            elif col < 3 and grid[row][col] == grid[row][col + 1]:
                return False
    return True


def check_won(grid):
    """ Return True if a value>=32 is found in the grid otherwise False """
    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[row][col] >= 32:
                return True
    return False


def copy_grid(grid):
    """ Return a copy of the grid """
    new_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for row in range(len(grid)):
        for col in range(len(grid)):
            new_grid[row][col] = grid[row][col]
    return new_grid


def grid_equal(grid1, grid2):
    """ Check if 2 grids are equal - return boolean value """
    if len(grid1) != len(grid2):
        return False
    for row in range(len(grid1)):
        for col in range(len(grid1)):
            if grid1[row][col] != grid2[row][col]:
                return False
    return True