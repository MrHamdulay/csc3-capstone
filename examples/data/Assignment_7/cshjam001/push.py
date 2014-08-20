"""2048
James Cushway
02-05-2014"""
#move up
def push_down (grid):
    for rep in range(4):
        for i in range (4):
            for j in range (4):
                if grid[i][j]==0 and (i-1)>=0:
                    grid[i][j],grid[i-1][j]=grid[i-1][j],0
    for y in range(3,-1,-1):
        for x in range(4):
            if (y-1)>=0 and grid[y][x]==grid[y-1][x]:
                grid[y][x],grid[y-1][x]=grid[y][x]*2,0
            for k in range(4):
                if grid[y][x]==0 and (y-1)>=0:
                    grid[y][x],grid[y-1][x]=grid[y-1][x],0
def push_up (grid):
    for rep in range(4):
        for i in range (4):
            for j in range (4):
                if grid[i][j]==0 and (i+1)<=3:
                    grid[i][j],grid[i+1][j]=grid[i+1][j],0
    for y in range(4):
        for x in range(4):
            if (y+1)<=3 and grid[y][x]==grid[y+1][x]:
                grid[y][x],grid[y+1][x]=grid[y][x]*2,0
            for k in range(4):
                if grid[y][x]==0 and (y+1)<=3:
                    grid[y][x],grid[y+1][x]=grid[y+1][x],0
def push_left (grid):
    for rep in range(4):
        for i in range (4):
            for j in range (4):
                if grid[i][j]==0 and j<3:
                    grid[i][j],grid[i][j+1]=grid[i][j+1],0
    for y in range(4):
        for x in range(4):
            if x<3 and grid[y][x]==grid[y][x+1]:
                grid[y][x],grid[y][x+1]=grid[y][x]*2,0
            for k in range(4):
                if grid[y][x]==0 and x<3:
                    grid[y][x],grid[y][x+1]=grid[y][x+1],0
def push_right (grid):
    for rep in range(4):
        for i in range (4):
            for j in range (4):
                if grid[i][j]==0 and j>0:
                    grid[i][j],grid[i][j-1]=grid[i][j-1],0
    for y in range(4):
        for x in range(3,-1,-1):
            if grid[y][x]==grid[y][x-1] and x>0:
                grid[y][x],grid[y][x-1]=grid[y][x]*2,0
            for k in range(4):
                if grid[y][x]==0 and x>0:
                    grid[y][x],grid[y][x-1]=grid[y][x-1],0


 