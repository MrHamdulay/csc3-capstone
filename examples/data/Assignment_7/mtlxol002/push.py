"""CSC1015F Assignment 7 Question 3
Xola Matlanyane MTLXOL002
3 May 2014""" #this question was done in much effort with much much help

def push_up (grid): #merging the values upwards
    #add equal values
    for i in range(3):
        for x in range(4):
            for j in range (i+1, 4):
                if grid[i][x] == grid[j][x]:
                    grid[i][x] += grid[j][x]
                    grid[j][x] = 0
                    break
                
    #shift the 'added' values upwards
    for i in range(3):
        for x in range(4):
            if grid[i][x] == 0:
                for j in range(i+1, 4):
                    if grid[j][x] != 0:
                        grid[i][x] = grid[j][x]
                        grid[j][x] = 0
                        break
    
    return grid
    

def push_down (grid): #merging the values downwards
    # add equal values
    for i in range (3,0,-1):
        for x in range (4):
            for j in range(i-1, -1,-1):
                if grid[i][x] == grid[j][x]:
                    grid[i][x] += grid[j][x]
                    grid[j][x] = 0
                    break
                
    #shift the 'added' values down
    for i in range (3, 0, -1):
        for x in range (4):
            if grid[i][x] == 0:
                for j in range (i-1, -1, -1):
                    if grid[j][x] != 0:
                        grid[i][x] = grid[j][x]
                        grid[j][x] = 0
                        break
    return grid
    

def push_left (grid): #merging the values leftwards
    #add equal values
    for i in range (4):
            for x in range (3):
                for j in range (x+1, 4):
                    if grid[i][x] == grid[i][j]:
                        grid[i][x] += grid[i][j]
                        grid[i][j] = 0
                        break
    
    #shift the 'addded' values leftward
    for i in range (4):
        for x in range(3):
            if grid[i][x] == 0:
                for j in range(x+1, 4):
                    if grid[i][j] != 0:
                        grid[i][x] = grid[i][j]
                        grid[i][j] = 0
                        break
    return grid
    

def push_right (grid): #merging the values rightwards
    #add equal values
    for i in range (4):
            for x in range (3, 0, -1):
                for j in range (x-1, -1, -1):
                    if grid[i][x] == grid[i][j]:
                        grid[i][x] += grid[i][j]
                        grid[i][j] = 0
                        break
    
    #shift                
    for i in range(4):
        for x in range (3, 0, -1):
            if grid[i][x] == 0:     # if empty
                for j in range(x-1, -1, -1):
                    if grid[i][j] != 0:     # goes left from 0 to find first non-zero place
                        grid[i][x] = grid[i][j]     # replaces the 0 with it
                        grid[i][j] = 0
                        break
    return grid
                            
                    