#program to manipulate 2-dimensional arrays of size 4x4
#KNNSAD001
#Assignment 7

#import function
import copy

#creating a 4x4 grid :

def create_grid(grid):
    for i in range (4):
        grid.append ([0]*4)
    return grid

#function to print out a 4x4 grid in 5-width columns within a box :

def print_grid (grid):
    print("+","-"*20,"+",sep="")
    for i in grid:
        print('|', end='')
        for j in i:
            j = str(j)
            if j == '0':
                print(' '.ljust(5), end = '')
            else:
                print(j.ljust(5),end = '')
        print('|')
    print("+","-"*20,"+",sep="")
    
    
#determine whether there are no 0 values and no adjascent values are equal; otherwise False :

def check_lost (grid):
    for i in range(len(grid)-1):
        for j in range(len(grid[i])-1):
            if grid[i][j] == 0:
                return False
            elif grid[i][j] == grid[i][j+1]:
                return False
            elif grid[i][j] == grid[i+1][j]:
                return False            
    return True


#function to test whether there is a value=32 or value>32 to determine winner :

def check_won (grid):
    for i in range(4):
            for j in range(4):
                if grid[i][j]>= 32:
                    return True
    return False

#function to return a copy of the grid :

def copy_grid (grid):
    gridcopy = copy.deepcopy(grid)
    return gridcopy


#function to check whether 2 grids are equal - returns Boolean value :

def grid_equal (grid1, grid2):
    if grid1==grid2:
        return True
    else:
        return False