def push_up(grid):
    for col in range(4):
        for row in range(3):
            count=1
            while (count< 4-row and grid[row][col]==0):
                grid[row][col] = (grid[row+count][col])*2
                grid[row+count][col] = 0  
                count+=1
    for col in range(4):
        for row in range(3):
            if grid[row][col]==grid[row+1][col]:          
                grid[row][col]=2*grid[row][col]           
                grid[row+1][col]=0 
    for col in range(4):
        for row in range(3):
            counter=1
            while (counter<(4-row) and grid[row][col]==0):     
                grid[row][col]=grid[row+counter][col]     
                grid[row+counter][col]=0                     
                counter+=1            
                
def push_down(grid):
    for col in range(4):                                     
        for row in range(3,0,-1):                               
            count=1                                           
            while (count<(row+1) and grid[row][col]==0):     
                grid[row][col]=grid[row-count][col]    
                grid[row-count][col]=0 
    for col in range(4):
        for row in range(3, 0, -1):
            count+=1                                               
            if grid[row][col]==grid[row-1][col]:          
                grid[row][col]=2*grid[row][col]           
                grid[row-1][col]=0                                        
    for col in range(4):
        for row in range(3,0,-1):
            counter=1
            while (counter<(row+1) and grid[row][col]==0):     
                grid[row][col]=grid[row-counter][col]    
                grid[row-counter][col]=0                    
                counter+=1  
                
def push_left(grid):
    for row in range(4):                                        
        for col in range(3):                                 
            count=1                                           
            while (count<(4-col) and grid[row][col]==0):  
                grid[row][col]=grid[row][col+count]     
                grid[row][col+count]=0                     
                count+=1          
    for row in range(4):
        for col in range(3):
            if grid[row][col]==grid[row][col+1]:          
                grid[row][col]=2*grid[row][col]           
                grid[row][col+1]=0
    for row in range(4):                                        
        for col in range(3):                                                 
            counter=1                                           
            while (counter<(4-col) and grid[row][col]==0):  
                grid[row][col]=grid[row][col+counter]    
                grid[row][col+counter]=0                     
                counter+=1
            
def push_right(grid):
    for row in range(4):                                        
        for col in range(3,0,-1):                                 
            count=1                                           
            while count<(col+1) and grid[row][col]==0:  
                grid[row][col]=grid[row][col-count]     
                grid[row][col-count]=0                     
                count+=1           
    for row in range(4):
        for col in range(3,0,-1):
            if grid[row][col]==grid[row][col-1]:          
                grid[row][col]=2*grid[row][col]           
                grid[row][col-1]=0   
    for row in range(4):                                        
        for col in range(3):                                     
            counter=1                                           
            while (counter<(col+1) and grid[row][col]==0):  
                grid[row][col]=grid[row][col-counter]     
                grid[row][col-counter]=0                     
                counter+=1
                
