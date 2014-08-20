def push_up (grid):
    """merge grid values upwards"""
    x=[[],[],[],[]]
    for i in range(4):
        for t in range(4):
            if grid[t][i]!=0:
                x[i].append(grid[t][i])        
            else:
                () 
    for i in range(4):
        while len(x[i])!=4:
            x[i].append(0)
             
    for i in range(4):
        if x[i][0]==x[i][1] and x[i][2]==x[i][3] and x[i][2]==x[i][1]:
            x[i][0]*=2
            x[i][1]*=2
            x[i][2]=0
            x[i][3]=0
                
        elif x[i][0]!=x[i][1] and x[i][2]!=x[i][3] and x[i][2]!=x[i][1]:
            ()
                    
        elif x[i][0]==x[i][1] and x[i][1]==x[i][2] and x[i][3]!=x[i][1]:
            x[i][0]*=2
            x[i][1]=x[i][2]
            x[i][2]=x[i][3]
            x[i][3]=0
                    
        elif x[i][0]==x[i][1] and x[i][2]!=x[i][3]:
            x[i][0]*=2
            x[i][1]=x[i][2]    
            x[i][2]=x[i][3]  
            x[i][3]=0 
                    
        elif x[i][0]!=x[i][1] and x[i][1]==x[i][2] and x[i][3]==x[i][2]:
            x[i][1]*=2
            x[i][2]=x[i][3]
            x[i][3]=0   
                    
        elif x[i][0]!=x[i][1] and x[i][2]==x[i][3] and x[i][1]!=x[i][2]:
            x[i][2]*=2
            x[i][3]=0
                            
        elif x[i][0]!=x[i][3] and x[i][0]==x[i][1] and x[i][2]==x[i][3]:
            x[i][0]*=2
            x[i][1]=x[i][2]*2
            x[i][2]=0
            x[i][3]=0
                    
        elif x[i][0]!=x[i][3] and x[i][1]==x[i][2]:
            x[i][1]*=2
            x[i][2]=x[i][3]
            x[i][3]=0
            
    
    for u in range(4):
        while len(grid[u])!=0: 
            del grid[u][0] 
                    
    for j in range(4):
        for t in range(4):
            grid[j].append(x[t][j])
        
    return grid
    
          
def push_down (grid):
    """merge grid values downwards"""
    x=[[],[],[],[]]
    for i in range(4):
        for t in range(4):
            if grid[t][i]!=0:
                x[i].append(grid[t][i])        
            else:
                () 
    
    for i in range(4):
        while len(x[i])!=4:
            x[i].insert(0,0)
   
    for i in range(4):
        if x[i][0]==x[i][1] and x[i][2]==x[i][3] and x[i][2]==x[i][1]:
            x[i][3]*=2
            x[i][1]=0
            x[i][2]*=2
            x[i][0]=0
                
        elif x[i][0]!=x[i][1] and x[i][2]!=x[i][3] and x[i][2]==x[i][1]:
            x[i][2]*=2
            x[i][1]=x[i][0]
            x[i][0]=0
                    
        elif x[i][0]==x[i][1] and x[i][1]==x[i][2] and x[i][3]!=x[i][1]:
            x[i][2]*=2
            x[i][1]=x[i][0]
            x[i][0]=0
                    
        elif x[i][0]==x[i][1] and x[i][2]!=x[i][3]:
            x[i][1]*=2
            x[i][0]=0    
                    
        elif x[i][0]!=x[i][1] and x[i][1]==x[i][2] and x[i][3]==x[i][2]:
            x[i][3]*=2
            x[i][2]=x[i][1]
            x[i][1]=x[i][0]
            x[i][0]=0
                    
                    
        elif x[i][0]!=x[i][1] and x[i][2]==x[i][3] and x[i][1]!=x[i][2]:
            x[i][3]*=2
            x[i][2]=x[i][1]
            x[i][1]=x[i][0]
            x[i][0]=0
                           
        elif x[i][0]!=x[i][3] and x[i][0]==x[i][1] and x[i][2]==x[i][3]:
            x[i][1]*=2
            x[i][3]*=2
            x[i][0]=0
            x[i][2]=0    
                    
        elif x[i][0]!=x[i][3] and x[i][1]==x[i][2]:
            x[i][2]*=2
            x[i][1]=x[i][0]
            x[i][0]=0          

            
    for u in range(4):
        while len(grid[u])!=0: 
            del grid[u][0] 
            
    for j in range(4):
        for t in range(4):
            grid[j].append(x[t][j])
    return grid
    

