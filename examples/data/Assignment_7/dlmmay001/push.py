def push_up (grid):
    for i in grid:
        for j in range(3):
            if i[j] == grid[j+1][j]:
                i[j] = i[j] + grid[j+1][j]
                grid[j+1][j] = 0
            
def push_down (grid):
    for i in grid:
        for j in range(3):
            if i[j] == grid[j+1][j]:
                grid[j+1][j] = i[j] + grid[j+1][j]
                i[j] = 0

def push_left (grid):
    for i in grid:
        for j in range(3):
            if i[j] == i[j+1]:
                i[j] = i[j] + i[j+1]
                i[j+1] = 0
        
                
def push_right (grid):
    for i in grid:
        for j in range(3):
            if i[j] == i[j+1]:
                i[j+1] = i[j] + i[j+1]
                i[j] = 0    
    
        
    