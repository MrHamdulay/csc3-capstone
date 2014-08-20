def push_up (grid):
    """merge grid values upwards"""
    for j in range(4):
        if grid [2][j] == 0:
            grid [2][j] = grid [3][j]
            grid [3][j] =0
        if grid [1][j] == 0:
            grid [1][j] = grid [2][j]
            grid [2][j] = grid [3][j]
            grid [3][j] =0
        if grid [0][j] == 0:
            grid [0][j] = grid [1][j]
            grid [1][j] = grid [2][j]
            grid [2][j] = grid [3][j]
            grid [3][j] =0
        if grid [0][j] == grid[1][j]:
            grid [0][j] = grid [0][j]*2
            grid[1][j] = 0
        if grid [1][j] == grid[2][j]:
            grid [1][j] = grid [1][j]*2
            grid[2][j] = 0
        if grid [2][j] == grid[3][j]:
            grid [2][j] = grid [2][j]*2
            grid[3][j] = 0
        if grid [2][j] == 0:
            grid [2][j] = grid [3][j]
            grid [3][j] =0
        if grid [1][j] == 0:
            grid [1][j] = grid [2][j]
            grid [2][j] = grid [3][j]
            grid [3][j] =0
        if grid [0][j] == 0:
            grid [0][j] = grid [1][j]
            grid [1][j] = grid [2][j]
            grid [2][j] = grid [3][j]
            grid [3][j] =0  
 
def push_down (grid):
    """merge grid values downwards"""
    for j in range(4):
        if grid [1][j] == 0:
            grid [1][j] = grid [0][j]
            grid [0][j] =0
        if grid [2][j] == 0:
            grid [2][j] = grid [1][j]
            grid [1][j] = grid [0][j]
            grid [0][j] =0
        if grid [3][j] == 0:
            grid [3][j] = grid [2][j]
            grid [2][j] = grid [1][j]
            grid [1][j] = grid [0][j]
            grid [0][j] =0
        if grid [3][j] == grid[2][j]:
            grid [3][j] = grid [3][j]*2
            grid[2][j] = 0
        if grid [2][j] == grid[1][j]:
            grid [2][j] = grid [2][j]*2
            grid[1][j] = 0
        if grid [1][j] == grid[0][j]:
            grid [1][j] = grid [1][j]*2
            grid[0][j] = 0
        if grid [1][j] == 0:
            grid [1][j] = grid [0][j]
            grid [0][j] =0
        if grid [2][j] == 0:
            grid [2][j] = grid [1][j]
            grid [1][j] = grid [0][j]
            grid [0][j] =0
        if grid [3][j] == 0:
            grid [3][j] = grid [2][j]
            grid [2][j] = grid [1][j]
            grid [1][j] = grid [0][j]
            grid [0][j] =0

def push_left (grid):
    """merge grid values left"""
    for i in range(4):
        if grid [i][2]==0:
            grid [i][2] = grid [i][3]
            grid [i][3] =0
        if grid [i][1]==0:
            grid [i][1] = grid [i][2]
            grid [i][2] = grid [i][3]
            grid [i][3] =0
        if grid[i][0]==0:
            grid [i][0] = grid [i][1]
            grid [i][1] = grid [i][2]
            grid [i][2] = grid [i][3]
            grid [i][3] =0
        if grid [i][0] == grid [i][1]:
            grid [i][0] = grid [i][0]*2
            grid [i][1] = 0
        if grid [i][1] == grid [i][2]:
            grid [i][1] = grid [i][1]*2
            grid [i][2] = 0
        if grid [i][2] == grid [i][3]:
            grid [i][2] = grid [i][2]*2
            grid [i][3] = 0
        if grid [i][2]==0:
            grid [i][2] = grid [i][3]
            grid [i][3] =0
        if grid [i][1]==0:
            grid [i][1] = grid [i][2]
            grid [i][2] = grid [i][3]
            grid [i][3] =0
        if grid[i][0]==0:
            grid [i][0] = grid [i][1]
            grid [i][1] = grid [i][2]
            grid [i][2] = grid [i][3]
            grid [i][3] =0
            
def push_right (grid):
    """merge grid values right""" 
    for i in range(4):
        if grid [i][1]==0:
            grid [i][1] = grid [i][0]
            grid [i][0] =0
        if grid [i][2]==0:
            grid [i][2] = grid [i][1]
            grid [i][1] = grid [i][0]
            grid [i][0] =0
        if grid[i][3]==0:
            grid [i][3] = grid [i][2]
            grid [i][2] = grid [i][1]
            grid [i][1] = grid [i][0]
            grid [i][0] =0
        if grid [i][3] == grid [i][2]:
            grid [i][3] = grid [i][3]*2
            grid [i][2] = 0
        if grid [i][2] == grid [i][1]:
            grid [i][2] = grid [i][2]*2
            grid [i][1] = 0
        if grid [i][1] == grid [i][0]:
            grid [i][1] = grid [i][1]*2
            grid [i][0] = 0
        if grid [i][1]==0:
            grid [i][1] = grid [i][0]
            grid [i][0] =0
        if grid [i][2]==0:        
            grid [i][2] = grid [i][1]
            grid [i][1] = grid [i][0] 
            grid [i][0] =0
        if grid [i][3]==0:
            grid [i][3] = grid [i][2]
            grid [i][2] = grid [i][1]
            grid [i][1] = grid [i][0]    
            grid [i][0] =0