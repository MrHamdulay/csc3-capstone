#shane horsley
#functions to be used in provided program

def push_up (grid):
    #3 STEPS shift, add, shift 
    def clearzero(): #shift all values upwards if there are open spaces above them
        for i in range(4):
            for row in range (3): 
                for col in range (4):
                    if grid[row][col]==0:
                        grid[row+1][col], grid[row][col]=grid[row][col], grid[row+1][col]
    clearzero()                 
              
    for row in range (3): #add numbers if the above number is equal
        for col in range (4):    
            if grid[row][col]==grid[row+1][col]:
                grid[row][col]+=grid[row][col]
                grid[row+1][col]=0    
                                    
    clearzero()   #move values upwards if there are open spaces above them
        
    return grid            

def push_down (grid):
   #repeat process as above but shifting down
    def clearzero():
        for i in range(4):
            for row in range (3,0,-1): 
                for col in range (4):
                    if grid[row][col]==0:
                        grid[row-1][col],grid[row][col]=grid[row][col],grid[row-1][col]
    clearzero()
    for row in range (3,0,-1): 
        for col in range (4):    
            if grid[row][col]==grid[row-1][col]:
                grid[row][col]+=grid[row][col]
                grid[row-1][col]=0      
    clearzero()
    
    return grid    

def push_left (grid):
   #same process shifting left now
    def clearzero():
        for i in range(4):
            for row in range (4): 
                for col in range (3):
                    if grid[row][col]==0:
                        grid[row][col+1],grid[row][col]=grid[row][col],grid[row][col+1]
    clearzero()
    for row in range (4): 
        for col in range (3):    
            if grid[row][col]==grid[row][col+1]:
                grid[row][col]+=grid[row][col]
                grid[row][col+1]=0                
    clearzero()    
    return grid

def push_right (grid):
    #same process shifting right 
    def clearzero():
        for i in range(4):
            for row in range (4):
                for col in range (3,0,-1):
                    if grid[row][col]==0:
                        grid[row][col-1],grid[row][col]=grid[row][col],grid[row][col-1]
    clearzero()

    for row in range (4): 
        for col in range (3,0,-1):    
            if grid[row][col]==grid[row][col-1]:
                grid[row][col]+=grid[row][col]
                grid[row][col-1]=0
    
    clearzero()
        
    return grid