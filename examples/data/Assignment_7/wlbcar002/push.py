#merge grid values upwards
def push_up (grid):
    for i in range(4):
        for y in range(4):
            for x in range(4):
                #check for empty space, if exists then move all subsequent numbers in that column up
                if grid[y][x] == 0 and (y+1)<=3:
                    grid[y][x],grid[y+1][x] = grid[y+1][x],0   
    #if a number in a column matches the following number, merge these two numbers upwards                
    for y in range(4):
        for x in range(4):
            if (y+1)<=3 and grid[y][x] == grid[y+1][x]:
                grid[y][x] *=2
                grid[y+1][x] = 0
            #if any empty spaces now exist, move the column up
            for i in range(4):
                if grid[y][x] == 0 and (y+1)<=3:
                    grid[y][x],grid[y+1][x] = grid[y+1][x],0   
                            
                
    
#merge grid values downwards
def push_down (grid):
    for i in range(4):
        for y in range(4):
            for x in range(4):
                #check for empty space, if exists then move all subsequent numbers in that column down
                if grid[y][x] == 0 and (y-1)>=0:
                    grid[y][x],grid[y-1][x] = grid[y-1][x],0
    #if a number in a column matches the number above it, merge these two numbers downwards 
    for y in range(3,-1,-1):
        for x in range(4):
            if (y-1)>=0 and grid[y][x] == grid[y-1][x]:
                grid[y][x] *=2
                grid[y-1][x] = 0
            for i in range(4):
                #if any empty spaces now exist, move the column down
                if grid[y][x] == 0 and (y-1)>=0:
                    grid[y][x],grid[y-1][x] = grid[y-1][x],0   
                            
                        
               
                    
#merge grid values left
def push_left (grid):
    for i in range(4):
        for y in range(4):
            for x in range(4):
                #check for empty space, if exists then move all subsequent numbers in that row to the left
                if grid[y][x] == 0 and (x+1)<=3:
                    grid[y][x],grid[y][x+1] = grid[y][x+1],0
    #if a number in a row matches the following number, merge these two numbers to the left 
    for y in range(4):
        for x in range(4):
            if (x+1)<=3 and grid[y][x] == grid[y][x+1]:
                grid[y][x] *=2
                grid[y][x+1] = 0
            for i in range(4):
                #if any empty spaces now exist, move the row to the left
                if grid[y][x] == 0 and (x+1)<=3:
                    grid[y][x],grid[y][x+1] = grid[y][x+1],0   
                            
                    

    
#merge grid values right
def push_right (grid):
    for i in range(4):
        for y in range(4):
            for x in range(4):
                #check for empty space, if exists then move all subsequent numbers in that row to the right
                if grid[y][x] == 0 and (x-1)>=0:
                    grid[y][x],grid[y][x-1] = grid[y][x-1],0
    #if a number in a row matches the number before it, merge these two numbers to the right                
    for y in range(4):
        for x in range(3,-1,-1):
            if (x-1)>=0 and grid[y][x] == grid[y][x-1]:
                grid[y][x] *=2
                grid[y][x-1] = 0
            for i in range(4):
                #if any empty spaces now exist, move the row to the right
                if grid[y][x] == 0 and (x-1)>=0:
                    grid[y][x],grid[y][x-1] = grid[y][x-1],0   
                            
                                