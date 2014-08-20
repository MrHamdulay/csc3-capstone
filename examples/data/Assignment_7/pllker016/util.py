#kereshnee pillay
#1 may 2014
#game grid

import copy

#create a grid
def create_grid(grid):
    for i in range (4):
        grid.append([0,0,0,0])
    
# print grid
def print_grid (grid):
    print("+--------------------+")
    for i in range(len(grid)):
        print("|", end = "")
        for j in range(len(grid)):
            if (grid[i][j] == 0):
                grid[i][j] = "" 
            print ("{0: <5}".format(grid[i][j]), end = "")
            if (grid[i][j] == ""):
                grid[i][j] = 0           
        print("|", end = "")
        print()
    print("+--------------------+")
    
#check for adjacent and 0 values
def check_lost (grid):
#number next to    
    lost = True
    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j+1]: 
                lost = False

#check number below
    for i in range(3):
        for j in range(4):
            if grid[i][j] == grid[i+1][j]:
                lost = False    
              
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                lost = False
            
    return lost
    
#check if grid equal 32    
def check_won (grid):
    won = False
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] >= 32: #check if any number in the grid is equal to 32
                won = True
    return won    

#copy the grid
def copy_grid(grid):
    return copy.deepcopy(grid) 

#check if two grids are equal
def grid_equal (grid1, grid2):
    if grid1 == grid2: 
        return True
    else:
        return False