def push_up (grid):
    """merge grid values upwards""" 
    for row in range (4): 
        if row == 0: continue 
        for col in range(4):
            top = row-1
                       
            count = 0
            for i in range(row,0,-1): 
                
                top1 = i-1 
                if grid[top1][col] == 0:
                    count += 1      
            
            if count > 0:
                grid[row-count][col] = grid[row][col] 
                grid[row][col] = 0 
            
            if grid[row-count][col] == grid[top-count][col]: 
                grid[top-count][col] = grid[row-count][col] + grid[top-count][col]
                grid[row-count][col] = 0




def push_down (grid):
    """merge grid values downwards"""
    for row in range (3,-1,-1): 
        if row == 3: continue 
        for col in range(4):
                down = row + 1
                    
                count = 0
                for i in range(row,3):
                    
                    down1 = i + 1 
                    
                    if grid[down1][col] == 0:
                        count += 1         
                
                if count > 0:
                    grid[row+count][col] = grid[row][col] 
                    grid[row][col] = 0 
                
                           
                if row+count < 3:
                    if grid[row+count][col] == grid[down+count][col]: 
                        grid[down+count][col] = grid[row+count][col] + grid[down+count][col]
                        grid[row+count][col] = 0    




def push_left (grid):
    """merge grid values left"""  
    for row in range (4):
        for col in range (4):
                     
            if col == 0: continue 
            
            left = col - 1            
            count = 0
            
            for i in range(col,0,-1):
                
                left1 = i - 1

                if grid[row][left1] == 0: 
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
                
            if col == 3: continue 
            right = col + 1            
            count = 0
                
            for i in range(col,3):
                    
                right1 = i + 1
                
                if grid[row][right1] == 0: 
                        count += 1
                        
            if count > 0:
                grid[row][col+count] = grid[row][col]
                grid[row][col] = 0
                
            if col+count < 3:
                if grid[row][col+count] == grid[row][right+count]:
                    grid[row][right+count] = grid[row][col+count] + grid[row][right+count]    
                    grid[row][col+count] = 0
  

                    
            
