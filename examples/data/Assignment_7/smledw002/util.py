#Author         : Edwin Samuels
#Student number : SMLEDW002
#Date           : 27 April 2014
#Function       : Manipulate 2 Dimensional arrays
#Title          : Question2


def create_grid(grid):
    """creates a 4x4 grid"""
    for i in range(4):
        grid.append([0]*4)


def print_grid(grid):
    """prints out a grid inside of a box"""
    print("+--------------------+")
    for y in grid:
        print("|", end="")
        for x in y:
            if x != 0:
                print("{0:<5}".format(x), end="")
            else:
                print("{0:<5}".format(""), end="")

        print("|")
    print("+--------------------+")


def check_lost(grid):
    """checks if there are no possible moves"""
    #vertical test change:
    for y in range(3):
        for x in range(4):
            if grid[y][x] == grid[y+1][x] and grid[y][x] != 0:
                return False
    #horizontal test change find space if space less then x
    for y in range(4):
        for x in range(3):
            #checks for equal adjacent values not equal to zero
            if grid[y][x] == grid[y][x+1] and grid[y][x] != 0:
                return False

    #test for zero values
    for y in range(4):
        for x in range(4):
            if grid[y][x] == 0:
                return False
    return True


def check_won(grid):
    """checks if theres a value greater then or equal to 32"""

    for y in range(4):
        for x in range(4):
            if grid[y][x] >= 32:
                return True
    return False


def copy_grid(grid):
    """copies a grid"""
    grid2 = []
    for i in grid:
        temporary_grid = []
        for l in i:
            #temporary grid temporarily stores a row
            temporary_grid.append(l)
        grid2.append(temporary_grid)
    return grid2


def grid_equal(grid1, grid2):
    """checks if all the values have an equal value"""
    for y in range(4):
        for x in range(4):
            if grid1[y][x] != grid2[y][x]:
                return False
    return True


