'''Module for grid functions in question 2
Tinotenda Chemvura CHMTIN004
01 May 2014'''

from copy import deepcopy
#___________________________________Module Starts Here_______________________________________________________
def create_grid(grid):
    """create a 4x4 grid"""
    for i in range (4):
        grid.append([0,0,0,0])
#____________________________________________________________________________________________________________
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    form = "{0:<5}"                     #format for the column width of 5
    print("+--------------------+")
    for row in grid:                    #go through the four lists (rows)
        print("|",end = "")
        for column in row:              #go through the 4 contents of the current list(row)
            if column == 0:
                column = " "
                print(form.format(column),end = "")        #the print function for each content of the grid
            else:
                print(form.format(column),end = "")
        print("|")        
    print("+--------------------+")
#____________________________________________________________________________________________________________
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    switch = True
        #check if there is any value equal to zero, if so, return False immediately
    for row in grid:
        for column in row:
            if column == 0:
                return False
    #check is there are any adjacent elements that are equal in the rows    
    for row in grid:
        for i in range(1,3):
            #if the current element == to the element next to it, return True
            if row[i] == row[i+1]: 
                return False
    #check if there are any equal adjacent equal elemnts in the columns
    for column in range(0,4):
        for row in range(0,3):
            #check is the current item is equal to the adjacent item in the next column to the right           
            if grid[row][column] == grid[row+1][column]:
                return False                  
    return switch
#____________________________________________________________________________________________________________
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    #check if any of the values is greater than or equal to 32, if so return True immediately else return false after the whole loop
    for row in grid:
            for column in row:
                if column >= 32:
                    return True
    return False
#____________________________________________________________________________________________________________
def copy_grid (grid):
   """return a copy of the grid"""
   return deepcopy(grid)
#____________________________________________________________________________________________________________
def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    switch = True
    for i in range(0,4):
        for j in range(0,4):
            if grid1[i][j] != grid2[i][j]:
                return False
    return switch
#_______________________________________End of module________________________________________________________