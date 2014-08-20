#Author: NLXALE001
#Date: 30 April 2014
#Assignment 7

import util

def push_up (grid):
    """merge grid values upwards"""
    grid = spaceup (grid) #get rid of spaces
    grid = spaceup (grid)
    grid = spaceup (grid)
    for i in range (0,3):       
        for j in range (0,4):
            #check if the value next to it is equal to it and must be merged
            if grid[i][j]==grid[i+1][j]:
                grid[i][j] = grid[i][j]*2
                grid[i+1][j] = 0
                grid = spaceup (grid) #get rid of spaces
                grid = spaceup (grid)
                grid = spaceup (grid)
    return (grid)

def push_down (grid):
    """merge grid values downwards"""    
    grid = spacedown (grid) #get rid of spaces
    grid = spacedown (grid)
    grid = spacedown (grid)
    for i in range (3,0,-1):       
        for j in range (0,4): 
            #check if the value next to it is equal to it and must be merged
            if grid[i][j]==grid[i-1][j]:
                grid[i][j] = grid[i][j]*2
                grid[i-1][j] = 0
                grid = spacedown (grid) #get rid of spaces
    return (grid)
    
def push_left (grid):
    """merge grid values left"""
    grid = spaceleft (grid) #get rid of spaces
    grid = spaceleft (grid)
    grid = spaceleft (grid)
    for i in range (0,4):       
        for j in range (0,3): 
            #check if the value next to it is equal to it and must be merged
            if grid[i][j]==grid[i][j+1]:
                grid[i][j] = grid[i][j]*2
                grid[i][j+1] = 0
                grid = spaceleft (grid) #get rid of spaces 
    return (grid)

def push_right (grid):
    """merge grid values right"""  
    grid = spaceright (grid) #get rid of spaces
    grid = spaceright (grid)
    grid = spaceright (grid)
    for i in range (0,4):       
        for j in range (3,1,-1): 
            #check if the value next to it is equal to it and must be merged
            if grid[i][j]==grid[i][j-1]:
                grid[i][j] = grid[i][j]*2
                grid[i][j-1] = 0
                grid = spaceright (grid) #get rid of spaces
    return (grid)
    
def spaceup (grid):
    """remove all spaces in the grid when pushed"""
    for i in range (0,4):
        for j in range (0,4):
            if grid[i][j]==0 or grid[i][j]=='':
                for m in range (i,3):
                    grid[m][j]=grid[m+1][j]
                grid[3][j]=0
            if grid[i][j]==0 or grid[i][j]=='' and i<3:
                for m in range (i,2):
                    grid[m][j]=grid[m+1][j]
                grid[3][j]=0 
            if grid[i][j]==0 or grid[i][j]=='' and i<2:
                for m in range (i,1):
                    grid[m][j]=grid[m+1][j]
                grid[3][j]=0 
    return (grid)

def spacedown (grid):
    """remove all spaces in the grid when pushed"""    
    for i in range (3,-1,-1):
        for j in range (0,4):
            if grid[i][j]==0 or grid[i][j]=='':
                for m in range (i,0,-1):
                    grid[m][j]=grid[m-1][j]
                grid[0][j]=0
            if grid[i][j]==0 or grid[i][j]=='' and i>1:
                for m in range (i,0,-1):
                    grid[m][j]=grid[m-1][j]
                grid[0][j]=0
            if grid[i][j]==0 or grid[i][j]=='' and i>2:
                for m in range (i,0,-1):
                    grid[m][j]=grid[m-1][j]
                grid[0][j]=0
    return (grid)

def spaceright (grid):
    """remove all spaces in the grid when pushed"""   
    for i in range (0,4):
        for j in range (3,-1,-1):
            if grid[i][j]==0 or grid[i][j]=='':
                for m in range (j,0,-1):
                    grid[i][m]=grid[i][m-1]
                grid[i][0]=0 
            if grid[i][j]==0 or grid[i][j]=='' and j>1:
                for m in range (j,0,-1):
                    grid[i][m]=grid[i][m-1]
                grid[i][0]=0 
            if grid[i][j]==0 or grid[i][j]=='' and j>2:
                for m in range (j,0,-1):
                    grid[i][m]=grid[i][m-1]
                grid[i][0]=0 
    return (grid)

def spaceleft (grid):
    """remove all spaces in the grid when pushed"""   
    for i in range (0,4):
        for j in range (0,4):
            if grid[i][j]==0 or grid[i][j]=='':
                for m in range (j,3):
                    grid[i][m]=grid[i][m+1]
                grid[i][3]=0 
            if grid[i][j]==0 or grid[i][j]=='' and j<3:
                for m in range (j,3):
                    grid[i][m]=grid[i][m+1]
                grid[i][3]=0 
            if grid[i][j]==0 or grid[i][j]=='' and j<2:
                for m in range (j,3):
                    grid[i][m]=grid[i][m+1]
                grid[i][3]=0 
    return (grid)
