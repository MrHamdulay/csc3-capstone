# Kate Bell
# BLLKAT005
# 28 April 2014 
import util

def push_up (grid):
    """merge grid values upwards""" 
    # First move as many values as far up as possible
    for row in range (0,3):
            for column in range (4):
                if grid[row][column]==0:
                    grid[row][column]=grid[row+1][column]
                    grid[row+1][column]=0 
                    
    for row in range (0,3):
            for column in range (4):
                if grid[row][column]==0:
                    grid[row][column]=grid[row+1][column]
                    grid[row+1][column]=0    
    
    # Loop through the 2d array. If a value is equal to the value above it, set the top value equal to the sum and the lower value equal to zero.
    for row in range (1,4):
        for column in range (4):
            if grid[row][column]==grid[row-1][column]:
                grid[row-1][column]= grid[row][column] + grid[row-1][column]
                grid[row][column]=0
            # If the higher value equals 0, switch the two values
            elif grid[row-1][column] == 0:
                grid[row-1][column]=grid[row][column]
                grid[row][column]=0
     
    for row in range (0,3):
            for column in range (4):
                if grid[row][column]==0:
                    grid[row][column]=grid[row+1][column]
                    grid[row+1][column]=0
                           
    for row in range (0,3):
            for column in range (4):
                if grid[row][column]==0:
                    grid[row][column]=grid[row+1][column]
                    grid[row+1][column]=0
        
                
def push_down (grid):
    """merge grid values downwards"""
    # First move as many values as down up as possible
    for row in range (3,0,-1):
        for column in range (4):
            if grid[row][column]==0 and not grid[row-1][column]==0:
                grid[row][column]=grid[row-1][column]
                grid[row-1][column]=0   
   
   # Loop through the 2d array. If a value is equal to the value beneath it, set the lower value equal to the sum and the higher value equal to zero.
    flag_row = -1
    flag_column = -1
    for row in range (0,3):
        for column in range (4):
            if row == flag_row and column == flag_column:
                continue
            # Flag the indeces of values which are the result of a sum, and do not include these values in further sums
            elif grid[row][column]==grid[row+1][column]:
                grid[row+1][column]= grid[row][column] + grid[row+1][column]
                grid[row][column]=0
                flag_row=row+1
                flag_column=column
            # If the bottom value equals 0, switch the two values
            elif grid[row+1][column] == 0:
                grid[row+1][column]=grid[row][column]
                grid[row][column]=0
         
              
    for row in range (3,0,-1):
        for column in range (4):
            if grid[row][column]==0 and not grid[row-1][column]==0:
                grid[row][column]=grid[row-1][column]
                grid[row-1][column]=0  
    
    for row in range (3,0,-1):
        for column in range (4):
            if grid[row][column]==0 and not grid[row-1][column]==0:
                grid[row][column]=grid[row-1][column]
                grid[row-1][column]=0
          
   

def push_left (grid):
    """merge grid values left"""
    # First move as many values as far left as possible    
    for row in range (4):
        for column in range (0,3):
            if grid[row][column]==0:
                        grid[row][column]=grid[row][column+1]
                        grid[row][column+1]=0 
    for row in range (4):
        for column in range (0,3):
            if grid[row][column]==0:
                        grid[row][column]=grid[row][column+1]
                        grid[row][column+1]=0        
    # Loop through the 2d array. If a value is equal to the value to its left, set the left value equal to the sum and the right value equal to zero.
    for row in range (4):
            for column in range (1,4):
                if grid[row][column]==grid[row][column-1]:
                    grid[row][column-1]= grid[row][column] + grid[row][column-1]
                    grid[row][column]=0
                # If the left value equals 0, switch the two values
                elif grid[row][column-1] == 0:
                    grid[row][column-1]=grid[row][column]
                    grid[row][column]=0
         
    for row in range (4):
        for column in range (0,3):
                if grid[row][column]==0:
                        grid[row][column]=grid[row][column+1]
                        grid[row][column+1]=0 
                        
    for row in range (4):
        for column in range (0,3):
                if grid[row][column]==0:
                        grid[row][column]=grid[row][column+1]
                        grid[row][column+1]=0     
        
def push_right (grid):
    """merge grid values right""" 
    # First move as many values as far right as possible
    for row in range (4):
        for column in range (3,0,-1):
            if grid[row][column]==0 and not grid[row][column-1]==0:
                grid[row][column]=grid[row][column-1]
                grid[row][column-1]=0 
    
    # Loop through the 2d array. If a value is equal to the value to its right, set the right value equal to the sum and the left value equal to zero.
    for row in range (4):
        for column in range (0,3):   
            if grid[row][column]==grid[row][column+1]:
                grid[row][column+1]= grid[row][column] + grid[row][column+1]
                grid[row][column]=0
            # If the right value equals 0, switch the two values
            elif grid[row][column+1] == 0:
                grid[row][column+1]=grid[row][column]
                grid[row][column]=0
           
    for row in range (4):
        for column in range (3,0,-1):
            if grid[row][column]==0 and not grid[row][column-1]==0:
                grid[row][column]=grid[row][column-1]
                grid[row][column-1]=0    
                
    for row in range (4):
        for column in range (3,0,-1):
            if grid[row][column]==0 and not grid[row][column-1]==0:
                grid[row][column]=grid[row][column-1]
                grid[row][column-1]=0   
    