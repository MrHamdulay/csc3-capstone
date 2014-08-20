#Description: Functions to move the values in the rows for the 2048 game
#Name: Paul Roux RXXPAU008
#Date: 01 May 2014

def push_up (grid):
    """merge grid values upwards"""
    #Moves all non-zero values up as far as possible
    for h in range(4):
            for i in range(3):
                for j in range(4):
                    if grid[i][j]==0:
                        grid[i][j]=grid[i+1][j]
                        grid[i+1][j]=0  
    
    #Merges adjacent values of the same value                   
    for i in range(3):
        for j in range(4):
            if grid[i][j]==grid[i+1][j]:
                grid[i][j]=grid[i][j]*2
                grid[i+1][j]=0
    
    #Moves all non-zero values up as far as possible              
    for h in range(4):
        for i in range(3):
            for j in range(4):
                if grid[i][j]==0:
                    grid[i][j]=grid[i+1][j]
                    grid[i+1][j]=0          
             
            

def push_down (grid):
    """merge grid values downwards"""
    #Moves all non-zero values down as far as possible
    for h in range(4):
            for i in range(3,0,-1):
                for j in range(4):
                    if grid[i][j]==0:
                        grid[i][j]=grid[i-1][j]
                        grid[i-1][j]=0
              
    #Merges adjacent values of the same value
    for i in range(3,0,-1):
        for j in range(4):
            if grid[i][j]==grid[i-1][j]:
                grid[i][j]=grid[i][j]*2
                grid[i-1][j]=0    
    
    #Moves all non-zero values down as far as possible
    for h in range(4):
        for i in range(3,0,-1):
            for j in range(4):
                if grid[i][j]==0:
                    grid[i][j]=grid[i-1][j]
                    grid[i-1][j]=0    


def push_left (grid):
    """merge grid values left"""
    #Moves all non-zero values left as far as possible
    for h in range(4):
        for i in range(4):
            for j in range(3):
                if grid[i][j]==0:
                    grid[i][j]=grid[i][j+1]
                    grid[i][j+1]=0  
                    
    #Merges adjacent values of the same value 
    for i in range(4):
        for j in range(3):
            if grid[i][j]==grid[i][j+1]:
                grid[i][j]=grid[i][j]*2
                grid[i][j+1]=0
                
    #Moves all non-zero values left as far as possible
    for h in range(4):
        for i in range(4):
            for j in range(3):
                if grid[i][j]==0:
                    grid[i][j]=grid[i][j+1]
                    grid[i][j+1]=0    
        

def push_right (grid):
    """merge grid values right"""
    #Moves all non-zero values right as far as possible
    for h in range(4):
            for i in range(4):
                for j in range(3,0,-1):
                    if grid[i][j]==0:
                        grid[i][j]=grid[i][j-1]
                        grid[i][j-1]=0  
                    
    #Merges adjacent values of the same value  
    for i in range(4):
        for j in range(3,0,-1):
            if grid[i][j]==grid[i][j-1]:
                grid[i][j]=grid[i][j]*2
                grid[i][j-1]=0
                                        
    #Moves all non-zero values right as far as possible    
    for h in range(4):
        for i in range(4):
            for j in range(3,0,-1):
                if grid[i][j]==0:
                    grid[i][j]=grid[i][j-1]
                    grid[i][j-1]=0    