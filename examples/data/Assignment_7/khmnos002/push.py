"""program to imitate 2048 game
nosipho khumalo
27 April 2014"""

import util

#merge grid values upwards
def push_up (grid):
    #pushes up            
    count = 1
    while count < 4:
        for row in range(4):
            for column in range(3):
                if grid[column][row] == 0:
                    if grid[column+1][row] != 0:
                        grid[column][row] = grid[column+1][row]
                        grid[column+1][row] = 0
        count = count + 1              
      

 #adds up
    for row in range(4):
        for column in range(3):
            if grid[column][row] == grid[column+1][row]:
                #merges them
                grid[column][row] = grid[column][row] + grid[column+1][row]
                grid[column+1][row] = 0
            elif (grid[column+1][row] == 0) and (column + 2 <= 2):
                if grid[column][row] == grid[column+2][row]:
                    grid[column][row] = grid[column][row] + grid[column+2][row]
                    grid[column+2][row] = 0                     
            elif (column + 3 == 3) and (grid[column+2][row] == 0):
                grid[column][row] = grid[column][row] + grid[column+3][row]
                grid[column+3][row] = 0                     
                     
    #pushes up            
    count = 1
    while count < 4:
        for row in range(4):
            for column in range(3):
                if grid[column][row] == 0:
                    if grid[column+1][row] != 0:
                        grid[column][row] = grid[column+1][row]
                        grid[column+1][row] = 0
        count = count + 1              
      
    return grid
    
#merge grid values downwards
def push_down (grid):
    count = 1
    while count < 4:
        for row in range(3, -1, -1):
            for column in range(3, 0, -1):
                if grid[column][row] == 0:
                    if grid[column-1][row] != 0:
                        grid[column][row] = grid[column-1][row]
                        grid[column-1][row] = 0
        count = count + 1    
    
    count = 1
    while count < 4:
        for row in range(3, 0, -1):
            for column in range(3, -1, -1):
                if grid[column][row] == grid[column-1][row]:
                    #merges them
                    grid[column][row] = 2*grid[column][row]
                    grid[column-1][row] = 0
                    count = count + 1
                        
    count = 1
    while count < 4:
        for row in range(3, -1, -1):
            for column in range(3, 0, -1):
                if grid[column][row] == 0:
                    if grid[column-1][row] != 0:
                        grid[column][row] = grid[column-1][row]
                        grid[column-1][row] = 0
        count = count + 1 
    
    """count = 1
    while count < 4:
        for row in range(3, -1, -1):
            for column in range(3, 0, -1):
                if grid[column][row] == grid[column-1][row]:
                    #merges them
                    grid[column][row] = 2*grid[column][row]
                    grid[column-1][row] = 0
                    count = count + 1"""    
    
    """#checking the merging again
    count = 1
    while count < 4:
        for row in range(3, -1, -1):
            for column in range(3, 0, -1):
                if grid[column][row] == grid[column-1][row]:
                    #merges them
                    grid[column][row] = grid[column][row] + grid[column-1][row]
                    grid[column-1][row] = 0
                    count = count + 1"""  
    return grid

# merge grid values left
def push_left (grid):
 #merging them
    for column in range(4):
        for row in range(3):
            if grid[column][row] == grid[column][row+1]:
                #merges them
                grid[column][row] = grid[column][row] + grid[column][row+1]
                grid[column][row+1] = 0
                            
    count = 1
    while count < 4:
        for column in range(4):
            for row in range(3):
                if grid[column][row] == 0:
                    if grid[column][row+1] != 0:
                        grid[column][row] = grid[column][row+1]
                        grid[column][row+1] = 0
        count = count + 1 
        
    #merging again
    for column in range(4):
        for row in range(3):
            if grid[column][row] == grid[column][row+1]:
                #merges them
                grid[column][row] = grid[column][row] + grid[column][row+1]
                grid[column][row+1] = 0
    return grid
                
# merge grid values right   
def push_right (grid):
 #merging them
    for column in range(4):
        for row in range(3,0,-1):
            if grid[column][row] == grid[column][row-1]:
                #merges them
                grid[column][row] = 2*grid[column][row]
                grid[column][row-1] = 0
    #shifting                   
    count = 1
    while count < 4:
        for column in range(4):
            for row in range(3,0,-1):
                if grid[column][row] == 0:
                    if grid[column][row-1] != 0:
                        grid[column][row] = grid[column][row-1]
                        grid[column][row-1] = 0
        count = count + 1 
        
    #merging again
    for column in range(4):
        for row in range(3,0,-1):
            if grid[column][row] == grid[column][row-1]:
                #merges them
                grid[column][row] = grid[column][row] + grid[column][row-1]
                grid[column][row-1] = 0
    return grid    


 