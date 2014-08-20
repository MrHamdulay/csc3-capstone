"""Tejasvin Bagirathi BGRTEJ001
Assignment 7, Question 2
push.py"""

import util

def push_up(grid):
    """Function to merge grid values upwards."""
    #Temporarily store grid values from each column in column
    for x in range(4):
        #Column to temporarily stpre values
        column = []
        #Loop through to add vertical columns to column
        for y in range(4):
            column.append(grid[y][x])
        #Remove all zeroes before significant numbers. "av" is an accumulator, this allows for
        #deleting zeroes
            av = 0
        #Loop through column, delete zeros and add zero to end
        for num in range(3):
            #If there is a zero, delete the zero, which shifts everything forward
            if column[num-av] == 0:
                del column[num-av]
                #Add zero to end
                column.append(0)
                av += 1
        #Loop from top to bottom in the grid, add any equal adjacent numbers and store the sum in the
        #higher number of the two blocks
        for num in range(3):
            #Check to see if adjacent values are equal
            if column[num] == column[num+1]:
                #If equal, add numbers together
                column[num] = column[num]+column[num+1]
                #Delete lower value and replace with zero 
                del column[num+1]
                column.append(0)
        #Put each new column into the original grid
        for y in range(4):
            grid[y][x] = column[y]
            
def push_down(grid):
    """Function to merge grid values downwards."""
    #Similar code to push_up(grid), except use the reverse list function. Therfore zeroes are
    #removed and blocks added from bottom to top
    for x in range(4):
        #Column to temporarily stpre values
        column = []
        #Loop through to add vertical columns to column
        for y in range(4):
            #Add values to temporary array
            column.append(grid[y][x])
            #Remove all zeroes before significant numbers, "av" is an accumulator, this allows for
            #deleting zeroes            
            av = 0
        column.reverse()
        #Loop through column, delete zeros and add zero to end
        for num in range(3):
            #If there is a zero, delete the zero, which shifts everything forward 
            if column[num-av] == 0:
                del column[num-av]
                #Add zero to end
                column.append(0)
                av += 1
        #Loop from bottom to top in the grid, add any equal adjacent numbers and store the sum in the
        #higher number of the two blocks
        for num in range(3):
            #Check to see if adjacent values are equal
            if column[num] == column[num+1]:
                #If equal, add numbers
                column[num] = column[num]+column[num+1]
                #Delete adjacent number
                del column[num+1]
                #Add zero to replace number
                column.append(0)
        #Reverse column
        column.reverse()
        #Put each new column into the original grid
        for y in range(4):
            grid[y][x] = column[y]

def push_left(grid):
    """Function to merge grid values left."""
    #Blocks are stored in temporary row variable, then added right to left   
    #Loop through grid
    for i in range(4):
        #Temporary row to store values from each row in the grid
        row = []
        for j in range(4):
            #Add each row in orginal grid to row
            row.append(grid[i][j])
            av = 0
        #Loop through column, delete zeros and add zero to end
        for num in range(3):
            #If there is a zero, delete the zero, which shifts everything forward 
            if row[num-av] == 0:
                del row[num-av]
                #Add zero to end
                row.append(0)
                av += 1
        #If any adjacent values are the same, add them together
        for num in range(3):
            #If value and adjacent value are the same, add the values
            if row[num] == row[num+1]:
                row[num] = row[num]+row[num+1]
                #Delete adjacent value
                del row[num+1]
                #Replace deleted number with 0
                row.append(0)
        #Add row to orginal grid 
        for h in range(4):
            grid[i][h] = row[h]
            
def push_right(grid):
    """Function to merge grid values right."""
    #Similar code to push_left(grid), except use the reverse list function. Therfore zeroes are
    #removed and blocks added from left to right    
    for y in range(4):
        row = []
        #loop through row
        for x in range(4):
            #Add each row from grid into row
            row.append(grid[y][x])
            av = 0
        row.reverse()
        #Loop through column, delete zeros and add zero to end
        for num in range(3):
            #If there is a zero, delete the zero, which shifts everything forward 
            if row[num-av] == 0:
                del row[num-av]
                #Add zero to end
                row.append(0)
                av += 1
        #If any adjacent values are the same, add them together
        for num in range(3):
            #If value and adjacent value are the same, add the values
            if row[num] == row[num+1]:
                #Add values, then replace number with vlaue which was calculated 
                row[num] = row[num]+row[num+1]
                #Delete added value whcih has been added
                del row[num+1]
                #Replace with zero
                row.append(0)
            #Revverse the row
        row.reverse()
        #Add row to orginal grid
        for x in range(4):
            grid[y][x] = row[x]   