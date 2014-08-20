
#02 May 2014
#if adjacent cells are equal, they are merged into one with twice the value and then moved.




def push_up (grid):
    
    for column in range (len(grid)):
        g=[0,0,0,0,0,0,0,0]
        for row in range(4):
            g[row]=grid[row][column]
        for i in range (4):
            if g[i]==0:
                if g[i+1]==0:
                    if g[i+2]==0:
                        if g[i+3]==0:
                            g[i]=g[i+3]
                            g[i+3]=0
                        else:
                            g[i]=g[i+3]
                            g[i+3]=0
                    else:
                        g[i]=g[i+2]
                        g[i+2]=0
                else:
                    g[i]=g[i+1]
                    g[i+1]=0
        for j in range (4):
            if g[j]==g[j+1]:
                g[j]+=g[j+1]
                g[j+1]=g[j+2]
                g[j+2]=g[j+3]
                g[j+3]=g[j+4]
        for k in range (4):
            grid[k][column]=g[k]
            
            
def push_down (grid):
    
    for column in range (len(grid)):
        g=[0,0,0,0,0,0,0,0]
        for row in range(4):
            g[row]=grid[row][column]
        for i in range (3,-1,-1):
            if g[i]==0:
                if g[i-1]==0:
                    if g[i-2]==0:
                        if g[i-3]==0:
                            g[i]=g[i-3]
                            g[i-3]=0
                        else:
                            g[i]=g[i-3]
                            g[i-3]=0
                    else:
                        g[i]=g[i-2]
                        g[i-2]=0
                else:
                    g[i]=g[i-1]
                    g[i-1]=0
        for j in range (3,-1,-1):
            if g[j]==g[j-1]:
                g[j]+=g[j-1]
                g[j-1]=g[j-2]
                g[j-2]=g[j-3]
                g[j-3]=g[j-4]
        for k in range (4):
            grid[k][column]=g[k]                                

            
def push_right (grid):
    
    for row in range (len(grid)):
            g=[0,0,0,0,0,0,0,0]
            for column in range(4):
                g[column]=grid[row][column]
            for i in range (3,-1,-1):
                if g[i]==0:
                    if g[i-1]==0:
                        if g[i-2]==0:
                            if g[i-3]==0:
                                g[i]=g[i-3]
                                g[i-3]=0
                            else:
                                g[i]=g[i-3]
                                g[i-3]=0
                        else:
                            g[i]=g[i-2]
                            g[i-2]=0
                    else:
                        g[i]=g[i-1]
                        g[i-1]=0
            for j in range (3,-1,-1):
                if g[j]==g[j-1]:
                    g[j]+=g[j-1]
                    g[j-1]=g[j-2]
                    g[j-2]=g[j-3]
                    g[j-3]=g[j-4]
            for k in range (4):
                grid[row][k]=g[k]    
                
                
                
                
                
def push_left (grid):
    
    for row in range (len(grid)):
            g=[0,0,0,0,0,0,0,0]
            for column in range(4):
                g[column]=grid[row][column]
            for i in range (4):
                if g[i]==0:
                    if g[i+1]==0:
                        if g[i+2]==0:
                            if g[i+3]==0:
                                g[i]=g[i+3]
                                g[i+3]=0
                            else:
                                g[i]=g[i+3]
                                g[i+3]=0
                        else:
                            g[i]=g[i+2]
                            g[i+2]=0
                    else:
                        g[i]=g[i+1]
                        g[i+1]=0
            for j in range (4):
                if g[j]==g[j+1]:
                    g[j]+=g[j+1]
                    g[j+1]=g[j+2]
                    g[j+2]=g[j+3]
                    g[j+3]=g[j+4]
            for k in range (4):
                grid[row][k]=g[k]    