"""Assignment 7, Question 2
Module of utilities for Question 3
Author: SWNREI001
28 April 2014 """

def create_grid(grid):
    """create a 4x4 grid"""
    while len(grid) < 4:
        grid.append([0 for i in range(4)]) # creates a list of 4 0's

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print('+','-' * len(grid) * 5, '+', sep = "") # top row, e.g. +----+
    for row in grid:
        print('|', end = "")
        for cell in row:
            if cell == 0: 
                print("".ljust(5), end = "") # only print if j is not empty
            else:
                print(str(cell).ljust(5), end = "") # str.ljust left justifies to specified range
        print('|') #end of row, boundary   
    print('+','-' * len(grid) * 5, '+', sep = "") # same as top
    
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 0:
                return False
            else:
                # in the following: 1) check if x +/- 1 & y +/- 1 are valid indexes of grid
                #                   2) then check if they are equal
                if y < len(grid[x]) - 1 and grid[x][y + 1] == grid[x][y]:
                    return False
                elif y > 0 and grid[x][y-1] == grid[x][y]:
                    return False
                elif x < len(grid) - 1 and grid[x + 1][y] == grid[x][y]:
                    return False
                elif x > 0 and grid[x-1][y] == grid[x][y]:
                    return False
    return True # return True if all zero and equivalency checks failed

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for row in grid:
        for value in row: # iterate through grid
            if value >= 32: # check every value
                return True # win is if the value >= 32
    return False # otherwise, not a win

def copy_grid (grid):
    """return a copy of the grid"""
    new_grid = []
    for row in grid:
        new_row = []
        for value in row:
            new_row.append(value)
        new_grid.append(new_row)
    return new_grid    

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if len(grid1) != len(grid2):
        return False
    for x in range(len(grid1)): # above ensure this is the same as grid2
        if len(grid1[x]) != len(grid2[x]):
            return False
        for y in range(len(grid1)): # above ensures this is the same as grid2
            if grid1[x][y] != grid2[x][y]:
                return False #b/c lacks equality
    return True