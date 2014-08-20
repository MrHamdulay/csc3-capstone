#Vhrjoc001
#the fucntions used to create 2048 plus the util
#Assignment 7 Question 3
 
#the movemtnt of up
def push_up (grid): 
    """merge grid values upwards"""
    for a in range (4): 
        for i in range(3,0,-1): 
            for j in range(4): 
                if grid[i-1][j]==0: 
                    grid[i-1][j]=grid[i][j] 
                    grid[i][j]=0
    #joining like numbers 
    for i in range(3): 
        for j in range(4):         
            if grid[i][j]==grid[i+1][j]: 
                grid[i][j]=(grid[i][j])*2
                grid[i+1][j]=0
    #pafter adding the numbers continue to move them            
    for a in range (4): 
        for i in range(3,0,-1): 
            for j in range(4): 
                if grid[i-1][j]==0: 
                    grid[i-1][j]=grid[i][j] 
                    grid[i][j]=0 
#The next three are the same 
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