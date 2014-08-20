#Question 3


# Merge upwards
def push_up (grid):
    """merge grid values upwards"""
    for col in range(4):
         for row in range(3):
             if grid[row][col] == grid[row+1][col] or grid[row][col] == grid[0][col]:
                 
                 grid[row][col] = grid[row+1][col]*2
                 grid[row+1][col] = 0
                    
                 
# Merge down
def push_down (grid):
    """merge grid values downwards"""
    for col in range(4):
        for row in range(3):
            if grid[row][col] == grid[row+1][col] or grid[row][col] == grid[0][col]:
                grid[row+1][col] = grid[row][col]*2
                grid[row][col] = 0

# Merge left                
def push_left (grid):
    """merge grid values left"""
    for row in range(4):
        for col in range(3):
            if grid[row][col] == grid[row][col+1] or grid[row][col] == grid[0][col]:
                grid[row][col] = grid[row][col]*2
                grid[row][col+1] = 0
                
# Merge right                 
def push_right (grid):
    """merge grid values right"""  
    for row in range(4):
        for col in range(3):
            if grid[row][col] == grid[row][col+1] or grid[row][col] == grid[0][col]:
                grid[row][col+1] = grid[row][col]*2
                grid[row][col] = 0
                move(direction)    
                
