#DenishaRamaloo
#push
def push_up (grid):
    """merge grid values upwards"""
    for col in range (len(grid)):
        temp=[0,0,0,0,0,0,0,0]
        for row in range(4):
            temp[row]=grid[row][col]
        for i in range (4):
            if temp[i]==0:
                if temp[i+1]==0:
                    if temp[i+2]==0:
                        if temp[i+3]==0:
                            temp[i]=temp[i+3]
                            temp[i+3]=0
                        else:
                            temp[i]=temp[i+3]
                            temp[i+3]=0
                    else:
                        temp[i]=temp[i+2]
                        temp[i+2]=0
                else:
                    temp[i]=temp[i+1]
                    temp[i+1]=0
        for j in range (4):
            if temp[j]==temp[j+1]:
                temp[j]+=temp[j+1]
                temp[j+1]=temp[j+2]
                temp[j+2]=temp[j+3]
                temp[j+3]=temp[j+4]
        for k in range (4):
            grid[k][col]=temp[k]
            
            
def push_down (grid):
    """merge grid values downwards"""
    for col in range (len(grid)):
        temp=[0,0,0,0,0,0,0,0]
        for row in range(4):
            temp[row]=grid[row][col]
        for i in range (3,-1,-1):
            if temp[i]==0:
                if temp[i-1]==0:
                    if temp[i-2]==0:
                        if temp[i-3]==0:
                            temp[i]=temp[i-3]
                            temp[i-3]=0
                        else:
                            temp[i]=temp[i-3]
                            temp[i-3]=0
                    else:
                        temp[i]=temp[i-2]
                        temp[i-2]=0
                else:
                    temp[i]=temp[i-1]
                    temp[i-1]=0
        for j in range (3,-1,-1):
            if temp[j]==temp[j-1]:
                temp[j]+=temp[j-1]
                temp[j-1]=temp[j-2]
                temp[j-2]=temp[j-3]
                temp[j-3]=temp[j-4]
        for k in range (4):
            grid[k][col]=temp[k]                                

            
def push_right (grid):
    """merge grid values left"""
    for row in range (len(grid)):
            temp=[0,0,0,0,0,0,0,0]
            for col in range(4):
                temp[col]=grid[row][col]
            for i in range (3,-1,-1):
                if temp[i]==0:
                    if temp[i-1]==0:
                        if temp[i-2]==0:
                            if temp[i-3]==0:
                                temp[i]=temp[i-3]
                                temp[i-3]=0
                            else:
                                temp[i]=temp[i-3]
                                temp[i-3]=0
                        else:
                            temp[i]=temp[i-2]
                            temp[i-2]=0
                    else:
                        temp[i]=temp[i-1]
                        temp[i-1]=0
            for j in range (3,-1,-1):
                if temp[j]==temp[j-1]:
                    temp[j]+=temp[j-1]
                    temp[j-1]=temp[j-2]
                    temp[j-2]=temp[j-3]
                    temp[j-3]=temp[j-4]
            for k in range (4):
                grid[row][k]=temp[k]    
def push_left (grid):
    """merge grid values right"""
    for row in range (len(grid)):
            temp=[0,0,0,0,0,0,0,0]
            for col in range(4):
                temp[col]=grid[row][col]
            for i in range (4):
                if temp[i]==0:
                    if temp[i+1]==0:
                        if temp[i+2]==0:
                            if temp[i+3]==0:
                                temp[i]=temp[i+3]
                                temp[i+3]=0
                            else:
                                temp[i]=temp[i+3]
                                temp[i+3]=0
                        else:
                            temp[i]=temp[i+2]
                            temp[i+2]=0
                    else:
                        temp[i]=temp[i+1]
                        temp[i+1]=0
            for j in range (4):
                if temp[j]==temp[j+1]:
                    temp[j]+=temp[j+1]
                    temp[j+1]=temp[j+2]
                    temp[j+2]=temp[j+3]
                    temp[j+3]=temp[j+4]
            for k in range (4):
                grid[row][k]=temp[k]  