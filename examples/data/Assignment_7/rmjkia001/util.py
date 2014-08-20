"""Util program for a grid test
Kiara Ramjith
April 2014"""
import copy
def create_grid(grid):
    """create a 4x4 grid"""
    grid.append([0,0,0,0]) #appends the grid with a list of 0s
    grid.append([0,0,0,0])
    grid.append([0,0,0,0])
    grid.append([0,0,0,0])
    return grid
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    gridc=copy.deepcopy(grid)
    for row in range (len(gridc)):        #Checks if there are 0 values and makes them an empty string
            for col in range(len(gridc)):    
                if gridc[row][col]==0:
                    gridc[row][col]=''
    print("+--------------------+") #prints the grid neatly
    print("|"+"{0:<5}{1:<5}{2:<5}{3:<5}".format(gridc[0][0],gridc[0][1],gridc[0][2],gridc[0][3])+"|")
    print("|"+"{0:<5}{1:<5}{2:<5}{3:<5}".format(gridc[1][0],gridc[1][1],gridc[1][2],gridc[1][3])+"|")
    print("|"+"{0:<5}{1:<5}{2:<5}{3:<5}".format(gridc[2][0],gridc[2][1],gridc[2][2],gridc[2][3])+"|")
    print("|"+"{0:<5}{1:<5}{2:<5}{3:<5}".format(gridc[3][0],gridc[3][1],gridc[3][2],gridc[3][3])+"|")
    print("+--------------------+")
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False
    for row in range (len(grid)):
        if(row==0 or row ==3): #if it at the end or the grid there are certain numbers that work
            continue
        for col in range(len(grid)):
            if(col==0 or col==3): #if it at the end or the grid, move on
                continue
            elif(grid[row][col]==0):
                return False            
            elif(grid[row][col]==grid[row][col+1]): #checks all the numbers around the current value
                return False
            elif(grid[row][col]==grid[row][col-1]):
                return False            
            elif(grid[row][col]==grid[row+1][col]):
                return False
            elif(grid[row][col]==grid[row-1][col]):
                return False
    else:
        return True"""
    height=4
    for row in range (height):
        for col in range (height):
            if grid[row][col]==0:
                return False
    if grid[0][0]==grid[0][1] or grid[0][0]==grid[1][0]:
        return False
    if grid[0][3]==grid[0][2] or grid[0][3]==grid[1][3]:
        return False
    if grid[3][0]==grid[2][0] or grid[3][0]==grid[3][1]:
        return False
    if grid[3][3]==grid[3][2] or grid[3][3]==grid[2][3]:
        return False
    if grid[0][1]==grid[0][2] or grid[0][1]==grid[1][1]:
        return False
    if grid[0][2]==grid[1][2]:
        return False
    if grid[1][0]==grid[1][1] or grid[1][0]==grid[2][0]:
        return False
    if grid[2][0]==grid[2][1]:
        return False
    if grid[3][1]==grid[2][1] or grid[3][1]==grid[3][2]:
        return False
    if grid[3][2]==grid[2][2]:
        return False
    if grid[2][3]==grid[2][2] or grid[2][3]==grid[1][3]:
        return False
    if grid[1][3]==grid[1][2]:
        return False
    if grid[1][1]==grid[1][2] or grid[1][1]==grid[2][1]:
        return False
    if grid[2][1]==grid[2][2]:
        return False
    if grid[1][2]==grid[2][2]:
        return False
    else:
        return True    
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for row in range (len(grid)): # goes through the grid to find a high number
        for col in range(len(grid)): 
            if (grid[row][col]==0):
                continue
            if (grid[row][col]>=32):
                return True
    else:
        return False
def copy_grid (grid):
    """return a copy of the grid"""
    gridCopy=copy.deepcopy(grid) #returns a copy of the grid that has a different id
    return gridCopy
 
def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1==grid2: #checks if two grids are equal
        return True
    else:
        return False
