#2048
#Helin Kim
#KMXHYE004  

def push_up (grid):
 
    
    for column in range (4):      
        no = 1
        ct = 0
        
              
        for row in range(4):
            if row == 0: continue 
            
            tp = row-1
          
            counter = 0
            for i in range(row,0,-1):
                
                top1 = i-1 
                if grid[top1][column] == 0:
                    counter += 1         
            
            if counter > 0:
                grid[row-counter][column] = grid[row][column] 
                grid[row][column] = 0 
            
            if no == grid[row-counter][column]:
                continue
                       
            if row-counter > 0:
                if grid[row-counter][column] == grid[tp-counter][column]:                                  
                    grid[tp-counter][column] = grid[row-counter][column] + grid[tp-counter][column]
                    no = grid[tp-counter][column]
                    grid[row-counter][column] = 0
                    ct += 1
                    
          
                           
def push_down (grid):
   
    for column in range (4): 
        no = 1 
        for row in range(3,-1,-1):
            if row == 3: 
                continue 
            down = row + 1
              
                
                    
            counter = 0
            for i in range(row,3): 
                    
                down1 = i + 1 
                    
                if grid[down1][column] == 0:
                    counter += 1 
            if counter > 0:
                grid[row+counter][column] = grid[row][column] 
                grid[row][column] = 0 
                
            if no == grid[row+counter][column]:
                    continue
                
                           
            if row+counter < 3:
                if grid[row+counter][column] == grid[down+counter][column]: 
                        grid[down+counter][column] = grid[row+counter][column] + grid[down+counter][column]
                        grid[row+counter][column] = 0    
                        no = grid[down+counter][column]
def push_left (grid):
  
    for row in range (4):
        no = 1
        for column in range (4):
          
           
            if column == 0: continue 
            
            left = column - 1            
            counter = 0
            
            for i in range(column,0,-1):
                
                left1 = i - 1

                if grid[row][left1] == 0: 
                    counter += 1
                    
            if counter > 0:
                grid[row][column-counter] = grid[row][column]
                grid[row][column] = 0
            
            if no == grid[row][column-counter]:
                continue
            if column-counter > 0:
                if grid[row][column-counter] == grid[row][left-counter]:
                    grid[row][left-counter] = grid[row][column-counter] + grid[row][left-counter]
                    grid[row][column-counter] = 0
                    no = grid[row][left-counter]
                    
            
             
                

def push_right (grid):
   
    for row in range (4):
        no = 1
        for column in range (3,-1,-1):
      
            if column == 3: continue
            right = column + 1            
            counter = 0
                
            for i in range(column,3):
                    
                right1 = i + 1
            
                if grid[row][right1] == 0: 
                        counter += 1
                        
            if counter > 0:
                grid[row][column+counter] = grid[row][column]
                grid[row][column] = 0
                
            if no == grid[row][column+counter]:
                continue
                
            if column+counter < 3:
                if grid[row][column+counter] == grid[row][right+counter]:
                    grid[row][right+counter] = grid[row][column+counter] + grid[row][right+counter]    
                    grid[row][column+counter] = 0
                    no = grid[row][right+counter]
  