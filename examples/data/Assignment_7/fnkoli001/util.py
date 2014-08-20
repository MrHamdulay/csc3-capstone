def create_grid(grid):
    """create a 4x4 grid"""
    for horizontal in range(0, 4):
        grid.append([0, 0, 0, 0])


def print_grid(grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for row in grid:
        row_string = "|"
        for no in row:
            if no == 0:
                row_string += " " * 5
            else:
                row_string += str(no) + " " * (5 - len(str(no)))
        print(row_string + "|")
    print("+--------------------+")


def check_lost(grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    lost = False
    if len([i for i in grid if 0 in i]) == 0:
        #Check if adjcent numbers are equal, must be a perfect square grid
        for row_no in range(0, len(grid)):
            for colomb_no in range(0, len(grid[row_no]) - 1):
                if grid[row_no][colomb_no] != grid[row_no][colomb_no + 1] and grid[colomb_no][row_no] != \
                        grid[colomb_no + 1][row_no]:
                    lost = True
    return lost


def check_won(grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    won = False
    for row in grid:
        for no in row:
            if no >= 32:
                won = True
    return won

def copy_grid(grid):
    """return a copy of the grid"""
    copied_grid=[]
    for row in grid:
        copied_row=[]
        for no in row:
            copied_row.append(no)
        copied_grid.append(copied_row)
    return copied_grid

def grid_equal(grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    equal = False
    if grid1 == grid2:
        equal = True
    return equal