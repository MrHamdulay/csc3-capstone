""" Utility functions
Tameryn Pillay
2 May 2014 """

import copy

# create the grid
def create_grid(grid):
       for k in range(4):
              grid.append([0,0,0,0])
   
              
# print out a 4x4 grid in 5-width columns                    
def print_grid(grid):
       print('+--------------------+')
       for k in range(4):
              print('|',end='')
              for i in range(4):
                     if grid[k][i]==0:
                            print('{0:<5}'.format(' '),end='')
                     else:
                            print('{0:<5}'.format(grid[k][i]),end='') 
              print('|')
       print('+--------------------+')
   
   
# True if there are no 0 values and no adjacent values that are equal    
def check_lost (grid):
       for k in range(3):
              for i in range(3):
                     if grid[k][i]==0:
                            return False
                     elif grid[k][i]== grid[k][i+1]:
                            return False
                     elif grid[k][i]==grid[k+1][i]:
                            return False
                     else:
                            return True
                     
                     
# True if value>=32 is found in the grid
def check_won (grid):
       for k in range(4):
              for i in range(4):
                     if  grid[k][i]>=32:
                            return True
       return False      


# return copy of the grid                   
def copy_grid (grid):
       copy_grid=copy.deepcopy(grid)
       return copy_grid


# check to see if 2 grids are equal
def grid_equal (grid1, grid2):
       if grid1==grid2:
              return True
       return False
                                       

