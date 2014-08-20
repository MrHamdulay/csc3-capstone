"""Functions to create, print, check won, check lost and check equal for grids for 2048 game
joshua gullan
3/5/2014"""
import copy    

def create_grid(grid):
    grid=grid
    height=4   
    for i in range(height):     #creates a grid of zeros
        grid.append([0,0,0,0])
    return grid

def print_grid(grid):
    height=4
    print("+","-"*20,"+", sep="", end="")
    print()
    for i in range(height):
        print("|", sep="", end="")
        for j in range(4):
            num = grid[i][j]
            if num==0:
                num = ""
            print(num, " " * (5-len(str(num))), sep = "", end="")  #ensures formatting is correct and prints grid
        print("|", sep="")
       
    print("+","-"*20,"+", sep="")

def check_lost (grid):
    if 0 in grid:      #if there's a 0, then return false
        return False
    for row in range(4):                  
        for col in range(4):
            if row!=3:
                if grid[row][col]==grid[row+1][col]:   #if there are available values that can merge, return false
                    return False
            if col!=3:
                if grid[row][col]==grid[row][col+1]:   #if there are available values that can merge, return false
                    return False
    else:
        return True

def check_won(grid):
    for i in range(4):
            for j in range(4):  
                num = grid[i][j]
                if grid[i][j]>=32:   #check for value equal to or higher than 32 
                    return True
    return False

def copy_grid(grid):
    return copy.deepcopy(grid)    #returns deepcopy of grid
  
def grid_equal(grid1, grid2):
    if grid1==grid2:     #checks if grids are equal
        return True
    else: return False
    