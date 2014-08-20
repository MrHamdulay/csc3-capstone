#Program of grid modules
#Kayla Hendricks
#30 April 2014

def create_grid(grid):
    for i in range(4):              #making list happen 4 times
        grid.append([0]*4)         #adding number "0" 4 times in a list
        
def print_grid(grid):
    #print 2d array
    print("+","-"*20,"+",sep="")
    for row in range(4):
        print("|",end="")
        for col in range(4):
            if grid[row][col]!=0:
                #print number, left-adjusted, in a width of 5
                print("{0:<5}".format(grid[row][col]),end="")
            else:
                #if number in grid position = 0, print an empty string
                print("{0:<5}".format(""),end="")
        print("|")
    print("+","-"*20,"+",sep="")
    
def check_lost(grid):
    ans=""
    for row in range(4):
        for col in range(4):
            if grid[row][col]==0:
                ans="yes"
        
    #check if numbers next to one another are equal
    for row in range(4):
        for col in range(3):
            if grid[row][col] == grid[row][col+1]:
                ans="yes"
        
    
    #check if numbers above or below are equal
    for row in range(3):
        for col in range(4):
            if grid[row][col] == grid[row+1][col]:
                ans="yes"

        
    if ans=="yes":
        return False
    else:
        return True
        
        
def check_won(grid):            #works
    ans=""
    for row in range(4):
        for col in range(4):
            if grid[row][col]>=32:
                ans="yes"
    if ans=="yes":
        return True
    else:
        return False

import copy
def copy_grid(grid):
    #save copy of grid as x
    x=copy.deepcopy(grid)
    return x

def grid_equal(grid1,grid2):
    if grid1==grid2:
        return True
    else:
        return False
    
        

    
        
        
        
        
    
            
                 
    