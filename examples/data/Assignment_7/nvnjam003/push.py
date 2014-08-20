#Assignment 7, Question 3
#James Nevin   
#01/05/2014

def push_up(grid): #Push up
    alreadyEdited = [] #List of coordinates already changed
    for row in range (1, 4): #Start from second row from top
        for column in range (4): #Go through columns
            for x in range (row, 0, -1): #Go through rows between row and top
                isClear = True #If numbers inbetween
                for y in range (row-x+1, row):
                    if (grid[y][column] != 0): #There are numbers inbetween
                        isClear = False
                if (grid[row-x][column] == grid[row][column] and isClear and [row-x, column] not in alreadyEdited and grid[row][column] != 0): #If rows are equal and nothing inbetween and not changed
                    grid[row-x][column] = 2*grid[row][column]
                    grid[row][column] = 0
                    alreadyEdited.append([row - x, column]) #Add to edited list
                if (grid[row-x][column] == 0 and grid[row][column] != 0): #If row is zero
                    grid[row-x][column] = grid[row][column]
                    grid[row][column] = 0
                    
def push_down(grid): #Push down
    alreadyEdited = []
    for row in range (3, -1, -1): #Start from bottom
        for column in range (4): #Same as push up, just going from bottom
            for x in range (1, row+1):
                isClear = True
                for y in range (row-x+1, row):
                    if (grid[y][column] != 0):
                        isClear = False                
                if (grid[row-x][column] == grid[row][column] and isClear and [row, column] not in alreadyEdited and grid[row][column] != 0):
                    grid[row][column] = 2*grid[row][column]
                    grid[row-x][column] = 0
                    alreadyEdited.append([row, column])
                if (grid[row][column] == 0 and grid[row-x][column] != 0):
                    grid[row][column] = grid[row-x][column]
                    grid[row-x][column] = 0

def push_left(grid): #Push left
    alreadyEdited = [] #List of coordinates already changed
    for row in range (4):
        for column in range (1, 4): #Start from second from left
            for x in range (column, 0, -1): #Going through columns
                isClear = True 
                for y in range (column-x+1, column): #Checking if numbers between
                    if (grid[row][y] != 0):
                        isClear = False                 
                if (grid[row][column-x] == grid[row][column] and isClear and [row, column - x] not in alreadyEdited and grid[row][column] != 0): #If columns equal and no numbers between and not yet changed
                    grid[row][column-x] = 2*grid[row][column]
                    grid[row][column] = 0 #Add to list of changed
                    alreadyEdited.append([row, column-x])
                if (grid[row][column-x] == 0 and grid[row][column] != 0): #If empty column
                    grid[row][column-x] = grid[row][column]
                    grid[row][column] = 0

def push_right(grid): #Push right
    alreadyEdited = []
    for row in range (4):
        for column in range (3, -1, -1): #Start from right
            for x in range (1, column+1): #Same as left, just going from right
                isClear = True
                for y in range (column-x+1, column):
                    if (grid[row][y] != 0):
                        isClear = False                 
                if (grid[row][column-x] == grid[row][column] and isClear and [row, column] not in alreadyEdited and grid[row][column] != 0):
                    grid[row][column] = 2*grid[row][column]
                    grid[row][column-x] = 0
                    alreadyEdited.append([row, column])
                if (grid[row][column] == 0 and grid[row][column-x] != 0):
                    grid[row][column] = grid[row][column-x]
                    grid[row][column-x] = 0