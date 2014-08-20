"""Utility functions for 4x4 grids
B.Player
27/04/2014"""

def create_grid(grid):
   """create a 4x4 grid"""
   for i in range(4):
      grid.append([0]*4)

def print_grid(grid):
   """print out 4x4 grid in 5-width columns within a box"""
   print("+",'-'*20,'+',sep='')
   for row in range(4):     
      print("|",end='')
      for col in range(4):         
         format_string = "{0:<5}"
         if grid[row][col]==0: print(format_string.format(" "),end='') 
         else: print(format_string.format(grid[row][col]),end='')        
      print("|")
   print("+",'-'*20,'+',sep='')   
   
   
def check_lost(grid):
   """returns true if there are no 0 values and no adjacent values that are equal; otherwise false"""
   flag = True
   for row in range(4):
      for col in range(4):
         if grid[row][col]==0:return False
         if 0<col<3 and 0<row<3:
            if grid[row][col]== grid[row][col+1]: flag = False
            elif grid[row][col]== grid[row][col-1]: flag = False         
            elif grid[row][col]== grid[row-1][col]: flag = False
            elif grid[row][col]== grid[row+1][col]: flag = False
         else:
            if col==0:
               if grid[row][col]== grid[row][col+1]: flag = False 
               elif row!=0:
                  if grid[row][col]== grid[row-1][col]: flag = False
               elif row!=3:
                  if grid[row][col]== grid[row+1][col]: flag = False               
            else:               
               if grid[row][col]== grid[row][col-1]: flag = False 
               elif row!=0:  
                  if grid[row][col]== grid[row-1][col]: flag = False
               elif row!=3:
                  if grid[row][col]== grid[row+1][col]: flag = False               
                             
   return flag


def check_won(grid):
   """returns true if a value>=32 is found in the grid; otherwise Flase"""
   flag=False
   for row in range(4):
      for col in range(4):
         if grid[row][col]>=32: flag=True 
   return flag

def copy_grid(grid):
   """returns a copy of the grid"""   
   grid2=[]
   for row in range(4):
      grid2.append([0]*4)
   for row in range(4):
      for col in range(4):
         grid2[row][col]=grid[row][col]    
   return grid2
         

def grid_equal(grid1,grid2):
   """Checks if 2 grids are equal - returns boolean value"""
   flag=True
   for row in range(4):
      for col in range(4):
         if grid2[row][col]!=grid1[row][col]:flag=False         
   return flag