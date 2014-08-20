#Athour:Percival Munhuwaani
#Program: A program to manipulate 2-dimensional arrays of size 4x4
#Date:01/05/2014
def create_grid(grid):
    for i in range(4):
        grid.append([0]*4)
def print_grid(grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+"+"-"*20+"+",end="")
    print()
    for row in range(4):
        print("|",end="")
        for col in range(4):
            if grid[row][col]==0:
                print('{:<5}'.format(" "),end="")
            else:
                print('{:<5}'.format(grid[row][col]),end="")
        print("|",end="")
        print()
    print("+"+"-"*20+"+",end="")

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for row in range(4):
        for col in range(4):
            if grid[row][col]==0:
                return False
    for row in range(4):
        for col in range(4):
            grid_ref=grid[row][col]
            if 0<=col+1<4:
                if grid_ref==grid[row][col+1]:
                    return False
            if 0<=col-1<4:
                if grid_ref==grid[row][col-1]:
                    return False
            if 0<=row-1<4:
                if grid_ref==grid[row-1][col]:
                    return False            
            if 0<=row+1<4:
                if grid_ref==grid[row+1][col]:
                    return False
    return True
            
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for row in range(4):
        for col in range(4):
            if grid[row][col]>=32 or grid[col][row]>=32:
                return True
    return False
def copy_grid(grid):
    """return a copy of the grid"""
    copy=[]
    create_grid(copy)
    for row in range(4):
        for col in range(4):
            copy[row][col]=grid[row][col]
    return copy
def grid_equal(grid1,grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1==grid2:
        return True
    return False

    

    
        
    
    
    