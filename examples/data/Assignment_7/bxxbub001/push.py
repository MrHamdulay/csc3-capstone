#B.Booi
import util
def push_left(grid):

    for y in range(3):
        for x in range(3):
            if grid[x][y]==0:
                continue
            else:
                for i in range(x,0,-1):
                    #make sure not out of range
                    if x-1 >= 0:
                        if gird[x-1][y]==0:
                            grid[x-1][y]=grid[x][y]
                            grid[x][y]=0
    for y in range(3):
        for x in range(3): 
            if grid[x][y]== grid[x-1][y]:
                grid[x-1][y]= grid[x][y]+grid[x-1][y]
    
                
    util.print_grid(grid) 
    
def push_Right(grid):

    for y in range(3,0,-1):
        for x in range(3,0,-1):
            if grid[x][y]==0:
                continue
            else:
                for i in range(x,0,-1):
                    #make sure not out of range
                    if x-1 >= 0:
                        if gird[x+1][y]==0:
                            grid[x+1][y]=grid[x][y]
                            grid[x][y]=0 
    for y in range(3,0,-1):
        for x in range(3,0,-1):
            if grid[x][y]== grid[x-1][y]:
                grid[x-1][y]= grid[x][y]+grid[x-1][y]
                
    util.print_grid(grid) 
                
                
def push_up(grid):

    for y in range(3,0,-1):
        for x in range(3,0,-1):
            if grid[x][y]==0:
                continue
            else:
                for i in range(x,0,-1):
                    #make sure not out of range
                    if x-1 >= 0:
                        if gird[x][y-1]==0:
                            grid[x][y-1]=grid[x][y]
                            grid[x][y]=0
                            
    for y2 in range(3,0,-1):
        for x2 in range(3,0,-1):
            if grid[x][y]== grid[x][y-1]:
                grid[x][y-1]= grid[x][y]+grid[x][y-1]
                
    util.print_grid(grid)         
                
def push_down(grid):

    for y in range(3):
        for x in range(3):
            if grid[x][y]==0:
                continue
            else:
                for i in range(x,0,-1):
                    #make sure not out of range
                    if x-1 >= 0:
                        if gird[x][y+1]==0:
                            grid[x][y+1]=grid[x][y]
                            grid[x][y]=0
                            
    for y2 in range(3):
        for x2 in range(3):
            if grid[x][y]== grid[x][y+1]:
                grid[x][y+1]= grid[x][y]+grid[x][y+1]
                
    util.print_grid(grid) 