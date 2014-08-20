__author__ = 'George de Kock'
""" Module of utility functions to manipulate 2-dimensional arrays of size 4x4
    2014-04-27 """

import copy


def create_grid(grid):
    for a in range(4):
        grid.append([0, 0, 0, 0])


def print_grid(grid):
    border = "+--------------------+"
    print(border)
    for a in range(4):
        print("|", end="")
        for b in range(4):
            space = (5-len(str(grid[a][b])))*" "  #calculating the length of each number to know number of spaces to show
            if grid[a][b] == 0:
                print("     ",end="")
            else:
                print(grid[a][b],space,sep="",end="")
        print("|")
    print(border)


def check_lost(grid):
    for a in range(4):
        for b in range(4):
            if grid[a][b] == 0:
                return False
            elif (a<3) and (b <3):
                if (grid[a][b] == grid[a+1][b]) or (grid[a][b] == grid[a][b+1]):
                    return False
    return True


def check_won(grid):
    for a in range(4):
        for b in range(4):
            #if grid[a][b] == " ":
            #    continue
            if grid[a][b] >= 32:
                return True
    return False


def copy_grid(grid):
    return copy.deepcopy(grid)


def grid_equal(grid1, grid2):
    for a in range(4):
        for b in range(4):
            if grid1[a][b] != grid2[a][b]:
                return False
    return True