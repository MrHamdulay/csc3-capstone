"""program to do grid manipulation
herman claassens
1 may 2014"""

import copy

def create_grid (grid): # create a 4x4 grid filled with zeros
   for i in range (4):
      grid.append ([0] * 4)
    
def print_grid(grid):
   print('+--------------------+') # print a 4x4 grid in a box
   for row in range (4):
      print('|',end=(''))
      for col in range (4):
         if grid[row][col] == 0:
            print('{0:<5}'.format(" "),end='')
         else:
            print('{0:<5}'.format(grid[row][col]),end='') # box has a colum with of 5
      print('|',end=(''))
      print ()  
   print ('+--------------------+') 
   

def check_lost(grid):
   for rows in range(4):
      for col in range(4):
         if grid[rows][col]==0:   # if there are still zeros in the grid the game can continue
            return False
   for rows in range(4):
      for col in range(3):   
         if grid[rows][col]==grid[rows][col+1]: # if adjascent cells are equal the game can continue
            return False
   for rows in range(3):
      for col in range(4): 
         if grid[rows][col]==grid[rows+1][col]:
            return False
   else: return True # if there are no zeros and no adjescent cells that are even, the game ends


def check_won(grid):
   for row in range(4):   # if there is a value greater than or equal to 32 in the grid, the player wins the game
      for col in range(4):
            if grid[row][col] >= 32:
               return True
   return False
   

def copy_grid(grid):
   new_grid=copy.deepcopy(grid) # make a copy of a grid you are sent
   return new_grid

def grid_equal(grid1, grid2): # check if two grids are equal to each other (the value i each cells is equal to the corresponding cell in another grid
   for rows in range(4):
      for col in range(4):
         if grid1[rows][col]!=grid2[rows][col]:
            return False
   else: return True
   
   




