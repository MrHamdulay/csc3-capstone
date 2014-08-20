"""Merges adjecent blocks that are equal
Tafadzwa Moyo
2 May 2014"""
#Merges grid upwards         
def push_left (grid):
    for i in range(4):
        for a in range(3, 0, -1):
            if grid[i][a-1]==0:
                grid[i][a-1]=grid[i][a]
                grid[i][a]=0    
    for i in range(4):
        for a in range(3):
            if grid[i][a]==grid[i][a+1]:
                grid[i][a]+=grid[i][a]
                grid[i][a+1]=0
    for i in range(4):
        for a in range(3, 0, -1):
            if grid[i][a-1]==0:
                grid[i][a-1]=grid[i][a]
                grid[i][a]=0     
    return grid
#
def push_right(grid):
    grid[0].reverse()
    grid[1].reverse()
    grid[2].reverse()
    grid[3].reverse()
    push_left(grid)
    grid[0].reverse()
    grid[1].reverse()
    grid[2].reverse()
    grid[3].reverse()    
    return grid
def push_up(grid):
    row0=[]
    row1=[]
    row2=[]
    row3=[]
    i=0
    for a in range(4):
        row0.append(grid[a][i])
    i=1
    for a in range(4):
        row1.append(grid[a][i])    
    i=2
    for a in range(4):
        row2.append(grid[a][i])
    i=3
    for a in range(4):
        row3.append(grid[a][i])
    grid=[row0, row1, row2, row3]
    push_left(grid)
    row0=[]
    row1=[]
    row2=[]
    row3=[]
    i=0
    for a in range(4):
        row0.append(grid[a][i])
    i=1
    for a in range(4):
        row1.append(grid[a][i])    
    i=2
    for a in range(4):
        row2.append(grid[a][i])
    i=3
    for a in range(4):
        row3.append(grid[a][i])
    for i in range(4):
        grid[0][i]=row0[i]
    for i in range(4):
        grid[0][i]=row1[i]
    for i in range(4):
        grid[0][i]=row2[i]
    for i in range(4):
        grid[0][i]=row3[i]
    return grid