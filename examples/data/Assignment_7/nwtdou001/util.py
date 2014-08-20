'''util.py
utility functions for the 2048 game
douglas newton
29 april 2014'''

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0]*4)

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    
    text = ''
    text += '+'+'-----'*4+'+\n'    
    for y in range(len(grid)):
        text += '|'
        for x in range(len(grid[y])):
            value = grid[y][x]
            if value==0:
                text +=' '*5
            else:
                text += str(value).ljust(5)
        text += '|\n'
    text += '+'+'-----'*4+'+'
    print(text)

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    # whether there are pairs (adjacent values) in the grid. none found yet
    for y in range(4):
        for x in range(4):
            value = grid[y][x]
            # if theres a gap, user hasn't lost
            if value==0:
                return False
            # any equal adjacent values means user hasn't lost
            if x<3: 
                if grid[y][x+1]==value:
                    return False
            if x>0:
                if grid[y][x-1]==value:
                    return False
            if y<3:
                if grid[y+1][x]==value:
                    return False
            if y>0:
                if grid[y-1][x]==value:
                    return False
    # at this point, there are no gaps and no adjacent values: user has lost
    return True

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for y in range(4):
        for x in range(4):
            if grid[y][x]>=32:
                return True
    return False

def copy_grid(grid):
    """return a copy of the grid"""
    new_grid = []
    for i in range(4):
        line = [0]*4
        for j in range(4):
            line[j] = grid[i][j]
        new_grid.append(line)
    return new_grid

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    for y in range(4):
        for x in range(4):
            if grid1[y][x]!=grid2[y][x]:
                return False
    return True
