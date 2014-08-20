"""Assignment 7, Question 3
Push.py
Helper functions for the game of 2048 (in 2048.py)"""

# NOTE: merged blocks added as strings to prevent merging twice in one turn;
# returned to int form at end of turn

def destring(grid):
    """Helper function to replace strings in grid with ints"""
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if type(grid[i][j]) == str:
                grid[i][j] = eval(grid[i][j])

def push(line):
    """Does the actual work of pushing and merging lines of the grid;
    Push/merge is done towards index 0 of line; merges added as string"""
    for n in range(len(line)): # repeat once for each element
        for i in range(len(line)):
            if i == 0:
                continue # ensure indexing will work
            if not (type(line[i]) == str) and line[i] != 0 and line[i] == line[i-1]:
                # only merge if not zero, not strings and equal
                line[i-1] = str(line[i] + line[i-1])
                line[i] = 0
            elif line[i-1] == 0:
                line[i-1] = line[i]
                line[i] = 0

def push_up(grid):
    """Pushes blocks in grid upwards, merging equal and adjacent blocks"""
    for j in range(len(grid[0])):
        line = []
        for i in range(len(grid)): # add as columns, not rows
            line.append(grid[i][j])
        push(line)
        # add values in line back to grid
        for index in range(len(line)):
            grid[index][j] = line[index]
    destring(grid)

def push_down(grid):
    """Pushes blocks in grid downwards, merging equal and adjacent blocks"""
    for j in range(len(grid[0])):
        line = []
        for i in range(len(grid)): # add as columns, not rows
            line.append(grid[i][j])
        line = line[::-1]# same as upwards logic, but reversed so push is downwards
        push(line)
        # add values in line back to grid
        for index in range(len(line)):
            grid[index][j] = line[::-1][index] # reverse again to put in grid in correct order
    destring(grid)
            

def push_left(grid):
    """Pushes blocks in grid to the left, merging equal, adjacent blocks"""
    for i in grid:
        push(i)
    destring(grid)

def push_right(grid):
    """Pushes blocks in grid to the right, merging equal, adjacent blocks"""
    for i in grid:
        line = i[::-1] # reverse to work with push function
        push(line)
        for n in range(len(i)):
            i[n] = line[::-1][n] # re-reverse to get back to original order
    destring(grid) # remove added strings; replace with ints

