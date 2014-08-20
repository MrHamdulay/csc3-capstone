"""Question 2 - utilities for 2048 program
Jembe Moran
28 April 2014"""
import copy #to use deepcopy function
def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4): #loop addition of 0's
        grid.append([0]*4) #append lists of 0 0 0 0 to empty list 
    return grid

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+", "-"*20, "+", sep="")
    tempgrid=copy.deepcopy(grid) #to ensure that original grade maintains 0's, but to print spaces
    for row in range(4):
        print("|", end="") #border
        for col in range(4):
            if tempgrid[row][col]==0: #if zero print empty string
                tempgrid[row][col]=" "
            tempprint="{0:<5}".format(tempgrid[row][col]) #format 5 spaces after each value
            print(tempprint, end="") #print grid
        print("|") #border
    print("+", "-"*20, "+", sep="") #borxer

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    global tempgrid
    tempgrid=grid
    for row in range(4):
        for col in range(4):
            if grid[row][col]==0: #if there is a 0, you cannot lose, therefore break out and return False
                return False
            if check_adjacent(row, col) is True: #checks if adjacent values equal
                return False
    else: return True #after checking all values for adjacent or 0's, and no result, player has lost
    

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for row in range(4): #loop through values
        for col in range(4):
            if grid[row][col]>=32: #check for item in grid that satisfy winning condition
                return True
    else: return False

def copy_grid (x):
    """return a copy of the grid"""
    return copy.deepcopy(x) #copy entire grid, hardcoded copy

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    for row in range(4):
        for col in range(4):
            if grid1[row][col]!=grid2[row][col]: #if any difference
                return False
    else: return True #if no difference

if __name__=="__main__": #testing program
    grid = []    
    create_grid (grid)    
    print_grid(grid)
    
#"{0:<10}".format(name)

def check_adjacent(x,y):
    grid=tempgrid #get grid from check_lost function
    if 0<x<3 and 0<y<3: #therefore you can check all four sides
        if grid[x][y]==grid[x+1][y] or grid[x][y]==grid[x-1][y] or grid[x][y]==grid[x][y+1] or grid[x][y]==grid[x][y-1]: #check all four sides (above, below, to the right, to the left for equality)
            return True
    elif x==0 and 0<y<3: #if you cannot check to the left
        if grid[x][y]==grid[x+1][y] or grid[x][y]==grid[x][y+1] or grid[x][y]==grid[x][y-1]:
            return True
    elif x==3 and 0<y<3: #if you cannot check to the right
        if grid[x][y]==grid[x-1][y] or grid[x][y]==grid[x][y+1] or grid[x][y]==grid[x][y-1]:
            return True
    elif y==0 and 0<x<3: #if you cannot check above
        if grid[x][y]==grid[x+1][y] or grid[x][y]==grid[x-1][y] or grid[x][y]==grid[x][y+1]:
            return True
    elif y==3 and 0<x<3: #if you cannot check below
        if grid[x][y]==grid[x+1][y] or grid[x][y]==grid[x-1][y] or grid[x][y]==grid[x][y-1]:
            return True
    elif x==0 and y==0: #if you cannot check left and above
        if grid[x][y]==grid[x+1][y] or grid[x][y]==grid[x][y+1]:
            return True
    elif x==0 and y==3: #if you cannot check left and below
        if grid[x][y]==grid[x+1][y] or grid[x][y]==grid[x][y-1]:
            return True
    elif x==3 and y==0: #if you cannot check right and above
        if grid[x][y]==grid[x-1][y] or grid[x][y]==grid[x][y+1]:
            return True
    elif x==3 and y==3: #if you cannot check right and below
        if grid[x][y]==grid[x-1][y] or grid[x][y]==grid[x][y-1]:
            return True
    else: return False