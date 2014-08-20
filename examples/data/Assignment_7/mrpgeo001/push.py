"""Push functions for 2048
Geoff Murphy
MRPGEO001
01 May 2014"""


def push_up(grid):
    
    for i in range(3):
        if grid[0][0] == 0:             #Checks if a value is equal to 0
            grid[0][0] = grid[1][0]     #If it is, it moves the value below it up (makes itself equal to the lower value)
            grid[1][0] = 0              #Then makes the lower value equal to 0
        
        if grid[0][1] == 0:
            grid[0][1] = grid[1][1]
            grid[1][1] = 0
        
        if grid[0][2] == 0:
            grid[0][2] = grid[1][2]
            grid[1][2] = 0
        
        if grid[0][3] == 0:
            grid[0][3] = grid[1][3]
            grid[1][3] = 0    
        
        if grid[1][0] == 0:
            grid[1][0] = grid[2][0]
            grid[2][0] = 0
        
        if grid[1][1] == 0:
            grid[1][1] = grid[2][1]
            grid[2][1] = 0
        
        if grid[1][2] == 0:
            grid[1][2] = grid[2][2]
            grid[2][2] = 0
        
        if grid[1][3] == 0:
            grid[1][3] = grid[2][3]
            grid[2][3] = 0
        
        if grid[2][0] == 0:
            grid[2][0] = grid[3][0]
            grid[3][0] = 0    
        
        if grid[2][1] == 0:
            grid[2][1] = grid[3][1]
            grid[3][1] = 0 
        
        if grid[2][2] == 0:
            grid[2][2] = grid[3][2]
            grid[3][2] = 0 
    
        if grid[2][3] == 0:
            grid[2][3] = grid[3][3]
            grid[3][3] = 0 
        
    if grid[1][0] == grid[0][0]:        #Checks if the lower value is equal to the upper value
        grid[1][0] = 0                  #And makes the lower value equal to 0
        grid[0][0] = grid[0][0]*2       #If it is, it makes the upper value equal to the twice itself
            
    if grid[1][1] == grid[0][1]:
        grid[1][1] = 0
        grid[0][1] = grid[0][1]*2
        
    if grid[1][2] == grid[0][2]:
        grid[1][2] = 0
        grid[0][2] = grid[0][2]*2 
    
        
    if grid[1][3] == grid[0][3]:
        grid[1][3] = 0
        grid[0][3] = grid[0][3]*2   
        
        
    if grid[2][0] == grid[1][0]:
        grid[2][0] = 0
        grid[1][0] = grid[1][0]*2
        
    if grid[2][1] == grid[1][1]:
        grid[2][1] = 0
        grid[1][1] = grid[1][1]*2
        
    if grid[2][2] == grid[1][2]:
        grid[2][2] = 0
        grid[1][2] = grid[1][2]*2 
        
    if grid[2][3] == grid[1][3]:
        grid[2][3] = 0
        grid[1][3] = grid[1][3]*2    
    
    
    if grid[3][0] == grid[2][0]:
        grid[3][0] = 0
        grid[2][0] = grid[2][0]*2
        
    if grid[3][1] == grid[2][1]:
        grid[3][1] = 0
        grid[2][1] = grid[2][1]*2
        
    if grid[3][2] == grid[2][2]:
        grid[3][2] = 0
        grid[2][2] = grid[2][2]*2 
        
    if grid[3][3] == grid[2][3]:
        grid[3][3] = 0
        grid[2][3] = grid[2][3]*2  
        
    for i in range(3):
        if grid[0][0] == 0:             #Does the same as the original for loop for zero values
            grid[0][0] = grid[1][0]     #To take account of changes after the values have moved/doubled
            grid[1][0] = 0            
        
        if grid[0][1] == 0:
            grid[0][1] = grid[1][1]
            grid[1][1] = 0
        
        if grid[0][2] == 0:
            grid[0][2] = grid[1][2]
            grid[1][2] = 0
        
        if grid[0][3] == 0:
            grid[0][3] = grid[1][3]
            grid[1][3] = 0    
        
        if grid[1][0] == 0:
            grid[1][0] = grid[2][0]
            grid[2][0] = 0
        
        if grid[1][1] == 0:
            grid[1][1] = grid[2][1]
            grid[2][1] = 0
        
        if grid[1][2] == 0:
            grid[1][2] = grid[2][2]
            grid[2][2] = 0
        
        if grid[1][3] == 0:
            grid[1][3] = grid[2][3]
            grid[2][3] = 0
        
        if grid[2][0] == 0:
            grid[2][0] = grid[3][0]
            grid[3][0] = 0    
        
        if grid[2][1] == 0:
            grid[2][1] = grid[3][1]
            grid[3][1] = 0 
        
        if grid[2][2] == 0:
            grid[2][2] = grid[3][2]
            grid[3][2] = 0 
    
        if grid[2][3] == 0:
            grid[2][3] = grid[3][3]
            grid[3][3] = 0 
    
        
