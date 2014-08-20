"""thrianka naidoo
ndxthr005
assignment 7: q3, 2048"""

import util
height = 4

def push_up (grid):
    """merge grid values upwards"""
    for i in range (3):                                 #itertion 
        for row in range(1,height):                     #iterates through rows and columns
            for col in range(height):
                if grid[row-1][col] == grid[row-1][col] == 0:
                    grid[row-1][col] = grid[row][col]   # row-1, merges and moves data upwards
                    grid[row][col] = 0                  #changes grid value to 0
                   
    for row in range(1,height):
        for col in range(height):
            if grid[row-1][col] == grid[row][col]:
                grid[row-1][col] = grid[row-1][col] *2  #multplies by 2 
                grid[row][col] = 0
                
    for row in range(1,height):
        for col in range(height):
            if grid[row-1][col]== grid[row-1][col]==0:
                grid[row-1][col] = grid[row][col]
                grid[row][col]= 0
            
    return grid                                         #reproduces the gride once, complete

def push_down (grid):
    """merge grid values downwards"""
    for i in range (3):
        for row in range(2,-1,-1):
            for col in range(3,-1,-1):
                if grid[row+1][col] == grid[row+1][col] ==0:
                    grid[row+1][col] = grid[row][col]
                    grid[row][col] = 0
                      
    for row in range(2,-1,-1):
        for col in range(3,-1,-1):
            if grid[row+1][col] == grid[row][col]:
                grid[row+1][col] = grid[row][col] *2
                grid[row][col] =0
                   
    for row in range(2,-1,-1):
        for col in range(3,-1,-1):
            if grid[row+1][col]== grid[row+1][col]==0:
                grid[row+1][col] = grid[row][col]
                grid[row][col]=0 
                
    return grid

def push_left (grid):
    """merge grid values left"""
    for i in range (3):
        for row in range(height):
            for col in range(1,height):
                if grid[row][col-1] == grid[row][col-1] ==0:
                    grid[row][col-1] = grid[row][col]
                    grid[row][col] = 0
                      
    for row in range(height):
        for col in range(1,height):
            if grid[row][col-1] == grid[row][col]:
                grid[row][col-1] = grid[row][col-1] *2
                grid[row][col] =0
                   
    for row in range(height):
        for col in range(1,height):
            if grid[row][col-1]== grid[row][col-1]==0:
                grid[row][col-1] = grid[row][col]
                grid[row][col]=0    
    return grid

def push_right (grid):
    """merge grid values right""" 
    for i in range (3):
        for row in range(3,-1,-1):
            for col in range(2,-1,-1):
                if grid[row][col+1] == grid[row][col+1] ==0:
                    grid[row][col+1] = grid[row][col]
                    grid[row][col] = 0
                      
    for row in range(3,-1,-1):
        for col in range(2,-1,-1):
            if grid[row][col+1] == grid[row][col]:
                grid[row][col+1] = grid[row][col+1] *2
                grid[row][col] =0
                   
    for row in range(3,-1,-1):
        for col in range(2,-1,-1):
            if grid[row][col+1]== grid[row][col+1]==0:
                grid[row][col+1] = grid[row][col]
                grid[row][col]=0    
                
    return grid