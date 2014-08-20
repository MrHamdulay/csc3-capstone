"""Assignment 7 Push
Yaseen Sulliman
29 April 2014"""

def push_up (grid):
    """merge grid values upwards"""
    for column in range(4):                                     
        for row in range(3):                                    
            counter=1                                           
            while counter<(4-row) and grid[row][column]==0:     
                grid[row][column]=grid[row+counter][column]    
                grid[row+counter][column]=0                     
                counter+=1                                      
    
    for column in range(4):                                     
        for row in range(3):                                   
            if grid[row][column]==grid[row+1][column]:           
                grid[row][column]=2*grid[row][column]           
                grid[row+1][column]=0                          

    for column in range(4):                                     
        for row in range(3):                                    
            counter=1                                           
            while counter<(4-row) and grid[row][column]==0:     
                grid[row][column]=grid[row+counter][column]     
                grid[row+counter][column]=0                     
                counter+=1                                      

def push_down (grid):
    """merge grid values downwards"""
    for column in range(4):                                     
        for row in range(3,0,-1):                               
            counter=1                                           
            while counter<(row+1) and grid[row][column]==0:     
                grid[row][column]=grid[row-counter][column]     
                grid[row-counter][column]=0                     
                counter+=1                                      
    
    for column in range(4):                                     
        for row in range(3,0,-1):                               
            if grid[row][column]==grid[row-1][column]:           
                grid[row][column]=2*grid[row][column]           
                grid[row-1][column]=0                           

    for column in range(4):                                     
        for row in range(3,0,-1):                               
            counter=1                                           
            while counter<(row+1) and grid[row][column]==0:     
                grid[row][column]=grid[row-counter][column]     
                grid[row-counter][column]=0                     
                counter+=1                                      
def push_left (grid):
    """merge grid values left"""
    for row in range(4):                                        
        for column in range(3):                                 
            counter=1                                           
            while counter<(4-column) and grid[row][column]==0:  
                grid[row][column]=grid[row][column+counter]     
                grid[row][column+counter]=0                     
                counter+=1                                      
    
    for row in range(4):                                        
        for column in range(3):                                 
            if grid[row][column]==grid[row][column+1]:           
                grid[row][column]=2*grid[row][column]           
                grid[row][column+1]=0                           

    for row in range(4):                                        
        for column in range(3):                                 
            counter=1                                           
            while counter<(4-column) and grid[row][column]==0:  
                grid[row][column]=grid[row][column+counter]     
                grid[row][column+counter]=0                     
                counter+=1                                      

def push_right (grid):
    """merge grid values right"""    
    for row in range(4):                                        
        for column in range(3,0,-1):                            
            counter=1                                           
            while counter<(column+1) and grid[row][column]==0: 
                grid[row][column]=grid[row][column-counter]    
                grid[row][column-counter]=0                     
                counter+=1                                      
    
    for row in range(4):                                        
        for column in range(3,0,-1):                            
            if grid[row][column]==grid[row][column-1]:           
                grid[row][column]=2*grid[row][column]           
                grid[row][column-1]=0                           

    for row in range(4):                                        
        for column in range(3,0,-1):                            
            counter=1                                           
            while counter<(column+1) and grid[row][column]==0:  
                grid[row][column]=grid[row][column-counter]     
                grid[row][column-counter]=0                     
                counter+=1                                      
