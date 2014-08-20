"""this module contains utility functions that will be used to create the game 2048
quincy cele
1 may 2014"""
import copy
def create_grid(grid):
   for i in range(4):
      grid.append([0]*4)
      
   return grid
   

def print_grid (grid):
   print("+","-"*20,"+",sep="")
   for row in range (4):
      print("|",end="")
      for col in range (4):
         if grid[row][col] == 0:
            print ("{:<5}".format(''), end="")
         else:
            print ("{:<5}".format(grid[row][col]), end="")
      print("|")
   print("+","-"*20,"+",sep="")

def check_lost(grid):
   for row in range(4):
      for col in range(4):
         if grid[row][col]==0:
            return False
         elif grid[0][0]==grid[1][0] or grid[0][0]==grid[0][1]:
            return False
         elif grid[0][3]==grid[1][3] or grid[0][3]==grid[0][2]:
            return False
         elif grid[3][0]==grid[2][0] or grid[3][0]==grid[3][1]:
            return False
         elif grid[3][3]==grid[2][3] or grid[3][3]==grid[3][2]:
            return False
         
         elif grid[0][col]==grid[1][col] or grid[0][col]==grid[0][col-1] or grid[0][col]==grid[0][col+1]:
            return False
         elif grid[3][col]==grid[2][col] or grid[3][col]==grid[3][col-1] or grid[3][col]==grid[3][col+1]:
            return False
         
         if row == 1 or row == 2:
            if col == 0:
               if grid[row][col] == grid[row][col+1] or grid[row][col] == grid[row+1][col] or grid[row][col] == grid[row-1][col]:
                  return False
            if col == 3:
               if grid[row][col] == grid[row][col-1] or grid[row][col] == grid[row+1][col] or grid[row][col] == grid[row-1][col]:
                  return False        
            else:
               if grid[row][col] == grid[row][col+1] or grid[row][col] == grid[row][col-1] or grid[row][col] == grid[row+1][col] or grid[row][col] == grid[row-1][col]:
                  return False               
         #elif grid[row][0]==grid[row][1] or grid[row][0]==grid[row-1][0] or grid[row][0]==grid[row+1][0]:
            #return False
         #elif grid[row][3]==grid[row][2] or grid[row][3]==grid[row-1][3] or grid[row][3]==grid[row-1][3]:
            #return False
         #elif grid[row][col]==grid[row+1][col] or grid[row][col]==grid[row-1][col] or grid[row][col]==grid[row][col+1] or grid[row][col]==grid[row][col-1]:
            #return False
         else:
            return True
         
def check_won(grid):
   for row in range(4):
      for col in range(4):
         if grid[row][col] >= 32:
            return True
   return False

def copy_grid(grid):
   new_grid= copy.deepcopy(grid)
   return new_grid

def grid_equal(grid1,grid2):
   for row in range(4):
      for col in range(4):
         if grid1[row][col]!=grid2[row][col]:
            return False
   return True