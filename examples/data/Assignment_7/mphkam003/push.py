""" merge adjacent equal values and eliminate gaps
kamogelo mphela
20 april 2014"""

def push_up (grid):
    """merge grid values upwards"""
    # move each block upwards from the bottom. this must be done three times
    for num in range(3):
        for y in range(3,0,-1):
            for x in range(4):
                if grid[y-1][x] == 0:
                    grid[y-1][x] = grid[y][x]
                    grid[y][x] = 0    
     #add blocks on top of each other starting at the top              
    for y in range (3):
        for x in range (4):
            if grid[y+1][x] == grid[y][x]:
                grid[y][x] *= 2
                grid[y+1][x] = 0
     # move everyting up again           
    for num in range(3):           
        for y in range(3,0,-1):
            for x in range(4):
                if grid[y-1][x] == 0:
                    grid[y-1][x] = grid[y][x]
                    grid[y][x] = 0    
            

def push_down (grid):
    """merge grid values downwards"""
    # move everything downwards
    for num in range(3):  
        for y in range(3):
            for x in range(4):
                if grid[y+1][x] == 0:
                    grid[y+1][x] = grid[y][x]
                    grid[y][x] = 0
                    
   # add adjacent values            
    for y in range (3,0,-1):
        for x in range (4):
            if grid[y-1][x] == grid[y][x]:
                grid[y][x]*=2
                grid[y-1][x] = 0
                
    # move everything downwards
    for num in range(3):
        for y in range(3):
            for x in range(4):
                if grid[y+1][x]==0:
                    grid[y+1][x] = grid[y][x]
                    grid[y][x] = 0        

def push_left (grid):
    """merge grid values left"""
    
    # move everthing to the left
    for num in range(3):

        for y in range(4):
            for x in range(3,0,-1):
                if grid[y][x-1] == 0:
                    grid[y][x-1] = grid[y][x]
                    grid[y][x] = 0
                
     #add adacent values
    for y in range (4):
        for x in range(3):
            if grid[y][x+1]== grid[y][x]:
                grid[y][x] *= 2
                grid[y][x+1]=0
                
    # move everything to the left again
    for num in range(3):
        for y in range(4):
            for x in range(3,0,-1):
                if grid[y][x-1] == 0:
                    grid[y][x-1] = grid[y][x]
                    grid[y][x] = 0    
    
    
    
    
def push_right (grid):
    """merge grid values right""" 
    
    # move everthing to the left
    for num in range(3):   

        for y in range(4):
            for x in range(3):
                if grid[y][x+1] == 0:
                    grid[y][x+1] = grid[y][x]
                    grid[y][x] = 0
                
     #add adacent values
    for y in range (4):
        for x in range(3,0,-1):
            if grid[y][x-1]== grid[y][x]:
                grid[y][x] *= 2
                grid[y][x-1]=0
                
    # move everything to the left again
    for num in range(3):
        for y in range(4):
            for x in range(3):
                if grid[y][x+1] == 0:
                    grid[y][x+1] = grid[y][x]
                    grid[y][x] = 0    
                
    