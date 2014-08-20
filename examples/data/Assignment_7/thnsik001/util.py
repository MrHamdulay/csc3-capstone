"""Sikhulile Thenjwayo
Assignment 7 q2
01/05/2014"""

grid =[]
def create_grid(grid):
    #create a 4x4 grid
    for i in range (4):
        grid.append ([0] * 4)
    return grid

def print_grid(grid):
    #print out a 4x4 grid in 5-width columns within a box
    print("+--------------------+")
    for row in range (4):
        print("|",end="")
        for col in range (4): 
            if grid[row][col] == 0:
                print(" ",end=" "*(5-(len(str(grid[row][col])))))
            else:
                print (grid[row][col],end=" "*(5-(len(str(grid[row][col])))))
        print ("|")  
    print("+--------------------+")
        
        
def check_lost(grid):
    #return True if there are no 0 values and no adjacent values that are equal; otherwise False
    check = True
    for row in range(4):
        for col in range(4): #try column
            if grid[row][col]==0:
                check = False
                
    if check == True:        
        for row in range (4):
            for col in range (3):  
                if grid[row][col]==grid[row][col+1]:
                    check = False
                    
        for row in range (3):
            for col in range (4):  
                if grid[row][col]==grid[row+1][col]:
                    check = False    
    return check

def check_won(grid):
    #return True if a value>=32 is found in the grid; otherwise False
    for row in range (4):
            for col in range (4):     
                if grid[row][col] >=32:
                    return True
    return False

def copy_grid(grid):
    #return a copy of the grid
    copy = []
    for i in range (4):
            copy.append ([0] * 4) 
            
    for row in range (4):
        for col in range (4): 
            copy[row][col] = grid[row][col]
    return copy

def grid_equal(grid1,grid2):
    #check if 2 grids are equal - return boolean value
    equal = True
    for row in range (4):
            for col in range (4):   
                if grid1[row][col]!=grid2[row][col]:
                    equal = False
    return equal