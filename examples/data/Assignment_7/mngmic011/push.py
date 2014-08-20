"""question 3
assignment 7
Micaela Menegaldo"""

def push_up(grid):
    
    for i in range(4):
        for row in range(3):
            for column in range(4):
                if grid[row][column]==' ':
                    grid[row][column]=0
                if grid[row][column]==0:
                    grid[row][column]=grid[row+1][column]
                    grid[row+1][column]=0
    
    for row in range(3):
        for column in range(4):
            if grid[row][column]==grid[row+1][column]:
                grid[row][column]+=grid[row+1][column]
                grid[row+1][column]=0
                
    for i in range(4):
        for row in range(3):
            for column in range(4):
                if grid[row][column]==' ':
                    grid[row][column]=0
                if grid[row][column]==0:
                    grid[row][column]=grid[row+1][column]
                    grid[row+1][column]=0    
                    
    return grid

def push_down(grid):
    
    for i in range(4):
        for row in range(3,0,-1):
            for column in range(4):
                if grid[row][column]==' ':
                    grid[row][column]=0
                if grid[row][column]==0:
                    grid[row][column]=grid[row-1][column]
                    grid[row-1][column]=0
                    
    for row in range(3,0,-1):
        for column in range(4):
            if grid[row][column]==grid[row-1][column]:
                grid[row][column]+=grid[row-1][column]
                grid[row-1][column]=0
             
    for i in range(4):
        for row in range(3,0,-1):
            for column in range(4):
                if grid[row][column]==' ':
                    grid[row][column]=0
                if grid[row][column]==0:
                    grid[row][column]=grid[row-1][column]
                    grid[row-1][column]=0    
    
    return grid

def push_left(grid):
    for i in range(4):
        for row in range(4):
            for column in range(3):
                if grid[row][column]==' ':
                    grid[row][column]=0
                if grid[row][column]==0:
                    grid[row][column]=grid[row][column+1]
                    grid[row][column+1]=0  
    
    for row in range(4):
        for column in range(3):
            if grid[row][column]==grid[row][column+1]:
                grid[row][column]+=grid[row][column+1]
                grid[row][column+1]=0
                
    for i in range(4):
            for row in range(4):
                for column in range(3):
                    if grid[row][column]==' ':
                        grid[row][column]=0
                    if grid[row][column]==0:
                        grid[row][column]=grid[row][column+1]
                        grid[row][column+1]=0
                        
    return grid
                
def push_right(grid):
    for i in range(4):
        for row in range(4):
            for column in range(3,0,-1):
                if grid[row][column]==' ':
                    grid[row][column]=0
                if grid[row][column]==0:
                    grid[row][column]=grid[row][column-1]
                    grid[row][column-1]=0     
                    
    for row in range(4):
        for column in range(3,0,-1):
            if grid[row][column]==grid[row][column-1]:
                grid[row][column]+=grid[row][column-1]
                grid[row][column-1]=0   
                
    for i in range(4):
        for row in range(4):
            for column in range(3,0,-1):
                if grid[row][column]==' ':
                    grid[row][column]=0
                if grid[row][column]==0:
                    grid[row][column]=grid[row][column-1]
                    grid[row][column-1]=0         
                    
    return grid
                    
if __name__=='__main__':
    grid=[[2,0,0,2],[2,0,0,8],[0,0,4,8],[0,8,0,0]]
    print(grid)
    new=push_left(grid)
    print(new)    