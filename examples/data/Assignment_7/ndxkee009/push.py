"""Keegan Naidoo
NDXKEE009
27 April 2014"""

def push_up (grid):     # Moves values in grid up and adds values that are equal

    for row in range(4):
        for col in range(4):
            if grid[row][col]==" ":
                grid[row][col]=0

            current = grid[row][col]
            
            rowcount = row
            
            while rowcount > 0:
                rowcount -= 1
                
                if grid[rowcount][col] == 0:
                    grid[rowcount][col] = current
                    grid[rowcount+1][col] = 0
                else:
                    if current == grid[rowcount][col]:
                        grid[rowcount][col] += current
                        grid[rowcount+1][col] = 0
                

def push_down (grid):  # Moves values in grid down and adds values that are equal

    for row in range(4):
        for col in range(4):
            if grid[row][col]==" ":
                grid[row][col]=0
                
            current = grid[row][col]
            
            rowcount = row
            
            while rowcount >0 and rowcount < 3:
                
                rowcount += 1                 
                
                if grid[rowcount][col] == 0:
                    grid[rowcount][col] = current
                    grid[row][col] = 0
                    
                else:
                    if current == grid[rowcount][col]:
                        grid[rowcount][col] += current
                        grid[rowcount-1][col] = 0
                        
def push_left (grid):   # Moves values in grid left and adds values that are equal
   
    for row in range(4):
        for col in range(4):
            if grid[row][col]==" ":
                grid[row][col]=0

            current = grid[row][col]
            
            colcount = col
            
            while colcount > 0:
                colcount -= 1
                
                if grid[row][colcount] == 0:
                    grid[row][colcount] = current
                    grid[row][colcount+1] = 0
                else:
                    if current == grid[row][colcount]:
                        grid[row][colcount] += current
                        grid[row][colcount+1] = 0
    
                    
def push_right (grid):   # Moves values in grid right and adds values that are equal
   
    for row in range(4):
        for col in range(4):
            if grid[row][col]==" ":
                grid[row][col]=0

            current = grid[row][col]
            
            colcount = col
            
            while colcount < 3:
                colcount += 1
                
                if grid[row][colcount] == 0:
                    grid[row][colcount] = current
                    grid[row][colcount-1] = 0
                else:
                    if current == grid[row][colcount]:
                        grid[row][colcount] += current
                        grid[row][colcount-1] = 0