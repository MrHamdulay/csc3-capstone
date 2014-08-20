#Ikhlaas Pohplonker
#1 May 214
#a program that merges adjacent equal values and eliminates gaps
def push_up(grid):#merges grid values upwards
    for column in range (4):
        for row in range (3):
            x=1
            while x<(4-row) and grid[row][column]==0:#checks if the grid value is equal to zero
                grid[row][column]=grid[row+x][column]
                grid[row+x][column]=0
                x=x+1
    for column in range(4):
        for row in range(3):
            if grid[row][column]==grid[row+1][column]:#checks if two grid values that vertically adjacent are equal
                grid[row][column]=2*grid[row][column]
                grid[row+1][column]=0
    for column in range (4):
        for row in range (3):
            x=1
            while x<(4-row) and grid[row][column]==0:#checks if the grid value is equal to zero
                grid[row][column]=grid[row+x][column]
                grid[row+x][column]=0
                x=x+1   
                
def push_left(grid):#merges grid values left
    for row in range (4):
        for column in range (3):
            x=1
            while x<(4-column) and grid[row][column]==0:#checks if the grid value is equal to zero
                grid[row][column]=grid[row][column+x]
                grid[row][column+x]=0
                x=x+1
    for row in range(4):
        for column in range(3):
            if grid[row][column]==grid[row][column+1]:#checks if two grid values that horizontally adjacent are equal
                grid[row][column]=2*grid[row][column]
                grid[row][column+1]=0
    for row in range (4):
        for column in range (3):
            x=1
            while x<(4-column) and grid[row][column]==0:#checks if the grid value is equal to zero
                grid[row][column]=grid[row][column+x]
                grid[row][column+x]=0
                x=x+1     

def push_down (grid):#merges grid values downwards
    for column in range(4):
        for row in range(3,0,-1):
            x=1
            while x<(row+1) and grid[row][column]==0:#checks if the grid value is equal to zero
                grid[row][column]=grid[row-x][column]
                grid[row-x][column]=0
                x=x+1
    for column in range(4):
        for row in range(3,0,-1):
            if grid[row][column]==grid[row-1][column]:#checks if two grid values that vertically adjacent are equal
                grid[row][column]=2*grid[row][column]
                grid[row-1][column]=0
    for column in range(4):
        for row in range(3,0,-1):
            x=1
            while x<(row+1) and grid[row][column]==0:#checks if the grid value is equal to zero
                grid[row][column]=grid[row-x][column]
                grid[row-x][column]=0
                x=x+1
def push_right (grid):#merges grid values right
    for row in range(4):
        for column in range(3,0,-1):
            x=1
            while x<(column+1) and grid[row][column]==0:#checks if the grid value is equal to zero
                grid[row][column]=grid[row][column-x]
                grid[row][column-x]=0
                x=x+1
    for row in range(4):
        for column in range(3,0,-1):
            if grid[row][column]==grid[row][column-1]:#checks if two grid values that horizontally adjacent are equal
                grid[row][column]=2*grid[row][column]
                grid[row][column-1]=0
    for row in range(4):
        for column in range(3,0,-1):
            x=1
            while x<(column+1) and grid[row][column]==0:#checks if the grid value is equal to zero
                grid[row][column]=grid[row][column-x]
                grid[row][column-x]=0
                x=x+1    
         
                                     
                          

