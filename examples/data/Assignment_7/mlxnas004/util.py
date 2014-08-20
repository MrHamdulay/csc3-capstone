"""nasha somoina meoli
30th april 2014
program containing utlity fucntions for 2048 game"""

def create_grid(grid):
    for i in range(4):
        grid.append([0]*4)
    return grid

def print_grid(grid):

    print("+"+"-"*20+"+")
    for row in range(4):
        for col in range(4):
            if col == 0:
                print("|",end="")
            
            item ="{0:<5}".format(grid[row][col])
            if grid[row][col] != 0:
                print(item,end = "")
            else:
                print(" "*5,end="")
            if col == 3:
                print("|",end = "")
        print()
    print("+"+"-"*20+"+")

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for row in range(4):
        for col in range(4):
            x=grid[row][col]
            if x == 0:
                return False
            if col > 0:
                if x == grid[row][col-1]:
                    return False
            elif col <3:
                if x == grid[row][col+1]:
                    return False                
            if row > 0:
                if x == grid[row-1][col]:
                    return False
            elif row < 3:
                if x == grid[row+1][col]:
                    return False                
    return True
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for row in range(4):
        for col in range(4):

            if grid[row][col] >= 32:
                return True
    else:
        return False
def copy_grid (grid):
   
    """return a copy of the grid"""
    import copy
    grid2 = copy.deepcopy(grid)
    return grid2

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True
    else:
        return False