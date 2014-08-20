#Assignment 7
#Question 3


def push_up (grid):
    for loop in range(3): 
        for i in range(1,4):
            for j in range(4):
                if grid[i-1][j]==0 or grid[i-1][j]==' ':
                    grid[i-1][j]=grid[i][j]
                    grid[i][j]=0
                    
    
    for i in range(1,4):
        for j in range(4):    
            if grid[i-1][j]==grid[i][j]:
                grid[i-1][j]+=grid[i][j]
                grid[i][j]=0
    
    for i in range(1,4):
        for j in range(4):
            if grid[i-1][j]==0 or grid[i-1][j]==' ':
                grid[i-1][j]=grid[i][j]
                grid[i][j]=0    
    return grid



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

