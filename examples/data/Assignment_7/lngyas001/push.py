def push_up (grid):
    """merge grid values upwards"""
    for i in range(len(grid)):
        if i == 0:
            pass
        for j in range(4):
            position = grid[i][j]
            up = i -1
            if position == grid[up][j]:
                grid[up][j] *= 2
                grid[i][j] = 0
                
                    
def push_down (grid):
    """merge grid values downwards"""
    for i in range(len(grid)):
        if i == 0:
            pass
        for j in range(4):
            position = grid[i][j]
            down = i + 1
            if position == grid[down][j]:
                    grid[down][j] *= 2
                    grid[i][j] = 0
            

def push_left (grid):
    """merge grid values left"""
    for i in range(len(grid)):
        if i == 0:
            pass
        for j in range(4):
            position = grid[i][j]
            to_left = j - 1
            if position==grid[i][to_left]:
                grid[to_left][j] *= 2
                grid[i][j] = 0        


def push_right (grid):
    """merge grid values right"""        
    for i in range(len(grid)):
        if i == 0:
            pass
        for j in range(4):
            position = grid[i][j]
            to_right = j +1
            if position==grid[i][to_right]:
                grid[to_right][j] *= 2
                grid[i][j] = 0  