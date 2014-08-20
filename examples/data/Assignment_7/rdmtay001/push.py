# moving part of 2048
# Tayla Radmore
# 2 May 2014


def push_up (grid):
    """merge grid values upwards"""
    for col in range(4):
        small_list=[]
        
        for row in range(4):
            if grid[row][col]==0:                    
                small_list.append(grid[row][col])
            else:
                small_list.append(1)
            
            if small_list==[0,0,0,1]:             #option 2       
                x=grid[3][col]
                grid[3][col]=0
                grid[0][col]=x
                
            if small_list==[0,0,1,0]:         #option 3
                x=grid[2][col]
                grid[2][col]=0
                grid[0][col]=x
                
            if small_list==[0,0,1,1]:                #option 4
                if grid[2][col]==grid[3][col]:       #same number
                    x=grid[2][col]*2
                    grid[2][col]=0
                    grid[3][col]=0
                    grid[0][col]=x
                    
                else:                               #different number
                    first=grid[2][col]
                    second=grid[3][col]
                    grid[2][col]=0
                    grid[3][col]=0
                    grid[0][col]=first
                    grid[1][col]=second
                    
            if small_list==[0,1,0,0]:              #option 5
                x=grid[1][col]
                grid[1][col]=0
                grid[0][col]=x                
                
                
            if small_list==[0,1,1,0]:               #option 6
                if grid[1][col]==grid[2][col]:       #same
                    x=grid[1][col]*2
                    grid[1][col]=0
                    grid[2][col]=0
                    grid[0][col]=x
                    
                else:                              #different
                    first=grid[1][col]
                    second=grid[2][col]
                    grid[1][col]=0
                    grid[2][col]=0
                    grid[0][col]=first
                    grid[1][col]=second
                    
            if small_list==[0,1,0,1]:                #option 7
                if grid[1][col]==grid[3][col]:       #same
                    x=(grid[1][col])*2
                    grid[1][col]=0
                    grid[3][col]=0
                    grid[0][col]=x
                                    
                else:                              #different
                    first=grid[1][col]
                    second=grid[3][col]
                    grid[1][col]=0
                    grid[3][col]=0
                    grid[0][col]=first
                    grid[1][col]=second                
            
            if small_list==[0,1,1,1]:               #option 8
                if grid[1][col]==grid[2][col]:      # second and third row same
                    x=(grid[1][col])*2
                    grid[1][col]=0
                    grid[2][col]=0
                    grid[0][col]=x
                    y=grid[3][col]
                    grid[3][col]=0
                    grid[1][col]=y
                    
                elif grid[2][col]==grid[3][col]:       # third and fourth row same
                    x=(grid[2][col])*2
                    grid[2][col]=0
                    grid[3][col]=0
                    y=grid[1][col]
                    grid[0][col]=y                    
                    grid[1][col]=x
                    
                else:                               # different
                    x=grid[1][col]
                    y=grid[2][col]
                    z=grid[3][col]
                    grid[0][col]=x
                    grid[1][col]=y
                    grid[2][col]=z
                    grid[3][col]=0
                    
            if small_list==[1,1,0,0]:                  # option 10
                if grid[0][col]==grid[1][col]:       #same
                    x=(grid[1][col])*2
                    grid[0][col]=0
                    grid[1][col]=0
                    grid[0][col]=x
                                                    
            if small_list==[1,0,1,0]:               # option 11
                if grid[0][col]==grid[2][col]:       #same
                    x=(grid[0][col])*2
                    grid[2][col]=0
                    grid[0][col]=x
                                                   
                else:                              #different
                    second=grid[2][col]
                    grid[2][col]=0
                    grid[1][col]=second 
                    
            if small_list==[1,0,0,1]:              #option 12
                if grid[0][col]==grid[3][col]:       #same
                    x=(grid[0][col])*2
                    grid[3][col]=0
                    grid[0][col]=x
                                                   
                else:                              #different
                    second=grid[3][col]
                    grid[3][col]=0
                    grid[1][col]=second 
                    
            if small_list==[1,1,1,0]:            #option 13
                if grid[0][col]==grid[1][col]:      # second and first row same
                    x=(grid[1][col])*2
                    grid[0][col]=0
                    grid[1][col]=0
                    grid[0][col]=x
                    y=grid[2][col]
                    grid[2][col]=0
                    grid[1][col]=y
                                    
                elif grid[1][col]==grid[2][col]:       # third and second row same
                    x=(grid[2][col])*2
                    grid[1][col]=0
                    grid[2][col]=0                                        
                    grid[1][col]=x 
                    
            if small_list==[1,1,0,1]:                 #option 14
                if grid[0][col]==grid[1][col]:      # first and second row same
                    x=(grid[1][col])*2
                    grid[0][col]=0
                    grid[1][col]=0
                    grid[0][col]=x
                    y=grid[3][col]
                    grid[3][col]=0
                    grid[1][col]=y
                                   
                elif grid[1][col]==grid[3][col]:       # second and fourth row same
                    x=(grid[1][col])*2
                    grid[1][col]=0
                    grid[3][col]=0                                    
                    grid[1][col]=x
                                   
                else:                               # different
                    z=grid[3][col]
                    rid[2][col]=z
                    grid[3][col]=0  
                    
            if small_list==[1,0,1,1]:              # option 15
                if grid[0][col]==grid[2][col]:      # first and third row same
                    x=(grid[0][col])*2
                    grid[0][col]=0
                    grid[2][col]=0
                    grid[0][col]=x
                    y=grid[3][col]
                    grid[3][col]=0
                    grid[1][col]=y
                    
                elif grid[2][col]==grid[3][col]:       # third and fourth row same
                    x=(grid[2][col])*2
                    grid[2][col]=0
                    grid[3][col]=0                   
                    grid[1][col]=x
                                   
                else:                               # different
                    y=grid[2][col]
                    z=grid[3][col]
                    grid[1][col]=y
                    grid[2][col]=z
                    grid[3][col]=0 
                    
            if small_list==[1,1,1,1]:                          #option 16
                if grid[0][col]==grid[1][col]:              # first and second row same and possibly of third and fourth same
                    x=(grid[0][col])*2
                    grid[0][col]=x
                    y=grid[2][col]
                    z=grid[3][col]
                    grid[1][col]=y
                    grid[2][col]=z
                    if grid[2][col]==grid[1][col]:
                        x_2=(grid[2][col])*2
                        grid[2][col]=x_2
                        grid[3][col]=0                       
                        
                elif grid[1][col]==grid[2][col]:            # second and third row same
                    x=(grid[1][col])*2
                    grid[1][col]=x
                    y=grid[2][col]
                    z=grid[3][col]
                    grid[1][col]=y
                    grid[2][col]=z 
                    
                elif grid[2][col]==grid[3][col]:           #third and fourth row same
                    x=(grid[2][col])*2
                    grid[2][col]=x
                    grid[3][col]=0
                    
                    
