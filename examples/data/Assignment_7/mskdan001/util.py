"""danson masuka 1 may 2014 modules for the 2048 game"""""

#the 4x4 grid
def create_grid(grid):
    grid = []
    for col in range(4):
        for row in range(4):
            grid.append([0]*4)

def print_grid (grid):
    print ("+"+"-"*20+"+")
    
    for col in range(4):
        print ("|",end="")
        for row in range(4):
            if grid[col][row] == 0:
                print ("{:<5}".format(" "),end="")
            else:
                print ("{:<5}".format(grid[col][row]),end="")
        print ("|")
    print ("+"+"-"*20+"+")

def check_lost (grid):
    for col in range(4):
        for row in range(4):
            if grid[col][row] == 0:
                return False
    for col in range(4):
        for row in range(4):
            gref = grid[col][row]
            if 0 <= row+1 < 4:
                if gref == grid[col][row+1]:
                    return False
            if 0 <= row-1 < 4:
                if gref == grid[col][row-1]:
                    return False
            if 0 <= col+1 < 4:
                if gref == grid[col+1][row]:
                    return False
            if 0 <= col-1 < 4:
                if gref == grid[col-1][row]:
                    return False
        return True

def check_won (grid):
    for col in range(4):
        for row in range(4):
            if grid[col][row] >=32 or grid[row][col] >=32:
                return True
    return False

def copy_grid (grid):
    copy = []
    create_grid(copy)
    for col in range(4):
        for row in range(4):
            copy[col][row] = grid[col][row]
    return copy

def grid_equal (grid1, grid2):
    if grid1 == grid2:
        return True
    return False
