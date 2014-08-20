"""module of utility functions
clare walker
27 april 2014"""


def create_grid(grid):
    """create a 4x4 grid"""
    for row in range(4): #4 rows
        grid.append([0]*4) #4 column
        

def print_grid(grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+"+("-"*20) +"+")
    for row in range(4):
        for col in range(4):
            if grid[row][col] ==0:
                if col ==0:
                    print("|{0:<5}".format(' '), end="")
                elif col ==3:
                    print("{0:<5}|".format(' '), end="")
                else:
                    print("{0:<5}".format(' '), end="")
            elif col ==0:
                print("|{0:<5}".format(grid[row][col]), end="")
            elif col==3:
                print("{0:<5}|".format(grid[row][col]), end="")
            else:
                print("{0:<5}".format(grid[row][col]), end="")
            
        print()
    print("+"+("-"*20) +"+")
    
def check_lost(grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    zeros=True
    no_equal=True
    for row in range(4): #check if any zeros
        for col in range(4):
            if grid[row][col] == 0:
                zeros = False
    for row in range(4): #check for adjacent equal values
        if row ==0:
            for col in range(4):
                if col == 0:
                    if grid[row][col] == grid[row+1][col] or grid[row][col] == grid[row][col+1]:
                        no_equal=True
                elif col==3:
                    if grid[row][col] == grid[row+1][col] or grid[row][col] == grid[row][col-1]:
                        no_equal =False
                else:
                    if grid[row][col] == grid[row+1][col] or grid[row][col] == grid[row][col-1] or grid[row][col] == grid[row][col+1]:
                        no_equal=False
        elif row ==3:
            for col in range(4):
                if col == 0:
                    if grid[row][col] == grid[row-1][col] or grid[row][col] == grid[row][col+1]:
                        no_equal=False
                elif col==3:
                    if grid[row][col] == grid[row-1][col] or grid[row][col] == grid[row][col-1]:
                        no_equal =False
                else:
                    if grid[row][col] == grid[row-1][col] or grid[row][col] == grid[row][col-1] or grid[row][col] == grid[row][col+1]:
                        no_equal=False
        else:
            for col in range(4):
                if col ==0:
                    if grid[row][col] == grid[row-1][col] or grid[row][col] == grid[row][col+1] or grid[row][col] ==grid[row+1][col]:
                        no_equal = False
                elif col ==3:
                    if grid[row][col] == grid[row-1][col] or grid[row][col] == grid[row][col-1] or grid[row][col]==grid[row+1][col]:
                        no_equal = False                    
                else:
                    if grid[row][col] == grid[row-1][col] or grid[row][col] == grid[row][col-1] or grid[row][col] == grid[row][col+1] or grid[row][col] ==grid[row+1][col]:
                        no_equal = False
    if zeros and no_equal:
        return True
    else:
        return False
                
           
def check_won(grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for row in range(4):
        for col in range(4):
            
            
            if grid[row][col] >= 32:
                return True
    else:
        return False
def copy_grid(grid):
    """return a copy of the grid"""
    newgrid=[]
    for row in range(4):
        newgrid.append([0]*4)
    for row in range(4):
        for col in range(4):
            newgrid[row][col]=grid[row][col]
            
    return newgrid
            
def grid_equal(grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    
    for row in range(4):
        for col in range(4):
            if grid1[row][col] !=grid2[row][col]:
                return False
    else:
        return True