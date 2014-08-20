#push module
#Joshua Hewitson
#2/5/2014

def push_up (grid):
    """merge grid values upwards"""
    #move values up
    push_up1(grid)
    push_up2(grid)
    push_up3(grid)
    #add equal values
    merge_up(grid)
    #move values up
    push_up1(grid)
    push_up2(grid)
    push_up3(grid)    

def push_down (grid):
    """merge grid values downwards"""
    push_down1(grid)
    push_down2(grid)
    push_down3(grid)
    merge_down(grid)
    push_down1(grid)
    push_down2(grid)
    push_down3(grid)

def push_left (grid):
    """merge grid values left"""
    push_left1(grid)
    push_left2(grid)
    push_left3(grid)
    merge_left(grid)
    push_left1(grid)
    push_left2(grid)
    push_left3(grid)

def push_right (grid):
    """merge grid values right"""
    push_right1(grid)
    push_right2(grid)
    push_right3(grid)
    merge_right(grid)
    push_right1(grid)
    push_right2(grid)
    push_right3(grid)
    
def push_up1 (grid):
    i = 1
    for j in range(4):
        if grid[i][j] != 0:
            if grid[i-1][j] == 0:
                grid[i-1][j] = grid[i][j]
                grid[i][j] = 0

def push_up2 (grid):
    i = 2
    for j in range(4):
        if grid[i][j] != 0:
            if grid[i-1][j] == 0:
                grid[i-1][j] = grid[i][j]
                grid[i][j] = 0

    push_up1(grid)

def push_up3 (grid):
    i = 3
    for j in range(4):
        if grid[i][j] != 0:
            if grid[i-1][j] == 0:
                grid[i-1][j] = grid[i][j]
                grid[i][j] = 0

    push_up2(grid)
    push_up1(grid)
    
def push_down1 (grid):
    i = 2
    for j in range(4):
        if grid[i][j] != 0:
            if grid[i+1][j] == 0:
                grid[i+1][j] = grid[i][j]
                grid[i][j] = 0

def push_down2 (grid):
    i = 1
    for j in range(4):
        if grid[i][j] != 0:
            if grid[i+1][j] == 0:
                grid[i+1][j] = grid[i][j]
                grid[i][j] = 0

    push_down1(grid)

def push_down3 (grid):
    i = 0
    for j in range(4):
        if grid[i][j] != 0:
            if grid[i+1][j] == 0:
                grid[i+1][j] = grid[i][j]
                grid[i][j] = 0

    push_down2(grid)
    push_down1(grid)

def push_left1 (grid):
    j = 1
    for i in range(4):
        if grid[i][j] != 0:
            if grid[i][j-1] == 0:
                grid[i][j-1] = grid[i][j]
                grid[i][j] = 0

def push_left2 (grid):
    j = 2
    for i in range(4):
        if grid[i][j] != 0:
            if grid[i][j-1] == 0:
                grid[i][j-1] = grid[i][j]
                grid[i][j] = 0

    push_left1(grid)

def push_left3 (grid):
    j = 3
    for i in range(4):
        if grid[i][j] != 0:
            if grid[i][j-1] == 0:
                grid[i][j-1] = grid[i][j]
                grid[i][j] = 0

    push_left2(grid)
    push_left1(grid)
        
def push_right1 (grid):
    j = 2
    for i in range(4):
        if grid[i][j] != 0:
            if grid[i][j+1] == 0:
                grid[i][j+1] = grid[i][j]
                grid[i][j] = 0

def push_right2 (grid):
    j = 1
    for i in range(4):
        if grid[i][j] != 0:
            if grid[i][j+1] == 0:
                grid[i][j+1] = grid[i][j]
                grid[i][j] = 0

    push_right1(grid)

def push_right3 (grid):
    j = 0
    for i in range(4):
        if grid[i][j] != 0:
            if grid[i][j+1] == 0:
                grid[i][j+1] = grid[i][j]
                grid[i][j] = 0

    push_right2(grid)
    push_right1(grid)
    
def merge_up(grid):
    for i in range(0,3,1):
        for j in range(4):
            if grid[i+1][j] == grid[i][j]:
                grid[i][j] *= 2
                grid[i+1][j] = 0
                
def merge_down(grid):
    for i in range(0,3,1):
        for j in range(4):
            if grid[i+1][j] == grid[i][j]:
                grid[i+1][j] *= 2
                grid[i][j] = 0
                
def merge_left(grid):
    for j in range(0,3,1):
        for i in range(4):
            if grid[i][j+1] == grid[i][j]:
                grid[i][j] *= 2
                grid[i][j+1] = 0
                
def merge_right(grid):
    for j in range(0,3,1):
        for i in range(4):
            if grid[i][j+1] == grid[i][j]:
                grid[i][j+1] *= 2
                grid[i][j] = 0