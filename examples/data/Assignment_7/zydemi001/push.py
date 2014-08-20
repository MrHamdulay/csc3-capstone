#A program containing a set of merging functions that merge equal values and eliminate gaps, as needed in order to play the game "2048"
#Author: Emiel Zyde
#Date: 27 April 2014


def push_up(grid):
    """ merge grid values upwards """ 
    
    #in order to ensure than all spaces are removed, we have to run through the grid three times
    for iteration in range (3):
        for row in range (1,4):         #will loop through the various rows
            for col in range (4):       #loops through the various columns 
                #we must now start shifting the spaces
                #if a space or a zero is found, we must delete the space or the zero and replace it by the item in the row below it
                if grid[row-1][col] == ' ' or grid[row-1][col] == 0:
                    grid[row-1][col] = grid[row][col]
                    grid[row][col] = 0    #we replace the value in the column below by a zero, in order to avoid the duplication of values
    
    #now we must check if adjacent values are equal
    #if they are, we must add them
    #else, nothing must happen
    for row in range(1,4):
        for col in range (4):
            if grid[row-1][col] == grid[row][col]:
                grid[row-1][col] = grid[row-1][col] * 2   # since the values are equal, we can simply double the one value
                grid[row][col] = 0
    
    #during the addition process, we might have opened some new gaps, which need to be closed now
    #this can be done by re-using the code we used previously 
    for row in range (1,4):        
        for col in range (4):                 
            if grid[row-1][col] == ' ' or grid[row-1][col] == 0:
                grid[row-1][col] = grid[row][col]
                grid[row][col] = 0    
    
    return grid     #returns the grid to the program, for it to be printed and for the game to continue
    
    
def push_down(grid):    
    """ merge grid values downwards """ 
    
    for iteration in range (3):
            for row in range (2,-1,-1):         #will loop through the various rows
                for col in range (3,-1,-1):       #will loop through the various columns
                #this time we want it to start from below, hence the reversal of the indeces in the range indicators --> we want to avoid it working from the top up and adding incorrectly 
                    if grid[row+1][col] == ' ' or grid[row+1][col] == 0:
                        grid[row+1][col] = grid[row][col]
                        grid[row][col] = 0    #we are repeating the same process as before, but from the bottom up 
    
    for row in range(2,-1,-1):
            for col in range (3,-1,-1):
                if grid[row+1][col] == grid[row][col]:  #grid[row+1] will check if the value in a given row is equal to the value in the row below it --> if so, it will add the values together/ double the given value 
                    grid[row+1][col] = grid[row+1][col] * 2   # since the values are equal, we can simply double the one value
                    grid[row][col] = 0        
                
    #again, we may have created gaps whilst adding the values together and these can again be filled by re-using the previous code
                
    for row in range (2,-1,-1):        
            for col in range (3,-1,-1):                 
                if grid[row+1][col] == ' ' or grid[row+1][col] == 0:
                    grid[row+1][col] = grid[row][col]
                    grid[row][col] = 0    
                    
    return grid 
            
def push_left(grid):    
    """ merge grid values left"""         

    #in order to ensure than all spaces are removed, we have to run through the grid three times
    for iteration in range (3):
        for row in range (4):         #will loop through the various rows
            for col in range (1,4):       #loops through the various columns 
            #we must now start shifting the spaces
            #if a space or a zero is found, we must delete the space or the zero and replace it by the item in the column next to it 
                if grid[row][col-1] == ' ' or grid[row][col-1] == 0:
                    grid[row][col-1] = grid[row][col]
                    grid[row][col] = 0    #we replace the value in the column below by a zero, in order to avoid the duplication of values
        
        #now we must check if adjacent values are equal
        #if they are, we must add them
        #else, nothing must happen
    for row in range(4):
        for col in range (1,4):
            if grid[row][col-1] == grid[row][col]:
                grid[row][col-1] = grid[row][col-1] * 2   # since the values are equal, we can simply double the one value
                grid[row][col] = 0
        
        #during the addition process, we might have opened some new gaps, which need to be closed now
        #this can be done by re-using the code we used previously 
    for row in range (4):        
        for col in range (1,4):                 
            if grid[row][col-1] == ' ' or grid[row][col-1] == 0:
                grid[row][col-1] = grid[row][col]
                grid[row][col] = 0    
        
    return grid     #returns the grid to the program, for it to be printed and for the game to continue            

def push_right(grid):    
    """ merge grid values right"""         

    #in order to ensure than all spaces are removed, we have to run through the grid three times
    for iteration in range (3):
        for row in range (3,-1,-1):         #will loop through the various rows
            for col in range (2,-1,-1):       #loops through the various columns 
            #we must now start shifting the spaces
            #if a space or a zero is found, we must delete the space or the zero and replace it by the item in the column next to it 
                if grid[row][col+1] == ' ' or grid[row][col+1] == 0:
                    grid[row][col+1] = grid[row][col]
                    grid[row][col] = 0    #we replace the value in the column below by a zero, in order to avoid the duplication of values
        
        #now we must check if adjacent values are equal
        #if they are, we must add them
        #else, nothing must happen
    for row in range(3,-1,-1):
        for col in range (2,-1,-1):
            if grid[row][col+1] == grid[row][col]:
                grid[row][col+1] = grid[row][col+1] * 2   # since the values are equal, we can simply double the one value
                grid[row][col] = 0
        
        #during the addition process, we might have opened some new gaps, which need to be closed now
        #this can be done by re-using the code we used previously 
    for row in range (3,-1,-1):        
        for col in range (2,-1,-1):                 
            if grid[row][col+1] == ' ' or grid[row][col+1] == 0:
                grid[row][col+1] = grid[row][col]
                grid[row][col] = 0    
        
    return grid     #returns the grid to the program, for it to be printed and for the game to continue  