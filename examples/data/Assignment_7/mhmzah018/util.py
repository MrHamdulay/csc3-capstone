"""Assignment 7 - question 2
Zaheer Mahmood
29 - 04 -2014"""

#to allow for later use
import copy

#create function to create a 4X4 grid
def create_grid(grid):              
    for i in range(4):
        grid.append([0]*4) 
    return grid

# create function to print out a 4x4 grid in a box
def print_grid(grid):                   
    print("+--------------------+")
    for i in grid:
        print('|', end='')
        for z in i:
            z = str(z)
            if z == '0':
                print(' '.ljust(5), end = '')
            else:
                print(z.ljust(5),end = '')
        print('|')
    print("+--------------------+")    
    
  
#detrmines wheter there are more valid moves availiable
def check_lost (grid):
    for i in range(len(grid)-1):
        for m in range(len(grid[i])-1):
            if grid[i][m] == 0:
                return False
            elif grid[i][m] == grid[i+1][m]:
                return False
            elif grid[i][m] == grid[i][m+1]:
                return False
    return True


 #create function to determine whether there is a winner i.e. value greater tha 32
def check_won(grid):           
    for i in grid:
        for j in i:
            if j>=32:
                return True
    else:
        return False

# create function to return a copy of the grid after importing copy
def copy_grid (grid):
    copygrid = copy.deepcopy(grid)
    return copygrid


#create function to check whether two grids are equal
def grid_equal (grid1, grid2):
    if grid1==grid2:
        return True
    else:
        return False