def push_left(grid):
    """merge grid values left"""
    count = []
    for i in range(5):
        for row in range(4):
            for col in range(3):
                if grid[row][col] == 0:
                    grid[row][col] = grid[row][col + 1] 
                    grid[row][col +1] = 0
                elif row not in count:
                    if grid[row][col] == grid[row][col + 1]:
                        grid[row][col]= grid[row][col] + grid[row][col+1]
                        grid[row][col+1] = 0 
                        count.append(row)
                else:
                    continue
                
def push_right(grid):
    """merge grid values right"""
    count = []
    for i in range(5):
        for row in range(4):
            for col in range(3,0,-1):
                if grid[row][col] == 0:
                    grid[row][col] = grid[row][col - 1] 
                    grid[row][col -1] = 0
                elif row not in count:
                    if grid[row][col] == grid[row][col - 1]:
                        grid[row][col]= grid[row][col] + grid[row][col-1]
                        grid[row][col-1] = 0
                        count.append(row)
                else:
                    continue

def push_up(grid):
    """merge grid values upwards"""
    count = []
    for i in range(5):
        for row in range(3):
            for col in range(4):
                if grid[row][col] == 0:
                    grid[row][col] = grid[row+1][col] 
                    grid[row+1][col] = 0
                elif col not in count:
                    if grid[row][col] == grid[row+1][col]:
                        grid[row][col]= grid[row][col] + grid[row+1][col]
                        grid[row+1][col] = 0
                        count.append(col)
                else:
                    continue    

def push_down(grid):
    """merge grid values upwards"""
    count = []
    for i in range(5):
        for row in range(3,0,-1):
            for col in range(4):
                if grid[row][col] == 0:
                    grid[row][col] = grid[row-1][col] 
                    grid[row-1][col] = 0
                elif col not in count:
                    if grid[row][col] == grid[row-1][col]:
                        grid[row][col]= grid[row][col] + grid[row-1][col]
                        grid[row-1][col] = 0
                        count.append(col)
                else:
                    continue   
    
       