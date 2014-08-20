'''module for question 2
nicole henning
due 2 may 2014'''

import copy

def create_grid(grid):
    #create a 4x4 grid
    for i in range (4):
        grid.append([0] *4)


def print_grid (grid):
    #print out a 4x4 grid in 5-width columns within a box

    print("+","-"*20,"+",sep="") #for top border of box
    
    for row in range (4):
        print("|", end="") # left border of box
        for col in range (4):
            if grid[row][col] == 0:
                print ("{0:<5}".format(" "),end="") #if 0 must print empty string
            else: 
                print ("{0:<5}".format(grid[row][col]),end="") #for width of 5
        print("|") #right border of box
        
    print("+","-"*20,"+",sep="") #for bottom border of box


def check_lost (grid):
    #return True if there are no 0 values and no adjacent values that are equal; otherwise False
   
    #if grid[][] equals one to right or one to left return false
    #if grid[][] equals one above or one below return false
    #if grid[][] is 0 return false
    for row in range(4):
        for col in range(3):
            if grid[row][col]==grid[row][col+1]:
                return False #ie game is not lost, can carry on
            
    for row in range(3):
        for col in range(4):
            if grid[row][col]==grid[row+1][col]:
                return False
            
    for row in range(4):
        for col in grid[row]:
            if col == 0:
                return False
    
    #if none of the above are present, game is lost
    return True
              

grid = [[2048,4,0,0],[8,4,2,0],[4,2,0,2],[2,0,0,0]]
def check_won (grid):
    #return True if a value>=32 is found in the grid; otherwise False
    for row in range(4):
        if 32 in grid[row] or 64 in grid[row] or 128 in grid[row] or 256 in grid[row] or 512 in grid[row] or 1024 in grid[row] or 2048 in grid[row] :
            return True
    return False
    

def copy_grid (grid):
    #return a copy of the grid
    copy_list = copy.deepcopy(grid) 
    #use deepcopy so that copy_list is comletely seperate
    #(ie when changing a figure in grid it will not change in copy_list)
        
    return copy_list



def grid_equal (grid1, grid2):
    #check if 2 grids are equal - return boolean value
    if grid1==grid2:
        return True
    else:
        return False
