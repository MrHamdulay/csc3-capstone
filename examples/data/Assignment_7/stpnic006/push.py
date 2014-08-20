"""Nicholas Stephenson
Push Code, Assignment 7"""

def push_up (grid):
    #Merge grid values up
    
    for col in [0,1,2,3]:
        for row in [2,1,0]:
            if grid[row][col] == 0:
                for i in range(row,3):
                    grid[i][col] = grid[i+1][col]
                grid[3][col] = 0
    #The above removes spaces in up direction
    
    for col in [0,1,2,3]:
        for row in [0,1,2]:
            if grid[row][col] == grid[row+1][col]:
                grid[row][col] = grid[row][col]*2
                for i in range (row,2):
                    grid[i+1][col] = grid[i+2][col]
                grid[3][col] = 0
    #The above merges like numbers, if possible, while shifting into the created spaces upwards


def push_down (grid):
    #Merge grid values downwards
    
    for col in [0,1,2,3]:
        for row in [1,2,3]:
            if grid[row][col] == 0:
                for i in range(row,0,-1):
                    grid[i][col] = grid[i-1][col]
                grid[0][col] = 0
    #The above removes spaces in down direction
    
    for col in [0,1,2,3]:
        for row in [3,2,1]:
            if grid[row][col] == grid[row-1][col]:
                grid[row][col] = grid[row][col]*2
                for i in range (row,1,-1):
                    grid[i-1][col] = grid[i-2][col]
                grid[0][col] = 0
    #The above merges like numbers, if possible, while shifting into the created spaces, downwards
    
def push_left (grid):
    #Merge grid values left
    
    for row in [0,1,2,3]:
        for col in [2,1,0]:
            if grid[row][col] == 0:
                for i in range(col,3):
                    grid[row][i] = grid[row][i+1]
                grid[row][3] = 0
    #The above removes spaces in left direction
    
    for row in [0,1,2,3]:
        for col in [0,1,2]:
            if grid[row][col] == grid[row][col+1]:
                grid[row][col] = grid[row][col]*2
                for i in range (col,2):
                    grid[row][i+1] = grid[row][i+2]
                grid[row][3] = 0
    #The above merges like numbers, if possible, while shifting into the created spaces, to the left
    
def push_right (grid):
    #Merge grid values right
    
    for row in [0,1,2,3]:
        for col in [1,2,3]:
            if grid[row][col] == 0:
                for i in range(col,0,-1):
                    grid[row][i] = grid[row][i-1]
                grid[row][0] = 0
    #The above removes spaces in left direction
    
    for row in [0,1,2,3]:
        for col in [3,2,1]:
            if grid[row][col] == grid[row][col-1]:
                grid[row][col] = grid[row][col]*2
                for i in range (col,1,-1):
                    grid[row][i-1] = grid[row][i-2]
                grid[row][0] = 0
    #The above merges like numbers, if possible, while shifting into the created spaces, to the right
    
    