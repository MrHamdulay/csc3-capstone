# Aaron Krishna
# 02 May 2014
# 2048 Game

def push_up (grid): #funtion that combines values if pushed up
    for a in range (4): #pushes the values up to their maximum heights
        for i in range(3,0,-1):
            for j in range(4):
                if grid[i-1][j]==0:
                    grid[i-1][j]=grid[i][j]
                    grid[i][j]=0
                    
    for i in range(3): #combines like values, starting with the upper-most similar value
        for j in range(4):        
            if grid[i][j]==grid[i+1][j]:
                grid[i][j]=(grid[i][j])*2
                grid[i+1][j]=0
               
    for a in range (4): #push the values up to their maximum heights after the combining
        for i in range(3,0,-1):
            for j in range(4):
                if grid[i-1][j]==0:
                    grid[i-1][j]=grid[i][j]
                    grid[i][j]=0 

def push_down (grid): #same concept as push_up but just pushed down
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
                    
def push_left (grid): #same concept as push_up but just pushed left
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
            
def push_right (grid): #same concept as push_up but just pushed right  
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