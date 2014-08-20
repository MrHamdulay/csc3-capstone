'''Wade Cresswell'''
def push_up (grid):
    """merge grid values upwards"""
    for i in range(4):
        for row in range (3): #removes all the zeros and push grid up
                for coloumn in range (4):
                    if grid[row][coloumn]==0:
                        grid[row][coloumn],grid[row+1][coloumn]=grid[row+1][coloumn],grid[row][coloumn]
                      
              
    for row in range (3): #merges like numbers, multiplys the top one by two and makes the other value 0
                for coloumn in range (4):    
                    if grid[row][coloumn]==grid[row+1][coloumn]:
                                    grid[row][coloumn]*=2
                                    grid[row+1][coloumn]=0                    
    for i in range(4):
        for row in range (3): #removes zeros again so that there are no spaces
                for coloumn in range (4):
                    if grid[row][coloumn]==0:
                        grid[row][coloumn],grid[row+1][coloumn]=grid[row+1][coloumn],grid[row][coloumn]    
    return grid            

def push_down (grid):
    """merge grid values downwards"""
    for i in range(4):
        for row in range (3,0,-1): #removes all the zeros and push grid down
                for coloumn in range (4):
                    if grid[row][coloumn]==0:
                        grid[row-1][coloumn],grid[row][coloumn]=grid[row][coloumn],grid[row-1][coloumn]
    
    for row in range (3,0,-1): #merges like numbers up, multiplys the top one by two and makes the other value 0
        for coloumn in range (4):    
                if grid[row][coloumn]==grid[row-1][coloumn]:
                                grid[row][coloumn]*=2
                                grid[row-1][coloumn]=0      
    for i in range(4):
        for row in range (3,0,-1): #removes all the zeros and push grid down
                for coloumn in range (4):
                    if grid[row][coloumn]==0:
                        grid[row-1][coloumn],grid[row][coloumn]=grid[row][coloumn],grid[row-1][coloumn]    
    return grid    

def push_left (grid):
    """merge grid values left"""
    for i in range(4):
            for row in range (4): #removes all the zeros and push grid left
                    for coloumn in range (3):
                        if grid[row][coloumn]==0:
                            grid[row][coloumn+1],grid[row][coloumn]=grid[row][coloumn],grid[row][coloumn+1]
    
    for row in range (4): #merges like numbers, multiplys the left one by two and makes the other value 0
            for coloumn in range (3):    
                    if grid[row][coloumn]==grid[row][coloumn+1]:
                                    grid[row][coloumn]*=2
                                    grid[row][coloumn+1]=0                
    for i in range(4):
            for row in range (4): #removes all the zeros and push grid left
                    for coloumn in range (3):
                        if grid[row][coloumn]==0:
                            grid[row][coloumn+1],grid[row][coloumn]=grid[row][coloumn],grid[row][coloumn+1]    
    return grid

def push_right (grid):
    """merge grid values right""" 
    for i in range(4):
            for row in range (4): #removes all the zeros and push grid right
                    for coloumn in range (3,0,-1):
                        if grid[row][coloumn]==0:
                            grid[row][coloumn-1],grid[row][coloumn]=grid[row][coloumn],grid[row][coloumn-1]
    

    for row in range (4): #merges like numbers right, multiplys the right one by two and makes the other value 0
        for coloumn in range (3,0,-1):    
                if grid[row][coloumn]==grid[row][coloumn-1]:
                                grid[row][coloumn]*=2
                                grid[row][coloumn-1]=0
    
    for i in range(4):
            for row in range (4): #removes all the zeros and push grid right
                    for coloumn in range (3,0,-1):
                        if grid[row][coloumn]==0:
                            grid[row][coloumn-1],grid[row][coloumn]=grid[row][coloumn],grid[row][coloumn-1]    
    return grid