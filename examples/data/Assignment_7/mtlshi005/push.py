

def push_up (grid):
    """merge grid values upwards"""
    
    for row in range(4):
            for col in range(4):
                if (row+1)>=0: continue
                elif grid[row][col]==grid[row+1][col]:
                        return grid[row][col]+ grid[row+1][col]    
    
    




def push_down (grid):
    """merge grid values downwards"""
    
    for row in range(4):
                for col in range(4):
                    if (row-1)>=0:
                        continue
                    
                    elif grid[row][col]==grid[row-1][col]:
                            return grid[row][col]+ grid[row-1][col]    
    


def push_left (grid):
    """merge grid values left"""
    for row in range(4):
        for col in range(4):
            if (col-1)>=0:
                continue
            
            elif grid[row][col]==grid[row][col-1]:
                    return grid[row][col]+ grid[row][col-1]
    





def push_right (grid):
    """merge grid values right"""          
    for row in range(4):
            for col in range(4):
                if (col+1)>=0:
                    continue
                
                elif grid[row][col]==grid[row][col+1]:
                        return grid[row][col]+ grid[row][col+1]    
    