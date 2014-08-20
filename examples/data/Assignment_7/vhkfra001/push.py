# Assignment 7
# Question 3: Merge functions for '2048' game.
# Frans van Hoek
# 2 May 2014

def push_up (grid):
    #merge grid values upwards
    # first add equal values
    for i in range(3):
        for x in range(4):
            for j in range (i+1, 4):
                if grid[i][x] == grid[j][x]:
                    grid[i][x] += grid[j][x]
                    grid[j][x] = 0
                    break
                
    # now shift the values upwards
    for i in range(3):
        for x in range(4):
            if grid[i][x] == 0:
                for j in range(i+1, 4):
                    if grid[j][x] != 0:
                        grid[i][x] = grid[j][x]
                        grid[j][x] = 0
                        break
    
    return grid
    

def push_down (grid):
    #merge grid values downwards
    # first add equal values
    for i in range (3,0,-1):
        for x in range (4):
            for j in range(i-1, -1,-1):
                if grid[i][x] == grid[j][x]:
                    grid[i][x] += grid[j][x]
                    grid[j][x] = 0
                    break
                
    # now shift down
    for i in range (3, 0, -1):
        for x in range (4):
            if grid[i][x] == 0:
                for j in range (i-1, -1, -1):
                    if grid[j][x] != 0:
                        grid[i][x] = grid[j][x]
                        grid[j][x] = 0
                        break
    return grid
    

def push_left (grid):
    #merge grid values left
    # first add equal values
    for i in range (4):
            for x in range (3):
                for j in range (x+1, 4):
                    if grid[i][x] == grid[i][j]:
                        grid[i][x] += grid[i][j]
                        grid[i][j] = 0
                        break
    
    # now shift left
    for i in range (4):
        for x in range(3):
            if grid[i][x] == 0:
                for j in range(x+1, 4):
                    if grid[i][j] != 0:
                        grid[i][x] = grid[i][j]
                        grid[i][j] = 0
                        break
    return grid
    

def push_right (grid):
    #merge grid values right
    # first add equal values
    for i in range (4):
            for x in range (3, 0, -1):
                for j in range (x-1, -1, -1):
                    if grid[i][x] == grid[i][j]:
                        grid[i][x] += grid[i][j]
                        grid[i][j] = 0
                        break
    
    # now shift                
    for i in range(4):
        for x in range (3, 0, -1):
            if grid[i][x] == 0:     # if it's empty
                for j in range(x-1, -1, -1):
                    if grid[i][j] != 0:     # goes left from 0 to find first non-zero place
                        grid[i][x] = grid[i][j]     # replaces the 0 with it
                        grid[i][j] = 0
                        break
    return grid
                            
                    