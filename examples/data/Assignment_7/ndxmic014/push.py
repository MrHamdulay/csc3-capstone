'''NDXMIC014
April 30 2014'''

def push_up (grid):
    """merge grid values upwards"""
    for column in range (len(grid)):
        template=[0,0,0,0,0,0,0,0]
        for row in range(4):
            template[row]=grid[row][column]
        for i in range (4):
            if template[i]==0:
                if template[i+1]==0:
                    if template[i+2]==0:
                        if template[i+3]==0:
                            template[i]=template[i+3]
                            template[i+3]=0
                        else:
                            template[i]=template[i+3]
                            template[i+3]=0
                    else:
                        template[i]=template[i+2]
                        template[i+2]=0
                else:
                    template[i]=template[i+1]
                    template[i+1]=0
        for j in range (4):
            if template[j]==template[j+1]:
                template[j]+=template[j+1]
                template[j+1]=template[j+2]
                template[j+2]=template[j+3]
                template[j+3]=template[j+4]
        for k in range (4):
            grid[k][column]=template[k]
            
            
def push_down (grid):
    """merge grid values downwards"""
    for column in range (len(grid)):
        template=[0,0,0,0,0,0,0,0]
        for row in range(4):
            template[row]=grid[row][column]
        for i in range (3,-1,-1):
            if template[i]==0:
                if template[i-1]==0:
                    if template[i-2]==0:
                        if template[i-3]==0:
                            template[i]=template[i-3]
                            template[i-3]=0
                        else:
                            template[i]=template[i-3]
                            template[i-3]=0
                    else:
                        template[i]=template[i-2]
                        template[i-2]=0
                else:
                    template[i]=template[i-1]
                    template[i-1]=0
        for j in range (3,-1,-1):
            if template[j]==template[j-1]:
                template[j]+=template[j-1]
                template[j-1]=template[j-2]
                template[j-2]=template[j-3]
                template[j-3]=template[j-4]
        for k in range (4):
            grid[k][column]=template[k]                                

            
def push_right (grid):
    """merge grid values left"""
    for row in range (len(grid)):
            template=[0,0,0,0,0,0,0,0]
            for column in range(4):
                template[column]=grid[row][column]
            for i in range (3,-1,-1):
                if template[i]==0:
                    if template[i-1]==0:
                        if template[i-2]==0:
                            if template[i-3]==0:
                                template[i]=template[i-3]
                                template[i-3]=0
                            else:
                                template[i]=template[i-3]
                                template[i-3]=0
                        else:
                            template[i]=template[i-2]
                            template[i-2]=0
                    else:
                        template[i]=template[i-1]
                        template[i-1]=0
            for j in range (3,-1,-1):
                if template[j]==template[j-1]:
                    template[j]+=template[j-1]
                    template[j-1]=template[j-2]
                    template[j-2]=template[j-3]
                    template[j-3]=template[j-4]
            for k in range (4):
                grid[row][k]=template[k]    
def push_left (grid):
    """merge grid values right"""
    for row in range (len(grid)):
            template=[0,0,0,0,0,0,0,0]
            for column in range(4):
                template[column]=grid[row][column]
            for i in range (4):
                if template[i]==0:
                    if template[i+1]==0:
                        if template[i+2]==0:
                            if template[i+3]==0:
                                template[i]=template[i+3]
                                template[i+3]=0
                            else:
                                template[i]=template[i+3]
                                template[i+3]=0
                        else:
                            template[i]=template[i+2]
                            template[i+2]=0
                    else:
                        template[i]=template[i+1]
                        template[i+1]=0
            for j in range (4):
                if template[j]==template[j+1]:
                    template[j]+=template[j+1]
                    template[j+1]=template[j+2]
                    template[j+2]=template[j+3]
                    template[j+3]=template[j+4]
            for k in range (4):
                grid[row][k]=template[k]  