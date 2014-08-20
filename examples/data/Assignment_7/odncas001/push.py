"""main game functions for 2048 game
casey o'donnell
29 april 2014"""

def push_up(grid):
    for col in range(len(grid)):
        zeros=0
        for row in range(len(grid)):
            if grid[row][col]==0:
                zeros+=1
            else:
                grid[row][col],grid[row-zeros][col]=0,grid[row][col]
        if zeros!=4:
            for row in range(1,4):
                if grid[row][col]==grid[row-1][col]:
                    grid[row][col],grid[row-1][col]=0,grid[row-1][col]*2
                    if row!=3:
                        for i in range(row,3):
                            grid[i][col],grid[i+1][col]=grid[i+1][col],grid[i][col]
    return grid

def push_down(grid):
    for col in range(len(grid)):
        zeros=0
        for row in range(3,-1,-1):
            if grid[row][col]==0:
                zeros+=1
            else:
                grid[row][col],grid[row+zeros][col]=0,grid[row][col]
        if zeros!=4:
            for row in range(2,-1,-1):
                if grid[row][col]==grid[row+1][col]:
                    grid[row][col],grid[row+1][col]=0,grid[row+1][col]*2
                    if row!=0:
                        for i in range(row,0,-1):
                            grid[i][col],grid[i-1][col]=grid[i-1][col],grid[i][col]    
    return grid

def push_left(grid):
    for row in range(len(grid)):
        zeros=0
        for col in range(4):
            if grid[row][col]==0:
                zeros+=1
            else:
                grid[row][col],grid[row][col-zeros]=grid[row][col-zeros],grid[row][col]
        if zeros!=4:
            for col in range(1,4):
                if grid[row][col]==grid[row][col-1]:
                    grid[row][col],grid[row][col-1]=0,grid[row][col-1]*2
                    if col!=3:
                        for i in range(col,3):
                            grid[row][i],grid[row][i+1]=grid[row][i+1],grid[row][i]
    return grid 

def push_right(grid):
    for row in range(len(grid)):
        zeros=0
        for col in range(3,-1,-1):
            if grid[row][col]==0:
                zeros+=1
            else:
                grid[row][col],grid[row][col+zeros]=grid[row][col+zeros],grid[row][col]
        if zeros!=4:
            for col in range(2,-1,-1):
                if grid[row][col]==grid[row][col+1]:
                    grid[row][col],grid[row][col+1]=0,grid[row][col+1]*2
                    if col!=0:
                        for i in range(col,0,-1):
                            grid[row][i],grid[row][i-1]=grid[row][i-1],grid[row][i]
    return grid 


                
                
            
        
    
    
    