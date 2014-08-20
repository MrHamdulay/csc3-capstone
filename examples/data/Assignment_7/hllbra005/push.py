def push_up (grid):
    for row in range (4):
        for col in range (4):
            if grid[row][col]==" ":
                grid[row][col]= grid[row+1][col]

def push_down (grid):
    
    for row in range (4):
            for col in range (4):
                if grid[row][col]==" ":
                    grid[row][col]= grid[row-1][col]    

def push_left (grid):
    
    for row in range (4):
            for col in range (4):
                if grid[row][col]==" ":
                    grid[row][col]= grid[row1][col-1]    

def push_right (grid):
    for row in range (4):
            for col in range (4):
                if grid[row][col]==" ":
                    grid[row][col]= grid[row][col+1]    
    
