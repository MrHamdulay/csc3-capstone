"""program to manipulate 2-D arrays
nosipho khumalo
27 April 2014"""

import copy

#declaring variables
flag = False
#create a 4x4 grid
def create_grid(grid):
   for i in range(4):
      grid.append([0]*4)


#print out a 4x4 grid in 5-width columns within a box
def print_grid (grid):
   print("+", "-"*20, "+", sep = "")
   for row in range(4):
      for column in range(4):
         if column == 0:
            if grid[row][column] != 0:
               print("|" + "{0:<5}".format(grid[row][column]), end= "")
            else:
               print("|" + "{0:<5}".format(""), end = "")
         elif column == 3:
            if grid[row][column] != 0:
               print("{0:<5}".format(grid[row][column]) + "|")
            else:
               print("{0:<5}".format("") + "|")
         else:
            if grid[row][column] != 0:
               print("{0:<5}".format(grid[row][column]) , end = "")
            else:
               print("{0:<5}".format(""), end = "")                 
   print("+", "-"*20, "+", sep = "")
   
# return True if there are no 0 values and no adjacent values that are equal; otherwise False 
def check_lost (grid):
   global flag
   for i in range(len(grid)):
      if 0 not in grid[i]:
         flag = True
      else:
         flag = False
   #checking adjacent
   
   #side by horizontal
   for row in range(3):
      for column in range(3):
         if grid[row][column] == grid[row+1][column]:
            flag = False
            break
   #side vertical
   for column in range(3):
      for row in range(3):
         if grid[column][row] == grid[row][column+1]:
            flag = False
            break   
   return flag

# return True if a value>=32 is found in the grid; otherwise False
def check_won (grid):
   global flag
   for i in range(4):
      for j in range(4):
         if grid[i][j] >=  32:
            flag = True
   return flag

#return a copy of the grid
def copy_grid (grid):
   #deep copy returns copy but original won't change (internet)
   return copy.deepcopy(grid)


#check if 2 grids are equal - return boolean value
def grid_equal (grid1, grid2):
   global flag
   for i in range(4):
      if grid1[i] == grid2[i]:
         flag = True
      else:
         flag = False
         break
   return flag