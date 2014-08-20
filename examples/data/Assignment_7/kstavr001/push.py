
#Assignment 7,Question 3
#Avreyna Kistensamy
#29 April 2014

def push_left(grid):
    """merge grid values left"""
    for adj in range (3):
        for row in range(4):
            for col in range(3):
                if grid[row][col] == 0:
                    grid[row][col] = grid[row][col+1] #shift
                    grid[row][col+1] = 0 #delete value
                    
    for row in range(4):
        for col in range (3):
            if grid[row][col] == grid[row][col+1]:
                grid[row][col] = grid[row][col] * 2
                grid[row][col+1] = 0
            
            
    for adj in range (3):
        for row in range(4):
            for col in range(3):
                if grid[row][col] == 0:
                    grid[row][col] = grid[row][col+1] #shift
                    grid[row][col+1] = 0 #delete value 
                    

def push_right(grid):
    """merge grid values right"""
    for adj in range (4):
        for row in range(4):
            for col in range(3, 0, -1):
                if grid[row][col] == 0: 
                    grid[row][col] = grid[row][col-1] #shift
                    grid[row][col-1] = 0 #delete value
                    
    for row in range(4):
        for col in range (3):
            if grid[row][col] == grid[row][col+1]:
                grid[row][col] = grid[row][col] * 2
                grid[row][col+1] = 0
                
 
    for adj in range (4):
        for row in range(4):
            for col in range(3, 0, -1):
                if grid[row][col] == 0:
                    grid[row][col] = grid[row][col-1] #shift
                    grid[row][col-1] = 0  #delete value

def push_up(grid):
    """merge grid values upwards"""
    for adj in range (3):
        for row in range(3):
            for col in range(4):
                if grid[row][col] == 0:
                    grid[row][col] = grid[row+1][col] #shift
                    grid[row+1][col] = 0 #delete value
    
    for row in range(3):
        for col  in range (4):
            if grid[row][col] == grid[row+1][col]:
                grid[row][col] = grid[row][col] * 2 #merge numbers
                grid[row+1][col] = 0 #delete value
         
    for adj in range (3):
        for row in range(3):
            for col in range(4):
                if grid[row][col] == 0:
                    grid[row][col] = grid[row+1][col]
                    grid[row+1][col] = 0 #delete value               

def push_down(grid):
    """merge grid values downwards"""
    for adj in range (3):
        for row in range(3):
            for col in range(4):
                if (grid[row+1][col] == 0):
                    grid[row+1][col] = grid[row][col]
                    grid[row][col] = 0 #delete value
                
    for row in range(3, 0, -1):
        for col  in range (4):
            if grid[row][col] == grid[row-1][col]:
                grid[row][col] = grid[row][col] * 2
                grid[row-1][col] = 0  
          
          
    for adj in range (3):
        for row in range(3):
            for col in range(4):
                if (grid[row+1][col] == 0):
                    grid[row+1][col] = grid[row][col] #shift
                    grid[row][col] = 0 #delete value
                
#All functions quite similar
#Difference in ranges
#Avoiding index out of range error