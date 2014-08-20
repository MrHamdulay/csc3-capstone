"""Module of utility functions
Carla Wilby
27 April 2014"""

import copy
#create a 4x4 grid
def create_grid(grid):
    for i in range(4):
        grid.append([0,0,0,0])   
    return grid


#print out a 4x4 grid in 5-width columns within a box
def print_grid(grid):
    print("+","-"*20,"+",sep="")
    for y in range(4):
        print("|",end="")
        for x in range(4):
            a = grid[y][x]
            if a == 0:
                a = " "
            print("{0:<5}".format(a),end="")
        print("|")    
    print("+","-"*20,"+",sep="")


#return true if there are no 0 values and no adjacent values that are equal; otherwise false  
def check_lost(grid):   
    lost = False
    lost1 = True
    lost2 = True
    #test for zeroes
    for y in range(4):
        for x in range(4):
            if grid[y][x] ==  0:
                lost1 = False
                break
                                
    #test for equal adjacent values
    for y in range(3):
        for x in range(3):
            if (grid[y][x] == grid[y][x+1]) or (grid[y][x] == grid[y+1][x]):
                lost2 = False
                break
                
    if lost1 == True and lost2 == True:
        lost = True
                
    return lost

#return true if a value>=32 is found in the grid; otherwise false  
def check_won(grid):
    won = False
    for y in range(4):
        for x in range(4):
            if grid[y][x] >=32:
                won = True
    return won
  
    
#return a copy of the grid 
def copy_grid(grid):
    temp_grid = [[] for i in range(4)]
    for y in range(4):
        for x in range(4):
            temp_grid[y].append(grid[y][x])
    return temp_grid


#check if 2 grids are equal - return boolean value
def grid_equal(grid1,grid2):
    if grid1 == grid2:
        return True
    else:
        return False
    