#The 2048 program 

def push_up (grid):
    
    #Let it loop through 3 times to move up all spaces
    for loop in range(3):
        for i in range(1,4):
            for j in range(4):
                if grid[i-1][j]==0 or grid[i-1][j]==' ':
                    grid[i-1][j]=grid[i][j]
                    grid[i][j]=0
                    
    #Check if the adjacent position is equal and then add them
    for i in range(1,4):
        for j in range(4):    
            
            if grid[i-1][j]==grid[i][j]:
                grid[i-1][j]+=grid[i][j]
                grid[i][j]=0
                
    #Must now fill up the gaps that have opened up 
    for i in range(1,4):
        for j in range(4):
            if grid[i-1][j]==0 or grid[i-1][j]==' ':
                grid[i-1][j]=grid[i][j]
                grid[i][j]=0    
    return


#Have the various loops to make sure each number is in the right place
def push_down (grid):
    for loop in range(3):
        for i in range(2,-1,-1):
            for j in range(3,-1,-1):
                if grid[i+1][j]==0 or grid[i+1][j]==' ':
                    grid[i+1][j]=grid[i][j]
                    grid[i][j]=0
    
    for i in range(2,-1,-1):
        for j in range(3,-1,-1):
            
            if grid[i+1][j]==grid[i][j]:
                grid[i+1][j]+=grid[i][j]
                grid[i][j]=0
                    
    for i in range(2,-1,-1):
        for j in range(3,-1,-1):
            if grid[i+1][j]==0 or grid[i+1][j]==' ':
                grid[i+1][j]=grid[i][j]
                grid[i][j]=0            
    
    return grid




def push_left (grid):
    for loop in range(3):
        
        for i in range(4):
            for j in range(1,4):
                if grid[i][j-1]==0 or grid[i][j-1]==' ':
                    grid[i][j-1]=grid[i][j]
                    grid[i][j]=0
                    
                    
    for i in range(4):
        for j in range(1,4):            
            
            if grid[i][j-1]==grid[i][j]:
                grid[i][j-1]+=grid[i][j]
                grid[i][j]=0
                
    for i in range(4):
        for j in range(1,4):
            if grid[i][j-1]==0 or grid[i][j-1]==' ':
                grid[i][j-1]=grid[i][j]
                grid[i][j]=0            

    return grid



def push_right (grid):
    
    for loop in range(3):
    
        for i in range(3,-1,-1):
            for j in range(2,-1,-1):
                if grid[i][j+1]==0 or grid[i][j+1]==' ':
                    grid[i][j+1]=grid[i][j]
                    grid[i][j]=0
                   
    for i in range(3,-1,-1):
        for j in range(2,-1,-1):    
            
            if grid[i][j+1]==grid[i][j]:
                grid[i][j+1]+=grid[i][j]
                grid[i][j]=0
                
    for i in range(3,-1,-1):
        for j in range(2,-1,-1):
            if grid[i][j+1]==0 or grid[i][j+1]==' ':
                grid[i][j+1]=grid[i][j]
                grid[i][j]=0            
                
    return grid

