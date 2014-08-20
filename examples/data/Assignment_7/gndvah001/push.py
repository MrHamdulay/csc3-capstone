"""Push thing 2048
Vahin Gounden
28/04/2014"""

def push_up (grid):
    """merge grid values upwards"""
    for i in range(3):
        for r in range(1,4):
            for c in range(4):
                if grid[r-1][c] == 0:
                    grid[r-1][c] = grid[r][c]
                    grid[r][c] = 0
                   
    for r in range(1,4):
        for c in range(4):    
                if grid[r-1][c] == grid[r][c]:
                    grid[r-1][c] = grid[r-1][c]*2
                    grid[r][c] = 0
                        
    for r in range(1,4):
        for c in range(4):
            if grid[r-1][c] == 0:
                grid[r-1][c] = grid[r][c]
                grid[r][c] = 0    
                
    return grid
                
def push_down (grid):
    """merge grid values downwards"""
    for i in range(3):
        for r in range(2,-1,-1):
            for c in range(3,-1,-1):
                if grid[r+1][c] == 0:
                    grid[r+1][c] = grid[r][c]
                    grid[r][c] = 0
                    
    for r in range(2,-1,-1):
        for c in range(3,-1,-1):    
                if grid[r+1][c] == grid[r][c]:
                    grid[r+1][c] = grid[r+1][c]*2
                    grid[r][c] = 0
                    
    for r in range(2,-1,-1):
        for c in range(3,-1,-1):
            if grid[r+1][c] == 0:
                grid[r+1][c] = grid[r][c]
                grid[r][c] = 0
                
    return grid
                                                          
def push_left (grid):
    """merge grid values left"""
    for i in range(3):
        for r in range(4):
            for c in range(1,4):
                if grid[r][c-1] == 0:
                    grid[r][c-1] = grid[r][c]
                    grid[r][c] = 0
                    
    for r in range(4):
        for c in range(1,4):                    
            if grid[r][c-1] == grid[r][c]:
                grid[r][c-1] = grid[r][c-1]*2
                grid[r][c] = 0
                
    for r in range(4):
        for c in range(1,4):
            if grid[r][c-1] == 0:
                grid[r][c-1] = grid[r][c]
                grid[r][c] = 0

    return grid

def push_right (grid):
    """merge grid values right"""   
    for i in range(3):
        for r in range(3,-1,-1):
            for c in range(2,-1,-1):
                if grid[r][c+1] == 0:
                    grid[r][c+1] = grid[r][c]
                    grid[r][c] = 0
                    
    for r in range(3,-1,-1):
        for c in range(2,-1,-1):
            if grid[r][c+1] == grid[r][c]:
                grid[r][c+1] = grid[r][c+1]*2
                grid[r][c] = 0
                
    for r in range(3,-1,-1):
        for c in range(2,-1,-1):
            if grid[r][c+1] == 0:
                grid[r][c+1] = grid[r][c]
                grid[r][c] = 0
                
    return grid