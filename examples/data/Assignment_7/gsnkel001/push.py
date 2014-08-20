#2048 game functions
#1 may 2014
#kelly goosen

def push_up(grid): #defining function up
    """merge grid values upwards"""
    for x in range(1,3+1):
        for m in range(4):
            if grid[x][m]!=0:
                currPos = x
                while grid[currPos-1][m] ==0 and currPos>0: #iterating through positions
                    grid[currPos-1][m] =grid[currPos][m]
                    grid[currPos][m] =0
                    currPos =currPos-1
    for x in range(3):
        for m in range(4):
            if grid[x][m] ==grid[x+1][m]:
                grid[x][m] =2*grid[x][m] #multiplying by 2
                for i in range(x+1,3):
                    grid[i][m] =grid[i+1][m]
                grid[3][m]=0
                
def push_down(grid): #defining function down
    """merge grid values downwards"""
    for x in range(2,0-1,-1):
        for m in range(4):
            if grid[x][m]!=0:
                currPos=x
                while currPos<3 and grid[currPos+1][m] == 0:
                    grid[currPos+1][m] = grid[currPos][m]
                    grid[currPos][m]=0
                    currPos =currPos+1
    for x in range(3,1-1,-1):
        for m in range(4):
            if grid[x][m] ==grid[x-1][m]:
                grid[x][m]=2*grid[x][m]
                for i in range(x-1,0-1,-1):
                    grid[i][m] =grid[i-1][m]
                    grid[0][m]=0

def push_left(grid): #defining function left
    """merge grid values left"""
    for m in range(1,3+1):
        for x in range(4):
            if grid[x][m]!=0:
                currPos=m
                while currPos>0 and grid[x][currPos-1]==0:
                    grid[x][currPos-1]=grid[x][currPos]
                    grid[x][currPos]=0
                    currPos=currPos-1
    for m in range(3):
        for x in range(4):
            if grid[x][m] ==grid[x][m+1]:
                grid[x][m] =2*grid[x][m]
                for i in range(m+1,3):
                    grid[x][i]=grid[x][i+1]
                grid[x][3]=0
    
def push_right(grid): #defining function right
    """merge grid values right"""
    for m in range(2,0-1,-1):
        for x in range(4):
            if grid[x][m]!=0:
                currPos=m
                while currPos<3 and grid[x][currPos+1]==0:
                    grid[x][currPos+1]=grid[x][currPos]
                    grid[x][currPos] = 0
                    currPos = currPos+1
    for m in range(3,0,-1):
        for x in range(4):
            if grid[x][m]==grid[x][m-1]:
                grid[x][m]=2*grid[x][m]
                for i in range(m-1,0,-1):
                    grid[x][i] =grid[x][i-1]
                grid[x][0]=0