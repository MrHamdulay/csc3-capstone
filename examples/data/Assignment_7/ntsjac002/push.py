'''
Jacob Ntesang
01 May 2014'''

"""merge grid values upwards"""
def push_up (grid):
    for x in range(4):
        for y in range(4):
            if x != 0:
                if grid[x][y] == grid[x-1][y]:
                    if grid[x-2][y] == 0 and grid[x-3][y] == 0:
                        grid[x-3][y] = grid[x-1][y] + grid[x][y]
                        grid[x-1][y] = 0
                        grid[x][y] = 0
                    elif grid[x-2][y] == 0:
                        grid[x-2][y] = grid[x-1][y] + grid[x][y]
                        grid[x-1][y] = 0
                        grid[x][y] = 0
                    else:
                        grid[x-1][y] = grid[x-1][y] + grid[x][y]
                        grid[x-1][y] = 0
                        grid[x][y] = 0 
                elif grid[x][y] == grid[x-1][y] and grid[x][y] == grid[x-2][y]:
                    #if grid[x-1][y] == 0 and grid[x-2][y] == 0:
                        grid[x-2][y] = grid[x-2][y] + grid[x-1][y]
                        grid[x-1][y] = grid[x][y]
                        grid[x][y] = 0
                elif grid[x-1][y] == 0 and grid[x-2][y] == grid[x][y]:
                    grid[x-2][y] = grid[x-2][y] + grid[x][y]
                    grid[x][y] = 0
                elif grid[x-1][y] == 0 and grid[x-2][y] == 0 and grid[x-3][y] == grid[x][y] :
                    grid[x-3][y] = grid[x][y] + grid[x-3][y]
                    grid[x][y] = 0
                elif grid[x-1][y] == 0 and grid[x-2][y] == 0 and grid[x-3][y] == 0:
                    grid[x-3][y] = grid[x-3][y] +grid[x][y]
                    grid[x][y] = 0
                elif grid[x-1][y] == 0 and grid[x-2][y] == 0:
                    grid[x-2][y] = grid[x-2][y] + grid[x][y]
                    grid[x][y] = 0
                    
                
                elif grid[x-1][y] == 0 and grid[x-2][y] == 0 and grid[x-3][y] == 0:
                    grid[x-3][y] = grid[x][y] + grid[x-3][y]
                    grid[0][y]=grid[x][y]
                    grid[x][y]=0
                elif grid[x-1][y] == 0:
                    grid[x-1][y] = grid[x-1][y] + grid[x][y]
                    grid[x][y] = 0
                    
'''def push_down (grid):
    """merge grid values downwards"""
    for x in range(4):
        for y in range(4):
            if ( x != 3 :
                 :
                grid[x+2][y] = grid[x+1][y] + grid[x][y]
                grid[x+1][y] = 0
                grid[x][y] = 0
            elif (x == 0 and grid[x][y] == grid[x+3][y]) or (x == 0 and grid[x+3][y] == 0):
                    grid[x+3][y] = grid[x+3][y] + grid[x][y]
                    grid[x+2][y] = 0
                    grid[x+1][y] = 0
                    grid[x][y] = 0  '''              
def push_left (grid):
    """merge grid values left"""
    for x in range(4):
            for y in range(4):
                if y > 0:
                    if grid[x][y-1] == grid[x][y]:
                        if grid[x][y-1] == 0:
                            grid[x][y-1] = grid[x][y-1] + grid[x][y]
                            grid[x][y] = 0
                        else:
                            grid[x][y-1] = grid[x][y-1] + grid[x][y]
                            grid[x][y] = 0                            
                    elif grid[x][y-1] == 0 and grid[x][y-2] == 0 and grid[x][y-3] == 0:
                        grid[x][y-3] = grid[x][y-2] + grid[x][y]
                        grid[x][y] = 0  
                    elif grid[x][y-2] == grid[x][y] and grid[x][y-1] == 0:
                        grid[x][y-2] = grid[x][y-2] + grid[x][y]
                        grid[x][y] = 0
                        grid[x][y-1] = 0
                    elif grid[x][y-1] == 0:
                        grid[x][y-1] = grid[x][y-1] + grid[x][y]
                        grid[x][y] = 0
                        
def push_right (grid):
    """merge grid values right"""  
    for x in range(4):
            for y in range(4):
                if y+1 <=  3:
                    if grid[x][y+1] == grid[x][y]:
                        if grid[x][y+1] == 0:
                            grid[x][y+1] = grid[x][y+1] + grid[x][y]
                            grid[x][y] = 0
                        else:
                            grid[x][y+1] = grid[x][y+1] + grid[x][y]
                            grid[x][y] = 0                             
                    elif grid[x][y+1] == 0:
                            grid[x][y+1] = grid[x][y+1] + grid[x][y]
                            grid[x][y] = 0
                    elif grid[x][y+1] == 0 and grid[x][y+2] == 0:
                        if grid[x][y+3] == 0:
                            grid[x][y+3] = grid[x][y+3] + grid[x][y] 
                            grid[x][y] = 0
                        else:
                            grif[x][y+2] = grid[x][y+2] + grid[x][y]
                            grid[x][y] = 0
                    elif grid[x][y+1] == 0 and grid[x][y+2] == 0 and grid[x][y+3] == grid[x][y]:
                        grid[x][y+3] = grid[x][y+3] + grid[x][y]
                        grid[x][y] = 0
            
                       
                                                
                    
                            