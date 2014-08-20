#Konrad Hugo
#2014/05/02
#question3 assignment7

def push_up (grid): #Merges values upwards in grid
   
    for col in range(4):                                     
        for row in range(3):                                    
            summer=1                                           
            while summer<(4-row) and grid[row][col]==0:     
                grid[row][col]=grid[row+summer][col]    
                grid[row+summer][col]=0                     
                summer+=1                                      
    
    for col in range(4):                                     
        for row in range(3):                                   
            if grid[row][col]==grid[row+1][col]:           
                grid[row][col]=2*grid[row][col]           
                grid[row+1][col]=0                          

    for col in range(4):                                     
        for row in range(3):                                    
            summer=1                                           
            while summer<(4-row) and grid[row][col]==0:     
                grid[row][col]=grid[row+summer][col]     
                grid[row+summer][col]=0                     
                summer+=1                                      

def push_down (grid): #Merges values downwards within grid
    
    for col in range(4):                                     
        for row in range(3,0,-1):                               
            summer=1                                           
            while summer<(row+1) and grid[row][col]==0:     
                grid[row][col]=grid[row-summer][col]     
                grid[row-summer][col]=0                     
                summer+=1                                      
    
    for col in range(4):                                     
        for row in range(3,0,-1):                               
            if grid[row][col]==grid[row-1][col]:           
                grid[row][col]=2*grid[row][col]           
                grid[row-1][col]=0                           

    for col in range(4):                                     
        for row in range(3,0,-1):                               
            summer=1                                           
            while summer<(row+1) and grid[row][col]==0:     
                grid[row][col]=grid[row-summer][col]     
                grid[row-summer][col]=0                     
                summer+=1                                      

def push_left (grid): #Merges values leftwards
    
    for row in range(4):                                        
        for col in range(3):                                 
            summer=1                                           
            while summer<(4-col) and grid[row][col]==0:  
                grid[row][col]=grid[row][col+summer]     
                grid[row][col+summer]=0                     
                summer+=1                                      
    
    for row in range(4):                                        
        for col in range(3):                                 
            if grid[row][col]==grid[row][col+1]:           
                grid[row][col]=2*grid[row][col]           
                grid[row][col+1]=0                           

    for row in range(4):                                        
        for col in range(3):                                 
            summer=1                                           
            while summer<(4-col) and grid[row][col]==0:  
                grid[row][col]=grid[row][col+summer]     
                grid[row][col+summer]=0                     
                summer+=1                                      

def push_right (grid): #merge values to the right
        
    for row in range(4):                                        
        for col in range(3,0,-1):                            
            summer=1                                           
            while summer<(col+1) and grid[row][col]==0: 
                grid[row][col]=grid[row][col-summer]    
                grid[row][col-summer]=0                     
                summer+=1                                      
    
    for row in range(4):                                        
        for col in range(3,0,-1):                            
            if grid[row][col]==grid[row][col-1]:           
                grid[row][col]=2*grid[row][col]           
                grid[row][col-1]=0                           

    for row in range(4):                                        
        for col in range(3,0,-1):                            
            summer=1                                           
            while summer<(col+1) and grid[row][col]==0:  
                grid[row][col]=grid[row][col-summer]     
                grid[row][col-summer]=0                     
                summer+=1                                      
