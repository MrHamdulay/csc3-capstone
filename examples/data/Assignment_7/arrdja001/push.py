"""Assignment 7 Question4 push.py
2 May 2014 Djavan Arrigone"""

def push_up (grid): 
    """merge grid values upwards"""
    #moves grid values to max height.
    for a in range (4): 
        for i in range(3,0,-1): 
            for j in range(4): 
                if grid[i-1][j]==0: 
                    grid[i-1][j]=grid[i][j] 
                    grid[i][j]=0
    #merges exact values starting with the furthest up in the grid.  
    for i in range(3): 
        for j in range(4):         
            if grid[i][j]==grid[i+1][j]: 
                grid[i][j]=(grid[i][j])*2
                grid[i+1][j]=0
    #after merging exact values pushes to max height.            
    for a in range (4): 
        for i in range(3,0,-1): 
            for j in range(4): 
                if grid[i-1][j]==0: 
                    grid[i-1][j]=grid[i][j] 
                    grid[i][j]=0 

#The next three functions solutions are similar relating to direction of movement.
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
