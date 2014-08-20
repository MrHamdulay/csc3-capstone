"""A program to imitate the 2048 game
Alison Hoernle
HRNALI002
30 April 2014"""

# to move a value up, you need to go through each row and if there are any spaces then move them up, and only after that merge identical pairs.

# merge grid values up
def push_up(grid):
    
    # remove any zeroes in the row
    merged = [] # create an empty list to make sure you don't merge the values twice in one turn
    for i in range(5):
        for col in range(4):
            for row in range(3):
                if grid[row][col] == 0:
                    grid[row][col] = grid[row+1][col]
                    grid[row+1][col] = 0
            
            # if no zeroes then check for adjacent items       
            for row in range(3):
                if col not in merged:
                    if grid[row][col] == grid[row+1][col]:
                        grid[row][col] = grid[row][col] + grid[row][col]
                        grid[row+1][col] = 0
                        merged.append(col)
    
    return grid

# merge grid values to the right
def push_right(grid):
    
    # remove any zeroes in the row
    merged = []
    for i in range(5): # creating an empty list to add the row to so that it doesn't add multiple values in one turn.
        for row in range(4):
            for col in range(3,0,-1):
                if grid[row][col] == 0:
                    grid[row][col] = grid[row][col-1]
                    grid[row][col-1] = 0
            
            # check for adjacent values
            for col in range(3,0,-1):
                
                if row not in merged:
                    if grid[row][col] == grid[row][col-1]:
                        grid[row][col] = grid[row][col] + grid[row][col]
                        grid[row][col-1] = 0
                        merged.append(row)
                    
    return grid

# merge grid values to the left                
def push_left (grid):
    
    # remove any zeroes in the row
    merged = []
    for i in range(5):
        for row in range(4): 
            for col in range(3):
                if grid[row][col] == 0:
                    grid[row][col] = grid[row][col+1]
                    grid[row][col+1] = 0
                
            # check for adjacent values that are the same and merge them
            for col in range(3):
                if row not in merged:
                    if grid[row][col] == grid[row][col+1]:
                        grid[row][col] = grid[row][col] + grid[row][col]
                        grid[row][col+1] = 0
                        merged.append(row)
                
    return grid

# merge grid values downwards    
def push_down(grid):
    # remove any zeroes in the row
    merged = []
    for i in range(5):
        for col in range(4):
            for row in range(3,0,-1):
                if grid[row][col] == 0:
                    grid[row][col] = grid[row-1][col]
                    grid[row-1][col] = 0
            
            # check for adjacent values that are the same and move them        
            for row in range(3,0,-1):
                if col not in merged:
                    if grid[row][col] == grid[row-1][col]:
                        grid[row][col] = grid[row][col] + grid[row][col]
                        grid[row-1][col] = 0
                        merged.append(col)
    return grid