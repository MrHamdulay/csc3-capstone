def p_d (grid):
    for i in range(3):
        for R in range(2,-1,-1):
            for C in range(3,-1,-1):
                if grid[R+1][C] == 0:
                    grid[R+1][C] = grid[row][column]
                    grid[R][C] = 0
                    
    for R in range(2,-1,-1):
        for C in range(3,-1,-1):    
                if grid[R+1][C] == grid[R][C]:
                    grid[R+1][C] = grid[R+1][C]*2
                    grid[R][C] = 0
                    
    for R in range(2,-1,-1):
        for C in range(3,-1,-1):
            if grid[R+1][C] == 0:
                grid[R+1][C] = grid[R][C]
                grid[R][C] = 0
                
    return grid
                                                          
def p_l (grid):
    for i in range(3):
        for R in range(4):
            for C in range(1,4):
                if grid[R][C-1] == 0:
                    grid[R][C-1] = grid[R][C]
                    grid[R][C] = 0
                    
    for R in range(4):
        for C in range(1,4):                    
            if grid[R][C-1] == grid[R][C]:
                grid[R][C-1] = grid[R][C-1]*2
                grid[R][C] = 0
                
    for R in range(4):
        for C in range(1,4):
            if grid[R][C-1] == 0:
                grid[R][C-1] = grid[R][C]
                grid[R][C] = 0

    return grid

def p_up (grid):
    for i in range(3):
        for R in range(1,4):
            for C in range(4):
                if grid[R-1][C] == 0:
                    grid[R-1][C] = grid[R][C]
                    grid[R][C] = 0
                   
    for R in range(1,4):
        for C in range(4):    
                if grid[R-1][C]== grid[R][C]:
                    grid[R-1][C]= grid[R-1][C]*2
                    grid[R][C] = 0
                        
    for R in range(1,4):
        for C in range(4):
            if grid[R-1][C] == 0:
                grid[R-1][C] = grid[R][C]
                grid[R][C] = 0    
                
    return grid

def p_rt (grid):
    for i in range(3):
        for R in range(3,-1,-1):
            for C in range(2,-1,-1):
                if grid[R][C+1] == 0:
                    grid[R][C+1] = grid[R][C]
                    grid[R][C] = 0
                    
    for R in range(3,-1,-1):
        for C in range(2,-1,-1):
            if grid[R][C+1] == grid[R][C]:
                grid[R][C+1] = grid[R][C+1]*2
                grid[R][C] = 0
                
    for R in range(3,-1,-1):
        for C in range(2,-1,-1):
            if grid[R][C+1] == 0:
                grid[R][C+1] = grid[R][C]
                grid[R][C] = 0
                
    return grid