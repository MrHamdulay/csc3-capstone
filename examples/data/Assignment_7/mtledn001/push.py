'''This one is called push.py
Ednecia Matlapeng
-- May Day 2014'''

         

def push_down (grid):
    """merge grid values downwards"""
    #first push down
    count=0
    while count<4:
        for i in range(3,-1,-1):
            for k in range(3,-1,-1):
                if grid[k][i]==0:
                    grid[k][i]=grid[k-1][i]
                    grid[k-1][i]=0
        count+=1
        #Now merge the ones that are equal
        for i in range(3,-1,-1):
                for k in range (3,-1,-1):
                    if grid[k][i]==grid[k-1][i]:
                        grid[k][i]=(grid[k][i])*2
                        grid[k-1][i]=0   
    #Re push again to eliminate the zeros from adding
    count=0
    while count<4:
        for i in range(3,-1,-1):
            for k in range(3,-1,-1):
                if grid[k][i]==0:
                    temp=grid[k-1][i]
                    grid[k][i]=temp
                    grid[k-1][i]=0
        count+=1     

def push_right (grid):
    """merge grid values left"""
    #First push left
    for i in range(0,3):
        for k in range(0,3):
            print(i)
            #if grid[i][k]==0:
                
  










def push_left (grid):
    """merge grid values left"""
    #First push left
    count =0
    while count<4:
        for i in range(0,4):
            for k in range(0,3):
                if grid[i][k]==0: 
                    grid[i][k]=grid[i][k+1]
                    grid[i][k+1]=0
        count+=1
    #Merge the same values
    for i in range(3,-1,-1):
        for k in range(3,-1,-1):
            if grid[i][k]==grid[i][k-1]: 
                grid[i][k]*=2
                grid[i][k-1]=0
    #Now I push left againt to eliminate the zeros
    count = 0
    while count<4:
        for i in range(0,4):
            for k in range(0,3):
                if grid[i][k]==0: 
                    grid[i][k]=grid[i][k+1]
                    grid[i][k+1]=0
        count+=1
    
        
def push_up (grid):
    """merge grid values upwards"""
    #first push up
    for i in range(0,4):
        for k in range(0,3): 
            if grid[k][i]==0:
                grid[k][i]=grid[k+1][i]
                grid[k+1][i]=0
    #Now merge the ones that are equal
    for i in range(0,3):
            for k in range(0,3):
                if grid[k][i]==grid[k+1][i]:
                    grid[k][i]=(grid[k][i])*2
                    grid[k+1][i]=0  
    #Now you push up again
    count=0
    while count<4:
        for i in range(0,4):
            for k in range(0,3):
                if grid[k][i]==0:
                    grid[k][i]=grid[k+1][i]
                    grid[k+1][i]=0  
        count+=1 

        

