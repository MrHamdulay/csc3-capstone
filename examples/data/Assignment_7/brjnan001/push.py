"""To create game '2048'
Nandani Birjanund
27 April"""

import util
def push_up (grid):
    """merge grid values upwards"""
    for i in range (3):   
        for row in range(1,4):
            for col in range(4):
                if grid[row-1][col] == grid[row-1][col] ==0:
                    grid[row-1][col] = grid[row][col]
                    grid[row][col] = 0
                   
    for row in range(1,4):
        for col in range(4):
            if grid[row-1][col] == grid[row][col]:
                grid[row-1][col] = grid[row-1][col] *2
                grid[row][col] =0
                
    for row in range(1,4):
        for col in range(4):
            if grid[row-1][col]== grid[row-1][col]==0:
                grid[row-1][col] = grid[row][col]
                grid[row][col]=0
            
    return grid

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
        for row in range(4):
            for col in range(1,4):
                if grid[row][col-1] == grid[row][col-1] ==0:
                    grid[row][col-1] = grid[row][col]
                    grid[row][col] = 0
                      
    for row in range(4):
        for col in range(1,4):
            if grid[row][col-1] == grid[row][col]:
                grid[row][col-1] = grid[row][col-1] *2
                grid[row][col] =0
                   
    for row in range(4):
        for col in range(1,4):
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