def push_down (grid):
    """merge grid values downwards"""
    for col in range(4):
            small_list=[] 
            
            for row in range(4):
                if grid[row][col]==0:                    
                    small_list.append(grid[row][col])
                else:
                    small_list.append(1)
                
                if small_list==[1,0,0,0]:             #option 9       
                    x=grid[0][col]
                    grid[0][col]=0
                    grid[3][col]=x
                    
                if small_list==[0,0,1,0]:         #option 3
                    x=grid[2][col]
                    grid[2][col]=0
                    grid[3][col]=x
                    
                if small_list==[0,0,1,1]:                #option 4
                    if grid[2][col]==grid[3][col]:       #same number
                        x=(grid[2][col])*2
                        grid[2][col]=0
                        grid[3][col]=x
                        
                    
                        
                if small_list==[0,1,0,0]:              #option 5
                    x=grid[1][col]
                    grid[1][col]=0
                    grid[3][col]=x                
                    
                    
                if small_list==[0,1,1,0]:               #option 6
                    if grid[1][col]==grid[2][col]:       #same
                        x=(grid[1][col])*2
                        grid[1][col]=0
                        grid[2][col]=0
                        grid[3][col]=x
                        
                    else:                              #different
                        first=grid[1][col]
                        second=grid[2][col]
                        grid[1][col]=0
                        grid[2][col]=0
                        grid[2][col]=first
                        grid[3][col]=second
                        
                if small_list==[0,1,0,1]:                #option 7
                    if grid[1][col]==grid[3][col]:       #same
                        x=(grid[1][col])*2
                        grid[1][col]=0
                        grid[3][col]=0
                        grid[3][col]=x
                                        
                    else:                              #different
                        first=grid[1][col]
                        grid[1][col]=0
                        grid[2][col]=first
                                        
                
                if small_list==[0,1,1,1]:               #option 8
                    if grid[1][col]==grid[2][col]:      # second and third row same
                        x=(grid[1][col])*2
                        grid[1][col]=0
                        grid[2][col]=x
                    
                        
                    elif grid[2][col]==grid[3][col]:       # third and fourth row same
                        x=(grid[2][col])*2
                        y=grid[1][col]
                        grid[2][col]=y                    
                        grid[3][col]=x
                        
                        
                if small_list==[1,1,0,0]:                  # option 10
                    if grid[0][col]==grid[1][col]:       #same
                        x=(grid[1][col])*2
                        grid[0][col]=0
                        grid[1][col]=0
                        grid[3][col]=x
                        
                    else: 
                        x=grid[0][col]
                        y=grid[1][col]
                        grid[0][col]=0
                        grid[1][col]=0
                        grid[2][col]=x
                        grid[3][col]=y
                                                        
                if small_list==[1,0,1,0]:               # option 11
                    if grid[0][col]==grid[2][col]:       #same
                        x=(grid[0][col])*2
                        grid[2][col]=0
                        grid[0][col]=0
                        grid[3][col]=x
                                                       
                    else:                              #different
                        first=grid[0][col]
                        second=grid[2][col]
                        grid[0][col]=0
                        grid[2][col]=first
                        grid[3][col]=second 
                        
                if small_list==[1,0,0,1]:              #option 12
                    if grid[0][col]==grid[3][col]:       #same
                        x=(grid[0][col])*2
                        grid[3][col]=x
                        grid[0][col]=0
                                                       
                    else:                              #different
                        first=grid[0][col]
                        grid[0][col]=0
                        grid[2][col]=first 
                        
                if small_list==[1,1,1,0]:            #option 13
                    if grid[0][col]==grid[1][col]:      # second and first row same
                        x=(grid[1][col])*2
                        grid[0][col]=0
                        grid[1][col]=0
                        y=grid[2][col]
                        grid[2][col]=x
                        grid[3][col]=y
                                        
                    elif grid[1][col]==grid[2][col]:       # third and second row same
                        x=(grid[2][col])*2
                        y=grid[0][col]
                        grid[1][col]=0
                        grid[0][col]=0
                        grid[2][col]=y                                        
                        grid[3][col]=x 
                        
                    else:                              #different
                        x=grid[0][col]
                        y=grid[1][col]
                        z=grid[2][col]
                        grid[0][col]=0
                        grid[1][col]=x
                        grid[2][col]=y
                        grid[3][col]=z
                        
                if small_list==[1,1,0,1]:                 #option 14
                    if grid[0][col]==grid[1][col]:      # first and second row same
                        x=(grid[1][col])*2
                        grid[0][col]=0
                        grid[1][col]=0
                        grid[2][col]=x
                        
                                                             
                    elif grid[1][col]==grid[3][col]:       # second and fourth row same
                        x=(grid[1][col])*2
                        grid[0][col]=y
                        grid[1][col]=0
                        grid[3][col]=x
                        grid[0][col]=0
                        grid[2][col]=y
                                       
                    else:                               # different
                        
                        z=grid[1][col]
                        grid[2][col]=z
                        x=grid[0][col]
                        grid[1][col]=x
                        grid[0][col]=0
                        
                if small_list==[1,0,1,1]:              # option 15
                    if grid[0][col]==grid[2][col]:      # first and third row same
                        x=(grid[0][col])*2
                        grid[0][col]=0
                        grid[2][col]=x
                        
                        
                    elif grid[2][col]==grid[3][col]:       # third and fourth row same
                        x=(grid[2][col])*2
                        y=grid[0][col]
                        grid[0][col]=0
                        grid[2][col]=y
                        grid[3][col]=x
                                       
                    else:                               # different
                        x=grid[0][col]
                        grid[1][col]=x
                        grid[0][col]=0 
                        
                if small_list==[1,1,1,1]:                          #option 16
                    if grid[2][col]==grid[3][col]:              # third and second row same and possibly of third and fourth same
                        x=(grid[2][col])*2
                        grid[3][col]=x
                        y=grid[0][col]
                        z=grid[1][col]
                        grid[1][col]=y
                        grid[2][col]=z
                        grid[0][col]=0
                        if grid[2][col]==grid[1][col]:
                            x_2=(grid[2][col])*2
                            grid[2][col]=x_2
                            grid[1][col]=0                       
                            
                    elif grid[1][col]==grid[2][col]:            # second and third row same
                        x=(grid[1][col])*2
                        grid[2][col]=x
                        y=grid[0][col]
                        grid[3][col]=y
                        grid[0][col]=0 
                        
                    elif grid[0][col]==grid[1][col]:           #third and fourth row same
                        x=(grid[0][col])*2
                        grid[1][col]=x
                        grid[0][col]=0





