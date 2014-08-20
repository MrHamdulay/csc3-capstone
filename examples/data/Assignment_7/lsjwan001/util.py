# Program manipulates 2-dimensional arrays
# Wandile Lesejane
# 30 April 2014
grid=[]

def create_grid(grid):
    """create a 4x4 grid"""
    height=4
    for i in range(height):
        grid.append([0]*4)
        
def print_grid(grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    height=4
    print("+","-"*20,"+",sep="")
    for row in range(height):
        print("|",end="")
        for col in range(height):
            if grid[row][col]!=0:
                print('{0:<5}'.format(grid[row][col]),end="")
            else:
                print(" "*5,end="")
            
        print("|")
    print("+","-"*20,"+",sep="")
         
def check_lost(grid):
    height=4
    for row in range(height):
        for col in range(height):
            if grid[row][col]!=grid[row][col+1]:
                return False
            elif grid[row][col]==grid[row+1][col]:
                return False
            elif grid[row][col]==0:
                return False
    
            else:
                return True

def check_won(grid):
    won=False
    """return True if a value=32 is found in the grid; otherwise False"""
    height=4
    for row in range(height):
        for col in range(height):
            if grid[row][col]>=32:
                won=True
    if won:
        return True
    else:
        return False
    

def copy_grid(grid):
    """return a copy of the grid"""
    import copy
    grid=copy.deepcopy(grid)
    return grid

def grid_equal(grid1,grid2):
    """check if 2 grids are equal - return boolean value"""
    height=4
    for row in range(height):
        for col in range(height):
            if grid1[row][col]==grid2[row][col]:
                return True
            else:
                return False
