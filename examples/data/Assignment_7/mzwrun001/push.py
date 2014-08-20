def push_up (grid):
    for row in range(3):
        for col in range(4):
            if grid[row][col]!=0:    
                if grid[row][col]==grid[row-1][col]:
                    grid[row][col]+=grid[row-1][col]
                    grid[row][col]=grid[row-1][col]
                elif grid[row-1][col]==0:
                    grid[row][col]=grid[row-1][col]
    else:
        return grid[row][col]
                
def push_down(grid):
    for row in range(3):
        for col in range(4):
            if grid[row][col]!=0:    
                if grid[row][col]==grid[row+1][col]:
                    grid[row][col]+=grid[row+1][col]
                    grid[row][col]=grid[row+1][col]
                elif grid[row+1][col]==0:
                    grid[row][col]=grid[row+1][col]
    else:
        return grid[row][col]    
                    
def push_left(grid):
    for row in range(4):
        for col in range(3):
            if grid[row][col]!=0:    
                if grid[row][col]==grid[row][col-1]:
                    grid[row][col]+=grid[row][col-1]
                    grid[row][col]=grid[row][col-1]
                elif grid[row][col-1]==0:
                    grid[row][col]=grid[row][col-1]
    else:
        return grid[row][col]        
                        
def push_down(grid):
    for row in range(4):
        for col in range(3):
            if grid[row][col]!=0:    
                if grid[row][col]==grid[row][col+1]:
                    grid[row][col]+=grid[row][col+1]
                    grid[row][col]=grid[row][col+1]
                elif grid[row][col+1]==0:
                    grid[row][col]=grid[row][col+1]
    else:
        return grid[row][col]            
           
           
           