def push_left (grid):
    """merge grid values left"""
    for row in range(4):
            small_list=[]
            
            for col in range(4):
                if grid[row][col]==0:                    
                    small_list.append(grid[row][col])
                else:
                    small_list.append(1)
                
                if small_list==[0,0,0,1]:             #option 2       
                    x=grid[row][3]
                    grid[row][3]=0
                    grid[row][0]=x
                    
                if small_list==[0,0,1,0]:         #option 3
                    x=grid[row][2]
                    grid[row][2]=0
                    grid[row][0]=x
                    
                if small_list==[0,0,1,1]:                #option 4
                    if grid[row][2]==grid[row][3]:       #same number
                        x=(grid[row][2])*2
                        grid[row][2]=0
                        grid[row][3]=0
                        grid[row][0]=x
                        
                    else:                               #different number
                        first=grid[row][2]
                        second=grid[row][3]
                        grid[row][2]=0
                        grid[row][3]=0
                        grid[row][0]=first
                        grid[row][1]=second
                        
                if small_list==[0,1,0,0]:              #option 5
                    x=grid[row][1]
                    grid[row][1]=0
                    grid[row][0]=x                
                    
                    
                if small_list==[0,1,1,0]:               #option 6
                    if grid[row][1]==grid[row][2]:       #same
                        x=(grid[row][1])*2
                        grid[row][1]=0
                        grid[row][2]=0
                        grid[row][0]=x
                        
                    else:                              #different
                        first=grid[row][1]
                        second=grid[row][2]
                        grid[row][1]=0
                        grid[row][2]=0
                        grid[row][0]=first
                        grid[row][1]=second
                        
                if small_list==[0,1,0,1]:                #option 7
                    if grid[row][1]==grid[row][3]:       #same
                        x=(grid[row][1])*2
                        grid[row][1]=0
                        grid[row][3]=0
                        grid[row][0]=x
                                        
                    else:                              #different
                        first=grid[row][1]
                        second=grid[row][3]
                        grid[row][1]=0
                        grid[row][3]=0
                        grid[row][0]=first
                        grid[row][1]=second                
                
                if small_list==[0,1,1,1]:               #option 8
                    if grid[row][1]==grid[row][2]:      # second and third row same
                        x=(grid[row][1])*2
                        grid[row][1]=0
                        grid[row][2]=0
                        grid[row][0]=x
                        y=grid[row][3]
                        grid[row][3]=0
                        grid[row][1]=y
                        
                    elif grid[row][2]==grid[row][3]:       # third and fourth row same
                        x=(grid[row][2])*2
                        grid[row][2]=0
                        grid[row][3]=0
                        y=grid[row][1]
                        grid[row][0]=y                    
                        grid[row][1]=x
                        
                    else:                               # different
                        x=grid[row][1]
                        y=grid[row][2]
                        z=grid[row][3]
                        grid[row][0]=x
                        grid[row][1]=y
                        grid[row][2]=z
                        grid[row][3]=0
                        
                if small_list==[1,1,0,0]:                  # option 10
                    if grid[row][0]==grid[row][1]:       #same
                        x=(grid[row][1])*2
                        grid[row][0]=0
                        grid[row][1]=0
                        grid[row][0]=x
                                                        
                if small_list==[1,0,1,0]:               # option 11
                    if grid[row][0]==grid[row][2]:       #same
                        x=(grid[row][0])*2
                        grid[row][2]=0
                        grid[row][0]=x
                                                       
                    else:                              #different
                        second=grid[row][2]
                        grid[row][2]=0
                        grid[row][1]=second 
                        
                if small_list==[1,0,0,1]:              #option 12
                    if grid[row][0]==grid[row][3]:       #same
                        x=(grid[row][0])*2
                        grid[row][3]=0
                        grid[row][0]=x
                                                       
                    else:                              #different
                        second=grid[row][3]
                        grid[row][3]=0
                        grid[row][1]=second 
                        
                if small_list==[1,1,1,0]:            #option 13
                    if grid[row][0]==grid[row][1]:      # second and first row same
                        x=(grid[row][1])*2
                        grid[row][0]=0
                        grid[row][1]=0
                        grid[row][0]=x
                        y=grid[row][2]
                        grid[row][2]=0
                        grid[row][1]=y
                                        
                    elif grid[row][1]==grid[row][2]:       # third and second row same
                        x=(grid[row][2])*2
                        grid[row][1]=0
                        grid[row][2]=0                                        
                        grid[row][1]=x 
                        
                if small_list==[1,1,0,1]:                 #option 14
                    if grid[row][0]==grid[row][1]:      # first and second row same
                        x=(grid[row][1])*2
                        grid[row][0]=0
                        grid[row][1]=0
                        grid[row][0]=x
                        y=grid[row][3]
                        grid[row][3]=0
                        grid[row][1]=y
                                       
                    elif grid[row][1]==grid[row][3]:       # second and fourth row same
                        x=(grid[row][1])*2
                        grid[row][1]=0
                        grid[row][3]=0                                    
                        grid[row][1]=x
                                       
                    else:                               # different
                        z=grid[row][3]
                        rid[row][2]=z
                        grid[row][3]=0  
                        
                if small_list==[1,0,1,1]:              # option 15
                    if grid[row][0]==grid[row][2]:      # first and third row same
                        x=(grid[row][0])*2
                        grid[row][0]=0
                        grid[row][2]=0
                        grid[row][0]=x
                        y=grid[row][3]
                        grid[row][3]=0
                        grid[row][1]=y
                        
                    elif grid[row][2]==grid[row][3]:       # third and fourth row same
                        x=(grid[row][2])*2
                        grid[row][2]=0
                        grid[row][3]=0                   
                        grid[row][1]=x
                                       
                    else:                               # different
                        y=grid[row][2]
                        z=grid[row][3]
                        grid[row][1]=y
                        grid[row][2]=z
                        grid[row][3]=0 
                        
                if small_list==[1,1,1,1]:                          #option 16
                    if grid[row][0]==grid[row][1]:              # first and second row same and possibly of third and fourth same
                        x=(grid[row][0])*2
                        grid[row][0]=x
                        y=grid[row][2]
                        z=grid[row][3]
                        grid[row][1]=y
                        grid[row][2]=z
                        if grid[row][2]==grid[row][1]:
                            x_2=(grid[row][2])*2
                            grid[row][2]=x_2
                            grid[row][3]=0                       
                            
                    elif grid[row][1]==grid[row][2]:            # second and third row same
                        x=(grid[row][1])*2
                        grid[row][1]=x
                        z=grid[row][3]
                        grid[row][2]=z 
                        grid[row][3]=0
                        
                    elif grid[row][2]==grid[row][3]:           #third and fourth row same
                        x=(grid[row][2])*2
                        grid[row][2]=x
                        grid[row][3]=0    
    





    
