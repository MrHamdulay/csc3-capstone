''' Assignment 7, question 3 (extended)
This is a module of functions to be used in push.py
Tristan Subroyen
30 April 2014 '''

def shiftSpaceUp (i, grid):
    ''' If a value above a non-zero value is zero, shift the non-zero value up '''
    for j in range (1,4): # iterate through rows...
        value = grid[j][i] # store a value
        if value != 0: # if the value is non-zero...
            # move the value into a new space above
            for j2 in range (0,j):
                newVal = grid[j2][i]
                if newVal == 0:
                    grid[j][i] = 0
                    grid[j2][i] = value
                    break
                
def shiftSpaceDown (i, grid):
    ''' If a value below a non-zero value is zero, shift the vaue downwards '''
    for j in range (2, -1, -1):
        value = grid[j][i]
        if value != 0:
            for j2 in range (3, j, -1):
                value2 = grid[j2][i]
                if value2 == 0:
                    grid[i][j] = 0
                    grid[j2][i] = value
                    break

def shiftSpaceRight (j, grid):
    ''' If a value to the right of a non-zero value is zero, shift the non-zero value into that space '''
    for i in range (2, -1, -1):
        value = grid[j][i]
        if value != 0:
            for i2 in range (3, i, -1):
                value2 = grid[j][i2]
                if value2 == 0:
                    grid[j][i] = 0
                    grid[j][i2] = value
                    break

def shiftSpaceLeft (j, grid):
    ''' If a value to the left of a non-zero value is zero, shift the non-zero value into that space '''
    for i in range (1, 4):
        value = grid[j][i]
        if value != 0:
            for i2 in range (0, i):
                value2 = grid[j][i2]
                if value2 == 0:
                    grid[j][i] = 0
                    grid[j][i2] = value
                    break
                
def mergeValUp (i , grid):
    ''' If a non-zero value is below an equal value, merge the two (and add) '''
    for j in range (3):
        value = grid[j][i]
        value2 = grid[j+1][i]
        if value == value2:
            grid[j][i] = value*2
            grid[j+1][i] = 0

def mergeValDown (i, grid):
    ''' If a non-zero value is above an equal value, merge the two (and add) '''
    for j in range (3, 0, -1):
        value = grid[j][i]
        value2 = grid[j-1][i]
        if value == value2:
            grid[j][i] = value*2
            grid[j-1][i] = 0
            
def mergeValRight (j, grid):
    ''' If a non-zero value is to the left of an equal value, merge the two (and add) '''
    for i in range (3, 0, -1):
        value = grid[j][i]
        value2 = grid[j][i-1]
        if value == value2:
            grid[j][i] = value*2
            grid[j][i-1] = 0

def mergeValLeft (j, grid):
    ''' If a non-zero value is to the right of an equal value, merge the two (and add) '''
    for i in range (3):
        value = grid[j][i]
        value2 = grid[j][i+1]
        if value == value2:
            grid[j][i] = value*2
            grid[j][i+1] = 0