def push_down(grid):

    for i in range(3):
        if grid[3][0] == 0:             #Checks if a value is equal to 0
            grid[3][0] = grid[2][0]     #If it is, it moves the value above it down (makes itself equal to the upper value)
            grid[2][0] = 0              #Then makes the upper value equal to 0
        
        if grid[3][1] == 0:
            grid[3][1] = grid[2][1]
            grid[2][1] = 0
        
        if grid[3][2] == 0:
            grid[3][2] = grid[2][2]
            grid[2][2] = 0
        
        if grid[3][3] == 0:
            grid[3][3] = grid[2][3]
            grid[2][3] = 0    
        
        if grid[2][0] == 0:
            grid[2][0] = grid[1][0]
            grid[1][0] = 0
        
        if grid[2][1] == 0:
            grid[2][1] = grid[1][1]
            grid[1][1] = 0
        
        if grid[2][2] == 0:
            grid[2][2] = grid[1][2]
            grid[1][2] = 0
        
        if grid[2][3] == 0:
            grid[2][3] = grid[1][3]
            grid[1][3] = 0
        
        if grid[1][0] == 0:
            grid[1][0] = grid[0][0]
            grid[0][0] = 0    
        
        if grid[1][1] == 0:
            grid[1][1] = grid[0][1]
            grid[0][1] = 0 
        
        if grid[1][2] == 0:
            grid[1][2] = grid[0][2]
            grid[0][2] = 0 
    
        if grid[1][3] == 0:
            grid[1][3] = grid[0][3]
            grid[0][3] = 0 

    if grid[1][0] == grid[0][0]:        #Checks if the lower value is equal to the upper value
        grid[0][0] = 0                  #And makes the upper value equal to 0
        grid[1][0] = grid[1][0]*2       #If it is, it makes the lower value equal to twice itself
            
    if grid[1][1] == grid[0][1]:
        grid[0][1] = 0
        grid[1][1] = grid[1][1]*2
        
    if grid[1][2] == grid[0][2]:
        grid[0][2] = 0
        grid[1][2] = grid[1][2]*2 
    
        
    if grid[1][3] == grid[0][3]:
        grid[0][3] = 0
        grid[1][3] = grid[1][3]*2   
        
        
    if grid[2][0] == grid[1][0]:
        grid[1][0] = 0
        grid[2][0] = grid[2][0]*2
        
    if grid[2][1] == grid[1][1]:
        grid[1][1] = 0
        grid[2][1] = grid[2][1]*2
        
    if grid[2][2] == grid[1][2]:
        grid[1][2] = 0
        grid[2][2] = grid[2][2]*2 
        
    if grid[2][3] == grid[1][3]:
        grid[1][3] = 0
        grid[2][3] = grid[2][3]*2    
    
    
    if grid[3][0] == grid[2][0]:
        grid[2][0] = 0
        grid[3][0] = grid[3][0]*2
        
    if grid[3][1] == grid[2][1]:
        grid[3][1] = 0
        grid[3][1] = grid[3][1]*2
        
    if grid[3][2] == grid[2][2]:
        grid[2][2] = 0
        grid[3][2] = grid[3][2]*2 
        
    if grid[3][3] == grid[2][3]:
        grid[2][3] = 0
        grid[3][3] = grid[3][3]*2  
        
        
    for i in range(3):
        if grid[3][0] == 0:             #Does the same as the original for loop for zero values
            grid[3][0] = grid[2][0]     #To take account of the values that moved/doubled
            grid[2][0] = 0              
        
        if grid[3][1] == 0:
            grid[3][1] = grid[2][1]
            grid[2][1] = 0
        
        if grid[3][2] == 0:
            grid[3][2] = grid[2][2]
            grid[2][2] = 0
        
        if grid[3][3] == 0:
            grid[3][3] = grid[2][3]
            grid[2][3] = 0    
        
        if grid[2][0] == 0:
            grid[2][0] = grid[1][0]
            grid[1][0] = 0
        
        if grid[2][1] == 0:
            grid[2][1] = grid[1][1]
            grid[1][1] = 0
        
        if grid[2][2] == 0:
            grid[2][2] = grid[1][2]
            grid[1][2] = 0
        
        if grid[2][3] == 0:
            grid[2][3] = grid[1][3]
            grid[1][3] = 0
        
        if grid[1][0] == 0:
            grid[1][0] = grid[0][0]
            grid[0][0] = 0    
        
        if grid[1][1] == 0:
            grid[1][1] = grid[0][1]
            grid[0][1] = 0 
        
        if grid[1][2] == 0:
            grid[1][2] = grid[0][2]
            grid[0][2] = 0 
    
        if grid[1][3] == 0:
            grid[1][3] = grid[0][3]
            grid[0][3] = 0 
        
