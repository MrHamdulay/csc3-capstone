""" A module of merging functions for an assimilation of the 2048 game.
Author: Afika Nyati
Date: 1 May 2014"""


def push_up(grid): # Merges grid values upwards
    
    
    for x in range(4): # Loops through each row
        
        local_line = [] # Initializing a list used in the function to store manipulated data.
        
        for y in range(4): # Loops through each value in one row.
            local_line.append(grid[y][x]) # Notice that the values of the x and y indices have been inverted, so instead of the copying a row, a column is copied. This column is copied to the local list.
        
        pusher(local_line) # Inputs the local line copied from the original grid into the pusher function as an arguement to push the given line up.
        
        for value in range(4): # Loops through each value in the column.
            grid[value][x] = local_line[value] # The resulting numbers from the manipulated local line are coppied to the original grid.
            
    return grid # Grid is returned
        
        
    
    
def push_down(grid): # Merges grid values downwards
    
    
    for x in range(4): # Loops through each row
            
            local_line = [] # Initializing a list used in the function to store manipulated data.
            
            for y in range(3,-1,-1): # Loops through each value in one row. Notice that the numbers are looped in reverse. This is what changes the above function from push up to push down.
                local_line.append(grid[y][x]) # Notice that the values of the x and y indices have been inverted, so instead of the copying a row, a column is copied. This column is copied to the local list.
            
            pusher(local_line) # Inputs the local line copied from the original grid into the pusher function as an arguement to push the given line down.
            
            for value in range(3,-1,-1): # Loops through each value in the column. Notice that the numbers are looped in reverse. This is what changes the above function from push up to push down.
                grid[value][x] = local_line[3-value] # The resulting numbers from the manipulated local line are coppied to the original grid.
                
    return grid   # Grid is returned 
    

def push_left(grid): # Merges grid values left
    
    
    for x in range(4): # Loops through each row
                
        local_line = [] # Initializing a list used in the function to store manipulated data.
                
        for y in range(4): # Loops through each value in one row.
            local_line.append(grid[x][y]) # Notice that the values of the x and y indices now aren't inverted, this copies a row as it originally is. This row is copied to the local list.
                
        pusher(local_line) # Inputs the local line copied from the original grid into the pusher function as an arguement to push the given line to the left.
                
        for value in range(4): # Loops through each value in the column.
            grid[x][value] = local_line[value] # The resulting numbers from the manipulated local line are coppied to the original grid.
                    
    return grid  # Grid is returned      
    
    
def push_right(grid): # Merges grid values right
    
    
    for x in range(4): # Loops through each row
                    
            local_line = [] # Initializing a list used in the function to store manipulated data.
                    
            for y in range(3,-1,-1): # Loops through each value in one row. Notice that the numbers are looped in reverse. This is what changes the above function from push left to push right.
                local_line.append(grid[x][y]) # Notice that the values of the x and y indices aren't inverted, this copies a row as it originally is. This row is copied to the local list.
                    
            pusher(local_line) # Inputs the local line copied from the original grid into the pusher function as an arguement to push the given line right.
                    
            for value in range(3,-1,-1): # Loops through each value in the column. Notice that the numbers are looped in reverse. This is what changes the above function from push left to push right.
                grid[x][value] = local_line[3-value] # The resulting numbers from the manipulated local line are coppied to the original grid.
                        
    return grid   # Grid is returned     
    
    
def pusher(line): # Pushes a given arguement to the left and adds the first adjacent pair only. i.e. If there are three adjacent twos, it only adds the first two.
    
    # This part pushes the values in a line to the left
    
    for repeat in range(3): # The process of pushing has to be done three times because after moving to the left once, there still could be open spaces.
        
            for value in range(3): # This loops through only the first three numbers because there is no number on the right adjacent of the fourth number.
                
                if (line[value] == 0): # If the given value in the line is equal to zero.
                    line[value] = line[value +1] # The number right adjacent to the given number takes the place of the given number.
                    line[value +1] = 0 # The adjacent number becomes and open space (represented by 0).
                    
    for value in range (3): # This loops through only the first three numbers because there is no number on the right adjacent of the fourth number.
        
        if (line[value] == line[value +1]): # If the right adjacent number of the given value is equal to the given value.
            line[value] *= 2 # Add the two numbers together, which is effectively multipltying the given value by two.
            line[value +1] = 0 # The right adjacent number becomes and open space (represented by 0).
            break # This break statement stops the addition of more than one adjacent pair in the line, which is a feature of the 2048 game.
    
    
    
    # This part pushes the values in a line to the left again, because after the addition of adjacent numbers, there would be empty places again.   
        
    for repeat in range (3): # The process of pushing has to be done three times because after moving to the left once, there still could be open spaces.
            
        for value in range(3): # This loops through only the first three numbers because there is no number on the right adjacent of the fourth number.
                
            if (line[value]==0): # If the given value in the line is equal to zero.
                line[value] = line[value +1] # The number right adjacent to the given number takes the place of the given number.
                line[value +1] = 0  # The adjacent number becomes and open space (represented by 0).