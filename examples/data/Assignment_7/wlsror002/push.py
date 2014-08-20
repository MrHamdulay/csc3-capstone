

def push_up (grid):
    
    for a in range (4):
        for i in range(3,0,-1):
            for j in range(4):
                if grid[i-1][j]==0:
                    grid[i-1][j]=grid[i][j]
                    grid[i][j]=0
    
    for i in range(3):
        for j in range(4):        
            if grid[i][j]==grid[i+1][j]:
                grid[i][j]=(grid[i][j])*2
                grid[i+1][j]=0
            
    for a in range (4):
        for i in range(3,0,-1):
            for j in range(4):
                if grid[i-1][j]==0:
                    grid[i-1][j]=grid[i][j]
                    grid[i][j]=0 

def push_down (grid):
    
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