import util 

def push_up (grid):
    """merge grid values upwards"""
    for i in grid:
        for x in i:
            
                                  
def push_down (grid):
    """merge grid values downwards"""
    for i in range(4):
        for j in range(4):
            position = grid[i][j]
            down = i + 1
            if 0 <= down < 4:
                if position == grid[down][j]:
                    grid[down][j] *= 2
                    grid[i][j] = ""

def push_left (grid):
    """merge grid values left"""
    for i in range(4):
        for j in range(4):
            position = grid[i][j]
            toleft = j - 1
            if 0 <= toleft < 4:
                if position == grid[i][toleft]:
                    grid[toleft][j] *= 2
                    grid[i][j] = ""  
    

def push_right (grid):
    """merge grid values right"""    
    for i in range(4):
        for j in range (4):
            position = grid[i][j]
            toright = j + 1
            if 0 <= toright < 4:
                if position == grid[i][toright]:
                    grid[toright][j] *= 2
                    grid[i][j] = ""
            