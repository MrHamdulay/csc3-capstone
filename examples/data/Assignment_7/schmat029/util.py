#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     creates grid functions for 2048
#
# Author:      Matthias
#
# Created:     27-04-2014
# Copyright:   (c) Matthias 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def create_grid(grid):
    for i in range(4):
        # add a new empty list into grid
        grid.append([])
        for j in range(4):
            # add 0, 0, 0, 0 into this newly created sublist
            grid[i].append(0)
    return grid

def print_grid(grid):
    # print top border
    print("+" + "-"*20 + "+")
    for row in range(4):
        # print left border
        print("|", end="")
        for value in grid[row]:
            # only print non-zero values
            if value == 0:
                print(" " * 5, end="")
            else:
                print("{0:<5}".format(value), end="")
        # print right border
        print("|")
    # print bottom border
    print("+" + "-"*20 + "+")

def check_lost(grid):
    # check vor zero values
    for row in range(4):
        for value in grid[row]:
            if value == 0:
                return False
    # check for adjacent equal values
    for row in range(3):
        for column in range(3):
            # horizontally adjacent
            if grid[row][column] == grid[row][column + 1]:
                return False
            # vertically adjacent
            if grid[row][column] == grid[row + 1][column]:
                return False
    return True

def check_won(grid):
    for row in range(4):
        for value in grid[row]:
            # check if any one value is more or equal to 32
            if value >= 32:
                return True
    return False

def copy_grid(grid):
    new_grid = []
    for row in range(4):
        # add a new row
        new_grid.append([])
        for value in grid[row]:
            # copy each value into this newly created row
            new_grid[row].append(value)
    return new_grid

def grid_equal(grid1, grid2):
    for row in range(4):
        for column in range(4):
            # check if each value in grid1 is equal to the equivalent value in grid2
            if grid1[row][column] != grid2[row][column]:
                return False
    return True
