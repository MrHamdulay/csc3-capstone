#Assignment 7
#Question 3
#Barry Su
#30 April 2014
#Module with a set of merging functions that merge adjacent equal values and eliminate gaps

def push_up(grid):
    #create loops to move values up
    for i in range(3):
        for j in range(1,4):    #j = row
            for k in range(4):  #k = column
                if grid[j-1][k] == 0 or grid[j-1][k] == " ":
                    grid[j-1][k] = grid[j][k]
                    grid[j][k] = 0
                    
    #merge if adjacent numbers are equal
    for j in range(1,4):
        for k in range(4):    
            if grid[j-1][k] == grid[j][k]:
                grid[j-1][k] += grid[j][k]
                grid[j][k] = 0
                
    #fill up the spaces that are no longer occupied because adjacent numbers have merged
    for j in range(1,4):
        for k in range(4):
            if grid[j-1][k] == 0 or grid[j-1][k] == " ":
                grid[j-1][k] = grid[j][k]
                grid[j][k] = 0    
    return grid

def push_down(grid):
    #create loops to move values down
    for i in range(3):
            for j in range(2,-1,-1):
                for k in range(3,-1,-1):
                    if grid[j+1][k] == 0 or grid[j+1][k] == " ":
                        grid[j+1][k] = grid[j][k]
                        grid[j][k] = 0
    
    #merge if adjacent numbers are equal
    for j in range(2,-1,-1):
        for k in range(3,-1,-1):
            if grid[j+1][k] == grid[j][k]:
                grid[j+1][k] += grid[j][k]
                grid[j][k] = 0 
                
    #fill up the spaces that are no longer occupied because adjacent numbers have merged
    for j in range(2,-1,-1):
        for k in range(3,-1,-1):
            if grid[j+1][k] == 0 or grid[j+1][k] == " ":
                grid[j+1][k] = grid[j][k]
                grid[j][k] = 0                         
    return grid


def push_left(grid):
    #create loops to move values left
    for i in range(3):
        for j in range(4):    
            for k in range(1,4):
                if grid[j][k-1] == 0 or grid[j][k-1] == " ":
                    grid[j][k-1] = grid[j][k]
                    grid[j][k] = 0    
    
    #merge if adjacent numbers are equal
    for j in range(4):    
        for k in range(1,4):
            if grid[j][k-1] == grid[j][k]:
                grid[j][k-1] += grid[j][k]
                grid[j][k] = 0                     
    
    #fill up the spaces that are no longer occupied because adjacent numbers have merged
    for j in range(4):    
        for k in range(1,4):
            if grid[j][k-1] == 0 or grid[j][k-1] == " ":
                grid[j][k-1] = grid[j][k]
                grid[j][k] = 0                    
    return grid

def push_right (grid):
    #create loops to move values right
    for i in range(3):
        for j in range(3,-1,-1):
            for k in range(2,-1,-1):
                if grid[j][k+1] == 0 or grid[j][k+1] == " ":
                    grid[j][k+1] = grid[j][k]
                    grid[j][k] = 0 
    
    #merge if adjacent numbers are equal                 
    for j in range(3,-1,-1):
        for k in range(2,-1,-1):
            if grid[j][k+1] == grid[j][k]:
                grid[j][k+1] += grid[j][k]
                grid[j][k] = 0                     
    
    #fill up the spaces that are no longer occupied because adjacent numbers have merged
    for j in range(3,-1,-1):
        for k in range(2,-1,-1):
            if grid[j][k+1] == 0 or grid[j][k+1] == " ":
                grid[j][k+1] = grid[j][k]
                grid[j][k] = 0                 
    return grid


    