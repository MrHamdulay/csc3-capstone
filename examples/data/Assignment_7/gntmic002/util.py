#Assignment 7.2
#Michael Gant
#27/04/2014

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0]*4)

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+" + "-"*20+"+")
    for i in range(4):
        sLine = ""
        for j in range(4):
            if grid[i][j] == 0:
                sLine = sLine + " "*5
            else:
                sLine = sLine + str(grid[i][j]) + " "*(5-len(str(grid[i][j])))
        print("|"+sLine +"|")
    print("+" + "-"*20+"+")        
        
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    
    for i in range(4):
        for j in range(4):
            if (grid[i][j] == 0) :
                return False
            elif (j>0) and (grid[i][j]==grid[i][j-1]):
                return False
            elif (i>0) and grid[i][j]==grid[i-1][j]:
                return False
    return True
    
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in range(4):
        for j in range(4):
            if (grid[i][j] >= 32) :
                return True
    return False    

def copy_grid (grid):
    """return a copy of the grid"""
    gridcopy = []
    create_grid(gridcopy)
    for i in range(4):
        for j in range(4):
            gridcopy[i][j] = grid[i][j]
    return gridcopy

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True
    return False
        
        
        