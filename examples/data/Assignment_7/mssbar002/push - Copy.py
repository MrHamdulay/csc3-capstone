def push_up (grid):
    """merge grid values upwards"""
    temp = []
    for row in range(4):
        temp.append(grid[row][2])
    print("B4:", temp)
    
    for n in range(4):
        if n < 3: 
            if temp[n] == temp[n+1]:
                tileSum = temp[n]*2
                temp[n], temp[n+1] = 0,0
                for m in range(4):
                    if temp[m] == 0:
                        temp[m] == tileSum
            elif temp[n] != 0:
                for m in range(4):
                    if temp[m] == 0:
                        temp[m] = temp[n] 
                        temp[n] = 0
        if n == 3 and temp[3] != 0:
            for m in range(4):
                if temp[m] == 0:
                    temp[m] = temp[3] 
                    temp[3] = 0
                    break
            
 
    print("AFTA:", temp)
    for row in range(4):
        grid[row][2] = temp[row]
        
def push_down (grid):
    """merge grid values downwards"""

def push_left (grid):
    """merge grid values left"""

def push_right (grid):
    """merge grid values right"""    