#Piet Motalaota
#02 May 2014
import test

def push_up (grid):
    #merge grid values upwards
    col1 = []
    for i in range(4):
        col1.append(grid[i][0])
        
    col2 = []
    for i in range(4):
        col2.append(grid[i][1])
    col3 = []
    for i in range(4):
        col3.append(grid[i][2])
    col4 = []
    for i in range(4):
        col4.append(grid[i][3])

    col1 = test.shift(col1)
    col2 = test.shift(col2)
    col3 = test.shift(col3)
    col4 = test.shift(col4)

    for i in range(4):
        grid[i][0] = col1[i]
    for i in range(4):
        grid[i][1] = col2[i]
    for i in range(4):
        grid[i][2] = col3[i]
    for i in range(4):
        grid[i][3] = col4[i]
    
def push_down (grid):
    #merge grid values downwards
    col1 = []
    for i in range(4):
        col1.append(grid[i][0])
        
    col2 = []
    for i in range(4):
        col2.append(grid[i][1])
    col3 = []
    for i in range(4):
        col3.append(grid[i][2])
    col4 = []
    for i in range(4):
        col4.append(grid[i][3])

    col1 = test.shift2(col1)
    col2 = test.shift2(col2)
    col3 = test.shift2(col3)
    col4 = test.shift2(col4)

    for i in range(4):
        grid[i][0] = col1[i]
    for i in range(4):
        grid[i][1] = col2[i]
    for i in range(4):
        grid[i][2] = col3[i]
    for i in range(4):
        grid[i][3] = col4[i]
def push_left (grid):
    #merge grid values left
    for i in range(4):
        grid[i] = test.shift(grid[i])
        
def push_right (grid):
    #merge grid values right
    for i in range(4):
        grid[i] = test.shift2(grid[i])
        
