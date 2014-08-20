def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(0,4):
        grid.append([0]*4)
    return grid

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    str_grid = "+" + "-"*20 + "+\n"
    for row in range(0,4):
        str_grid += "|"
        for col in range(0,4):
            if grid[row][col] == 0:
                str_grid += " "*5
            else:
                str_val = str(grid[row][col])
                str_grid += str_val + " "*(5 - len(str_val))
        str_grid += "|\n"
    str_grid += "+" + "-"*20 + "+"
    print (str_grid)

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    row, col = 0,0
    zero, equal_adj = False, False
    while row < 4 and col < 4:
        if grid[row][col] == 0:
            zero = True
            break
        col += 1
        if col >= 4:
            row += 1
            col = 0
    row, col = 0,0
    while row < 4 and col < 4:
        if row != 3:
            if grid[row+1][col] == grid[row][col]:
                equal_adj = True
                break
        if row != 0:
            if grid[row-1][col] == grid[row][col]:
                equal_adj = True
                break            
        if col != 3:
            if grid[row][col+1] == grid[row][col]:
                equal_adj = True
                break
        if col != 0:
            if grid[row][col-1] == grid[row][col]:
                equal_adj = True
                break
        col += 1
        if col >= 4:
            row += 1
            col = 0
    return not (zero or equal_adj)
    

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for row in range(0,4):
        for col in range(0,4):
            if grid[row][col] >= 32:
                return True
    else:
        return False

def copy_grid (grid):
    """return a copy of the grid"""
    new_grid = []
    for i in range(0,4):
        new_grid.append([0]*4)    
    for row in range(0,4):
        for col in range(0,4):
            new_grid[row][col] = grid[row][col]
    return new_grid

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    for row in range(0,4):
        for col in range(0,4):
            if grid1[row][col] != grid2[row][col]:
                return False
    else:    
        return True