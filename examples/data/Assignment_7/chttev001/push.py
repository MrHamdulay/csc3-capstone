"""Tevin Chetty
30 April 2014
Program to play 2048"""

def push_up(grid):
    """merge grid values upwards"""
    for col in range (4): #col first as you are doing up down 
        for row in range(3): #3 to provide for the movement up
            if grid[row][col]==0:
                grid[row][col]=grid[row+1][col]
                grid[row+1][col]=0 
        for i in range(3, -1, -1):
            if grid[i][col]==grid[i-1][col]:
                grid[i-1][col]=grid[i-1][col]+grid[i-1][col] #when adjacent and equal, add together
                grid[i][col]=0
        for i in range(3): #three times because you have to move it up three times
            for row in range(3):
                if grid[row][col]==0:
                    grid[row][col]=grid[row+1][col]
                    grid[row+1][col]=0

def push_down(grid):
    """merge grid values downwards"""
    for col in range (4):#col first as you are doing up down 
        for row in range(3, 0, -1):#3 to provide for the movement up and to reverse order
            if grid[row][col]==0:
                grid[row][col]=grid[row-1][col]
                grid[row-1][col]=0
        for i in range(4):
            if grid[i][col]==grid[i-1][col]:
                grid[i-1][col]=grid[i-1][col]+grid[i-1][col]#when adjacent and equal, add together
                grid[i][col]=0
        for i in range(3):#three times because you have to move it down three times
            for row in range(3, 0, -1):
                if grid[row][col]==0:
                    grid[row][col]=grid[row-1][col]
                    grid[row-1][col]=0
    
 

#Push_left and push_right are very similar to up and down, just swapping row and col around
def push_left(grid):
    """merge grid values left"""
    for row in range (4):
        for col in range(3):
            if grid[row][col]==0:
                grid[row][col]=grid[row][col+1]
                grid[row][col+1]=0
        for i in range(3, -1, -1):
            if grid[row][i]==grid[row][i-1]:
                grid[row][i-1]=grid[row][i-1]+grid[row][i-1]
                grid[row][i]=0
        for i in range(3):
            for col in range(3):
                if grid[row][col]==0:
                    grid[row][col]=grid[row][col+1]
                    grid[row][col+1]=0

    
def push_right(grid):
    """merge grid values right""" 
    for row in range (4):
        for col in range(3, 0, -1):
            if grid[row][col]==0:
                grid[row][col]=grid[row][col-1]
                grid[row][col-1]=0
        for i in range(4):
            if grid[row][i]==grid[row][i-1]:
                grid[row][i-1]=grid[row][i-1]+grid[row][i-1]
                grid[row][i]=0
        for i in range(3):
            for col in range(3, 0, -1):
                if grid[row][col]==0:
                    grid[row][col]=grid[row][col-1]
                    grid[row][col-1]=0    