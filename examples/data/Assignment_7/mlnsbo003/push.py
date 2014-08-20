'''Push Module
Sbongakonke Mlangeni
02 May 2014'''

def push_up (grid):
    """merge grid values upwards"""
    for i in range(4::-1):
        for j in range(3):
            if grid[j][i] ==grid[j][i+1]:
                return grid[j][i] + grid[j][i+1]
            
def push_down (grid):
    """merge grid values downwards"""
    for i in range(4):
            for j in range(3):
                if grid[j][i] ==grid[j][i+1]:
                    return grid[j][i] + grid[j][i+1]    