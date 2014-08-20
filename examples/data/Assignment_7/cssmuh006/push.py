def shift_up(grid):
    #move number all the way up
    for i in range(4):
        for j in range(4):                
            if(grid[j][i]==0):
                for r in range(3):
                    if((j+r)<=3):
                        if(grid[j+r][i]!=0):                            
                            grid[j][i]=grid[j+r][i]
                            grid[j+r][i]=0
                            break     
    
def shift_down(grid):
    #move number all the way down
    for i in range(4):
        for j in range(3,-1,-1):
            if(grid[j][i]==0):
                for r in range(3):
                    if((j-r)>=0):
                        if(grid[j-r][i]!=0):  
                            grid[j][i]=grid[j-r][i]
                            grid[j-r][i]=0
                            break    
                        
def shift_left(grid):
    #move number all the way left
    for j in range(4):
        for i in range(4):
            if(grid[j][i]==0):
                for r in range(3):
                    if((i+r)<=3):
                        if(grid[j][i+r]!=0):
                            grid[j][i]=grid[j][i+r]
                            grid[j][i+r]=0
                            break
        
def shift_right(grid):
    #move number all the way right
    for j in range(4):
        for i in range(3,-1,-1):
            if(grid[j][i]==0):
                for r in range(3):
                    if((i-r)>=0):
                        if(grid[j][i-r]!=0):
                            grid[j][i]=grid[j][i-r]
                            grid[j][i-r]=0
                            break    
    
def push_up(grid):
#shifts numbers up and simultaneously adds equal number
    shift_up(grid)                  
    for i in range(4):
        for j in range(4):
            if(j!=3):
                if(grid[j][i]==grid[j+1][i]):
                    grid[j][i]+=grid[j+1][i]
                    grid[j+1][i]=0                    
    shift_up(grid)     
                    
def push_down(grid):
#shifts numbers down and simultaneously adds equal number
    shift_down(grid)                       
    for i in range(4):
        for j in range(3,-1,-1):
            if(j!=0):
                if(grid[j][i]==grid[j-1][i]):
                    grid[j][i]+=grid[j-1][i]
                    grid[j-1][i]=0              
    shift_down(grid) 
    
def push_left(grid):
#shifts numbers left and simultaneously adds equal number    
    shift_left(grid)
    for j in range(4):
        for i in range(4):
            if(i!=3):
                if(grid[j][i]==grid[j][i+1]):
                    grid[j][i]+=grid[j][i+1]
                    grid[j][i+1]=0       
    shift_left(grid)
    
def push_right(grid):
#shifts numbers right and simultaneously adds equal number    
    shift_right(grid)
    for j in range(4):
        for i in range(3,-1,-1):
            if(i!=0):
                if(grid[j][i]==grid[j][i-1]):
                    grid[j][i]+=grid[j][i-1]
                    grid[j][i-1]=0
    shift_right(grid)