# Anna Borysova
# ass7,q3
# 2014-05-01

import util

def transpose(grid):
    """swap rows and columns"""
    copy_grid = util.copy_grid(grid)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = copy_grid[j][i]

def push_up (grid):
    transpose(grid)
    push_left(grid)
    transpose(grid)
    
def push_down (grid):
    transpose(grid)
    push_right(grid)
    transpose(grid)


def push_left (grid):
    for i in range(len(grid)):
        j = 0
        while 0 in grid[i]:
            if grid[i][j] == 0:
                del grid[i][j]
                grid[i].append(1)     #differentiate between appended "0's" and original ones XD
            else: 
                j += 1                #move on if the thing at the front is non-zero
        
    for i in range(len(grid)):        # change ones back to zeros
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                grid[i][j] = 0
                
    for i in range(len(grid)):            
        for j in range(len(grid[i])-1):
            if grid[i][j] == grid[i][j+1]:
                grid[i][j] *= 2
                del grid[i][j+1]
                grid[i].append(0)
 

def push_right (grid):
    for i in range(len(grid)):
        grid[i] = grid[i][::-1]     #reverse horizontally
    push_left (grid)                
    for i in range(len(grid)):
        grid[i] = grid[i][::-1]
