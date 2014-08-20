"""ass.7, Q3- push functions for 2048.py
emma jordi
1 may 2014"""


def push_up (grid):
    """merge grid values upwards"""
    #go through columns and move values to the top if there are spaces
    
    for i in range(3):
        for row in range(1,4):
            for col in range(4):
                if grid[row-1][col]==0: #checks whether there is a zero above
                    grid[row-1][col]= grid[row][col]#if true, makes 0=block below
                    grid[row][col]=0 #makes block below = 0
                    
    #if numbers above are the same: add together(x2)        
    for row in range(1,4):
        for col in range(4):
            if grid[row-1][col]== grid[row][col]: #checks number above for equality
                grid[row-1][col]= 2 * grid[row-1][col] #makes number = number*2
                grid[row][col]=0
                
    #push up again cos 0 is created           
    for row in range(1,4):
        for col in range(4):
            if grid[row-1][col]==0:
                grid[row-1][col]= grid[row][col]
                grid[row][col]=0
                
    return grid

def push_down (grid):
    """merge grid values downwards"""
    #copy push_up(grid) but make change range. row+1
    for i in range(3):
        
        for row in range(2,-1,-1):
            for col in range(3,-1,-1):
                if grid[row+1][col] == 0:
                    grid[row+1][col] = grid[row][col]
                    grid[row][col] = 0
                
    for row in range(2,-1,-1):
        for col in range(3,-1,-1):
            if grid[row+1][col] == grid[row][col]:
                grid[row+1][col] = 2 * grid[row+1][col]
                grid[row][col] = 0
                    
    for row in range(2,-1,-1):
        for col in range(3,-1,-1):
            if grid[row+1][col] == 0:
                grid[row+1][col] = grid[row][col]
                grid[row][col] = 0
                    
    return grid    

def push_left (grid):
    """merge grid values left"""
    #merge from left to right if you move to the left
    #create array and copy row into a separate array and then copy back. 
    for i in range(3):
        
        for row in range(4):
            for col in range(1,4):
                if grid[row][col-1]==0:
                    grid[row][col-1]= grid[row][col]
                    grid[row][col]=0
                
    for row in range(4):
        for col in range(1,4):
            if grid[row][col-1]== grid[row][col]:
                grid[row][col-1]= 2 * grid[row][col-1]
                grid[row][col]=0
                    
    for row in range(4):
        for col in range(1,4):
            if grid[row][col-1]==0:
                grid[row][col-1]= grid[row][col]
                grid[row][col]=0
                    
    return grid       

def push_right (grid):
    """merge grid values right""" 
    #same as push_left except for parameters
    
    for i in range(3):
        
        for row in range(3,-1,-1):
            for col in range(2,-1,-1):
                if grid[row][col+1] == 0:
                    grid[row][col+1] = grid[row][col]
                    grid[row][col] = 0
            
    for row in range(3,-1,-1):
        for col in range(2,-1,-1):
            if grid[row][col+1] == grid[row][col]:
                grid[row][col+1] = 2 * grid[row][col+1]
                grid[row][col] = 0
                
    for row in range(3,-1,-1):
        for col in range(2,-1,-1):
            if grid[row][col+1] == 0:
                grid[row][col+1] = grid[row][col]
                grid[row][col] = 0
                
    return grid 