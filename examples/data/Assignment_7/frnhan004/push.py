"""Push-assignment 7
FRNHAN004
2 May 2014"""

def push_up(grid): 
    """check if 2 vertically adjacent numbers are equal starting from from row 1-row 3, if equal merge and push down if theres a 0, merge over the zero""" 
    for i in range (0,3): #checking spaces moving if spaces
        for row in range (1,4): #move up        
            for col in range (0,4):      
                if grid[row-1][col] == " " or grid[row-1][col] == 0:
                    grid[row-1][col] = grid[row][col]
                    grid[row][col] = 0    
    for row in range(1,4): #if same multiply by 2 and replace by 0
        for col in range (0,4):
            if grid[row-1][col] == grid[row][col]:
                grid[row-1][col] = (grid[row-1][col] * 2)   
                grid[row][col] = 0
    
    for row in range (1,4): #if repeat replaced by 0, move again so that no spaces     
        for col in range (0,4):                 
            if grid[row-1][col] == " " or grid[row-1][col] == 0:
                grid[row-1][col] = grid[row][col]
                grid[row][col] = 0    
    return grid     
    
    
def push_down(grid): 
    """check if 2 vertically adjacent numbers are equal starting from from row 2-row 0, if equal merge and push down if theres a 0, merge over the zero"""  
    for i in range (0,3): #move down
        for row in range (2,-1,-1): 
            for col in range (3,-1,-1): 
                if grid[row+1][col] == " " or grid[row+1][col] == 0:
                    grid[row+1][col] = grid[row][col]
                    grid[row][col] = 0  
    
    for row in range(2,-1,-1): #if same multiply by 2 and replace by 0
        for col in range (3,-1,-1):
            if grid[row+1][col] == grid[row][col]:  
                grid[row+1][col] = (grid[row+1][col] * 2)   
                grid[row][col] = 0        
  
                
    for row in range (2,-1,-1): #if repeat replaced by 0, move again so that no spaces    
        for col in range (3,-1,-1):                 
            if grid[row+1][col] == " " or grid[row+1][col] == 0:
                grid[row+1][col] = grid[row][col]
                grid[row][col] = 0    
    return grid 
            
def push_left(grid): 
    """check if 2 horizontally adjacent numbers are equal starting from from col 3 - col 1, if equal merge and push down if theres a 0, merge over the zero""" 
    for i in range (0,3): #move left
        for row in range (0,4):        
            for col in range (1,4):       
                if grid[row][col-1] == " " or grid[row][col-1] == 0:
                    grid[row][col-1] = grid[row][col]
                    grid[row][col] = 0    
        
       
    for row in range(0,4): #if same multiply by 2 and replace by 0
        for col in range (1,4):
            if grid[row][col-1] == grid[row][col]:
                grid[row][col-1] = (grid[row][col-1] * 2)   
                grid[row][col] = 0
        
       
    for row in range (0,4): #if repeat replaced by 0, move again so that no spaces          
        for col in range (1,4):                 
            if grid[row][col-1] == " " or grid[row][col-1] == 0:
                grid[row][col-1] = grid[row][col]
                grid[row][col] = 0     
    return grid

def push_right(grid):    
    """check if 2 horizontally adjacent numbers are equal starting from from row 0-row 2, if equal merge and push down if theres a 0, merge over the zero""" 
    for i in range (0,3): #move right
        for row in range (3,-1,-1):         
            for col in range (2,-1,-1):       
                if grid[row][col+1] == " " or grid[row][col+1] == 0:
                    grid[row][col+1] = grid[row][col]
                    grid[row][col] = 0    
       
    for row in range(3,-1,-1): #if same multiply by 2 and replace by 0
        for col in range (2,-1,-1):
            if grid[row][col+1] == grid[row][col]:
                grid[row][col+1] = (grid[row][col+1] * 2)   
                grid[row][col] = 0
        
        
    for row in range (3,-1,-1): #if repeat replaced by 0, move again so that no spaces          
        for col in range (2,-1,-1):                 
            if grid[row][col+1] == ' ' or grid[row][col+1] == 0:
                grid[row][col+1] = grid[row][col]
                grid[row][col] = 0      
    return grid