#Mbongeni Mazibuko
#MZBMBO002
#Assignment 7

def push_up (grid):
    """merges grid values upwards"""
    for k in range(4):
        for i in range(1,4):
            for j in range(4):
                if grid[i-1][j]==0:
                    grid[i-1][j]=grid[i][j]
                    grid[i][j]=0

    for n in range(4): 
        if grid[0][n]==grid[1][n]:
            grid[0][n]=grid[1][n]+grid[0][n]
            if grid[2][n]==grid[3][n]:
                grid[1][n]= grid[2][n]+grid[3][n]  
                grid[2][n]= 0
                grid[3][n]= 0
            else: 
                grid[1][n]= grid[2][n]  
                grid[2][n]= grid[3][n]
                grid[3][n]= 0
        elif grid[1][n]==grid[2][n]:
            grid[1][n]=grid[1][n]+grid[2][n]
            grid[0][n]=grid[0][n]
            grid[2][n]=grid[3][n]
            grid[3][n]=0
        elif grid[2][n]==grid[3][n]:
            grid[2][n]=grid[2][n]+grid[3][n]
            grid[1][n]=grid[1][n]
            grid[0][n]=grid[0][n]
            grid[3][n]=0   
                
def push_down (grid):
    """merges grid values downwards"""
    for k in range(4):
        for i in range(3,0,-1):
            for j in range(4):
                if grid[i][j]==0:
                    grid[i][j]=grid[i-1][j]
                    grid[i-1][j]=0

    for n in range(3,-1,-1): 
        if grid[3][n]==grid[2][n]:
            grid[3][n]=grid[2][n]+grid[3][n]
            if grid[1][n]==grid[0][n]:
                grid[2][n]= grid[1][n]+grid[0][n]  
                grid[1][n]= 0
                grid[0][n]= 0
            else: 
                grid[2][n]= grid[1][n]  
                grid[1][n]= grid[0][n]
                grid[0][n]= 0
        elif grid[2][n]==grid[1][n]:
            grid[2][n]=grid[2][n]+grid[1][n]
            grid[3][n]=grid[3][n]
            grid[1][n]=grid[0][n]
            grid[0][n]=0
        elif grid[1][n]==grid[0][n]:
            grid[1][n]=grid[1][n]+grid[0][n]
            grid[2][n]=grid[2][n]
            grid[3][n]=grid[3][n]
            grid[0][n]=0                

def push_left (grid):
    """merges grid values left"""
    for k in range(4):
        for i in range(4):
            for j in range(1,4):
                if grid[i][j-1]==0:
                    grid[i][j-1]=grid[i][j]
                    grid[i][j]=0
                    
    for n in range(4):
        if grid[n][0]==grid[n][1]:
            grid[n][0]=grid[n][0]+grid[n][1]
            if grid[n][2]==grid[n][3]:
                grid[n][1]= grid[n][2]+grid[n][3]  
                grid[n][2]= 0
                grid[n][3]= 0
            else: 
                grid[n][1]= grid[n][2]  
                grid[n][2]= grid[n][3]
                grid[n][3]= 0
        elif grid[n][1]==grid[n][2]:
            grid[n][1]=grid[n][1]+grid[n][2]
            grid[n][0]=grid[n][0]
            grid[n][2]=grid[n][3]
            grid[n][3]=0
        elif grid[n][2]==grid[n][3]:
            grid[n][2]=grid[n][2]+grid[n][3]
            grid[n][1]=grid[n][1]
            grid[n][0]=grid[n][0]
            grid[n][3]=0           

def push_right (grid):
    """merges grid values right""" 
    for k in range(4):
        for i in range(4):
            for j in range(3,0,-1):
                if grid[i][j]==0:
                    grid[i][j]=grid[i][j-1]
                    grid[i][j-1]=0
                
    for n in range(3,-1,-1): 
        if grid[n][3]==grid[n][2]:
            grid[n][3]=grid[n][2]+grid[n][3]
            if grid[n][1]==grid[n][0]:
                grid[n][2]= grid[n][1]+grid[n][0]
                grid[n][1]= 0
                grid[n][0]= 0
            else: 
                grid[n][2]= grid[n][1] 
                grid[n][1]= grid[n][0]
                grid[n][0]= 0
        elif grid[n][2]==grid[n][1]:
            grid[n][2]=grid[n][2]+grid[n][1]
            grid[n][3]=grid[n][3]
            grid[n][1]=grid[n][0]
            grid[n][0]=0
        elif grid[n][1]==grid[n][0]:
            grid[n][1]=grid[n][1]+grid[n][0]
            grid[n][2]=grid[n][2]
            grid[n][3]=grid[n][3]
            grid[n][0]=0