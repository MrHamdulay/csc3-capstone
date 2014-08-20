# A module of functions that merges numbers on a grid in different directions
# Martin Batek
# 30 April 2014

# Grid utility routines
import util

def push_up(grid):
    """Merge numbers upward"""
    oldgrid = util.copy_grid(grid)
    while len(grid)> 0:
        del grid[0]
    util.create_grid(grid)
    for column in range(4):
        position = 0
        merge = 0
        for row in range(4):
            if oldgrid[row][column] != 0:
                if oldgrid[row][column] == grid[merge][column]:
                    grid[merge][column] += oldgrid[row][column]
                    merge += 1
                else:
                    grid[position][column] = oldgrid[row][column]
                    position += 1
                    if position-merge >= 2:
                        merge += 1
                        
def push_down(grid):
    """Merge numbers downward"""
    oldgrid = util.copy_grid(grid)
    while len(grid)> 0:
        del grid[0]
    util.create_grid(grid)
    for column in range(4):
        position = 3
        merge = 3
        for row in range(3,-1,-1):
            if oldgrid[row][column] != 0:
                if oldgrid[row][column] == grid[merge][column]:
                    grid[merge][column] += oldgrid[row][column]
                    merge -= 1
                else:
                    grid[position][column] = oldgrid[row][column]
                    position -= 1
                    if merge - position >= 2:
                        merge -= 1
                        
def push_right(grid):
    """Merge numbers to the right"""
    oldgrid = util.copy_grid(grid)
    while len(grid)> 0:
        del grid[0]
    util.create_grid(grid)
    for row in range(4):
        position = 3
        merge = 3
        for column in range(3,-1,-1):
            if oldgrid[row][column] != 0:
                if oldgrid[row][column] == grid[row][merge]:
                    grid[row][merge] += oldgrid[row][column]
                    merge -= 1
                else:
                    grid[row][position] = oldgrid[row][column]
                    position -= 1
                    if merge - position >= 2:
                        merge -= 1
                    
def push_left(grid):
    """Merge numbers to the left"""
    oldgrid = util.copy_grid(grid)
    while len(grid)> 0:
        del grid[0]
    util.create_grid(grid)
    for row in range(4):
        position = 0
        merge = 0
        for column in range(4):
            if oldgrid[row][column] != 0:
                if oldgrid[row][column] == grid[row][merge]:
                    grid[row][merge] += oldgrid[row][column]
                    merge += 1
                else:
                    grid[row][position] = oldgrid[row][column]
                    position += 1
                    if position - merge >= 2:
                        merge += 1