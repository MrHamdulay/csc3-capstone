"""Assignment 7 Question 3
30 April 2014
Jordan Kadish, 2048 Game Functions"""

def push_up (grid):
    """merge grid values upwards"""
    #push the values up to their maximum heights
    for a in range (4):
        for i in range(3,0,-1):
            for j in range(4):
                if grid[i-1][j]==0:
                    grid[i-1][j]=grid[i][j]
                    grid[i][j]=0
    #fuse like values, starting with the upper-most similar value
    for i in range(3):
        for j in range(4):        
            if grid[i][j]==grid[i+1][j]:
                grid[i][j]=(grid[i][j])*2
                grid[i+1][j]=0
    #push the values up to their maximum heights after the fuse            
    for a in range (4):
        for i in range(3,0,-1):
            for j in range(4):
                if grid[i-1][j]==0:
                    grid[i-1][j]=grid[i][j]
                    grid[i][j]=0 
#The next three functions follow the same algorithm as the first
def push_down (grid):
    """merge grid values downwards"""
    for a in range(4):
        for i in range(2,-1,-1):
            for j in range(4):
                if grid[i+1][j]==0:
                    grid[i+1][j]=grid[i][j]
                    grid[i][j]=0
                    
    for i in range(2,-1,-1):
        for j in range(4):
            if grid[i][j]==grid[i+1][j]:
                grid[i+1][j]=(grid[i+1][j])*2
                grid[i][j]=0
                
    for a in range(4):
        for i in range(2,-1,-1):
            for j in range(4):
                if grid[i+1][j]==0:
                    grid[i+1][j]=grid[i][j]
                    grid[i][j]=0   
                    
def push_left (grid):
    """merge grid values left"""
    for a in range(4):
        for i in range(4): 
            for j in range(3,0,-1): 
                if grid[i][j-1]==0:
                    grid[i][j-1]=grid[i][j]
                    grid[i][j]=0
                    
    for i in range(4):
        for j in range(3): 
            if grid[i][j]==grid[i][j+1]:
                grid[i][j]=(grid[i][j])*2
                grid[i][j+1]=0    
                                   
    for a in range(4):
        for i in range(4): 
            for j in range(3,0,-1): 
                if grid[i][j-1]==0:
                    grid[i][j-1]=grid[i][j]
                    grid[i][j]=0
            
def push_right (grid):
    """merge grid values right"""    
    for a in range(4):
        for i in range(4):
            for j in range(3): 
                if grid[i][j+1]==0:
                    grid[i][j+1]=grid[i][j]
                    grid[i][j]=0
    for i in range(4):
            for j in range(3,0,-1): 
                if grid[i][j]==grid[i][j-1]:
                    grid[i][j]=(grid[i][j])*2
                    grid[i][j-1]=0
    for a in range(4):
        for i in range(4):
            for j in range(3): 
                if grid[i][j+1]==0:
                    grid[i][j+1]=grid[i][j]
                    grid[i][j]=0    