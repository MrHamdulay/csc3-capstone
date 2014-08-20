#OMG 2048 game
#Annie Ho
# programming for life

def push_up (grid):
 
    
    for colum in range (4):      
        stm = 1
        ct = 0
        
              
        for row in range(4):
            if row == 0: continue 
            
            top = row-1
          
            count = 0
            for i in range(row,0,-1):
                
                top1 = i-1 
                if grid[top1][colum] == 0:
                    count += 1         
            
            if count > 0:
                grid[row-count][colum] = grid[row][colum] 
                grid[row][colum] = 0 
            
            if stm == grid[row-count][colum]:
                continue
                       
            if row-count > 0:
                if grid[row-count][colum] == grid[top-count][colum]:                                  
                    grid[top-count][colum] = grid[row-count][colum] + grid[top-count][colum]
                    stm = grid[top-count][colum]
                    grid[row-count][colum] = 0
                    ct += 1
                    
          
                           
def push_down (grid):
   
    for colum in range (4): 
        stm = 1 
        for row in range(3,-1,-1):
            if row == 3: 
                continue 
            down = row + 1
              
                
                    
            count = 0
            for i in range(row,3): 
                    
                down1 = i + 1 
                    
                if grid[down1][colum] == 0:
                    count += 1 
            if count > 0:
                grid[row+count][colum] = grid[row][colum] 
                grid[row][colum] = 0 
                
            if stm == grid[row+count][colum]:
                    continue
                
                           
            if row+count < 3:
                if grid[row+count][colum] == grid[down+count][colum]: 
                        grid[down+count][colum] = grid[row+count][colum] + grid[down+count][colum]
                        grid[row+count][colum] = 0    
                        stm = grid[down+count][colum]
def push_left (grid):
  
    for row in range (4):
        stm = 1
        for colum in range (4):
          
           
            if colum == 0: continue 
            
            left = colum - 1            
            count = 0
            
            for i in range(colum,0,-1):
                
                left1 = i - 1

                if grid[row][left1] == 0: 
                    count += 1
                    
            if count > 0:
                grid[row][colum-count] = grid[row][colum]
                grid[row][colum] = 0
            
            if stm == grid[row][colum-count]:
                continue
            if colum-count > 0:
                if grid[row][colum-count] == grid[row][left-count]:
                    grid[row][left-count] = grid[row][colum-count] + grid[row][left-count]
                    grid[row][colum-count] = 0
                    stm = grid[row][left-count]
                    
            
             
                

def push_right (grid):
   
    for row in range (4):
        stm = 1
        for colum in range (3,-1,-1):
      
            if colum == 3: continue
            right = colum + 1            
            count = 0
                
            for i in range(colum,3):
                    
                right1 = i + 1
            
                if grid[row][right1] == 0: 
                        count += 1
                        
            if count > 0:
                grid[row][colum+count] = grid[row][colum]
                grid[row][colum] = 0
                
            if stm == grid[row][colum+count]:
                continue
                
            if colum+count < 3:
                if grid[row][colum+count] == grid[row][right+count]:
                    grid[row][right+count] = grid[row][colum+count] + grid[row][right+count]    
                    grid[row][colum+count] = 0
                    stm = grid[row][right+count]
  