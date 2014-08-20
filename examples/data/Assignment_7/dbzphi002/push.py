#Thembekile Dubazana
#dbzphi002
#Assignment7:Q3

def push_left (grid):
    """merge grid values left"""
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] !=0:
                if j==0:
                    grid[i][j]=grid[i][j]    
                else:
                    val=grid[i][j]
                    grid[i][j]=0
                    n=1
                    while grid[i][j-n]==0 and j-n > -1:
                        n+=1
                    grid[i][j-n+1]=val
    lsumming(grid)
    return grid

def push_right (grid):
    """merge grid values right"""         
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] !=0:
                if j==3:
                    grid[i][j]=grid[i][j]
                else:
                    val=grid[i][j]
                    grid[i][j]=0
                    n=1
                    if grid[i][j+n]==0 and j+n < 4:
                        n+=1
                    grid[i][j+n-1]=val 
    rsumming(grid)
    return grid
        
                        

def push_up (grid):
    """merge grid values upwards"""
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] !=0:
                if i==0:
                    grid[i][j]=grid[i][j]
                else:
                    val=grid[i][j]
                    grid[i][j]=0
                    n=1
                    while grid[i-n][j]==0 and i-n > -1:
                        n+=1
                    grid[i-n+1][j]=val
    usumming(grid)  
    return grid



def push_down (grid):
    """merge grid values downwards"""
    for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] !=0:
                    if i==3:
                        grid[i][j]=grid[i][j]
                    else:
                        val=grid[i][j]
                        grid[i][j]=0
                        n=1
                        if grid[i+n][j]==0 and i+n < 4 :
                            n+=1
                        grid[i+n-1][j]=val 
    dsumming(grid)
    return grid
                        
def lsumming(grid):
    for i in range(4):
        for k in range(3):
            if grid[i][k]==grid[i][k+1] and grid[i][k] !=0:
                m=grid[i][k]
                grid[i][k]=m*2
                grid[i][k+1]=0
            n=1   
            while grid[i][k-n]==0 and k-n > -1:
                n+=1
                grid[i][k-n+1]=grid[i][k] 
                grid[i][k]=0            
    return grid

def rsumming(grid):
    for i in range(4):
        for k in range(4):
            if grid[i][k]==grid[i][k-1] and grid[i][k] !=0 :
                m=grid[i][k]
                grid[i][k]=m*2
                grid[i][k-1]=0
            n=0
            if grid[i][k+n]==0 and k+n < 4 :
                n+=1
                grid[i][k+n-1]=grid[i][k] 
                grid[i][k]=0            
    return grid 

def usumming(grid):
    for i in range(3):
        for k in range(4):
            if grid[i][k]==grid[i-1][k] and grid[i][k] !=0:
                m=grid[i][k]
                grid[i][k]=m*2
                grid[i-1][k]=0
            n=1
            while grid[i-n][k]==0 and i-n > -1:
                n+=1
                grid[i-n+1][k]=grid[i][k] 
                grid[i][k]=0
    return grid  

def dsumming(grid):
    for i in range(4):
        for k in range(4):
            if i!=3:
                if grid[i+1][k]==grid[i][k] and grid[i][k] !=0:
                    m=grid[i][k]
                    grid[i][k]=0
                    grid[i+1][k]=m*2
                n=1
                if grid[i+n][k]==0:
                    n+=1
                    grid[i+n-1][k]=grid[i][k] 
                    grid[i][k]=0            
    return grid  