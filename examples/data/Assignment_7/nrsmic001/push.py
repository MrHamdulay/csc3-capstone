"""Program to run 2048
Micaela Narasmulu
3 May 2014"""

def push_up (grid): #merge grid values upwards
    for col in range (len(grid)):
        t=[0,0,0,0,0,0,0,0] 
        for row in range(4):
            t[row]=grid[row][col]
        for i in range (4):
            if t[i]==0:
                if t[i+1]==0:
                    if t[i+2]==0:
                        if t[i+3]==0:
                            t[i]=t[i+3]
                            t[i+3]=0
                        else:
                            t[i]=t[i+3]
                            t[i+3]=0
                    else:
                        t[i]=t[i+2]
                        t[i+2]=0
                else:
                    t[i]=t[i+1]
                    t[i+1]=0
        for j in range (4):
            if t[j]==t[j+1]:
                t[j]+=t[j+1]
                t[j+1]=t[j+2]
                t[j+2]=t[j+3]
                t[j+3]=t[j+4]
        for k in range (4):
            grid[k][col]=t[k]

def push_right (grid): #merge grid values left
    for row in range (len(grid)):
            t=[0,0,0,0,0,0,0,0]
            for col in range(4):
                t[col]=grid[row][col]
            for i in range (3,-1,-1):
                if t[i]==0:
                    if t[i-1]==0:
                        if t[i-2]==0:
                            if t[i-3]==0:
                                t[i]=t[i-3]
                                t[i-3]=0
                            else:
                                t[i]=t[i-3]
                                t[i-3]=0
                        else:
                            t[i]=t[i-2]
                            t[i-2]=0
                    else:
                        t[i]=t[i-1]
                        t[i-1]=0
            for j in range (3,-1,-1):
                if t[j]==t[j-1]:
                    t[j]+=t[j-1]
                    t[j-1]=t[j-2]
                    t[j-2]=t[j-3]
                    t[j-3]=t[j-4]
            for k in range (4):
                grid[row][k]=t[k]    
            
            
def push_down (grid): #merge grid values downwards
    for col in range (len(grid)):
        t=[0,0,0,0,0,0,0,0]
        for row in range(4):
            t[row]=grid[row][col]
        for i in range (3,-1,-1):
            if t[i]==0:
                if t[i-1]==0:
                    if t[i-2]==0:
                        if t[i-3]==0:
                            t[i]=t[i-3]
                            t[i-3]=0
                        else:
                            t[i]=t[i-3]
                            t[i-3]=0
                    else:
                        t[i]=t[i-2]
                        t[i-2]=0
                else:
                    t[i]=t[i-1]
                    t[i-1]=0
        for j in range (3,-1,-1):
            if t[j]==t[j-1]:
                t[j]+=t[j-1]
                t[j-1]=t[j-2]
                t[j-2]=t[j-3]
                t[j-3]=t[j-4]
        for k in range (4):
            grid[k][col]=t[k]                                

            

                
                
def push_left (grid): #merge grid values right
    for row in range (len(grid)):
            t=[0,0,0,0,0,0,0,0]
            for col in range(4):
                t[col]=grid[row][col]
            for i in range (4):
                if t[i]==0:
                    if t[i+1]==0:
                        if t[i+2]==0:
                            if t[i+3]==0:
                                t[i]=t[i+3]
                                t[i+3]=0
                            else:
                                t[i]=t[i+3]
                                t[i+3]=0
                        else:
                            t[i]=t[i+2]
                            t[i+2]=0
                    else:
                        t[i]=t[i+1]
                        t[i+1]=0
            for j in range (4):
                if t[j]==t[j+1]:
                    t[j]+=t[j+1]
                    t[j+1]=t[j+2]
                    t[j+2]=t[j+3]
                    t[j+3]=t[j+4]
            for k in range (4):
                grid[row][k]=t[k]  