#Riya Desai
#Util
#2 May 2014

global grid
grid = []

def create_grid(grid):
    #program to create a 4x4 grid
    for y in range(4):
        row = []
        
        for x in range(4):
            row.append(0)
        grid.append(row)
        
def print_grid(grid):
    #Program to print out a 4x4 grid - in columns of width 5 inside a box
    print("+",20*"-","+",sep="")
    
    for i in range(4):
        print("|",end="")
        
        for num in grid[i]:
            if num == 0:
                print("{0:<5}".format(" "), end="")
            
            else:
                print("{0:<5}".format(num), end="")
        print("|")
    print("+",20*"-","+",sep="")
    
def check_lost(grid):
    #Program to check if game is lost
    #Will return "True" if there are no zero values and no adjacent values that are equal
    #Will return "False" otherise
    
    for i in range(4):
        #Look for zero values in grid and return false if these zero values are found

        for num in range(4):
            if grid[i][num] == 0:
                return False
        #Look for values that are adjacent horizontally and return "False" if found
        
        for num in range(3):
            if grid[i][num] == grid[i][num+1]:
                return False
    
    #Look for values that are adjacent vertically and return "False" if found
    for i in range(3):
        for num in range(4):
            if grid[i][num] == grid[i+1][num]:
                return False
            
    #Return "True" if none of the above conditions are met
    return True

def check_won(grid):
    #Program to determine if game is won. Returns True if a value >= 32 is found on the grid. Otherwise returns False
    #Loop through all elements in grid and return True if any values equal or greater than 32 are found 
    
    for i in grid:
        for a in i:
            if a >= 32:
                return True
    return False

def copy_grid(grid):
    
    #Program that returns a copy of the grid
    #Define the new grid
    
    new_grid = []
    
    #Loop through elements of the original grid and append to the new grid
    
    for i in grid:
        new_row = []
       
        for a in i:
            new_row.append(a)
        new_grid.append(new_row)
    
    #Return the copy
    return new_grid

def grid_equal(grid1, grid2):
    #Program to determine if two supplied grids are equal
    #Loop through all the values in each grid
    
    for i in range(4):
        for num in range(4):
            
            #If any corresponding values in the two grids do not match, return False
            if grid1[i][num] != grid2[i][num]:
                return False
   
    #Return True if no such values are found.
    return True