def push_right (grid):
    """merge grid values right"""
    for row in range(4):
            small_list=[] 
            
            for col in range(4):
                if grid[row][col]==0:                    
                    small_list.append(grid[row][col])
                else:
                    small_list.append(1)
                
                if small_list==[1,0,0,0]:             #option 9       
                    x=grid[row][0]
                    grid[row][0]=0
                    grid[row][3]=x
                    
                if small_list==[0,0,1,0]:         #option 3
                    x=grid[row][2]
                    grid[row][2]=0
                    grid[row][3]=x
                    
                if small_list==[0,0,1,1]:                #option 4
                    if grid[row][2]==grid[row][3]:       #same number
                        x=(grid[row][2])*2
                        grid[row][2]=0
                        grid[row][3]=x
                        
                    
                        
                if small_list==[0,1,0,0]:              #option 5
                    x=grid[row][1]
                    grid[row][1]=0
                    grid[row][3]=x                
                    
                    
                if small_list==[0,1,1,0]:               #option 6
                    if grid[row][1]==grid[row][2]:       #same
                        x=(grid[row][1])*2
                        grid[row][1]=0
                        grid[row][2]=0
                        grid[row][3]=x
                        
                    else:                              #different
                        first=grid[row][1]
                        second=grid[row][2]
                        grid[row][1]=0
                        grid[row][2]=0
                        grid[row][2]=first
                        grid[row][3]=second
                        
                if small_list==[0,1,0,1]:                #option 7
                    if grid[row][1]==grid[row][3]:       #same
                        x=(grid[row][1])*2
                        grid[row][1]=0
                        grid[row][3]=0
                        grid[row][3]=x
                                        
                    else:                              #different
                        first=grid[row][1]
                        grid[row][1]=0
                        grid[row][2]=first
                                        
                
                if small_list==[0,1,1,1]:               #option 8
                    if grid[row][1]==grid[row][2]:      # second and third row same
                        x=(grid[row][1])*2
                        grid[row][1]=0
                        grid[row][2]=x
                    
                        
                    elif grid[row][2]==grid[row][3]:       # third and fourth row same
                        x=(grid[row][2])*2
                        y=grid[row][1]
                        grid[row][2]=y                    
                        grid[row][3]=x
                        
                        
                if small_list==[1,1,0,0]:                  # option 10
                    if grid[row][0]==grid[row][1]:       #same
                        x=(grid[row][1])*2
                        grid[row][0]=0
                        grid[row][1]=0
                        grid[row][3]=x
                        
                    else: 
                        x=grid[row][0]
                        y=grid[row][1]
                        grid[row][0]=0
                        grid[row][1]=0
                        grid[row][2]=x
                        grid[row][3]=y
                                                        
                if small_list==[1,0,1,0]:               # option 11
                    if grid[row][0]==grid[row][2]:       #same
                        x=(grid[row][0])*2
                        grid[row][2]=0
                        grid[row][0]=0
                        grid[row][3]=x
                                                       
                    else:                              #different
                        first=grid[row][0]
                        second=grid[row][2]
                        grid[row][0]=0
                        grid[row][2]=first
                        grid[row][3]=second 
                        
                if small_list==[1,0,0,1]:              #option 12
                    if grid[row][0]==grid[row][3]:       #same
                        x=(grid[row][0])*2
                        grid[row][3]=x
                        grid[row][0]=0
                                                       
                    else:                              #different
                        first=grid[row][0]
                        grid[row][0]=0
                        grid[row][2]=first 
                        
                if small_list==[1,1,1,0]:            #option 13
                    if grid[row][0]==grid[row][1]:      # second and first row same
                        x=(grid[row][1])*2
                        grid[row][0]=0
                        grid[row][1]=0
                        y=grid[row][2]
                        grid[row][2]=x
                        grid[row][3]=y
                                        
                    elif grid[row][1]==grid[row][2]:       # third and second row same
                        x=(grid[row][2])*2
                        y=grid[row][0]
                        grid[row][1]=0
                        grid[row][0]=0
                        grid[row][2]=y                                        
                        grid[row][3]=x 
                        
                    else:                              #different
                        x=grid[row][0]
                        y=grid[row][1]
                        z=grid[row][2]
                        grid[row][0]=0
                        grid[row][1]=x
                        grid[row][2]=y
                        grid[row][3]=z
                        
                if small_list==[1,1,0,1]:                 #option 14
                    if grid[row][0]==grid[row][1]:      # first and second row same
                        x=(grid[row][1])*2
                        grid[row][0]=0
                        grid[row][1]=0
                        grid[row][2]=x
                        
                                                             
                    elif grid[row][1]==grid[row][3]:       # second and fourth row same
                        x=(grid[row][1])*2
                        grid[row][0]=y
                        grid[row][1]=0
                        grid[row][3]=x
                        grid[row][0]=0
                        grid[row][2]=y
                                       
                    else:                               # different
                        
                        z=grid[row][1]
                        grid[row][2]=z
                        x=grid[row][0]
                        grid[row][1]=x
                        grid[row][0]=0
                        
                if small_list==[1,0,1,1]:              # option 15
                    if grid[row][0]==grid[row][2]:      # first and third row same
                        x=(grid[row][0])*2
                        grid[row][0]=0
                        grid[row][2]=x
                        
                        
                    elif grid[row][2]==grid[row][3]:       # third and fourth row same
                        x=(grid[row][2])*2
                        y=grid[row][0]
                        grid[row][0]=0
                        grid[row][2]=y
                        grid[row][3]=x
                                       
                    else:                               # different
                        x=grid[row][0]
                        grid[row][1]=x
                        grid[row][0]=0 
                        
                if small_list==[1,1,1,1]:                          #option 16
                    if grid[row][2]==grid[row][3]:              # third and second row same and possibly of third and fourth same
                        x=(grid[row][2])*2
                        grid[row][3]=x
                        y=grid[row][0]
                        z=grid[row][1]
                        grid[row][1]=y
                        grid[row][2]=z
                        if grid[row][2]==grid[row][1]:
                            x_2=(grid[row][2])*2
                            grid[row][2]=x_2
                            grid[row][1]=0                       
                            
                    elif grid[row][1]==grid[row][2]:            # second and third row same
                        x=(grid[row][1])*2
                        grid[row][2]=x
                        y=grid[row][0]
                        grid[row][3]=y
                        grid[row][0]=0 
                        
                    elif grid[row][2]==grid[row][3]:           #third and fourth row same
                        x=(grid[row][2])*2
                        y=grid[row][1]
                        z=grid[row][0]
                        grid[row][3]=x
                        grid[row][2]=y
                        grid[row][1]=z