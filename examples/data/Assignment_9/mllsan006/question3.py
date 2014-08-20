#a program to check if a complete Sudoku grid is valid or not
#sankara mallane
#12 may 2014

# function to check the row 
def checkRow(theGrid,n):
    
    Check = {} #empty dictionary
    for theNumber in theGrid[n]: # the for loop checks the ith row of the grid
        if not theCheck(theNumber, Check):
            return False # returns false if it is not valid
    return True # returns true if it is valid

# function to check the column
def checkColumn(theGrid,n):
    Check = {}
    for y in range(len(theGrid)): # the for loop checks the ith column of the grid
        if not theCheck(theGrid[y][n], Check):
            return False # returns false if it is not valid
    return True # returns true if it is valid

# check function
def theCheck(theNumber, Check):
    if theNumber in Check: return False # returns false if the number is not seen by checker
    if not 1 <= theNumber <= 9: return False #returns false if the number lies out of the range between 1 to 9
    Check[theNumber] = True #records in checker 
    return True #returns true   

# function to check the part of grid
def checkRegion(theGrid,x,y): # denoted by x and y referencing the position 0,0 as the top left hand part of the grid
    
    Check = {} # empty dictionary
    theTop = (y * 3) # the left part of the grid
    theBottom = (theTop + 2) # the bottom part of the grid
    theLeft = (x * 3) # the left part of the grid
    theRight = (theLeft + 2) # the right part of the grid
    
    for y in range(theTop, theBottom + 1): # for loop for the coordinates which are part of the grid
        for x in range(theLeft, theRight + 1):
            if not theCheck(theGrid[y][x], Check):
                return False # return false if it is not valid
    return True # return true if it is valid

# check functon
def checkGrid(theGrid): # combines all the above check funtions into one single function
    
    for y in range(len(theGrid)): # for loop to check through all the rows in the grid
        if not checkRow(theGrid,y):
            return False # return false if it is not valid
        
    for x in range(len(theGrid)): # for loop to check through all the columns in the grid
        if not checkColumn(theGrid,x):
            return False # return false if it is not valid
        
    for y in range(0,3): # for loop to check through all the regions in the grid
        for x in range(0,3):
            if not checkRegion(theGrid,x,y):
                #print('reg fail at',x,y)
                return False
    return True # return true when all the checks are passed
                # then the grid is valid

theGrid = [] # empty list
for i in range(9): # for loop to get the grid from user
    line = input() # the input from the user
    theRow = [] # empty list
    for character in line:
        theRow.append(eval(character)) # append integer to row
    theGrid.append(theRow) # then append that row to the grid

if checkGrid(theGrid):
    print('Sudoku grid is valid') # print when the complete Sudoku grid is valid 
else:
    print('Sudoku grid is not valid') # prnt when the complete Sudoku grid is not valid 