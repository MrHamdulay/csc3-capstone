"""utitlity functions to manipulate 2d arrays
   kevin kumasamba
   01 may 2014"""

def create_grid(grid):
    for i in range(4):
        grid.append([" "] * 4)
    return grid

def print_grid(grid):
    print("+", "-"*20, "+", sep="")
    for item in create_grid([]):
        print("|", end="")
        for x in item:
            print(" "*5, sep="", end="")
        print("|")
    print("+", "-"*20, "+", sep="")

def check_lost(grid):
    for i in grid:
        for j in i:
            if j == ' ':
                return False
    for i in range(len(grid)):
        for j in range(4):
            position = grid[i][j]
            to_right = j +1
            if 0 <= to_right <4:
                if position==grid[i][to_right]:
                    return False
            to_left = j - 1
            if 0 <= to_left <4:
                if position==grid[i][to_left]:
                    return False
            up = i -1
            if 0 <= up < 4:
                if position == grid[up][j]:
                    return False
            down = i + 1
            if 0 <= down <4:
                if position == grid[down][j]:
                    return False
    return True

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in grid:
        for j in i:
            if j >= 32:
                return True
    return False

def copy_grid (grid):
    """return a copy of the grid"""
    copy_grid = []
    create_grid(copy_grid)
    for i in range (4):
        for j in range (4):
            copy_grid[i][j] = grid[i][j]
    
    return copy_grid
    

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True
    else:
        return False