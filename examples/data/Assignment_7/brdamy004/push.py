# Assignment 7 question 3
# Amy Brodie
# 1/05/2014

def push_up(grid):
    """merge grid values upwards"""    
    merge = [True,True,True,True]
    for r in range(1,4):
        for c in range(4):
            x = 1
            y = 0
            while (x<=r):
                # move values up if position above is empty
                if grid[r-x][c] == 0:
                    grid[r-x][c] = grid[r-y][c]
                    grid[r-y][c] = 0
                # add values that are equal
                elif (grid[r-x][c] == grid[r-y][c]) and (merge[c] == True):
                    grid[r-x][c] += grid[r-y][c] 
                    grid[r-y][c] = 0 
                    merge[c] = False
                x += 1
                y += 1                


def push_down(grid):
    """merge grid values downwards"""
    merge = [True,True,True,True]
    for r in range(2,-1,-1):
        for c in range(4):
            x = 1
            y = 0
            while (x+r<=3):
                # move values down if position underneath is empty
                if grid[r+x][c] == 0:
                    grid[r+x][c] = grid[r+y][c]
                    grid[r+y][c] = 0 
                # add values that are equal
                elif (grid[r+x][c] == grid[r+y][c]) and (merge[c] == True):
                    grid[r+x][c] += grid[r+y][c]
                    grid[r+y][c] = 0
                    merge[c] = False
                x += 1
                y += 1
  
    
def push_left(grid):
    """merge grid values left"""
    merge = [True,True,True,True]
    for r in range(4):
        for c in range(1,4):
            x = 1
            y = 0
            while (x<=c):
                # move values left if position to the left is empty
                if grid[r][c-x] == 0:
                    grid[r][c-x] = grid[r][c-y]
                    grid[r][c-y] = 0
                # add values that are equal
                elif (grid[r][c-x] == grid[r][c-y]) and (merge[r] == True):
                    grid[r][c-x] += grid[r][c-y]
                    grid[r][c-y] = 0 
                    merge[r] = False
                x += 1
                y += 1
 
    
def push_right(grid):
    """merge grid values right"""
    merge = [True,True,True,True]
    for r in range(4):
        for c in range(2,-1,-1):
            x = 1
            y = 0
            while (x+c<=3):
                # move values right if position to the right is empty
                if grid[r][c+x] == 0:
                    grid[r][c+x] = grid[r][c+y]
                    grid[r][c+y] = 0
                # add values that are equal
                elif (grid[r][c+x] == grid[r][c+y]) and (merge[r] == True):
                    grid[r][c+x] += grid[r][c+y]
                    grid[r][c+y] = 0
                    merge[r] = False
                x += 1
                y += 1