def push_up (grid): 
    for row in range(4): 
        for col in range(4): 
            if grid[row][col]==" ":
                grid[row][col]=0
            current = grid[row][col] 
            rowcount = row 
            while rowcount > 0: 
                rowcount -= 1 
                if grid[rowcount][col] == 0:
                    grid[rowcount][col] = current 
                    grid[rowcount+1][col] = 0 
                else:
                    if current == grid[rowcount][col]:
                        grid[rowcount][col] += current
                        grid[rowcount+1][col] = 0
                        
                
                
def push_down (grid):
    """merge grid values downwards"""

    for row in range(4):
            for col in range(4):
                if grid[row][col]==" ":
                    grid[row][col]=0
        
                if grid[row][col]!=0:
                    y=grid[row][col]
                    grid[row][col]=0
                    
                    if grid[3][col]==0:
                        grid[3][col]=y
                        
                    else:
                        if grid[3][col]==y:
                            grid[3][col]+=y
                        
                            if grid[3][col]!=y and grid[3][col]!=0 :
                                if grid[2][col]==0:
                                    y=grid[2][col]
                                                       
                                    if grid[2][col]!=y and grid[2][col]!=0 :
                                        if grid[1][col]==0:
                                            y=grid[1][col]
                                                               
                                            if grid[1][col]!=y and grid[1][col]!=0 :
                                                if grid[0][col]==0:
                                                    y=grid[0][col]                                    
                                               
                                               
                        
               
               
def push_left (grid):
    """merge grid values left"""
    for row in range(4):
            for col in range(4):
                if grid[row][col]==" ":
                    grid[row][col]=0
        
                if grid[row][col]!=0:
                    y=grid[row][col]
                    grid[row][col]=0
                    
                    if grid[row][0]==0:
                        grid[row][0]=y
                        
                    else:
                        if grid[row][0]==y:
                            grid[row][0]+=y
                            
                            if grid[row][0]!=y and grid[row][0]!=0 :
                                if grid[row][1]==0:
                                    y=grid[row][1]
                                                        
                                    if grid[row][1]!=y and grid[row][1]!=0 :
                                        if grid[row][2]==0:
                                            y=grid[row][2]
                                                                
                                            if grid[row][2]!=y and grid[row][2]!=0 :
                                                if grid[row][3]==0:
                                                    y=grid[row][3]                                    
                        
    
                    
def push_right (grid):
    """merge grid values right"""
    for row in range(4):
            for col in range(4):
                if grid[row][col]==" ":
                    grid[row][col]=0
        
                if grid[row][col]!=0:
                    y=grid[row][col]
                    grid[row][col]=0
                    
                    if grid[row][3]==0:
                        grid[row][3]=y
                        
                    else:
                        if grid[row][3]==y:
                            grid[row][3]+=y
                        
                            if grid[row][3]!=y and grid[row][3]!=0 :
                                if grid[row][2]==0:
                                    y=grid[row][2]
                                                        
                                    if grid[row][2]!=y and grid[row][2]!=0 :
                                        if grid[row][1]==0:
                                            y=grid[row][1]
                                                                
                                            if grid[row][1]!=y and grid[row][1]!=0 :
                                                if grid[row][0]==0:
                                                    y=grid[row][0]
                                                    
                        
               