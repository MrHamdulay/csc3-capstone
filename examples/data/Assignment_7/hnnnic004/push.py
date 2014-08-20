'''module for moves in 2048
nicole henning
due 2 may 2014'''

def push_up (grid):
    #merge grid values upwards
    #go through every column and move to top if there are spaces
    for col in [0,1,2,3]:
        for row in [2,1,0]:
            if grid[row][col] == 0:
                for i in range(row,3):
                    grid[i][col] = grid[i+1][col]
                grid[3][col]=0
    #merge values (down) if they are the same
    for col in [0,1,2,3]:
        for row in [0,1,2]:
            if grid[row][col] == grid[row+1][col]:
                grid[row][col] = grid[row][col]*2
                for i in range(row,2):
                    grid[i+1][col] = grid[i+2][col]
                grid[3][col]=0                    
                    
       

def push_down (grid):
    #merge grid values downwards
    #go through every column and move to bottom if there are spaces
    for col in [0,1,2,3]:
        for row in [1,2,3]:
            if grid[row][col] == 0:
                for i in range(row,0,-1):
                    grid[i][col] = grid[i-1][col]
                grid[0][col]=0
    #merge values (up) if they are the same    
    for col in [0,1,2,3]:
        for row in [3,2,1]:
            if grid[row][col] == grid[row-1][col]:
                grid[row][col] = grid[row][col]*2
                for i in range(row,1,-1):
                    grid[i-1][col] = grid[i-2][col]
                grid[0][col]=0           


def push_left (grid):
    """merge grid values left"""
    #move to left (for everyrow) if there are spaces
    for row in [0,1,2,3]:
        for col in [2,1,0]:
            if grid[row][col] == 0:
                for i in range(col,3):
                    grid[row][i] = grid[row][i+1]
                grid[row][3]=0
                
    #merge values from l to r (if the same)
    for row in [0,1,2,3]:
        for col in [0,1,2]:
            if grid[row][col] == grid[row][col+1]:
                grid[row][col] = grid[row][col]*2
                for i in range(col,2):
                    grid[row][i+1] = grid[row][i+2]
                grid[row][3]=0                


def push_right (grid):
    #merge grid values right
    #move to right (for everyrow) if there are spaces
    for row in [0,1,2,3]:
        for col in [1,2,3]:
            if grid[row][col] == 0:
                for i in range(col,0,-1):
                    grid[row][i] = grid[row][i-1]
                grid[row][0]=0
    #merge values from l to r (if the same)
    for row in [0,1,2,3]:
        for col in [3,2,1]:
            if grid[row][col] == grid[row][col-1]:
                grid[row][col] = grid[row][col]*2
                for i in range(col,1,-1):
                    grid[row][i-1] = grid[row][i-2]
                grid[row][0]=0               
    