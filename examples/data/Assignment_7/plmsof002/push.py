#Push
#Sofia Palmer
#30 April 2014

def push_up (grid):
    """merge grid values upwards"""
    height = 4
    for row in range(height):
        for col in range(height):
            if str(grid[row][col]) == str(grid[row+1][col]):
                grid[row+1][col] = str((grid[row+1][col])**2)
            
            

def push_down (grid):
    """merge grid values downwards"""

def push_left (grid):
    """merge grid values left"""

def push_right (grid):
    """merge grid values right""" 