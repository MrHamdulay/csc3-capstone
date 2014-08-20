def push_up (grid):
    """merge grid values upwards"""
    for row in range(0,3):
        for col in range(4):
            if grid[row][col]==grid[row+1][col]:
                grid[row][col]=(grid[row][col])*2
                grid[row+1][col]=0
            if grid[row][col]==0:
                grid[row][col]=grid[row+1][col]
                grid[row+1][col]=0
    for col in range(4):
        if grid[0][col]==0:
            grid[0][col]=grid[1][col]
            grid[1][col]=grid[2][col]
            grid[2][col]=grid[3][col]
        if grid[0][col]==0:
            grid[0][col]=grid[1][col]
            grid[1][col]=grid[2][col]
            grid[2][col]=grid[3][col]
        if grid[0][col]==0:
            grid[0][col]=grid[1][col]
            grid[1][col]=grid[2][col]
            grid[2][col]=grid[3][col]        
            
                
                  
                                 

def push_down (grid):
    """merge grid values downwards"""
    for row in range(3):
            for col in range(4):
                    if grid[row][col]==grid[row-1][col]:
                        grid[row][col]=(grid[row][col])*2
                        grid[row-1][col]=0
                    if grid[row][col]==0:
                        grid[row][col]=grid[row-1][col]
                        grid[row-1][col]=0
                    grid[row+1][col]=grid[row][col]
    for col in range(4):
        if grid[3][col]==0:
            grid[3][col]=grid[2][col]
            grid[2][col]=grid[1][col]
            grid[1][col]=grid[0][col]
        if grid[3][col]==0:
            grid[3][col]=grid[2][col]
            grid[2][col]=grid[1][col]
            grid[1][col]=grid[0][col]
        if grid[3][col]==0:
            grid[3][col]=grid[2][col]
            grid[2][col]=grid[1][col]
            grid[1][col]=grid[0][col]
def push_left (grid):
    """merge grid values left"""
    for row in range(4):
            for col in range(0,3):
                if grid[row][0]==0:
                    if grid[row][col+1]==0:
                        grid[row][col]=grid[row][col+1]
                        grid[row][col+1]=0                    
                if grid[row][col]==grid[row][col+1]:
                    grid[row][col]=(grid[row][col])*2
                    grid[row][col+1]=0
                if grid[row][col]==0:
                    grid[row][col]=grid[row][col+1]
                    grid[row][col+1]=0
                

def push_right (grid):
    """merge grid values right"""    
    for row in range(4):
            for col in range(3):
                if grid[row][col]==grid[row][col-1]:
                    grid[row][col]=(grid[row][col])*2
                    grid[row][col-1]=0
                if grid[row][col]==0:
                    grid[row][col]=grid[row][col-1]
                    grid[row][col-1]=0
                grid[row][col+1]=grid[row][col]
