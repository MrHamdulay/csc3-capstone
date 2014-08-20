def push_up (grid):
    """merge grid values upwards"""
    for i in range (3):   
        for row in range(1,4):  
            for col in range(4): 
                if grid[row-1][col] == grid[row-1][col] ==0:  
                    grid[row-1][col] = grid[row][col]  #Make the item in the row below equal the current 1
                    grid[row][col] = 0  #removes the value from the grid and assigns 0 to it
                   
    for row in range(1,4):
        for col in range(4):
            if grid[row-1][col] == grid[row][col]:   #Check if they are the same
                grid[row][col] = 0  #removes th original item by making it = 0          
                grid[row-1][col] += grid[row-1][col]   #"Merge" by multiplying item by 2
                
    for row in range(1,4): 
        for col in range(4):
            if grid[row-1][col]== grid[row-1][col]==0:
                grid[row-1][col] = grid[row][col]
                grid[row][col] = 0

def push_down (grid):
    """merge grid values downwards"""
    for i in range (3):  
        for row in range (2,-1,-1):  #iterates backwards since weare now duing the oposite of pushing up 
            for col in range (3,-1,-1):  
                if grid[row+1][col] == grid[row+1][col] ==0:  
                    grid[row+1][col] = grid[row][col]  #Make the item in the row above equal to the current item
                    grid[row][col] = 0  #removes the value from the grid and assigns 0 to it
                      
    for row in range(2,-1,-1):
        for col in range(3,-1,-1):
            if grid[row+1][col] == grid[row][col]: #Check if they are the same
                grid[row][col] = 0 #removes the value from the grid and assigns 0 to it                
                grid[row+1][col] += grid[row+1][col]  # merges the two if the are equal
                   
    for row in range(2,-1,-1):  #Last repetition of the i loop after merging
        for col in range(3,-1,-1):
            if grid[row+1][col]== grid[row+1][col]==0:
                grid[row+1][col] = grid[row][col]
                grid[row][col]=0 

def push_left (grid):
    """merge grid values left"""
    for i in range (3):   
        for row in range(4):
            for col in range(1,4): #Starts from 1 since we don't need first column as the item wouldn't need to move
                if grid[row][col-1] == grid[row][col-1] ==0:
                    grid[row][col-1] = grid[row][col]  #Make the item in the column leftwards of current item equal to current item
                    grid[row][col] = 0  #removes the value from the grid and assigns 0 to it
                      
    for row in range(4):
        for col in range(1,4): 
            if grid[row][col-1] == grid[row][col]:
                grid[row][col-1] += grid[row][col] 
                grid[row][col] =0
                   
    for row in range(4):
        for col in range(1,4):
            if grid[row][col-1]== grid[row][col-1]==0:
                grid[row][col-1] = grid[row][col]
                grid[row][col]=0    

def push_right (grid):
    """merge grid values right""" 
    for i in range (3):
        for row in range(3,-1,-1):
            for col in range(2,-1,-1):
                if grid[row][col+1] == grid[row][col+1] ==0:
                    grid[row][col+1] = grid[row][col]
                    grid[row][col] = 0
                      
    for row in range(3,-1,-1):
        for col in range(2,-1,-1):
            if grid[row][col+1] == grid[row][col]:
                grid[row][col] = 0                
                grid[row][col+1] += grid[row][col+1]
                   
    for row in range(3,-1,-1):
        for col in range(2,-1,-1):
            if grid[row][col+1]== grid[row][col+1]==0:
                grid[row][col+1] = grid[row][col]
                grid[row][col]=0