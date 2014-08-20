#Question 3
#Making the game 2048
#By:Dean de Haast

def push_up (grid):
    """merge grid values upwards"""
    #Shift all the values to as high as they can go.
    for x in range(3):
        for i in range(3,0,-1):
            for j in range(4):
                if grid[i-1][j]==0:
                    grid[i-1][j]=grid[i][j]
                    grid[i][j]=0
    #Merge like values together.
    for i in range(3):
        for j in range(4):        
            if grid[i][j]==grid[i+1][j]:
                grid[i][j]=(grid[i][j])*2
                grid[i+1][j]=0
    #Shift all the values to as high as they can go after the merge
    for x in range(3):
        for i in range(3,0,-1):
            for j in range(4):
                if grid[i-1][j]==0:
                    grid[i-1][j]=grid[i][j]
                    grid[i][j]=0     

def push_down (grid):
    """merge grid values downwards"""
    #Shift all the values to as high as they can go.
    for x in range(3):
        for i in range(2,-1,-1): 
            for j in range(4): 
                if grid[i+1][j]==0: 
                    grid[i+1][j]=grid[i][j] 
                    grid[i][j]=0
    #Merge like values together.                   
    for i in range(2,-1,-1): 
        for j in range(4): 
            if grid[i][j]==grid[i+1][j]: 
                grid[i+1][j]=(grid[i+1][j])*2
                grid[i][j]=0
    #Shift all the values to as high as they can go after the merge                
    for x in range(3):
        for i in range(2,-1,-1): 
            for j in range(4): 
                if grid[i+1][j]==0: 
                    grid[i+1][j]=grid[i][j] 
                    grid[i][j]=0       
    

def push_left (grid):
    """merge grid values left"""
    #Shift all the values as far left as they can go.
    for x in range(3):
        for i in range(4):  
            for j in range(3,0,-1):  
                if grid[i][j-1]==0: 
                    grid[i][j-1]=grid[i][j] 
                    grid[i][j]=0
    #Merge like values together.                 
    for i in range(4): 
        for j in range(3):  
            if grid[i][j]==grid[i][j+1]: 
                grid[i][j]=(grid[i][j])*2
                grid[i][j+1]=0    
        #Shift all the values as far left as they can go after the merge                                 
    for x in range(3):
        for i in range(4):  
            for j in range(3,0,-1):  
                if grid[i][j-1]==0: 
                    grid[i][j-1]=grid[i][j] 
                    grid[i][j]=0    

def push_right (grid):
    """merge grid values right"""  
    #Shift all the values as far right as they can go.
    for x in range(3):
        for i in range(4):  
            for j in range(3):  
                if grid[i][j+1]==0: 
                    grid[i][j+1]=grid[i][j] 
                    grid[i][j]=0
    #Merge like values together.                  
    for i in range(4): 
        for j in range(3):  
            if grid[i][j]==grid[i][j+1]: 
                grid[i][j]=(grid[i][j])*2
                grid[i][j+1]=0    
    #Shift all the values as far right as they can go after the merge
    for x in range(3):
        for i in range(4):  
            for j in range(3):  
                if grid[i][j+1]==0: 
                    grid[i][j+1]=grid[i][j] 
                    grid[i][j]=0    