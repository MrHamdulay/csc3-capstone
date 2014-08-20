import util
def push_down(grid):
    #merge grid values upwards
    for i in range(4):
        for j in range(4):
            copy=copy[i][j]
            if i+1<4:                
                if copy==grid[i+1][j]:
                    grid[i+1][j]=copy*2
                elif copy!=grid[i+1][j]:
                    copy=grid[i][j]
                

def push_right(grid):
    for i in range(4):
        for j in range(4):
            copy=copy[i][j]
            if j+1<4:
                ref=grid[i][j+1]
                if ref==grid[i][j+1]:
                    grid[i][j+1]=ref*2
                elif ref!=grid[i][j+1]:
                    ref=grid[i][j]
                
                    
def push_up(grid):
    for i in range(4):
        for j in range(4):
            copy=copy[i][j]
            if 0<=i-1:
                copy=grid[i-1][j]
                if copy==grid[i-1][j]:
                    grid[i-1][j]=copy*2
                elif copy!=grid[i-1][j]:
                    copy=grid[i][j]
                
                    
def push_left(grid):
    for i in range(4):
        for j in range(4):
            copy=copy[i][j]
            if j+1<4:
                copy=grid[i][j+1]
                if copy==grid[i][j+1]:
                    grid[i][j+1]=copy*2
                elif copy!=grid[i][j+1]:
                    copy=grid[i][j]
                
                
            
    
    
                
            
                
            
            
            
                
                
            
    
    