def push_right(grid):
    
    for i in range(3):                      
        if grid[0][3] == 0:                 #Checks if a value to its right is equal to 0
            grid[0][3] = grid[0][2]         #If it is, it makes the right value equal to the left
            grid[0][2] = 0                  # and makes itself equal to 0
            
        if grid[0][2] == 0:
            grid[0][2] = grid[0][1]
            grid[0][1] = 0  
            
        if grid[0][1] == 0:
            grid[0][1] = grid[0][0]
            grid[0][0] = 0   
            
        if grid[1][3] == 0:
            grid[1][3] = grid[1][2]
            grid[1][2] = 0
            
        if grid[1][2] == 0:
            grid[1][2] = grid[1][1]
            grid[1][1] = 0  
            
        if grid[1][1] == 0:
            grid[1][1] = grid[1][0]
            grid[1][0] = 0  
            
            
        if grid[2][3] == 0:
            grid[2][3] = grid[2][2]
            grid[2][2] = 0
            
        if grid[2][2] == 0:
            grid[2][2] = grid[2][1]
            grid[2][1] = 0  
            
        if grid[2][1] == 0:
            grid[2][1] = grid[2][0]
            grid[2][0] = 0     
            
        
        if grid[3][3] == 0:
            grid[3][3] = grid[3][2]
            grid[3][2] = 0
            
        if grid[3][2] == 0:
            grid[3][2] = grid[3][1]
            grid[3][1] = 0  
            
        if grid[3][1] == 0:
            grid[3][1] = grid[3][0]
            grid[3][0] = 0         
        
    if grid[0][3] == grid[0][2]:        #Checks if the right value is equal to the left
        grid[0][3] = grid[0][3]*2       #If so, makes the right equal to the left 
        grid[0][2] = 0                  #And the left equal to 0
        
    if grid[0][2] == grid[0][1]:
        grid[0][2] = grid[0][2]*2
        grid[0][1] = 0
        
    if grid[0][1] == grid[0][0]:
        grid[0][1] = grid[0][1]*2
        grid[0][0] = 0
    
    if grid[1][3] == grid[1][2]:
        grid[1][3] = grid[1][3]*2
        grid[1][2] = 0
        
    if grid[1][2] == grid[1][1]:
        grid[1][2] = grid[1][2]*2
        grid[1][1] = 0
        
    if grid[1][1] == grid[1][0]:
        grid[1][1] = grid[1][1]*2
        grid[1][0] = 0
        
    
    if grid[2][3] == grid[2][2]:
        grid[2][3] = grid[2][3]*2
        grid[2][2] = 0
        
    if grid[2][2] == grid[2][1]:
        grid[2][2] = grid[2][2]*2
        grid[2][1] = 0
        
    if grid[2][1] == grid[2][0]:
        grid[2][1] = grid[2][1]*2
        grid[2][0] = 0 
        
        
    if grid[3][3] == grid[3][2]:
        grid[3][3] = grid[3][3]*2
        grid[3][2] = 0
        
    if grid[3][2] == grid[3][1]:
        grid[3][2] = grid[3][2]*2
        grid[3][1] = 0
        
    if grid[3][1] == grid[3][0]:
        grid[3][1] = grid[3][1]*2
        grid[3][0] = 0    
    
    
    for i in range(3):
        if grid[0][3] == 0:             #Does the same as the original for loop to account of changes in the grid
            grid[0][3] = grid[0][2]
            grid[0][2] = 0
            
        if grid[0][2] == 0:
            grid[0][2] = grid[0][1]
            grid[0][1] = 0  
            
        if grid[0][1] == 0:
            grid[0][1] = grid[0][0]
            grid[0][0] = 0   
            
        if grid[1][3] == 0:
            grid[1][3] = grid[1][2]
            grid[1][2] = 0
            
        if grid[1][2] == 0:
            grid[1][2] = grid[1][1]
            grid[1][1] = 0  
            
        if grid[1][1] == 0:
            grid[1][1] = grid[1][0]
            grid[1][0] = 0  
            
            
        if grid[2][3] == 0:
            grid[2][3] = grid[2][2]
            grid[2][2] = 0
            
        if grid[2][2] == 0:
            grid[2][2] = grid[2][1]
            grid[2][1] = 0  
            
        if grid[2][1] == 0:
            grid[2][1] = grid[2][0]
            grid[2][0] = 0     
            
        
        if grid[3][3] == 0:
            grid[3][3] = grid[3][2]
            grid[3][2] = 0
            
        if grid[3][2] == 0:
            grid[3][2] = grid[3][1]
            grid[3][1] = 0  
            
        if grid[3][1] == 0:
            grid[3][1] = grid[3][0]
            grid[3][0] = 0         
    
        
