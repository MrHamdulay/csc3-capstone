# push.py


height = 4

def push_up (grid):
    # merge grid values upwards
    
        # shift values up through empty spaces (0-values)               
        # loop three times starting with second row to ensure values move through all empty spaces            
        for i in range(3): 
                for row in range(1, height):
                        for col in range(height):
                                # checking for empty space (0-values) in space above
                                if grid[row-1][col] == 0 or grid[row-1][col] == " ": 
                                        # if empty space above, set empty space to value of below space's value
                                        grid[row-1][col] = grid[row][col] 
                                        # bottom value becomes 0 (empty space is now below value)
                                        grid[row][col] = 0   
                        
        # add values that are the same      
        # loop through grid values      
        for row in range(1, height):
                for col in range(height):
                        # if value above = number below
                        if grid[row-1][col] == grid[row][col]:
                                # add values in top space
                                grid[row-1][col] = grid[row-1][col] + grid[row][col]
                                # old space now has no number in it (has been moved up)          
                                grid[row][col] = 0
    
        # get rid of spaces resulted from addition            
        for row in range(1, height):
                for col in range(height):
                        if grid[row-1][col] == 0 or grid[row-1][col] == " ":
                                grid [row-1][col] == grid[row][col]
                                grid[row][col] = 0
   
                
# def push_down (grid):
"""merge grid values downwards"""

# def push_left (grid):
"""merge grid values left"""

# def push_right (grid):
"""merge grid values right"""                                
                                
