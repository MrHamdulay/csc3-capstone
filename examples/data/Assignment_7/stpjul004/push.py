""" A module to push and merge values in the grid 
 Author: Julius Stopforth (STPJUL004)
 Date: 2014-04-29 """

def push_up(grid):
    """ Push up then merge each column seperately """
    # Push
    for col in range(len(grid[0])):# Iterate through each column
        pushing = True #sentinel created
        start = 0 #initialize start and index points
        i = start
        while pushing:
            if i+1 <= len(grid): # check if index will be within bounds
                if grid[i][col] == 0: # skip over if index contains '0'
                    i += 1
                else: # if the value at index is non-zero
                    grid[i][col],grid[start][col] = grid[start][col],grid[i][col] 
                    # Swap start and index values
                    start += 1 #move the start point
                    i = start #reset the index point
            else:
                pushing = False # Stop pushing when out of bounds
    # Merge
    # Go through every value in the list
    for col in range(len(grid[0])):
        for i in range(len(grid)):
            #Check if there is a value below the current one
            if i+1 < len(grid): 
                #if the values are the same, add them then clear the bottom value's place, if the value is 0 swap places with the value below it 
                if grid[i][col] == grid[i+1][col] or grid[i][col] == 0:
                    #Swap and add values
                    grid[i][col] += grid[i+1][col]
                    grid[i+1][col] = 0
                    
def push_down(grid):
    """ Push down then merge each column seperately """
    # Push
    for col in range(len(grid[0])):# Iterate through each column
        pushing = True #sentinel created
        start = len(grid)-1 #initialize start and index points
        i = start
        while pushing:
            if i >= 0: # check if index will be within bounds
                if grid[i][col] == 0: # skip over if index contains '0'
                    i -= 1
                else: # if the value at index is non-zero
                    grid[i][col],grid[start][col] = grid[start][col],grid[i][col] 
                    # Swap start and index values
                    start -= 1 #move the start point
                    i = start #reset the index point
            else:
                pushing = False # Stop pushing when out of bounds
    # Merge
    # Go through every value in the list
    for col in range(len(grid[0])):
        for i in range(len(grid)-1,0,-1):
            #Check if there is a value below the current one
            if i-1 >= 0: 
                #if the values are the same, add them then clear the bottom value's place, if the value is 0 swap places with the value below it 
                if grid[i][col] == grid[i-1][col] or grid[i][col] == 0:
                    #Swap and add values
                    grid[i][col] += grid[i-1][col]
                    grid[i-1][col] = 0    
                    
def push_left(grid):
    """ Push left then merge each row seperately """
    # Push
    for row in range(len(grid)):# Iterate throught each row
        pushing = True #sentinel created
        start = 0 #initialize start and index points
        i = start
        while pushing:
            if i+1 <= len(grid[row]): # check if index will be within bounds
                if grid[row][i] == 0: # skip over if index contains '0'
                    i += 1
                else: # if the value at index is non-zero
                    grid[row][i],grid[row][start] = grid[row][start],grid[row][i] 
                    # Swap start and index values
                    start += 1 #move the start point
                    i = start #reset the index point
            else:
                pushing = False # Stop pushing when out of bounds
    # Merge
    # Go through every value in the list
    for row in range(len(grid)):
        for i in range(len(grid[row])):
            #Check if there is a value to the left of the current one
            if i+1 < len(grid): 
                #if the values are the same, add them then clear the left value's place, if the value is 0 swap places with the value to the left of it 
                if grid[row][i] == grid[row][i+1] or grid[row][i] == 0:
                    #Swap and add values
                    grid[row][i] += grid[row][i+1]
                    grid[row][i+1] = 0
                    
def push_right(grid):
    """ Push right then merge each row seperately """
    # Push
    for row in range(len(grid)):# Iterate through each row
        pushing = True #sentinel created
        start = len(grid[row])-1 #initialize start and index points
        i = start
        while pushing:
            if i > -1: # check if index will be within bounds
                if grid[row][i] == 0: # skip over if index contains '0'
                    i -= 1
                else: # if the value at index is non-zero
                    grid[row][i],grid[row][start] = grid[row][start],grid[row][i] 
                    # Swap start and index values
                    start -= 1 #move the start point
                    i = start #reset the index point
            else:
                pushing = False # Stop pushing when out of bounds
    # Merge
    # Go through every value in the list
    for row in range(len(grid[0])):
        for i in range(len(grid)-1,0,-1):
            #Check if there is a value to the right of the current one
            if i-1 >= 0: 
                #if the values are the same, add them then clear the right value's place, if the value is 0 swap places with the value to the right of it 
                if grid[row][i] == grid[row][i-1] or grid[row][i] == 0:
                    #Swap and add values
                    grid[row][i] += grid[row][i-1]
                    grid[row][i-1] = 0