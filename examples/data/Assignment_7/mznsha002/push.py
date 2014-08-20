# 2 May 2014
# Shaun Muzenda
# Module that sest of merging functions that merge adjacent equal values and eliminate gaps


import util

def push_up(grid):
    """merge grid values upwards"""
    for row in range(1,4):
            for col in range(4):          
                if grid[row][col] != 0:
                    shift = 0
                    while (row-shift-1)>=0 and grid[row-shift-1][col] == 0:                       
                        shift += 1
                    
                    if shift != 0:
                        grid[row-shift][col] = grid[row][col] 
                        grid[row][col] = 0    
                                      
    for row in range(1,4):
        for col in range(4): 
            if grid[row][col]==grid[row-1][col]:
                grid[row-1][col] = grid[row][col]*2
                grid[row][col] = 0
    
        for row in range(1,4):
            for col in range(4):          
                if grid[row][col] != 0:
                    shift = 0
                    while (row-shift-1)>=0 and grid[row-shift-1][col] == 0:                       
                        shift += 1
                    
                    if shift != 0:
                        grid[row-shift][col] = grid[row][col] 
                        grid[row][col] = 0       
              
def push_down(grid):
    """merge grid values downwards"""
    for row in range(2,-1,-1):
        for col in range(4):          
            if grid[row][col] != 0:
                shift = 0
                while  (row+shift+1)<=3 and grid[row+shift+1][col] == 0:  
                    shift += 1
                
                if shift != 0:
                    grid[row+shift][col] = grid[row][col] 
                    grid[row][col] = 0   
                    
    for row in range(2,-1,-1):
        for col in range(4): 
            if grid[row][col]==grid[row+1][col]:
                grid[row+1][col] = grid[row][col]*2
                grid[row][col] = 0    
                
    for row in range(2,-1,-1):
            for col in range(4):          
                if grid[row][col] != 0:
                    shift = 0
                    while  (row+shift+1)<=3 and grid[row+shift+1][col] == 0:  
                        shift += 1
                    
                    if shift != 0:
                        grid[row+shift][col] = grid[row][col] 
                        grid[row][col] = 0      
                        

                    
def push_right(grid):
    """merge grid values left"""
    for row in range(4):
        for col in range(2,-1,-1):          
            if grid[row][col] != 0:
                shift = 0
                while (col+shift+1)<=3 and grid[row][col+shift+1] == 0:                       
                    shift += 1
                
                if shift != 0:
                    grid[row][col+shift] = grid[row][col] 
                    grid[row][col] = 0 #Removes duplicates so that proper shifting up can processed
                                                
                        
    for row in range(4):
        for col in range(2,-1,-1): 
            if grid[row][col]==grid[row][col+1]:
                grid[row][col+1] = grid[row][col]*2
                grid[row][col] = 0
    
    for row in range(4):
        for col in range(2,-1,-1):          
            if grid[row][col] != 0:
                shift = 0
                while (col+shift+1)<=3 and grid[row][col+shift+1] == 0:                       
                    shift += 1
                
                if shift != 0:
                    grid[row][col+shift] = grid[row][col] 
                    grid[row][col] = 0
                    
def push_left(grid):
    """merge grid values right"""
    for row in range(4):
        for col in range(1,4):          
            if grid[row][col] != 0:
                shift = 0
                while grid[row][col-shift-1] == 0:                       
                    shift += 1
                
                if shift != 0:
                    grid[row][col-shift] = grid[row][col] 
                    grid[row][col] = 0 
                                                
                        
    for row in range(4):
        for col in range(1,4): 
            if grid[row][col]==grid[row][col-1]:
                grid[row][col-1] = grid[row][col]*2
                grid[row][col] = 0
    
    for row in range(4):
        for col in range(1,4):          
            if grid[row][col] != 0:
                shift = 0
                while grid[row][col-shift-1] == 0:                       
                    shift += 1
                
                if shift != 0:
                    grid[row][col-shift] = grid[row][col] 
                    grid[row][col] = 0