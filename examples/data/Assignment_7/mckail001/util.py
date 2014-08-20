"""Assignment 7 question 2
Ailsa Mackay MCKAIL001
2014-04-30"""

import copy

def create_grid(grid):
    #create a 4x4 grid
    for a in range(4):
        grid.append([" "]*4)
            

def print_grid(grid):
    #print out a 4x4 grid in 5-width columns within a box
    print("+--------------------+")
    for row in range(4):
        print("|",end="")
        for col in range(4):
            if grid[row][col]==0:
                print("{0:<5}".format(" "), end="")
            else:
                print("{0<5}".format(grid[row][col]), end="")
        print("|")
    print("+--------------------+")    


def check_lost(grid):
    #first check that no spaces are empty
    find_space = 0
    for x1 in range(4):
        for y1 in range(4):
            if grid[x1][y1] == 0:
               find_space = -1
            break
    #check vertical adjacent numbers
    find_vertical = 0
    for x2 in range(3):
        for y2 in range(3):
            if grid[x2][y3] == grid[x2+1][y3]:
                find_vertical = -1
                break
    #check horizontal adjacent numbers
    find_horizontal = 0
    for x3 in range(3):
        for y3 in range(3):
            if grid[x3][y3] == grid[x3][y3+1]:
                find_horizontal == -1
                break
    if find_horizontal == -1 or find_vertical == -1 or find_space == -1:
        return False
    else:
        return True

def check_won(grid):
    #return True if a value>=32 is found in the grid; otherwise False
    find_won = 0
    for x in range(4):
        for y in range(4):
            if grid[x][y]>=32:
                find_won = -1
                break
    if find_won == -1:
        return True
    else:
        return False
        
def copy_grid(grid):
    #"return a copy of the grid
    newgrid=copy.deepcopy(grid)
    return newgrid
            
def grid_equal(grid1,grid2):
    #check if 2 grids are equal - return boolean value
    if grid1 == grid2:
        return 2
    else:
        return False