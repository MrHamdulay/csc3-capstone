"""Functions for 2048 game
Onalerona Mosimege
30 April 2014"""

import copy 

# create a 4x4 grid
def create_grid(grid):
   for i in range(4):
      grid.append([0,0,0,0])


# print out a 4x4 grid in 5-width columns within a box
def print_grid (grid):
   a = "{0:<5}"
   print("+--------------------+")
   for row in range(4):
      for col in range(4):
         if col == 0:
            if grid[row][col] != 0:
               print("|" + a.format(grid[row][col]), end= "")
            else:
               print("|" + a.format(""), end = "")
         elif col == 3:
            if grid[row][col] != 0:
               print(a.format(grid[row][col]) + "|")
            else:
               print(a.format("") + "|")
         else:
            if grid[row][col] != 0:
               print(a.format(grid[row][col]) , end = "")
            else:
               print(a.format(""), end = "")                 
   print("+--------------------+")
   
#  return True if there are no 0 values and no adjacent values that are equal; otherwise False 
def check_lost (grid):
   b = False
   for i in range(len(grid)):
      if 0 not in grid[i]:
         b = True
      else:
         b = False
   #checking adjacent
   
   #side by horizontal
   for row in range(3):
      for col in range(3):
         if grid[row][col] == grid[row+1][col]:
            b = False
            break
   #side vertical
   for col in range(3):
      for row in range(3):
         if grid[col][row] == grid[row][col+1]:
            b = False
            break   
   return b

# return True if a value>=32 is found in the grid; otherwise False
def check_won (grid):
   b = False
   for i in range(len(grid)):
      for j in range(4):
         if grid[i][j] >=  32:
            b = True
   return b

#return a copy of the grid
def copy_grid (grid):
   #deep copy returns copy but original won't change (internet)
   return copy.deepcopy(grid)


#check if 2 grids are equal - return boolean value
def grid_equal (grid1, grid2):
   b = False
   for i in range(len(grid1)):
      if grid1[i] == grid2[i]:
         b = True
      else:
         b = False
         break
   return b