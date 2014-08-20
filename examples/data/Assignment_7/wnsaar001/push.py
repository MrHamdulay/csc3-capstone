"""30 April 2014
play 2048
Aaron Weinstein
"""
def push_up (grid):
    """merge grid values upwards"""
    for i in range(4):
        if grid[2][i] == 0:
            grid[2][i] = grid[3][i]
            grid[3][i] = 0
        if grid[1][i] == 0:
            grid[1][i] = grid[2][i]
            grid[2][i] = grid[3][i]
        if grid[0][i] == 0:
            grid[0][i] = grid[1][i]
            grid[1][i] = grid[2][i]
            grid[2][i] = grid[3][i]
            grid[3][i] = 0
        if grid[0][i] == grid[1][i]:
            grid[0][i] = grid[0][i]*2
            grid[1][i] = 0
        if grid[1][i] == grid[2][i]:
            grid[1][i] = grid[1][i]*2
            grid[2][i] = 0
        if grid[2][i] == grid[3][i]:
            grid[2][i] = grid[2][i]*2
            grid[3][i] = 0
        if grid[2][i] == 0:
            grid[2][i] = grid[3][i]
            grid[3][i] = 0
        if grid[0][i] == 0:
            grid[1][i]=grid[2][i]
            grid[2][i]=grid[3][i]
            grid[3][i] = 0
        if grid[0][i] == 0:
            grid[0][i]=grid[1][i]
            grid[1][i]=grid[2][i]
            grid[2][i]=grid[3][i]
            grid[3][i] = 0
def push_down (grid):
    """merge grid values downwards"""
    for i in range(4):
        if grid[1][i] == 0:
            grid[1][i] = grid[0][i]
            grid[0][i] = 0
        if grid[2][i] == 0:
            grid[2][i] = grid[1][i]
            grid[1][i] = grid[0][i]
            grid[0][i] = 0
        if grid[3][i] == 0:
            grid[3][i] = grid[2][i]
            grid[2][i] = grid[1][i]
            grid[1][i] = grid[0][i]
            grid[0][i] = 0
        if grid[3][i] == grid[2][i]:
            grid[3][i] = grid[3][i]*2
            grid[2][i] = 0
        if grid[2][i] == grid[1][i]:
            grid[2][i] = grid[2][i]*2
            grid[1][i] = 0
        if grid[1][i] == grid[0][i]:
            grid[1][i] = grid[1][i]*2
            grid[0][i] = 0
        if grid[1][i] == 0:
            grid[1][i] = grid[0][i]
            grid[0][i] = 0
        if grid[2][i] == 0:
            grid[2][i] = grid[1][i]
            grid[1][i] = grid[0][i]
            grid[0][i] = 0
        if grid[3][i] == 0:
            grid[3][i]=grid[2][i]
            grid[2][i]=grid[1][i]
            grid[1][i]=grid[0][i]
            grid[0][i] = 0
def push_left (grid):
    """merge grid values left"""
    for i in range(4):
        if grid[i][2] == 0:
            grid[i][2] = grid[i][3]
            grid[i][3] = 0
        if grid[i][1] == 0:
            grid[i][1] = grid[i][2]
            grid[i][2] = grid[i][3]
            grid[i][3] = 0
        if grid[i][0] == 0:
            grid[i][0] = grid[i][1]
            grid[i][1] = grid[i][2]
            grid[i][2] = grid[i][3]
            grid[i][3] = 0
        if grid[i][0] == grid[i][1]:
            grid[i][0] = grid[i][0]*2
            grid[i][1] = 0
        if grid[i][1] == grid[i][2]:
            grid[i][1] = grid[i][1]*2
            grid[i][2] = 0
        if grid[i][2] == grid[i][3]:
            grid[i][2] = grid[i][2]*2
            grid[i][3] = 0
        if grid[i][2] == 0:
            grid[i][2] = grid[i][3]
            grid[i][3] = 0
        if grid[i][1] == 0:
            grid[i][1] = grid[i][2]
            grid[i][2] = grid[i][3]
            grid[i][3] = 0
        if grid[i][0] == 0:
            grid[i][0] = grid[i][1]
            grid[i][1] = grid[i][2]
            grid[i][2] = grid[i][3]
            grid[i][3] = 0        
        
                      
def push_right (grid):
    """merge grid values right""" 
    for i in range(4):
        if grid[i][1] == 0:
            grid[i][1] = grid[i][0]
            grid[i][0] = 0
        if grid[i][2]==0:
            grid[i][2] = grid [i][1]
            grid[i][1] = grid [i][0]
            grid[i][0] = 0
        if grid[i][3] == 0:
            grid[i][3] = grid[i][2]
            grid[i][2] = grid[i][1]
            grid[i][1] = grid[i][0]
            grid[i][0] = 0
        if grid[i][3] == grid[i][2]:
            grid[i][3] = grid[i][3]*2
            grid[i][2] = 0
        if grid[i][2] == grid[i][1]:
            grid[i][2] = grid[i][2]*2
            grid[i][1] = 0
        if grid[i][1] == grid[i][0]:
            grid[i][1] = grid[i][1]*2
            grid[i][0] = 0
        if grid[i][1] == 0:
            grid[i][1] = grid[i][0]
            grid[i][0] = 0
        if grid[i][2] == 0:        
            grid[i][2] = grid[i][1]
            grid[i][1] = grid[i][0] 
            grid[i][0] = 0
        if grid[i][3] == 0:
            grid[i][3] = grid[i][2]
            grid[i][2] = grid[i][1]
            grid[i][1] = grid[i][0]    
            grid[i][0] = 0