"""Program for 2048 game
Khanyisile Morudu
27 April 2014"""

import util

#merge grid values upwards
def push_up (grid):
 #adds up
    for row in range(4):
        for col in range(3):
            if grid[col][row] == grid[col+1][row]:
                #merges them
                grid[col][row] = grid[col][row] + grid[col+1][row]
                grid[col+1][row] = 0
            elif (grid[col+1][row] == 0) and (col + 2 <= 2):
                if grid[col][row] == grid[col+2][row]:
                    grid[col][row] = grid[col][row] + grid[col+2][row]
                    grid[col+2][row] = 0                     
            if (col + 3 == 3) and (grid[col+2][row] == 0):
                if grid[col][row] == grid[col+3][row]:
                    grid[col][row] = grid[col][row] + grid[col+3][row]
                    grid[col+3][row] = 0                     
                     
    #pushes up            
    count = 1
    while count < 4:
        for row in range(4):
            for col in range(3):
                if grid[col][row] == 0:
                    if grid[col+1][row] != 0:
                        grid[col][row] = grid[col+1][row]
                        grid[col+1][row] = 0
        count = count + 1              
      
    return grid
    
#merge grid values downwards
def push_down (grid):
    count = 1
    while count < 4:
        for row in range(3, -1, -1):
            for col in range(3, 0, -1):
                if grid[col][row] == grid[col-1][row]:
                    #merges them
                    grid[col][row] = grid[col][row] + grid[col-1][row]
                    grid[col-1][row] = 0
                    count = count + 1
                        
    count = 1
    while count < 4:
        for row in range(3, -1, -1):
            for col in range(3, 0, -1):
                if grid[col][row] == 0:
                    if grid[col-1][row] != 0:
                        grid[col][row] = grid[col-1][row]
                        grid[col-1][row] = 0
        count = count + 1 
    
    #checking the merging again
    count = 1
    while count < 4:
        for row in range(3, -1, -1):
            for col in range(3, 0, -1):
                if grid[col][row] == grid[col-1][row]:
                    #merges them
                    grid[col][row] = grid[col][row] + grid[col-1][row]
                    grid[col-1][row] = 0
                    count = count + 1    
    return grid

# merge grid values left
def push_left (grid):
 #merging them
    for col in range(4):
        for row in range(3):
            if grid[col][row] == grid[col][row+1]:
                #merges them
                grid[col][row] = grid[col][row] + grid[col][row+1]
                grid[col][row+1] = 0
                            
    count = 1
    while count < 4:
        for col in range(4):
            for row in range(3):
                if grid[col][row] == 0:
                    if grid[col][row+1] != 0:
                        grid[col][row] = grid[col][row+1]
                        grid[col][row+1] = 0
        count = count + 1 
        
    #merging again
    for col in range(4):
        for row in range(3):
            if grid[col][row] == grid[col][row+1]:
                #merges them
                grid[col][row] = grid[col][row] + grid[col][row+1]
                grid[col][row+1] = 0
    return grid
                
# merge grid values right   
def push_right (grid):
 #merging them
    for col in range(4):
        for row in range(3,-1,-1):
            if grid[col][row] == grid[col][row-1]:
                #merges them
                grid[col][row] = grid[col][row] + grid[col][row-1]
                grid[col][row-1] = 0
    #shifting                   
    count = 1
    while count < 4:
        for col in range(4):
            for row in range(3,0,-1):
                if grid[col][row] == 0:
                    if grid[col][row-1] != 0:
                        grid[col][row] = grid[col][row-1]
                        grid[col][row-1] = 0
        count = count + 1 
        
    #merging again
    for col in range(4):
        for row in range(3,0,-1):
            if grid[col][row] == grid[col][row-1]:
                #merges them
                grid[col][row] = grid[col][row] + grid[col][row-1]
                grid[col][row-1] = 0
    return grid    

"""#checking merge again
    for row in range(4):
        for col in range(3):
            if grid[col][row] == grid[col+1][row]:
                #merges them
                grid[col][row] = grid[col][row] + grid[col+1][row]
                grid[col+1][row] = 0"""

 