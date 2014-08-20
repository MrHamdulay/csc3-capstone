# Matthew Finlayson - FNLMAT001
# Assignment 7 question 3
# 01/05/14

def get_column(grid, colNum):
    """takes in the grid and the required column index as parameters and returns a list of the column"""
    column = []
    for i in range(4):
        column.append(grid[i][colNum])
    return column

def shift_left(column):
    """removes all zeros from an array and adds them to the end"""
    while 0 in column:
        column.remove(0)
    for i in range (4-len(column)):
        column.append(0) 
    return column  

def shift_right(column):
    """removes all zeros from an array and adds them to the front"""
    while 0 in column:
        column.remove(0)
    for i in range (4-len(column)):
        column.insert(0,0)
    return column

def push_up (grid):
    """merge grid values upwards"""
    for colNum in range (4): # iterates through the columns in the grid
        
        column = get_column(grid, colNum) # gets the column specified by colNum
        
        column = shift_left(column) # shifts all the values of that column to the left
        
        for i in range (3): # adds up adjacent items if they are the same
            if column[i] == column[i+1]:
                column[i] = 2*column[i]
                column[i+1] = 0
                column = shift_left(column)
                
        for row in range(4): # replaces the values in the grid with the new column values
            for col in range (4):
                if (col == colNum):
                    grid[row][col] = column[row]
            
def push_down(grid):
    """merge grid values downwards"""
    for colNum in range(4): # iterates through the columns in the grid
        
        column = get_column(grid, colNum) # gets the column specified by colNum
        
        column = shift_right(column) # shifts all the values of that column to the right
    
        for i in range (1,4): # adds up adjacent items if they are the same
            if column[i-1] == column[i]:
                column[i-1] = 2*column[i]
                column[i] = 0
        column = shift_right(column)        
            
        for row in range(4): # replaces the values in the grid with the new column values
            for col in range (4):
                if (col == colNum):
                    grid[row][col] = column[row]        

def push_left(grid):
    """merge grid values left"""
    for rowNum in range (4): # iterates through each row in the grid
        
        row = grid[rowNum] # gets the current row
        
        row = shift_left(row) # shifts all the values to the left
        
        for i in range (3): # adds up adjacent items if they are the same
            if row[i] == row[i+1]:
                row[i] = 2*row[i]
                row[i+1] = 0
        row = shift_left(row)    
        
        grid[rowNum] = row # replaces the values in the grid with the new row values
    
def push_right(grid):
    """merge grid values right""" 
    for rowNum in range (4): # iterates through each row in the grid
        
        row = grid[rowNum]  # gets the current row
        
        row = shift_right(row) # shifts all the values to the right
        
        for i in range (1,4): # adds up adjacent items if they are the same
            if row[i] == row[i-1]:
                row[i-1] = 2*row[i]
                row[i] = 0
        row = shift_right(row)   
        
        grid[rowNum] = row

#grid = [[2,0,2,0],[0,4,0,8], [0,16,0,128], [2,2,2,2]]