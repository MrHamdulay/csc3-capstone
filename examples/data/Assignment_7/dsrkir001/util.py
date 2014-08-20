


#A module of utility functions to manipulate 2-dimensional arrays
#27 April 2014
#Kiran Desraj


#import function to be used when copying the grid
import copy



#create a 4x4 grid :
def create_grid(grid):
    for i in range (4):
        grid.append ([0]*4)
    return grid


#print out a 4x4 grid in 5-width columns within a box :
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
    
    
# no zeros and no matching values next to each other

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


#check if there is a value=>32

def check_won (grid):
    for i in range(4):
            for j in range(4):
                if grid[i][j]>= 32:
                    return True
    return False

#f return a copy of the grid :

def copy_grid (grid):
    grid2 = copy.deepcopy(grid)
    return grid2


#check whether every term in grids are equal:

def grid_equal (grid1, grid2):
    if grid1==grid2:
        return True
    else:
        return False