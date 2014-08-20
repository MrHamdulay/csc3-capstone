"""2048 game (Question 3)
1 May 2014
Jaren Hendricks"""

"""Function to merge grid values and to push values upwards"""
def push_up (grid):
    for k in range (4):
        for i in range(3,0,-1):
            for j in range(4):
                if grid[i-1][j]==0:
                    grid[i-1][j]=grid[i][j]
                    grid[i][j]=0
    
    # Combines values that are the same
    for i in range(3):
        for j in range(4):        
            if grid[i][j]==grid[i+1][j]:
                grid[i][j]=(grid[i][j])*2
                grid[i+1][j]=0
                
    # Values shifted upwards           
    for k in range (4):
        for i in range(3,0,-1):
            for j in range(4):
                if grid[i-1][j]==0:
                    grid[i-1][j]=grid[i][j]
                    grid[i][j]=0 
                    
""" Function to merge grid values and to push values downwards"""
def push_down (grid):
    for k in range(4):
        for i in range(2,-1,-1):
            for j in range(4):
                if grid[i+1][j]==0:
                    grid[i+1][j]=grid[i][j]
                    grid[i][j]=0
                    
    # Combines values that are the same
    for i in range(2,-1,-1):
        for j in range(4):
            if grid[i][j]==grid[i+1][j]:
                grid[i+1][j]=(grid[i+1][j])*2
                grid[i][j]=0
                
    # Values shifted downwards 
    for k in range(4):
        for i in range(2,-1,-1):
            for j in range(4):
                if grid[i+1][j]==0:
                    grid[i+1][j]=grid[i][j]
                    grid[i][j]=0   
                    
""" Function to merge grid values and to push values to the left"""
def push_left (grid):
    for k in range(4):
        for i in range(4): 
            for j in range(3,0,-1): 
                if grid[i][j-1]==0:
                    grid[i][j-1]=grid[i][j]
                    grid[i][j]=0
                    
    # Combines values that are the same
    for i in range(4):
        for j in range(3): 
            if grid[i][j]==grid[i][j+1]:
                grid[i][j]=(grid[i][j])*2
                grid[i][j+1]=0    
                                   
    # Values shifted to the left 
    for k in range(4):
        for i in range(4): 
            for j in range(3,0,-1): 
                if grid[i][j-1]==0:
                    grid[i][j-1]=grid[i][j]
                    grid[i][j]=0
            

""" Function to merge grid values and to push values to the right"""
def push_right (grid):   
    for k in range(4):
        for i in range(4):
            for j in range(3): 
                if grid[i][j+1]==0:
                    grid[i][j+1]=grid[i][j]
                    grid[i][j]=0

    # Combines values that are the same                
    for i in range(4):
            for j in range(3,0,-1): 
                if grid[i][j]==grid[i][j-1]:
                    grid[i][j]=(grid[i][j])*2
                    grid[i][j-1]=0
    
    # Values shifted to the right                 
    for k in range(4):
        for i in range(4):
            for j in range(3): 
                if grid[i][j+1]==0:
                    grid[i][j+1]=grid[i][j]
                    grid[i][j]=0    