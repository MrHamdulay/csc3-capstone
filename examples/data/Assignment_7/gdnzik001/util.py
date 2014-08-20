"""module of functions to manipulate 2d arrays of size 4x4
Zikho Godana
29 april 2014"""
import copy
grid = []
height= 4

def create_grid(grid):
    """create a 4x4 grid"""
    
    for i in range(height):
        grid.append([0]*height)
    
    
def print_grid(grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    gap=1
    output = "{0:<5}"
    print("+","-"*20,"+",sep="")
    for row in range (height):
        print("|",end="")
        for col in range (height): 
            if grid[row][col]==0:
                print(output.format(" "),end="")
            else:
                print (output.format(grid[row][col]),end="")
                
        print("|")
    print("+","-"*20,"+",sep="")
    
def check_lost(grid):
    """return True if the are no 0 values and adjacent values that are equal; otherwise False"""
   
    for row in range(height):
        if 0 in grid[row]:
            return False
        for col in range(height):
            #if row>0 and grid[row][col]==grid[row-1][col]:
               # return False
            if grid[row][col]==grid[row-1][col]:
                return False
                
            else:
                return True
    
        
def check_won(grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    won=False
    for row in range(height):
        for col in range(height):
            if grid[row][col]>=32:
                won=True
                break
            else:
                continue
    return won

def copy_grid(grid):
    """return a copy of the grid"""
    #copy grid to grid2 such that grid2 is not affected by a change in grid
    grid2=copy.deepcopy(grid) 
    return grid2

def grid_equal(grid1,grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1==grid2:
        return True
    else:
        return False
    