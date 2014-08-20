'''Joshen Credelio Jacob
01/05/2014'''


def push_down():
    #merge grid values down
    for i in range(4):
        for j in range(4):
            if grid[i][j]==grid[i][j-1]:
                return grid[i][j]*2
            else:
                return grid[i][j]  
            
def push_up():
    #merge grid values up
    i=4
    while i>0:
        j=4
        while j>0:
            if grid[i][j]==grid[i][j-1]:
                return grid[i][j]*2
            else:
                return grid[i][j] 
            j-=1
        i-=1

def push_right():
    #merge grid values right
    for j in range(4):
        for i in range(4):
            if grid[i][j]==grid[i+1][j]:
                return grid[i][j]*2
            else:
                return grid[i][j]  
  

def push_left():
    #merge grid values left
    j=4
    while j>0:
        i=4
        while i>0:
            if grid[i][j]==grid[i-1][j]:
                return grid[i][j]*2
            else:
                return grid[i][j] 
            i-=1
        j-=1
  
