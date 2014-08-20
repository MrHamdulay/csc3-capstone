# A module to write functions for 2048
# Wongwa Giqwa
# 01 May 2014

def push_up(grid):
    # merge grid values upwards
    for col in range (len(grid)):
            n_grid=[0,0,0,0,0,0,0,0] # create a new grid 
            for row in range(4):
                n_grid[row]=grid[row][col]
            for i in range (4):
                if n_grid[i]==0:
                    if n_grid[i+1]==0:
                        if n_grid[i+2]==0:
                            if n_grid[i+3]==0:
                                n_grid[i]=n_grid[i+3]
                                n_grid[i+3]=0
                            else:
                                n_grid[i]=n_grid[i+3]
                                n_grid[i+3]=0
                        else:
                            n_grid[i]=n_grid[i+2]
                            n_grid[i+2]=0
                    else:
                        n_grid[i]=n_grid[i+1]
                        n_grid[i+1]=0
            for j in range (4):
                if n_grid[j]==n_grid[j+1]:
                    n_grid[j]+=n_grid[j+1]
                    n_grid[j+1]=n_grid[j+2]
                    n_grid[j+2]=n_grid[j+3]
                    n_grid[j+3]=n_grid[j+4]
            for k in range (4):
                grid[k][col]=n_grid[k]    
                
def push_down(grid):
    # merge grid values downwards
    
    for col in range (len(grid)):
            n_grid=[0,0,0,0,0,0,0,0]
            for row in range(4):
                n_grid[row]=grid[row][col]
            for i in range (3,-1,-1):
                if n_grid[i]==0:
                    if n_grid[i-1]==0:
                        if n_grid[i-2]==0:
                            if n_grid[i-3]==0:
                                n_grid[i]=n_grid[i-3]
                                n_grid[i-3]=0
                            else:
                                n_grid[i]=n_grid[i-3]
                                n_grid[i-3]=0
                        else:
                            n_grid[i]=n_grid[i-2]
                            n_grid[i-2]=0
                    else:
                        n_grid[i]=n_grid[i-1]
                        n_grid[i-1]=0
            for j in range (3,-1,-1):
                if n_grid[j]==n_grid[j-1]:
                    n_grid[j]+=n_grid[j-1]
                    n_grid[j-1]=n_grid[j-2]
                    n_grid[j-2]=n_grid[j-3]
                    n_grid[j-3]=n_grid[j-4]
            for k in range (4):
                grid[k][col]=n_grid[k]

def push_left(grid):
    # merge grid values left
    
    for row in range (len(grid)):
                n_grid=[0,0,0,0,0,0,0,0]
                for col in range(4):
                    n_grid[col]=grid[row][col]
                for i in range (4):
                    if n_grid[i]==0:
                        if n_grid[i+1]==0:
                            if n_grid[i+2]==0:
                                if n_grid[i+3]==0:
                                    n_grid[i]=n_grid[i+3]
                                    n_grid[i+3]=0
                                else:
                                    n_grid[i]=n_grid[i+3]
                                    n_grid[i+3]=0
                            else:
                                n_grid[i]=n_grid[i+2]
                                n_grid[i+2]=0
                        else:
                            n_grid[i]=n_grid[i+1]
                            n_grid[i+1]=0
                for j in range (4):
                    if n_grid[j]==n_grid[j+1]:
                        n_grid[j]+=n_grid[j+1]
                        n_grid[j+1]=n_grid[j+2]
                        n_grid[j+2]=n_grid[j+3]
                        n_grid[j+3]=n_grid[j+4]
                for k in range (4):
                    grid[row][k]=n_grid[k]   
                    
def push_right(grid):
    # merge grid values right
    
    for row in range (len(grid)):
                n_grid=[0,0,0,0,0,0,0,0]
                for col in range(4):
                    n_grid[col]=grid[row][col]
                for i in range (3,-1,-1):
                    if n_grid[i]==0:
                        if n_grid[i-1]==0:
                            if n_grid[i-2]==0:
                                if n_grid[i-3]==0:
                                    n_grid[i]=n_grid[i-3]
                                    n_grid[i-3]=0
                                else:
                                    n_grid[i]=n_grid[i-3]
                                    n_grid[i-3]=0
                            else:
                                n_grid[i]=n_grid[i-2]
                                n_grid[i-2]=0
                        else:
                            n_grid[i]=n_grid[i-1]
                            n_grid[i-1]=0
                for j in range (3,-1,-1):
                    if n_grid[j]==n_grid[j-1]:
                        n_grid[j]+=n_grid[j-1]
                        n_grid[j-1]=n_grid[j-2]
                        n_grid[j-2]=n_grid[j-3]
                        n_grid[j-3]=n_grid[j-4]
                for k in range (4):
                    grid[row][k]=n_grid[k]        