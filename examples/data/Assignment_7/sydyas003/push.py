import util

def push_up (grid):
    """merge grid values upwards"""
    temp=[[],[],[],[]]
    for i in range(4):
        for j in range(4):
            temp[i].append(grid[j][i])
            
    for j in range(4):
        count=temp[j].count(0)
        for i in range(count):
            temp[j].remove(0)
            temp[j].append(0)
            
    for i in range(4):
        for j in range(3):
            if(temp[i][j]==temp[i][j+1] and temp[i][j]!=0):
                temp[i][j]=temp[i][j]+temp[i][j+1]
                temp[i].remove(temp[i][j+1])
                temp[i].append(0)
    for i in range(4):
        for j in range(4):
            grid[j][i]=temp[i][j]
    
def push_down (grid):
    """merge grid values downwards"""
    temp=[[],[],[],[]]
    for i in range(4):
        for j in range(4):
            temp[i].append(grid[j][i])
    for i in range(4):
        temp[i].reverse()
    for j in range(4):
        count=temp[j].count(0)
        for i in range(count):
            temp[j].remove(0)
            temp[j].append(0)
            
    for i in range(4):
        for j in range(3):
            if(temp[i][j]==temp[i][j+1] and temp[i][j]!=0):
                temp[i][j]=temp[i][j]+temp[i][j+1]
                temp[i].remove(temp[i][j+1])
                temp[i].append(0)
    for i in range(4):
        temp[i].reverse()     
        
    for i in range(4):
        for j in range(4):
            grid[j][i]=temp[i][j]
        

def push_left (grid):
    """merge grid values left"""
    
    for i in range(4):
        count=grid[i].count(0)
        for j in range(count):
            grid[i].remove(0)
            grid[i].append(0)
            
    for i in range(4):
        for j in range(3):
            if(grid[i][j]==grid[i][j+1]):
                grid[i][j]=2*grid[i][j]
                grid[i].remove(grid[i][j+1])
                grid[i].append(0)
    

def push_right (grid):
    """merge grid values right""" 
    temp=grid
    
    for i in range(4):
            temp[i].reverse()    
              
    for j in range(4):
        count=temp[j].count(0)
        for i in range(count):
            temp[j].remove(0)
            temp[j].append(0)
                
    for i in range(4):
        for j in range(3):
            if(temp[i][j]==temp[i][j+1] and temp[i][j]!=0):
                temp[i][j]=temp[i][j]+temp[i][j+1]
                temp[i].remove(temp[i][j+1])
                temp[i].append(0)
    for i in range(4):
        temp[i].reverse()    
                
    for i in range(4):
        for j in range(4):
            grid[i][j]=temp[i][j]                    