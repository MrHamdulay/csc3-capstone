"""Daniel Schwartz
SCHDAN037
util module for question 2
April 2014"""

#for copy_grid function
import copy


def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0, 0, 0, 0])


def print_grid(grid):
    """print out a 4x4 grid in 5-width columns within a box"""

    #top of box
    print("+" + "-----" * 4 + "+")

    #middle of box
    for row in range(4):
        format_str = ""
        for i in range(4):
            #dont print the 0
            if grid[row][i] == 0:
                format_str += "{0:<5}".format("")
            #print everything else
            else:
                format_str += "{0:<5}".format(grid[row][i])
        print("|", format_str, "|", sep="", end="")
        print()

    #bottom of box
    print("+" + "-----" * 4 + "+")


def check_lost(grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""

    #first check for zeros
    for row in range(4):
        for col in range(4):
            if grid[row][col] == 0:
                return False

    #second check for equal adjacent values
    for row in range(4):
        for col in range(4):
            if col == 0:
                if row == 0:
                    #top left corner
                    if grid[row][col] == grid[row + 1][col] or grid[row][col] == grid[row][col + 1]:
                        return False
                elif row == 3:
                    #bottom left corner
                    if grid[row][col] == grid[row - 1][col] or grid[row][col] == grid[row][col + 1]:
                        return False
                else:
                    #left column, not top/bottom
                    if grid[row][col] == grid[row + 1][col] or grid[row][col] == grid[row - 1][col] or grid[row][col] == grid[row][col + 1]:
                        return False
            elif col == 3:
                if row == 0:
                    #top right corner
                    if grid[row][col] == grid[row + 1][col] or grid[row][col] == grid[row][col - 1]:
                        return False
                elif row == 3:
                    #bottom right corner
                    if grid[row][col] == grid[row - 1][col] or grid[row][col] == grid[row][col - 1]:
                        return False
                else:
                    #right column, not top/bottom
                    if grid[row][col] == grid[row + 1][col] or grid[row][col] == grid[row - 1][col] or grid[row][col] == grid[row][col - 1]:
                        return False
            else:
                if row == 0:
                    #top row, not left/right col
                    if grid[row][col] == grid[row + 1][col] or grid[row][col] == grid[row][col + 1] or grid[row][col] == grid[row][col - 1]:
                        return False
                elif row == 3:
                    # bottom row, not left/right col
                    if grid[row][col] == grid[row - 1][col] or grid[row][col] == grid[row][col + 1] or grid[row][col] == grid[row][col - 1]:
                        return False
                else:
                    #all the middle area
                    if grid[row][col] == grid[row - 1][col] or grid[row][col] == grid[row + 1][col] or grid[row][col] == grid[row][col + 1] or grid[row][col] == grid[row][col - 1]:
                        return False
    return True


def check_won(grid):
    """return True if a value>=32 is found in the grid; otherwise False"""

    for row in range(4):
        for col in range(4):
            if grid[row][col] >= 32:
                return True

    return False


def copy_grid(grid):
    """return a copy of the grid"""
    #deepcopy used to make a real copy of the list and not point to it in memory
    copied = copy.deepcopy(grid)
    return copied



def grid_equal(grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True
    else:
        return False