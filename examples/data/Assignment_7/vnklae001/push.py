# Assignment 7 - Question 3
# The code for a 2048 game, using util.py and 2048.py.  The heart of the game is the set of merging functions that merge adjacent equal values and eliminate gaps
# Written by: Laene van Niekerk
# VNKLAE001

import util

def push_up(grid):     # Merge grid values upwards (i.e. copy the values into an array, manipulate the array and replace the origional array with the new array)
    old_grid = util.copy_grid(grid)     # Create a copy of the origional grid
    while len(grid) > 0:
        del grid[0]
    util.create_grid(grid)      # Grid with 0's
    for col in range(4):
        pos = 0
        merge = 0
        for row in range(4):
            if old_grid[row][col] == grid[merge][col]:
                grid[merge][col] += old_grid[row][col]
                merge += 1
            else:
                grid[pos][col] = old_grid[row][col]
                pos += 1
                if pos-merge >= 2:
                    merge += 1

def push_down(grid):   # Merge grid values downwards
    old_grid = util.copy_grid(grid)     # Create a copy of the origional grid
    while len(grid) > 0:
            del grid[0]
    util.create_grid(grid)      # Grid with 0's
    for col in range(4):
        pos = 3
        merge = 3
        for row in range(3,-1,-1):
            if old_grid[row][col] != 0:
                if old_grid[row][col] == grid[merge][col]:
                    grid[merge][col] += old_grid[row][col]
                merge -= 1
            else:
                grid[pos][col] = old_grid[row][col]
                pos -= 1
                if merge - pos >= 2:
                    merge -= 1    

def push_right(grid):   # Merge grid values left
    old_grid = util.copy_grid(grid)     # Create a copy of the origional grid
    while len(grid) > 0:
        del grid[0]
    util.create_grid(grid)      # Grid with 0's
    for row in range(4): 
        pos = 3
        merge = 3
        for col in range(3,-1,-1):
            if old_grid[row][col] != 0:
                if old_grid[row][col] == grid[row][merge]:
                    grid[row][merge] += old_grid[row][col]
                    merge -= 1
                else:
                    grid[row][pos] = old_grid[row][col]
                    pos -= 1
                    if merge - pos >= 2:
                        merge -= 1         

def push_left(grid):  # Merge grid values right 
    old_grid = util.copy_grid(grid)     # Create a copy of the origional grid
    while len(grid) > 0:
        del grid[0]
    util.create_grid(grid)      # Grid with 0's
    for row in range(4): 
        pos = 0
        merge = 0
        for col in range(4):
            if old_grid[row][col] != 0:
                if old_grid[row][col] == grid[row][merge]:
                    grid[row][merge] += old_grid[row][col]
                    merge += 1
                else:
                    grid[row][pos] = old_grid[row][col]
                    pos += 1
                    if pos - merge >= 2:
                        merge += 1      