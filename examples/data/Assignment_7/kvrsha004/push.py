""" Q3 of Assignment 7: 2048 Push and Merge Up/Down/Left/Right Functions
Shaheel Kooverjee
1st May 2014 """

def push_up (grid):
    """merge grid values upwards"""
    
    #remove spaces
    for i in range(3): #run thrice to remove all relevant spaces 
        for row in range(1,4): #loop through lower three rows from top
            for col in range(4): #loop through all columns
                if grid[row-1][col] == " " or grid[row-1][col] == 0:
                    grid[row-1][col] = grid[row][col] #replace space with item directly below
                    grid[row][col] = 0 #remove item below so as to have "moved" it up
    
    #merge adjacent values if equal                    
    for row in range(1,4):
        for col in range(4):
            if grid[row-1][col] == grid[row][col]:
                grid[row-1][col] *= 2 #double upper value if upper and lower equal
                grid[row][col] = 0 #remove lower value so as to have "merged" it with upper value
                
    #remove spaces after merge: repeat of first "remove spaces" loop
    for row in range(1,4):
        for col in range(4):
            if grid[row-1][col] == " " or grid[row-1][col] == 0:
                grid[row-1][col] = grid[row][col]
                grid[row][col] = 0            


def push_down (grid):
    """merge grid values downwards"""
    #same concept as used for push_up(grid); differences noted in comments
    
    for i in range(3):
        for row in range(2, -1, -1): #loop through upper three rows from bottom
            for col in range(4): #loop through all columns
                if grid[row+1][col] == " " or grid[row+1][col] == 0:
                    grid[row+1][col] = grid[row][col] #replace space with item directly above
                    grid[row][col] = 0 #remove item below so as to have "moved" it down
                       
    for row in range(2, -1, -1):
        for col in range(4):
            if grid[row+1][col] == grid[row][col]:
                grid[row+1][col] *= 2 #double lower value if lower and upper equal
                grid[row][col] = 0 #remove upper value so as to have "merged" it with lower value
                   
    for row in range(2, -1, -1):
        for col in range(4):
            if grid[row+1][col] == " " or grid[row+1][col] == 0:
                grid[row+1][col] = grid[row][col]
                grid[row][col] = 0  
                
                
def push_left (grid):
    """merge grid values left"""
    #same concept as used for push_up(grid); differences noted in comments
    
    for i in range(3):
        for col in range(1,4): #loop through last three columns from left
            for row in range(4): #loop through all rows
                if grid[row][col-1] == " " or grid[row][col-1] == 0:
                    grid[row][col-1] = grid[row][col] #replace space with item directly to the right
                    grid[row][col] = 0 #remove item to the right so as to have "moved" it to the left
                        
    for col in range(1,4):
        for row in range(4):
            if grid[row][col-1] == grid[row][col]:
                grid[row][col-1] *= 2 #double left value if left and right equal
                grid[row][col] = 0 #remove right value so as to have "merged" it with left value
                
    for col in range(1,4):
        for row in range(4):
            if grid[row][col-1] == " " or grid[row][col-1] == 0:
                grid[row][col-1] = grid[row][col]
                grid[row][col] = 0  
                

def push_right (grid):
    """merge grid values right"""
    #same concept as used for push_up(grid); differences noted in comments
    
    for i in range(3):
        for col in range(2, -1, -1): #loop through first three columns from right
            for row in range(4): #loop through all rows
                if grid[row][col+1] == " " or grid[row][col+1] == 0:
                    grid[row][col+1] = grid[row][col] #replace space with item directly to the left
                    grid[row][col] = 0 #remove item to the left so as to have "moved" it to the right
                       
    for col in range(2, -1, -1):
        for row in range(4):
            if grid[row][col+1] == grid[row][col]:
                grid[row][col+1] *= 2 #double right value if right and left equal
                grid[row][col] = 0 #remove left value so as to have "merged" it with right value
                   
    for col in range(2, -1, -1):
        for row in range(4):
            if grid[row][col+1] == " " or grid[row][col+1] == 0:
                grid[row][col+1] = grid[row][col]
                grid[row][col] = 0    