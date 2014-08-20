def push_up (grid):
    """merge grid values upwards""" 
    for row in range (4): 
        if row == 0: continue #cannot go up if it's at the top already
        for col in range(4):
            top = row-1
            
            
                
            tally = 0
            for i in range(row,0,-1): # counting upwards spaces                
                top1 = i-1 
                if grid[top1][col] == 0:
                    tally += 1  #counting no. of spaces          
            
            if tally > 0:
                grid[row-tally][col] = grid[row][col] #the current row goes up "tally" spaces
                grid[row][col] = 0 
            
                       
            if grid[row-tally][col] == grid[top-tally][col]: # now if the top row is the same as the current, they'll merge
                grid[top-tally][col] = grid[row-tally][col] + grid[top-tally][col]
                grid[row-tally][col] = 0
                    
          
                
                    
                
                
                 
            
            
def push_down (grid):
    """merge grid values downwards"""
    for row in range (3,-1,-1): 
        if row == 3: continue #cannot go down if it's at the bottom already.
        for col in range(4):
                down = row + 1
                # line 0 # 0 0 2 0  -  0 0 0 0
                # line 1 # 0 0 0 0  -  0 0 0 0     
                # line 2 # 2 0 0 0  -  0 0 0 0
                # line 3 # 0 0 0 0  -  2 0 2 0
                
                    
                tally = 0
                for i in range(row,3): # counting the spaces downwards
                    
                    down1 = i + 1 
                    
                    if grid[down1][col] == 0:
                        tally += 1  #counting number of spaces          
                
                if tally > 0:
                    grid[row+tally][col] = grid[row][col] #the current row goes down "tally" spaces
                    grid[row][col] = 0 
                
                           
                if row+tally < 3:
                    if grid[row+tally][col] == grid[down+tally][col]: # now if the bottom row is the same as the current, they'll merge
                        grid[down+tally][col] = grid[row+tally][col] + grid[down+tally][col]
                        grid[row+tally][col] = 0    
def push_left (grid):
    """merge grid values left"""  
    for row in range (4):
        for col in range (4):
                   
            if col == 0: continue #nothing to push if it's at the left end
            
            left = col - 1            
            tally = 0
            
            for i in range(col,0,-1):
                
                left1 = i - 1

                if grid[row][left1] == 0: #counting how many spaces there are to the left of the current object
                    tally += 1
                    
            if tally > 0:
                grid[row][col-tally] = grid[row][col]
                grid[row][col] = 0
            
            if col-tally > 0:
                if grid[row][col-tally] == grid[row][left-tally]:
                    grid[row][left-tally] = grid[row][col-tally] + grid[row][left-tally]
                    grid[row][col-tally] = 0
                    
            
             
                

def push_right (grid):
    """merge grid values right""" 
    for row in range (4):
        for col in range (3,-1,-1):
            # line 0 # 0 2 0 0  -  0 0 0 2
            # line 1 # 0 0 0 0  -  0 0 0 0     
            # line 2 # 0 2 0 0  -  0 0 0 2
            # line 3 # 0 0 0 0  -  0 0 0 0            
            if col == 3: continue #nothing to push if it's at the right end
                
            right = col + 1            
            tally = 0
                
            for i in range(col,3):
                    
                right1 = i + 1
                
                if grid[row][right1] == 0: #counting how many spaces there are to the right of the current object
                        tally += 1
                        
            if tally > 0:
                grid[row][col+tally] = grid[row][col]
                grid[row][col] = 0
                
            if col+tally < 3:
                if grid[row][col+tally] == grid[row][right+tally]:
                    grid[row][right+tally] = grid[row][col+tally] + grid[row][right+tally]    
                    grid[row][col+tally] = 0
  