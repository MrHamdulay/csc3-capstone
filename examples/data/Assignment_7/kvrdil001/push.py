#Dilan Koovarjee
#1 May 2014
#2048

def push_up (grid):
    
    for i in range (3): #rid of spaces 
        for x in range (1,4): #x for rows
            for y in range (4): #y for columns
                if grid[x-1][y]==" " or grid[x-1][y]==0:
                    grid[x-1][y]=grid[x][y]
                    grid[x][y]=0
                       
    for x in range (1,4): #merge all like adjacent tiles
        for y in range (4):
            if grid[x-1][y]==grid[x][y]:
                grid[x-1][y]=2*grid[x-1][y]  
                grid[x][y]=0 
                
    for x in range (1,4): #rid of spaces after merging
        for y in range (4):
            if grid[x-1][y]==" " or grid[x-1][y]==0:
                grid[x-1][y]=grid[x][y]
                grid[x][y]=0   
                
                

def push_down (grid):
    
    for i in range (3): #rid of spaces 
        for x in range (2, -1, -1): 
            for y in range (4): 
                if grid[x+1][y]==" " or grid[x+1][y]==0:
                    grid[x+1][y]=grid[x][y] 
                    grid[x][y]=0 
                       
    for x in range (2, -1, -1): #merge all like adjacent tiles
        for y in range (4):
            if grid[x+1][y]==grid[x][y]:
                grid[x+1][y]=2*grid[x+1][y] 
                grid[x][y]=0 
                   
    for x in range (2, -1, -1): #rid of spaces after merging
        for y in range (4):
            if grid[x+1][y]==" " or grid[x+1][y]==0:
                grid[x+1][y]=grid[x][y]
                grid[x][y]=0  
                
                
                
def push_left (grid):
   
    for i in range (3): #rid of spaces 
        for y in range (1,4): 
            for x in range (4): 
                if grid[x][y-1]==" " or grid[x][y-1]==0:
                    grid[x][y-1]=grid[x][y] 
                    grid[x][y]=0
                        
    for y in range (1,4): #merge all like adjacent tiles
        for x in range (4):
            if grid[x][y-1]==grid[x][y]:
                grid[x][y-1]=2*grid[x][y-1] 
                grid[x][y]=0
                
    for y in range (1,4): #rid of spaces after merging 
        for x in range (4):
            if grid[x][y-1]==" " or grid[x][y-1]==0:
                grid[x][y-1]=grid[x][y]
                grid[x][y]=0  
                
                

def push_right (grid):
    
    for i in range (3): #rid of spaces 
        for y in range (2, -1, -1): 
            for x in range (4): 
                if grid[x][y+1]==" " or grid[x][y+1]==0:
                    grid[x][y+1]=grid[x][y] 
                    grid[x][y]=0 
                       
    for y in range (2, -1, -1): #merge all like adjacent tiles
        for x in range (4):
            if grid[x][y+1]==grid[x][y]:
                grid[x][y+1]=2*grid[x][y+1]
                grid[x][y]=0 
                
    for y in range (2, -1, -1): #rid of spaces after merging
        for x in range (4):
            if grid[x][y+1]==" " or grid[x][y+1]==0:
                grid[x][y+1]=grid[x][y]
                grid[x][y]=0       