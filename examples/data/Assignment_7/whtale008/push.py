""" push componet of 2048
alexander whiting
30 april 2014"""

""" for each method the grid is shifted in the direction,then the blocks are 
merged if possible, then the grid is shifted again"""

def push_up (grid):
    """merge grid values upwards"""
    for x in range(0,4):
        for y in range(1,4):
            k = y
            while k >=1:
                if grid[k-1][x] == 0:
                    grid[k-1][x] = grid[k][x]
                    grid[k][x] = 0
                k -= 1
        for y in range(1,4):
            if grid[y][x] == grid[y-1][x]:
                grid[y-1][x] += grid[y][x]
                grid[y][x] = 0
               
        for y in range(1,4):
            k = y
            while k >=1:
                if grid[k-1][x] == 0:
                    grid[k-1][x] = grid[k][x]
                    grid[k][x] = 0
                k -= 1        
                
            
           

def push_down (grid):
    """merge grid values downwards"""
    for x in range(0,4):
        for y in range(2,-1,-1):
            k = y
            while k <= 2:
                if grid[k+1][x] == 0:
                    grid[k+1][x] = grid[k][x] 
                    grid[k][x] = 0
                k += 1
        for y in range(2,-1,-1):
            if grid[y][x] == grid[y+1][x]:
                grid[y+1][x] += grid[y][x]
                grid[y][x] = 0
        for y in range(2,-1,-1):
            k = y
            while k <= 2:
                if grid[k+1][x] == 0:
                    grid[k+1][x] = grid[k][x] 
                    grid[k][x] = 0
                k += 1        
                
                
                        
                
def push_left (grid):
    """merge grid values left"""
    
    for y in range(0,4):
        for x in range(1,4):
            k = x
            while k >= 1:
                if grid[y][k-1] == 0:
                    grid[y][k-1] = grid[y][k]
                    grid[y][k] = 0 
                k -= 1
        for x in range(1,4):
            if grid[y][x] == grid[y][x-1] :
                
                grid[y][x-1] += grid[y][x]
                grid[y][x] = 0
        for x in range(1,4):
            k = x
            while k >= 1:
                if grid[y][k-1] == 0:
                    grid[y][k-1] = grid[y][k]
                    grid[y][k] = 0 
                k -= 1        
                
                
                
            
          

def push_right (grid):
    """merge grid values right""" 
    for y in range(0,4):
            for x in range(2,-1,-1):
                k = x
                while k <=2:
                    if grid[y][k+1] == 0:
                        grid[y][k+1] = grid[y][k]    
                        grid[y][k] = 0
                    k += 1
            for x in range(2,-1,-1):
                
                if grid[y][x] == grid[y][x+1]:
                    grid[y][x+1] += grid[y][x]
                    grid[y][x] = 0
                    
            for x in range(2,-1,-1):
                k = x
                while k <=2:
                    if grid[y][k+1] == 0:
                        grid[y][k+1] = grid[y][k]    
                        grid[y][k] = 0
                    k += 1                                        
                
                