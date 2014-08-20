#Assignment 7, Question 2
#James Nevin
#01/05/2014

import copy
def create_grid(grid): #Create grid
    for x in range (0, 4):
        grid.append([0]*4) #Add list of 4 elements 4 times
    return grid

def print_grid(grid): #Print grid
    print ("+--------------------+") #Border
    for x in range (0, 4):
        print ("|", end = "") #Side
        for y in range (0, 4): #Going through list
            if (grid[x][y] == 0): #Only spaces if 0
                print ("     ", end = "")
            else: #Print number and spaces less length number
                print (str(grid[x][y]) + (5-len(str(grid[x][y])))*" ", end = "")
        print("|") #Side
    print ("+--------------------+") #Border

def check_lost(grid): #Check lost
    lost = True #Assuming true
    for x in range (0, 3):
        for y in range (0, 3):
            if (grid[x][y] == 0): #Not lost if is 0
                lost = False
                break
            elif (grid[x][y+1] == grid[x][y]): #If adjacent are equal, not lost
                lost = False
                break
            elif (grid[x+1][y] == grid[x][y]):
                lost = False
                break
    for y in range (0, 3): #Checking end row and column as above
        if (grid[3][y] == 0 or grid[3][y] == grid[3][y+1]):
            lost = False
            break
    for x in range (0, 3):
        if (grid[x][3] == 0 or grid[x][3] == grid[x+1][3]):
            lost = False
            break
    if grid[3][3] == 0: #Checking bottom corner
        lost = False
    return lost #Return result

def check_won(grid):
    won = False #Assume false
    for x in range (0, 4):
        for y in range (0, 4): #Going through grid
            if (grid[x][y] >= 32): #If found
                won = True
                break
    return won #Return result

def copy_grid (grid): #Copying grid
    return copy.deepcopy(grid) #Doing a deepcopy

def grid_equal(grid1, grid2): #Checking equal
    isEqual = True #Assume true
    for x in range (0, 4):
        for y in range (0, 4):
            if (grid1[x][y] != grid2[x][y]): #If any values not equal
                isEqual = False
                break
    return isEqual #Return result