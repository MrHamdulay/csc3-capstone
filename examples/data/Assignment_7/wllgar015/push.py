def push_up (grid):
    """merge grid values upwards""" 
    for row in range (4): 
        if row == 0: continue # cannot go up if it is already at the top
        for col in range(4):
            top = row-1
            # 0 0 0 0     -     2 0 2 0
            # 0 0 0 0     -     0 0 0 0     
            # 0 0 2 0     -     0 0 0 0
            # 2 0 0 0     -     0 0 0 0
            
                
            count = 0
            for i in range(row,0,-1): # counting the spaces upwards
                
                top1 = i-1 
                if grid[top1][col] == 0:
                    count += 1  # counting the number of spaces          
            
            if count > 0:
                grid[row-count][col] = grid[row][col] # the current row goes up "count" spaces
                grid[row][col] = 0 
            
                       
            if grid[row-count][col] == grid[top-count][col]: # if the top row is identical to the current row then they will merge
                grid[top-count][col] = grid[row-count][col] + grid[top-count][col]
                grid[row-count][col] = 0
                    
          
                
                    
                
                
                 
            
            
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
                
                    
                count = 0
                for i in range(row,3): # counting the spaces downwards
                    
                    down1 = i + 1 
                    
                    if grid[down1][col] == 0:
                        count += 1  #counting number of spaces          
                
                if count > 0:
                    grid[row+count][col] = grid[row][col] #the current row goes down "count" spaces
                    grid[row][col] = 0 
                
                           
                if row+count < 3:
                    if grid[row+count][col] == grid[down+count][col]: # now if the bottom row is the same as the current, they'll merge
                        grid[down+count][col] = grid[row+count][col] + grid[down+count][col]
                        grid[row+count][col] = 0    
def push_left (grid):
    """merge grid values left"""  
    for row in range (4):
        for col in range (4):
            # line 0 # 0 2 0 0  -  2 0 0 0
            # line 1 # 0 0 0 0  -  0 0 0 0     
            # line 2 # 0 2 0 0  -  2 0 0 0
            # line 3 # 0 0 0 0  -  0 0 0 0            
            if col == 0: continue #nothing to push if it's at the left end
            
            left = col - 1            
            count = 0
            
            for i in range(col,0,-1):
                
                left1 = i - 1

                if grid[row][left1] == 0: #counting how many spaces there are to the left of the current object
                    count += 1
                    
            if count > 0:
                grid[row][col-count] = grid[row][col]
                grid[row][col] = 0
            
            if col-count > 0:
                if grid[row][col-count] == grid[row][left-count]:
                    grid[row][left-count] = grid[row][col-count] + grid[row][left-count]
                    grid[row][col-count] = 0
                    
            
             
                

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
            count = 0
                
            for i in range(col,3):
                    
                right1 = i + 1
                
                if grid[row][right1] == 0: #counting how many spaces there are to the right of the current object
                        count += 1
                        
            if count > 0:
                grid[row][col+count] = grid[row][col]
                grid[row][col] = 0
                
            if col+count < 3:
                if grid[row][col+count] == grid[row][right+count]:
                    grid[row][right+count] = grid[row][col+count] + grid[row][right+count]    
                    grid[row][col+count] = 0
  