"""module for 2048/[32] game
Julian Albert
ALBJUL005
01 May 2014"""


def push_up(grid):
    """Merge grid value upwards"""
    # Push
    for column in range(len(grid[0])):# Iterate through each column
        pushing = True #sentinel created
        start = 0 #initialize start and index points
        i = start
        while pushing:
            if i+1 <= len(grid): # check if index will be within bounds
                if grid[i][column] == 0: # skip over if index contains '0'
                    i += 1
                else: # if the value at index is non-zero
                    grid[i][column],grid[start][column] = grid[start][column],grid[i][column] 
                    # Swap start and index values
                    start += 1 #move the start point
                    i = start #reset the index point
            else:
                pushing = False # Stop pushing when out of bounds
    # Merge
    # Go through every value in the list
    for column in range(len(grid[0])):
        for i in range(len(grid)):
            #Check if there is a value below the current one
            if i+1 < len(grid): 
                #if the values are the same, add them then clear the bottom value's place, if the value is 0 swap places with the value below it 
                if grid[i][column] == grid[i+1][column] or grid[i][column] == 0:
                    #Swap and add values
                    grid[i][column] += grid[i+1][column]
                    grid[i+1][column] = 0
                    
def push_down(grid):
    """Merge grid values downwards"""
    # Push
    for column in range(len(grid[0])):# Iterate through each column
        pushing = True #sentinel created
        start = len(grid)-1 #initialize start and index points
        i = start
        while pushing:
            if i >= 0: # check if index will be within bounds
                if grid[i][column] == 0: # skip over if index contains '0'
                    i -= 1
                else: # if the value at index is non-zero
                    grid[i][column],grid[start][column] = grid[start][column],grid[i][col] 
                    # Swap start and index values
                    start -= 1 #move the start point
                    i = start #reset the index point
            else:
                pushing = False # Stop pushing when out of bounds
    # Merge
    # Go through every value in the list
    for column in range(len(grid[0])):
        for i in range(len(grid)-1,0,-1):
            #Check if there is a value below the current one
            if i-1 >= 0: 
                #if the values are the same, add them then clear the bottom value's place, if the value is 0 swap places with the value below it 
                if grid[i][column] == grid[i-1][column] or grid[i][column] == 0:
                    #Swap and add values
                    grid[i][column] += grid[i-1][column]
                    grid[i-1][column] = 0    
                    
def push_left (grid):
    """Merge grid values left"""
    for row in range(4):                                        
        for column in range(3):                                 
            counter = 1                                           
            while counter < (4-column) and grid[row][column] == 0:  
                grid[row][column] = grid[row][column+counter]     
                grid[row][column+counter] = 0                     
                counter += 1                                      
    
    for row in range(4):                                        
        for column in range(3):                                 
            if grid[row][column] == grid[row][column+1]:           
                grid[row][column] = 2*grid[row][column]           
                grid[row][column+1] = 0                           

    for row in range(4):                                        
        for column in range(3):                                 
            counter = 1                                           
            while counter < (4-column) and grid[row][column] == 0:  
                grid[row][column] = grid[row][column+counter]     
                grid[row][column+counter] = 0                     
                counter += 1                                      

def push_right (grid):
    """Merge grid values right"""    
    for row in range(4):                                        
        for column in range(3,0,-1):                            
            counter = 1                                           
            while counter<(column+1) and grid[row][column] == 0: 
                grid[row][column] = grid[row][column-counter]    
                grid[row][column-counter] = 0                     
                counter+=1                                      
    
    for row in range(4):                                        
        for column in range(3,0,-1):                            
            if grid[row][column] == grid[row][column-1]:           
                grid[row][column] = 2*grid[row][column]           
                grid[row][column-1] = 0                           

    for row in range(4):                                        
        for column in range(3,0,-1):                            
            counter = 1                                           
            while counter < (column+1) and grid[row][column] == 0:  
                grid[row][column] = grid[row][column-counter]     
                grid[row][column-counter] = 0                     
                counter += 1                                      