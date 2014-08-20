#module that consists of a set of merging functions that merge adjacent equal values and eliminate gaps
#Ali Goldstein
#2 May 2014

def push_up (grid):
    """merge grid values upwards"""
    for i in range(3,0,-1):
        for j in range(4):
            if grid[i-1][j]==0:
                grid[i-1][j]=grid[i][j]
                grid[i][j]=0
            elif grid[i-1][j]==grid[i][j]:
                grid[i-1][j]+=grid[i][j]
                grid[i][j]=0    

def push_down (grid):
    """merge grid values downwards"""
    for i in range(3):
        for j in range(4):
            if grid[i+1][j]==0:
                grid[i+1][j]=grid[i][j]
                grid[i][j]=0
            elif grid[i+1][j]==grid[i][j]:
                grid[i+1][j]+=grid[i][j]
                grid[i][j]=0
                                
    

def push_left (grid):
    """merge grid values left"""
    for i in range(4):
        for j in range(3,0,-1):
            if grid[i][j-1]==0:
                grid[i][j-1]=grid[i][j]
                grid[i][j]=0
            elif grid[i][j-1]==grid[i][j]:
                grid[i][j-1]+=grid[i][j]
                grid[i][j]=0

def push_right (grid):
    """merge grid values right""" 
    for i in range(4):
        for j in range(3):
            if grid[i][j+1]==0:
                grid[i][j+1]=grid[i][j]
                grid[i][j]=0
            elif grid[i][j+1]==grid[i][j]:
                grid[i][j+1]+=grid[i][j]
                grid[i][j]=0    