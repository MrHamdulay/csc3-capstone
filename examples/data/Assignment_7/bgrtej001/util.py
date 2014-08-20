"""Tejasvin Bagirathi BGRTEJ001
Assignment 7, Question 2
util.py"""

global grid
grid = []

#Create grid function to make empty grid
def create_grid(grid):
    for i in range(4):
        #Create new row
        row_x = []
        for j in range(4):
            #Add zero's to row
            row_x.append(0)
        #Add row to grid
        grid.append(row_x)

def print_grid(grid):
    #Print top of box
    print('+', '-'*20, '+', sep = '')
    #Loop through grid vertically
    for i in range(len(grid)):
        print('|', end='')
        #Loop through each vertical element of grid 
        for j in grid[i]:
            #If 0, print empty spaces
            if j == 0:
                print('{0:<5}'.format(' '), end ='')
            #If number, print the number out
            else:
                print('{0:<5}'.format(j), end ='')
        print('|')
    print('+', '-'*20, '+', sep = '')
    
def check_lost(grid):
    for i in range(4):
        #Search for equal adjecent values
        for j in range(3):
            if grid[i][j] == grid[i][j+1]:
                return False
        #Search for 0 values in each horizontal element
        for j in range(3):
            if grid[i][j]==0:
                return False
    #Check if any horizontal adjacent elements are the same, first lop through vertically
    for i in range(3):
        #Loop through each horizontal element
        for j in range(4):
            #If any adjacent elements are the same, return false
            if grid[i][j] == grid[i+1][j]:
                return False    
    return True       
            
def check_won(grid):
    #Loop through grid veritcally
    for i in grid:
        #Loop through horizontal elements of grid
        for  j in i:
            #If any number is greater than 32, return true
            if j >= 32:
                return True
    return False

def copy_grid(grid):
    #Declare new grid
    grid_copy = []
    for i in grid:
        #Create new horizontal row
        new_row = []
        #Loop trhough each row in grid
        for j in i:
            #Add each element of the horizontal row to new row
            new_row.append(j)
        #Add new row to new grid
        grid_copy.append(new_row)
    #Return Copy
    return grid_copy

def grid_equal(grid1, grid2):
    for i in range(4):
        #Check to see if any values horizontally in grid don't match, if so return False
        for j in range(4):
            if grid1[i][j] != grid2[i][j]:
                return False
    return True