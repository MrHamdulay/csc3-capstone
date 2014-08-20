#Push and merge of 2048
#Jennifer Yuan (YNXYIS001)
#2 May 2014

def push_left(grid): #merges grid values left
    for k in range(4): #repeats the loop 4 times
        for row in range(4):
            for col in range(4):
                if col+1 < 4: #makes sure that index is in range
                    if grid[row][col] == 0: #if the value in the grid is zero, it moves all values to the left 
                        grid[row][col] = grid[row][col+1]
                        grid[row][col+1] = 0
    for row in range(4):
        for col in range(4):
            if col+1<4:
                if grid[row][col] == grid[row][col+1]: #Only does this step if a value is equal to the one next to it
                        grid[row][col] = grid[row][col]*2 #merges the two identicle values
                        grid[row][col+1] = 0 #places a 0 where to the right of the merged value
                        
    for k in range(4):
        for row in range(4):
            for col in range(4):
                if col+1 < 4:
                    if grid[row][col] == 0:
                        grid[row][col] = grid[row][col+1] #once again shifts all values to the left if there are 0s in the row
                        grid[row][col+1] = 0    
                            
def push_right(grid): #merges grid values right, all steps are the same, expcept that they values are pushed and merged to the right
    for k in range(3, -1, -1):
        for row in range(3, -1, -1):
            for col in range(4):
                if col-1 >-1:
                    if grid[row][col] == 0:
                        grid[row][col] = grid[row][col-1]
                        grid[row][col-1] = 0
    for row in range(3, -1, -1):
        for col in range(3, -1, -1):
            if col-1>-1:
                if grid[row][col] == grid[row][col-1]:
                        grid[row][col] = grid[row][col]*2
                        grid[row][col-1] = 0
                        
    for k in range(4):
        for row in range(3, -1, -1):
            for col in range(3, -1, -1):
                if col-1 > -1:
                    if grid[row][col] == 0:
                        grid[row][col] = grid[row][col-1]
                        grid[row][col-1] = 0 

def push_up(grid): #merges grid values upwards. All steps are the same, expect that all pushes and merges are upwards.
    for k in range(4):
        for row in range(4):
            for col in range(4):
                if row+1 < 4:
                    if grid[row][col] == 0:
                        grid[row][col] = grid[row+1][col]
                        grid[row+1][col] = 0
    for row in range(4):
        for col in range(4):
            if row+1<4:
                if grid[row][col] == grid[row+1][col]:
                        grid[row][col] = grid[row][col]*2
                        grid[row+1][col] = 0
                        
    for k in range(4):
        for row in range(4):
            for col in range(4):
                if row+1 < 4:
                    if grid[row][col] == 0:
                        grid[row][col] = grid[row+1][col]
                        grid[row+1][col] = 0   

def push_down(grid): #merges grid values downwards. All pushes and merges are the same as above just downwards. 
    for k in range(4):
        for row in range(4):
            for col in range(3, -1,-1):
                if row-1 >-1:
                    if grid[row][col] == 0:
                        grid[row][col] = grid[row-1][col]
                        grid[row-1][col] = 0
    for row in range(4):
        for col in range(4):
            if row-1>-1:
                if grid[row][col] == grid[row-1][col]:
                        grid[row][col] = grid[row][col]*2
                        grid[row-1][col] = 0
                        
    for k in range(4):
        for row in range(4):
            for col in range(4):
                if row-1 > -1:
                    if grid[row][col] == 0:
                        grid[row][col] = grid[row-1][col]
                        grid[row-1][col] = 0 
                                                        