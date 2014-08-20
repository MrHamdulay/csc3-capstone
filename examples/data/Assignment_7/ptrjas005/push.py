'''Jason Pietersen'''

import util

def push_up(grid):
    #Shifts numbers up but does not add
    for row in range(1,4):
            for col in range(4):          
                if grid[row][col] != 0:
                    shift = 0
                    while (row-shift-1)>=0 and grid[row-shift-1][col] == 0:                       
                        shift += 1
                    
                    if shift != 0:
                        grid[row-shift][col] = grid[row][col] 
                        grid[row][col] = 0    
                        
    #Adds adjacent numbers                
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
                        
def push_left(grid):
    for row in range(4):
        for col in range(1,4):          
            if grid[row][col] != 0:
                shift = 0
                while grid[row][col-shift-1] == 0:                       
                    shift += 1
                
                if shift != 0:
                    grid[row][col-shift] = grid[row][col] 
                    grid[row][col] = 0 #Removes duplicates so that proper shifting up can processed
                                                
                        
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
                    
def push_right(grid):
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