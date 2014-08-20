"""program to merge grids up, down, left or right
herman claassens
1 may 3014"""

import util

def shift(grid):
   for i in range(1,4):    # function that shifts a list left as long as there is a zero left of each value in the list
      pos=i-1
      while grid[pos]==0 and pos>=0:
         grid[pos]=grid[pos+1]
         grid[pos+1]=0
         pos-=1
   return grid
         

def add(grid):
   for i in range(1,4):   # function that adds values to the left together
      pos=i-1
      if grid[pos]==grid[i]:
         grid[pos]*=2
         grid[i]=0     
   return grid   

def push_left(grid):
   test_grid=util.copy_grid(grid)  # remove a single row from the grid
   for i in range(4):              # shift the list left
      lis=test_grid[i]             # add the values to the left
      lis=shift(lis)               # shift the left to the left again
      lis=add(lis)
      lis=shift(lis)
      test_grid[i]==lis
   for row in range(4):           # return the manipulated list into the grid
      for col in range(4):
         grid[row][col] = test_grid[row][col]   
      
def push_right(grid):
   test_grid=util.copy_grid(grid)  # remove a single row from a grid
   for i in range(4):
      lis=test_grid[i]           
      lis=lis[::-1]                # reverse the list
      lis=shift(lis)               # shift the list to the left
      lis=add(lis)                 # add the values to the left
      lis=shift(lis)               # shift the values to the left
      lis = lis[::-1]              # reverse the list back again
      test_grid[i]=lis
   for row in range(4):
      for col in range(4):         # add the list back into the grid
         grid[row][col] = test_grid[row][col]
         
def push_up(grid):
   test_grid=util.copy_grid(grid) 
   for i in range(4):
      lis=[]
      for j in range(4):             # remove a single column from a grid
         lis.append(test_grid[j][i])
      lis=shift(lis)                 # shift the column to the left
      lis=add(lis)                   # add the values to the left
      lis=shift(lis)                 # shift the values to the left again
      for j in range(4):
         test_grid[j][i]=lis[j]      # insert the manipulated list into the grid
   for row in range(4):
      for col in range(4):
         grid[row][col] = test_grid[row][col]    
         
def push_down(grid):
   test_grid=util.copy_grid(grid)   
   for i in range(4):
      lis=[]
      for j in range(4):          # remove a single column from a grid
         lis.append(test_grid[j][i])
      lis=lis[::-1]               # reverse the column
      lis=shift(lis)              # shift the column to the left
      lis=add(lis)                # add the values in the column to the left
      lis=shift(lis)              # shift the column list left 
      lis = lis[::-1]             # reverse the column back
      for j in range(4):
         test_grid[j][i]=lis [j] 
   for row in range(4):           # re insert the column
      for col in range(4):
         grid[row][col] = test_grid[row][col]       
         

         
         