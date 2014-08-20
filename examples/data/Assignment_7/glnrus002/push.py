#GLNRUS002
#30 APRIL
#Ass7, Q3
#.  Your task in this question is to complete the code for a 2048 program, using the utility module (util.py) from Question 2 and a supplied main program (2048.py).  The heart of the game is the set of merging functions that merge adjacent equal values and eliminate gaps 
def push_up (grid):
    """merge grid values upwards"""
    #move up where empty
    x=0
    y=0
    for i in range(4):
        for j in range(4):
            if grid[i-1][j]==0 and 0<i<3:
                tmp=grid[i][j]
                grid[i-1][j]=tmp
                grid[i][j]=grid[i+1][j]
            elif grid[i-1][j]==0:#bottom row
                grid[i-1][j]=grid[i][j]
                grid[i][j]=0
            elif i==0 and grid[i][j]==0:
                grid[i][j]=grid[i+1][j]
    return grid
                  
def push_down (grid):
    """merge grid values downwards"""

def push_left (grid):
    """merge grid values left"""

def push_right (grid):
    """merge grid values right"""          
