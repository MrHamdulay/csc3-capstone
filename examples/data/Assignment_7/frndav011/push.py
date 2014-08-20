import util

def push_up (grid):
    """merge grid values upwards"""
    for x in range(0,4):
            for y in range(0,4):
                if y-1 < 4  and y+1>=0 and x-1 <4 and x+1 >= 0:
                    if grid[x][y] == 0:
                        grid[x][y] = grid[x][y+1]
                    if grid[x][y] == grid[x][y+1]:
                        new_value = 2*grid[x][y]
    return new_value  


def push_down (grid):
    """merge grid values downwards"""

    for x in range(0,4):
        for y in range(0,4):
            if y+1 < 4  and y-1>=0 and x+1 <4 and x-1 >= 0:
                if grid[x][y] == 0:
                    grid[x][y] = grid[x][y-1]
                if grid[x][y] == grid[x][y-1]:
                    new_value = 2*grid[x][y]
    return new_value            
                
              

def push_left (grid):
    """merge grid values left"""
    for x in range(0,4):
            for y in range(0,4):
                if y-1 < 4  and y+1>=0 and x-1 <4 and x+1 >= 0:
                    if grid[x][y] == 0:
                        grid[x][y] = grid[x+1][y]
                    if grid[x][y] == grid[x+1][y]:
                        new_value = 2*grid[x][y]
    return new_value    

def push_right (grid):
    """merge grid values right"""               
    for x in range(0,4):
            for y in range(0,4):
                if y-1 < 4  and y+1>=0 and x-1 <4 and x+1 >= 0:
                    if grid[x][y] == 0:
                        grid[x][y] = grid[x-1][y]
                    if grid[x][y] == grid[x-1][y]:
                        new_value = 2*grid[x][y]        
            
                