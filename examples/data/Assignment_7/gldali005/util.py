#program where the user can enter a list of strings and these strings are then printed in the same order but without duplicates.
#Ali Goldstein
#30 april 2014

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0]*4)
    return grid 
    
def print_grid(grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for row in range(4):
        print("|", end="")
        for col in range(4):
            if grid[row][col]==0:
                grid[row][col]=" "
            print("{0:<5}".format(grid[row][col]), end="")
        print("|")
    print("+--------------------+")
    
    
def check_lost(grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    found=False
    for row in range(4):
        for col in range(4):
            if grid[row][col]==0 or (grid[row][col]==grid[row-1][col-1] or grid[row][col]==grid[row+1][col+1]):
                return found
            else:
                found=True
    return found
           
def check_won(grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for row in range(4):
        for col in range(4):
            if grid[row][col]>=32:
                return True
            
    return False
            
def copy_grid (grid):
    """return a copy of the grid"""
    grid2=[]
    grid2=create_grid(grid2)
    for i in range(4):
        for j in range(4):
            grid2[i][j]=grid[i][j]
    return grid2
    
    
def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    for row in range(4):
        for col in range(4):
            if not grid1[row][col]==grid2[row][col]:
                return False
    return True
                
            