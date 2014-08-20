"""this module executes direction and merges like values
quincy cele
2 may 2014"""
import util
def push_up (grid):
    """merge grid values upwards"""
    new_grid=[]
    new_grid=util.create_grid(new_grid)
    
    while grid!=new_grid:
        new_grid=util.copy_grid(grid)
        
        for row in range(3):
            for col in range(4):
                if grid[row][col]==0:
                    grid[row][col]=grid[row+1][col]
                    grid[row+1][col]=0
    for row in range(3):
        for col in range(4):    
            if grid[row][col]==grid[row+1][col]:
                grid[row][col]= grid[row][col]+grid[row+1][col]
                grid[row+1][col]=0
    for row in range(3):
        for col in range(4):
            if grid[row][col]==0:
                grid[row][col]=grid[row+1][col]
                grid[row+1][col]=0 
    return grid
            

def push_down (grid):
    """merge grid values downwards"""
 
    new_grid=[]
    new_grid=util.create_grid(new_grid)
    
    while grid!=new_grid:
        new_grid=util.copy_grid(grid)
        
        for row in range(3,0,-1):
            for col in range(4):
                if grid[row][col]==0:
                    grid[row][col]=grid[row-1][col]
                    grid[row-1][col]=0
    for row in range(3,0,-1):
        for col in range(4):    
            if grid[row][col]==grid[row-1][col]:
                grid[row][col]= grid[row][col]+grid[row-1][col]
                grid[row-1][col]=0
    for row in range(3,0,-1):
        for col in range(4):
            if grid[row][col]==0:
                grid[row][col]=grid[row-1][col]
                grid[row-1][col]=0 
    return grid    

def push_left (grid):
    """merge grid values left"""
    new_grid=[]
    new_grid=util.create_grid(new_grid)
      
    while grid!=new_grid:
        new_grid=util.copy_grid(grid)
        
        for row in range(4):
            for col in range(3):
                if grid[row][col]==0:
                    grid[row][col]=grid[row][col+1]
                    grid[row][col+1]=0
    for row in range(4):
        for col in range(3):    
            if grid[row][col]==grid[row][col+1]:
                grid[row][col]= grid[row][col]+grid[row][col+1]
                grid[row][col+1]=0
    for row in range(4):
        for col in range(3):
            if grid[row][col]==0:
                grid[row][col]=grid[row][col+1]
                grid[row][col+1]=0 
    return grid        

def push_right (grid):
    """merge grid values right""" 
    new_grid=[]
    new_grid=util.create_grid(new_grid)
      
    while grid!=new_grid:
        new_grid=util.copy_grid(grid)
        
        for row in range(4):
            for col in range(3,0,-1):
                if grid[row][col]==0:
                    grid[row][col]=grid[row][col-1]
                    grid[row][col-1]=0
    for row in range(4):
        for col in range(3,0,-1):    
            if grid[row][col]==grid[row][col-1]:
                grid[row][col]= grid[row][col]+grid[row][col-1]
                grid[row][col-1]=0
    for row in range(4):
        for col in range(3,0,-1):
            if grid[row][col]==0:
                grid[row][col]=grid[row][col-1]
                grid[row][col-1]=0 
    return grid        