def push_left (grid):
    """merge grid values left"""
    x=[[],[],[],[]]
    for i in range(4):
        for t in range(4):
            if grid[i][t]!=0:
                x[i].append(grid[i][t])        
            else:
                ()        
    for i in range(4):
        while len(x[i])!=4:
            x[i].append(0)
             
    for i in range(4):
        if x[i][0]==x[i][1] and x[i][2]==x[i][3] and x[i][2]==x[i][1]:
            x[i][0]*=2
            x[i][1]*=2
            x[i][2]=0
            x[i][3]=0
        
        elif x[i][0]!=x[i][1] and x[i][2]!=x[i][3] and x[i][2]!=x[i][1]:
            ()
            
        elif x[i][0]==x[i][1] and x[i][1]==x[i][2] and x[i][3]!=x[i][1]:
            x[i][0]*=2
            x[i][1]=x[i][2]
            x[i][2]=x[i][3]
            x[i][3]=0
            
        elif x[i][0]==x[i][1] and x[i][2]!=x[i][3]:
            x[i][0]*=2
            x[i][1]=x[i][2]    
            x[i][2]=x[i][3]  
            x[i][3]=0 
            
        elif x[i][0]!=x[i][1] and x[i][1]==x[i][2] and x[i][3]==x[i][2]:
            x[i][1]*=2
            x[i][2]=x[i][3]
            x[i][3]=0   
            
        elif x[i][0]!=x[i][1] and x[i][2]==x[i][3] and x[i][1]!=x[i][2]:
            x[i][2]*=2
            x[i][3]=0
                    
        elif x[i][0]!=x[i][3] and x[i][0]==x[i][1] and x[i][2]==x[i][3]:
            x[i][0]*=2
            x[i][1]=x[i][2]*2
            x[i][2]=0
            x[i][3]=0
            
        elif x[i][0]!=x[i][3] and x[i][1]==x[i][2]:
            x[i][1]*=2
            x[i][2]=x[i][3]
            x[i][3]=0
    
    for u in range(4):
        while len(grid)!=0: 
            del grid[u]         
    
    for i in range(4):
        grid.append(x[i])   
    return grid
        

def push_right (grid):
    """merge grid values right"""  
    x=[[],[],[],[]]
    for i in range(4):
        for t in range(4):
            if grid[i][t]!=0:
                x[i].append(grid[i][t])        
            else:
                ()        
    for i in range(4):
        while len(x[i])!=4:
            x[i].insert(0,0)    
    
    for i in range(4):
        if x[i][0]==x[i][1] and x[i][2]==x[i][3] and x[i][2]==x[i][1]:
            x[i][3]*=2
            x[i][1]=0
            x[i][2]*=2
            x[i][0]=0
        
        elif x[i][0]!=x[i][1] and x[i][2]!=x[i][3] and x[i][2]==x[i][1]:
            x[i][2]*=2
            x[i][1]=x[i][0]
            x[i][0]=0
            
        elif x[i][0]==x[i][1] and x[i][1]==x[i][2] and x[i][3]!=x[i][1]:
            x[i][2]*=2
            x[i][1]=x[i][0]
            x[i][0]=0
            
        elif x[i][0]==x[i][1] and x[i][2]!=x[i][3]:
            x[i][1]*=2
            x[i][0]=0    
            
        elif x[i][0]!=x[i][1] and x[i][1]==x[i][2] and x[i][3]==x[i][2]:
            x[i][3]*=2
            x[i][2]=x[i][1]
            x[i][1]=x[i][0]
            x[i][0]=0
            
            
        elif x[i][0]!=x[i][1] and x[i][2]==x[i][3] and x[i][1]!=x[i][2]:
            x[i][3]*=2
            x[i][2]=x[i][1]
            x[i][1]=x[i][0]
            x[i][0]=0
                   
        elif x[i][0]!=x[i][3] and x[i][0]==x[i][1] and x[i][2]==x[i][3]:
            x[i][1]*=2
            x[i][3]*=2
            x[i][0]=0
            x[i][2]=0    
            
        elif x[i][0]!=x[i][3] and x[i][1]==x[i][2]:
            x[i][2]*=2
            x[i][1]=x[i][0]
            x[i][0]=0
                
    for u in range(4):
        while len(grid)!=0: 
            del grid[u]        
    
    for i in range(4):
        grid.append(x[i])   
    return grid
        