def push_left(grid):
    for i in range(3):
        if grid[0][2] == 0:          #Checks if the left value is equal to 0  
            grid[0][2] = grid[0][3]  #If so, makes the left value equal to the right    
            grid[0][3] = 0           #And the right equal to 0
            
        if grid[0][1] == 0:            
            grid[0][1] = grid[0][2]     
            grid[0][2] = 0           
        
        if grid[0][0] == 0:            
            grid[0][0] = grid[0][1]     
            grid[0][1] = 0
        
         
        if grid[1][2] == 0:            
            grid[1][2] = grid[1][3]     
            grid[1][3] = 0              
              
        if grid[1][1] == 0:            
            grid[1][1] = grid[1][2]     
            grid[1][2] = 0            
        
        if grid[1][0] == 0:            
            grid[1][0] = grid[1][1]     
            grid[1][1] = 0
        
        if grid[2][2] == 0:            
            grid[2][2] = grid[2][3]     
            grid[2][3] = 0          
            
        
        if grid[2][1] == 0:            
            grid[2][1] = grid[2][2]     
            grid[2][2] = 0            
        
        if grid[2][0] == 0:            
            grid[2][0] = grid[2][1]     
            grid[2][1] = 0
        
        if grid[3][2] == 0:            
            grid[3][2] = grid[3][3]     
            grid[3][3] = 0              
            
        if grid[3][1] == 0:            
            grid[3][1] = grid[3][2]     
            grid[3][2] = 0         
            
        
        if grid[3][0] == 0:            
            grid[3][0] = grid[3][1]     
            grid[3][1] = 0
        
           
            
    if grid[0][1] == grid[0][0]:      #Checks if the left value is equal to the right
        grid[0][1] = 0                #And makes the right equal to 0
        grid[0][0] = grid[0][0]*2     #And makes the left twice itself
    
    if grid[0][2] == grid[0][1]:      
        grid[0][2] = 0                  
        grid[0][1] = grid[0][1]*2     
        
        
    if grid[0][3] == grid[0][2]:      
        grid[0][3] = 0                  
        grid[0][2] = grid[0][2]*2  
        
        
    if grid[1][1] == grid[1][0]:      
        grid[1][1] = 0                  
        grid[1][0] = grid[1][0]*2     
            
    if grid[1][2] == grid[1][1]:      
        grid[1][2] = 0                  
        grid[1][1] = grid[1][1]*2     
                
                
    if grid[1][3] == grid[1][2]:      
        grid[1][3] = 0                  
        grid[1][2] = grid[1][2]*2   
            

    if grid[2][1] == grid[2][0]:      
        grid[2][1] = 0                  
        grid[2][0] = grid[2][0]*2     
            
    if grid[2][2] == grid[2][1]:      
        grid[2][2] = 0                  
        grid[2][1] = grid[2][1]*2     
                
                
    if grid[2][3] == grid[2][2]:      
        grid[2][3] = 0                  
        grid[2][2] = grid[2][2]*2 
        

    if grid[3][1] == grid[3][0]:      
        grid[3][1] = 0                  
        grid[3][0] = grid[3][0]*2     
            
    if grid[3][2] == grid[3][1]:      
        grid[3][2] = 0                  
        grid[3][1] = grid[3][1]*2     
                
                
    if grid[3][3] == grid[3][2]:      
        grid[3][3] = 0                  
        grid[3][2] = grid[3][2]*2  
        
        
    for i in range(3):               #Does the same as the original for loop to take into account the changes in the grid
        if grid[0][2] == 0:            
            grid[0][2] = grid[0][3]     
            grid[0][3] = 0   
            
        if grid[0][1] == 0:            
            grid[0][1] = grid[0][2]     
            grid[0][2] = 0           
        
        if grid[0][0] == 0:            
            grid[0][0] = grid[0][1]     
            grid[0][1] = 0
        
         
        if grid[1][2] == 0:            
            grid[1][2] = grid[1][3]     
            grid[1][3] = 0              
              
        if grid[1][1] == 0:            
            grid[1][1] = grid[1][2]     
            grid[1][2] = 0            
        
        if grid[1][0] == 0:            
            grid[1][0] = grid[1][1]     
            grid[1][1] = 0
        
        if grid[2][2] == 0:            
            grid[2][2] = grid[2][3]     
            grid[2][3] = 0          
            
        
        if grid[2][1] == 0:            
            grid[2][1] = grid[2][2]     
            grid[2][2] = 0            
        
        if grid[2][0] == 0:            
            grid[2][0] = grid[2][1]     
            grid[2][1] = 0
        
        if grid[3][2] == 0:            
            grid[3][2] = grid[3][3]     
            grid[3][3] = 0              
            
        if grid[3][1] == 0:            
            grid[3][1] = grid[3][2]     
            grid[3][2] = 0         
            
        
        if grid[3][0] == 0:            
            grid[3][0] = grid[3][1]     
            grid[3][1] = 0
    