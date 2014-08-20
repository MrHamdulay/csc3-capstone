#Gina Horscroft, Assignment 7
#Push

def push_up (grid):
    """merge grid values upwards"""
    x = 0
    #shuffles numbers in direction
    while (x< 4):
        x+=1
        for i in range (3):
            for j in range (4):
                if (grid[i][j] == 0):
                    #then bring up number from below
                    grid[i][j] = grid[i+1][j]
                    grid[i+1][j] = 0
    #checks if any number = number below                
    for i in range (3):
        for j in range (4):    
            if (grid[i][j] != 0 and grid[i][j]==grid[i+1][j]):
                    grid[i][j] = 2*grid[i][j]
                    grid[i+1][j] = 0  
    #fills in any blanks left if any numbers merged                
    x = 0
    while (x< 4):
        x+=1
        for i in range (3):
            for j in range (4):
                if (grid[i][j] == 0):
                    #then bring up number from below
                    grid[i][j] = grid[i+1][j]
                    grid[i+1][j] = 0    
                    
    
def push_down (grid):
    """merge grid values downwards"""
    x = 0
    #shuffles numbers in direction
    while (x< 4):
        x+=1
        for i in range (3, 0, -1):
            for j in range (4):
                if (grid[i][j] == 0):
                    #then bring up number from above
                    grid[i][j] = grid[i-1][j]
                    grid[i-1][j] = 0
    #checks if any number = number 1 down            
    for i in range (3, 0, -1):
        for j in range (4): 
            if (grid[i][j] != 0 and grid[i][j]==grid[i-1][j]):
                grid[i][j] = 2*grid[i][j]
                grid[i-1][j] = 0
    #fills in any blanks left if any numbers merged             
    x = 0
    #shuffles numbers in direction
    while (x< 4):
        x+=1
        for i in range (3, 0, -1):
            for j in range (4):
                if (grid[i][j] == 0):
                    #then bring up number from above
                    grid[i][j] = grid[i-1][j]
                    grid[i-1][j] = 0    
        
                      

def push_left (grid):
    """merge grid values left"""
    x = 0
    #shuffles numbers in direction
    while (x< 4):
        x+=1
        for i in range (4):
            for j in range (3):
                if (grid[i][j] == 0):
                    #then bring up number from below
                    grid[i][j] = grid[i][j+1]
                    grid[i][j+1] = 0
    #checks if any number = number to left               
    for i in range (4):
        for j in range (3):    
            if (grid[i][j] != 0 and grid[i][j]==grid[i][j+1]):
                grid[i][j] = 2*grid[i][j]
                grid[i][j+1] = 0                
    #fills in any blanks left if any numbers merged                     
    x = 0
    while (x< 4):
        x+=1
        for i in range (4):
            for j in range (3):
                if (grid[i][j] == 0):
                    #then bring up number from below
                    grid[i][j] = grid[i][j+1]
                    grid[i][j+1] = 0    
    

def push_right (grid):
    """merge grid values right"""  
    x = 0
    #shuffles numbers in direction
    while (x< 4):
        x+=1
        for i in range (4):
            for j in range (3, 0, -1):
                if (grid[i][j] == 0):
                    #then bring up number from above
                    grid[i][j] = grid[i][j-1]
                    grid[i][j-1] = 0
    #checks if any number = number to right
    for i in range (4):
        for j in range (3, 0, -1):        
            if (grid[i][j] != 0 and grid[i][j]==grid[i][j-1]):
                grid[i][j] = 2*grid[i][j]
                grid[i][j-1] = 0 
    #fills in any blanks left if any numbers merged 
    x = 0
    while (x< 4):
        x+=1
        for i in range (4):
            for j in range (3, 0, -1):
                if (grid[i][j] == 0):
                    #then bring up number from above
                    grid[i][j] = grid[i][j-1]
                    grid[i][j-1] = 0    
                        
   