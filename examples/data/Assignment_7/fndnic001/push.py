import util
def push_up (grid):     #pushes all values up and merges adjacent pairs
    for k in range(3):
        for row in range (3,0,-1):
            for col in range (4):
                if grid [row-1][col] == 0:
                    grid [row-1][col] = grid[row][col]
                    grid[row][col] = 0
    
    for row in range (3):
        for col in range (4):    
            if grid [row+1][col] == grid[row][col]:
                grid [row][col] += grid[row+1][col]
                grid[row+1][col] = 0            
    for k in range(3):
        for row in range (3,0,-1):
            for col in range (4):   
                if grid [row-1][col] == 0:
                    grid [row-1][col] = grid[row][col]
                    grid[row][col] = 0 
    return grid
                 
                 
def push_down (grid):        #pushes all values down and merges adjacent pairs
    for k in range(3):
        for row in range (3):
            for col in range (4):
                if grid [row+1][col] == 0:
                    grid [row+1][col] = grid[row][col]
                    grid[row][col] = 0                
  
    for row in range (3,0,-1):
        for col in range (4):            
            if grid [row-1][col] == grid[row][col]:
                grid [row][col] += grid[row-1][col]
                grid[row-1][col] = 0      
                
    for k in range(3):
        for row in range (3):
            for col in range (4):
                if grid [row+1][col] == 0:
                    grid [row+1][col] = grid[row][col]
                    grid[row][col] = 0 
    return grid
             
                
def push_left (grid):      #pushes all values to left and merges adjacent pairs
    for k in range(3):
        for row in range (4):
            for col in range (3,0,-1):
                if grid [row][col-1] == 0:
                    grid [row][col-1] = grid[row][col]
                    grid[row][col] = 0
    for row in range (4):
        for col in range (3):
            if grid [row][col+1] == grid[row][col]:
                grid [row][col] += grid[row][col+1]
                grid[row][col+1] = 0
    for k in range(3):    
        for row in range (4):
            for col in range (3,0,-1):
                if grid [row][col-1] == 0:
                    grid [row][col-1] = grid[row][col]
                    grid[row][col] = 0     
    return grid
def push_right (grid):      #pushes all values to right and merges adjacent pairs
    for k in range(3):    
        for i in range (4):
            for j in range (3):
                if grid [i][j+1] == 0:
                    grid [i][j+1] = grid[i][j]
                    grid[i][j] = 0
    for i in range (4):
        for j in range (3,0,-1):           
            if grid [i][j-1] == grid[i][j]:
                grid [i][j] += grid[i][j-1]
                grid[i][j-1] = 0     
    for k in range(3):
        for i in range (4):
            for j in range (3):
                if grid [i][j+1] == 0:
                    grid [i][j+1] = grid[i][j]
                    grid[i][j] = 0
    return grid


