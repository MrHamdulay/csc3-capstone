'''Write a module of utility functions (called util.py) to manipulate 2-dimensional arrays of size 4x4
Sinead Urioshn
27 April 2014
'''

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range (4):
        grid.append([0]*4)
        
    return grid

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    #5 width columns
    txt='{0:<5}'
    #print 2d array
    #print frame
    print("+"+"-"*20+"+")
    
    for row in range(4):
        #set frame at start
        frame="|"
        for col in range(4):
            if grid[row][col]==0:	
                grid[row][col]=' '            
            print(frame+txt.format(grid[row][col]),end="")
            
            #change frame so that it indeed only prints character at beginning
            frame=""
            
        #get frame at end
        print("|")
    print("+"+"-"*20+"+")

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    #set flag
    check=True
    #loop and compare adjacent values
    for row in range(4):
        #loop 1 less for column because only want to check adjacent pairs with each other once 
        #This makes each column pair (for that column) that needs to be checked to be 3
        #we cannot go beyond index boundary
        for col in range(3):
            #check if 0 values
            if grid[row][col]==0:check=False
            if grid[row][col]==grid[row][col+1]:
                check=False
    #loop 1 less for row because only want to check adjacent pairs with each other once 
    #each value must be compared with that directly underneath it
    #we cannot go beyond index boundary
    #so row range must be 1 less
    for row in range(3):
        for col in range(4):
            if grid[row][col]==grid[row+1][col]:
                check=False 
    return check

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    #set flag
    check=False
    #loop through columns and rows to check for values>=32
    for row in range(4):
        for col in range(4):
            if grid[row][col]>=32:check=True
    return check

def copy_grid (grid):
    """return a copy of the grid"""
    #set empty list
    copy=[]
    #make 2d list with 0 values
    for i in range (4):
        copy.append([0]*4)  
    #loop through rows and columns to copy values of original grid to copy
    for row in range(4):
        for col in range(4):
            copy[row][col]=grid[row][col]
    return copy

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    #set flag
    check=True
    #loop through rows and columns
    #check for inequality which means two grids not same
    for row in range(4):
        for col in range(4):    
            if grid1[row][col]!=grid2[row][col]:
                check=False
    return check