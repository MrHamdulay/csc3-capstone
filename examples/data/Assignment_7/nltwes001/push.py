#ASSIGNMENT 7
#QUESTION 3
#NLTWES001

#Upward swipe
def push_up (grid):
    for row in range (4): 
        if row==0: 
            continue 
        for col in range(4):
            top = row-1
                
            tally = 0
            for i in range(row,0,-1):                
                top1 = i-1 
                if grid[top1][col] == 0:
                    tally += 1          
            
            if tally > 0:
                grid[row-tally][col] = grid[row][col]
                grid[row][col] = 0 
                
            if grid[row-tally][col] == grid[top-tally][col]: 
                grid[top-tally][col] = grid[row-tally][col] + grid[top-tally][col]
                grid[row-tally][col] = 0  

#Downward swipe            
def push_down (grid):
    for row in range (3,-1,-1): 
        if row==3:
            continue 
        for col in range(4):
                down = row + 1               
                tally = 0
                for i in range(row,3):
                    down1 = i + 1 
                
                    if grid[down1][col] == 0:
                        tally += 1         
                
                if tally > 0:
                    grid[row+tally][col] = grid[row][col]
                    grid[row][col] = 0 
                
                           
                if row+tally < 3:
                    if grid[row+tally][col] == grid[down+tally][col]:
                        grid[down+tally][col] = grid[row+tally][col] + grid[down+tally][col]
                        grid[row+tally][col] = 0    
                        
#Left swipe                        
def push_left (grid):
    for row in range (4):
        for col in range (4):
                   
            if col==0:
                continue 
            
            left = col - 1            
            tally = 0
            
            for i in range(col,0,-1):
                left1 = i - 1

                if grid[row][left1] == 0:
                    tally += 1
                    
            if tally > 0:
                grid[row][col-tally] = grid[row][col]
                grid[row][col] = 0
            
            if col-tally > 0:
                if grid[row][col-tally] == grid[row][left-tally]:
                    grid[row][left-tally] = grid[row][col-tally] + grid[row][left-tally]
                    grid[row][col-tally] = 0             

#right swipe
def push_right (grid):
    for row in range (4):
        for col in range (3,-1,-1):        
            if col == 3: 
                continue 
            right = col + 1            
            tally = 0
                
            for i in range(col,3):
                right1 = i + 1

                if grid[row][right1] == 0:
                        tally += 1
                        
            if tally > 0:
                grid[row][col+tally] = grid[row][col]
                grid[row][col] = 0
                
            if col+tally < 3:
                if grid[row][col+tally] == grid[row][right+tally]:
                    grid[row][right+tally] = grid[row][col+tally] + grid[row][right+tally]    
                    grid[row][col+tally] = 0
  