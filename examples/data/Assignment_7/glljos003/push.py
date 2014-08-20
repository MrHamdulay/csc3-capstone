"""Functions to merge in all directions for 2048 game
joshua gullan
4/3/2014"""

def push_left (grid): #goes through rows, removes emptyspace, merges and removes empty space again
    height=4
    for y in range(height):
        remove_emptyspace_left(y, grid)
        Left_merge(y, grid)
        remove_emptyspace_left(y, grid)     

def push_right (grid):  #goes through rows, removes emptyspace, merges and removes empty space again
    height=4
    for y in range(height):
        remove_emptyspace_right(y, grid)
        Right_merge(y, grid)
        remove_emptyspace_right(y, grid)   

def push_up (grid):   #goes through rows, removes emptyspace, merges and removes empty space again
    height=4
    for x in range(height):
        remove_emptyspace_up(x, grid)
        Up_merge(x, grid)
        remove_emptyspace_up(x, grid)
    
def push_down (grid):   #goes through rows, removes emptyspace, merges and removes empty space again
    height=4
    for x in range(height):
        remove_emptyspace_down(x, grid)
        Down_merge(x, grid)
        remove_emptyspace_down(x, grid)    


def remove_emptyspace_up(x, grid):  #removes empty space by deleting 0s
    n=4
    for y in range(1, n): 
        value = grid[y][x]
        if value != 0:
            for y2 in range(0, y):
                value2 = grid[y2][x]
                if value2 == 0:
                    grid[y][x]=0
                    grid[y2][x] =value
                    break    
                
def Up_merge(x, grid):   #goes through rows, removes emptyspace, merges and removes empty space again
    height=3
    for y in range (height):
        value = grid[y][x]
        value2 = grid[y+1][x]
        if value == value2:
            grid[y][x]=value*2
            grid[y+1][x] =0

def remove_emptyspace_down(x, grid):  #removes empty space by deleting 0s
    for y in range(2, -1, -1): 
        value = grid[y][x]
        if value != 0:
            for y2 in range(3, y, -1):
                value2 = grid[y2][x]
                if value2 == 0:
                    grid[y][x]=0
                    grid[y2][x] =value
                    break    
                
def Down_merge(x, grid):   #goes through rows, removes emptyspace, merges and removes empty space again
    for y in range (3, 0, -1):
        value = grid[y][x]
        value2 = grid[y-1][x]
        if value == value2:
            grid[y][x]=value*2
            grid[y-1][x] = 0


def remove_emptyspace_left(y, grid):  #removes empty space by deleting 0s
    n=4
    for x in range(1, n): 
        value = grid[y][x]
        if value != 0:
            for x2 in range(0, x):
                value2 = grid[y][x2]
                if value2 == 0:
                    grid[y][x]=0
                    grid[y][x2] = value
                    break    
                
def Left_merge(y, grid):    #goes through rows, removes emptyspace, merges and removes empty space again
    height=3
    for x in range (height):
        value = grid[y][x]
        value2 = grid[y][x+1]
        if value == value2:
            grid[y][x]=value*2
            grid[y][x+1] =0


def remove_emptyspace_right(y, grid):    #removes empty space by deleting 0s
    for x in range(2, -1, -1): 
        value = grid[y][x]
        if value != 0:
            for x2 in range(3, x, -1):
                value2 = grid[y][x2]
                if value2 == 0:
                    grid[y][x]=0
                    grid[y][x2] =value
                    break    
                
def Right_merge(y, grid):   #goes through rows, removes emptyspace, merges and removes empty space again
    for x in range (3, 0, -1):
        value = grid[y][x]
        value2 = grid[y][x-1]