#Dhriven Hamlall

def push_up (grid):
    """merge grid values upwards"""
    for t in range (3):
        
        for i in range(3):
            for k in range(4):
                if grid[i][k] == 0:
                    grid[i][k] = grid[i+1][k]#makes the top...the bottom number 
                    grid[i+1][k] = 0 #setting bottom number to 0 as this has to be the case (basis for the game) 
    #everythime a number moves where the number was will then contain a 0 which we dont actually see in the game 
    for i in range(3):
        for k  in range (4):
            if grid[i][k] == grid[i+1][k]:
                grid[i][k] *= 2 #if equal then doubles
                grid[i+1][k] = 0 #setting bottom number to 0
         
         
    for t in range (3):#assures everything moves to the right even after adding for e.g 2+2
        
        for i in range(3):
            for k in range(4):
                if grid[i][k] == 0:
                    grid[i][k] = grid[i+1][k]
                    grid[i+1][k] = 0                
#=====================================================================================================================
def push_down (grid):
    """merge grid values downwards"""
    for t in range (3):
        
        for i in range(3):
            for k in range(4):
                if (grid[i+1][k] == 0):
                    grid[i+1][k] = grid[i][k]
                    grid[i][k] = 0
                
    for i in range(3, 0, -1):
        for k  in range (4):
            if grid[i][k] == grid[i-1][k]:
                grid[i][k] *= 2
                grid[i-1][k] = 0  
                
    for t in range (3):
        
        for i in range(3):
            for k in range(4):
                if (grid[i+1][k] == 0):
                    grid[i+1][k] = grid[i][k]
                    grid[i][k] = 0
#=====================================================================================================================                
def push_left (grid):
    """merge grid values left"""
    for t in range (3):
        
        for i in range(4):
            for j in range(3):
                if grid[i][j] == 0:
                    grid[i][j] = grid[i][j+1]
                    grid[i][j+1] = 0
                    
    for i in range(4):
        for j in range (3):
            if grid[i][j] == grid[i][j+1]:
                grid[i][j] = grid[i][j] * 2 #same as grid[i][k] *= 2
                grid[i][j+1] = 0
            
          
    for t in range (3):
        
        for i in range(4):
            for j in range(3):
                if grid[i][j] == 0:
                    grid[i][j] = grid[i][j+1]
                    grid[i][j+1] = 0    
    
#=====================================================================================================================  
def push_right (grid):
    """merge grid values right"""
    for t in range (4):
        
        for i in range(4):
            for j in range(3, 0, -1):
                if grid[i][j] == 0: 
                    grid[i][j] = grid[i][j-1] 
                    grid[i][j-1] = 0
                    
    for i in range(4):
        for j in range (3):
            if grid[i][j] == grid[i][j+1]:
                grid[i][j] = grid[i][j] * 2
                grid[i][j+1] = 0
                
    
    for t in range (4):
        
        for i in range(4):
            for j in range(3, 0, -1):
                if grid[i][j] == 0:
                    grid[i][j] = grid[i][j-1]
                    grid[i][j-1] = 0 