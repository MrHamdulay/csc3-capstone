"""KLSADA002
CSC1015F Assigment 7 Q3
29/04/14"""

def push_up (grid):
    """merge grid values upwards"""
    for k in range (4):
        for i in range (3,0,-1):
            for j in range (4):
                if grid [i-1][j] == 0:
                    grid [i-1][j] = grid[i][j]
                    grid[i][j] = 0
    
    for i in range (3):
        for j in range (4):    
            if grid [i+1][j] == grid[i][j]:
                grid [i][j] += grid[i+1][j]
                grid[i+1][j] = 0            
    for k in range(4):
        for i in range (3,0,-1):
            for j in range (4):   
                if grid [i-1][j] == 0:
                    grid [i-1][j] = grid[i][j]
                    grid[i][j] = 0 
                 
                
def push_down (grid):
    """merge grid values downwards"""
    for k in range (4):
        for i in range (3):
            for j in range (4):
                if grid [i+1][j] == 0:
                    grid [i+1][j] = grid[i][j]
                    grid[i][j] = 0                
      
    for i in range (3,0,-1):
        for j in range (4):            
            if grid [i-1][j] == grid[i][j]:
                grid [i][j] += grid[i-1][j]
                grid[i-1][j] = 0      
                
    for k in range(4):
        for i in range (3):
            for j in range (4):
                if grid [i+1][j] == 0:
                    grid [i+1][j] = grid[i][j]
                    grid[i][j] = 0 
         
                
def push_left (grid):
    """merge grid values left"""
    for k in range(4):    
        for i in range (4):
            for j in range (3,0,-1):
                if grid [i][j-1] == 0:
                    grid [i][j-1] = grid[i][j]
                    grid[i][j] = 0
    for i in range (4):
        for j in range (3):
            if grid [i][j+1] == grid[i][j]:
                grid [i][j] += grid[i][j+1]
                grid[i][j+1] = 0
    for k in range (4):
        for i in range (4):
            for j in range (3,0,-1):
                if grid [i][j-1] == 0:
                    grid [i][j-1] = grid[i][j]
                    grid[i][j] = 0                
def push_right (grid):
    """merge grid values right"""
    for k in range(4):
        for i in range (4):
            for j in range (3):
                if grid [i][j+1] == 0:
                    grid [i][j+1] = grid[i][j]
                    grid[i][j] = 0
    for i in range (4):
        for j in range (3,0,-1):           
            if grid [i][j-1] == grid[i][j]:
                grid [i][j] += grid[i][j-1]
                grid[i][j-1] = 0     
    for k in range(4):
        for i in range (4):
            for j in range (3):
                if grid [i][j+1] == 0:
                    grid [i][j+1] = grid[i][j]
                    grid[i][j] = 0