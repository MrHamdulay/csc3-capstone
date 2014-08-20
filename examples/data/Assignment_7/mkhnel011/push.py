""" 2048 functions
question 3
nelisile mkhwebane
01/05/2014"""

""" a function that shifts and adds the values of the grid upwards """

#import util

def push_up (grid):
   
   """ to make sure that the first row doesn't shift farther up"""
   for row in range (1, 4):
      """ since we want to go through all the columns still """
      for col in range (4):
         if grid[row-1][col] == 0 and grid [row-2][col]==0 and grid[row - 3][col]== 0:
                     grid [row - 3][col] = grid[row-3][col] + grid[row][col]
                     grid[row][col] = 0  
         elif grid[row-1][col] == 0 and grid [row-2][col]== 0:
            if grid[row-3][col] == grid[row][col]:
               grid[row-3][col]= grid[row-3][col] + grid [row][col]
               grid[row][col] = 0
            else:
               grid[row-2][col]= grid[row][col]
         elif grid[row-1][col] == 0 and grid[row-2][col] == 0:
            if grid[row-2][col] == grid[row][col]:
               grid[row-2][col] = grid[row-2][col]+grid[row][col]
               grid[row][col] = 0         
            else:
               grid[row-1][col]= grid[row][col]
               grid[row][col] = 0
         elif grid[row-1][col] == grid[row][col]:
            """add the top and the bottom blocks to each other, if they are equal"""
            grid[row-1][col] = grid[row][col] + grid[row-1][col]
            grid[row][col] = 0
         elif grid[row-1][col] == 0:
            if grid[row-2][col]== grid[row][col]:
               grid[row-2][col]= grid[row-2][col]+ grid[row][col]
               grid[row][col]=0
            else:
               grid[row-1][col]= grid[row][col]
               grid[row][col]= 0

def push_down(grid):
   """ to make sure the bottom row doesn't shift further down """
   for row in range (4):
      """ we still want it to get through all the columns so..."""
      for col in range (4):
         if  row!= 3:
            if grid[row][col] == grid[row+1][col]:
               grid[row+1][col] = grid[row+1][col]+grid[row][col]
               grid[row][col]= 0
            elif grid[row+1][col] == 0:
               grid[row+1][col] = grid[row+1][col] + grid[row][col]
               grid[row][col] = 0
               
         '''elif grid[row+1][col] == 0 and grid[row+2][col]== 0:
            if grid[row+3][col] == grid[row][col]:
               grid[row+3][col] = grid[row][col]+ grid[row+3]
            else:row
               grid[row+2][col] = grid[row][col]'''

def push_left(grid):
   for row in range (4):
      """ since we want to go through all the columns still """
      for col in range (4):
            if grid[row][col-1] == 0 and grid [row][col-2]==0 and grid[row][col-3]== 0:
               grid [row][col-3] = grid[row][col-3] + grid[row][col]
               grid[row][col] = 0  
            elif grid[row][col-1] == 0 and grid [row][col-2]== 0:
               if grid[row][col-3] == grid[row][col]:
                  grid[row][col-3]= grid[row][col-3] + grid [row][col]
                  grid[row][col] = 0
               else:
                  grid[row][col-2]= grid[row][col]
                  grid[row][col] = 0
            elif grid[row][col-1] == 0 and grid [row][col-2]== 0:
               grid[row][col-2]=grid[row][col]
            elif grid[row][col-1]!= grid[row][col]:
               grid[row][col-1] = grid[row][col]
               grid[row][col-1] = grid[row][col-1]
            elif grid[row][col-2] == grid[row][col]:
               grid[row][col-2]= grid[row][col-2] + grid[row][col]
            elif grid[row][col]==grid[row][col-1]:
               grid[row][col-1]= grid[row][col-1] + grid [row][col]
            elif grid[row][col-2] == 0 and grid[row][col-2] == 0:
               if grid[row][col-2] == grid[row][col]:
                  grid[row][col-2] = grid[row][col-2]+grid[row][col]
                  grid[row][col] = 0         
               else:
                  grid[row][col-1]= grid[row][col]
                  grid[row][col] = 0
            elif grid[row][col-1] == grid[row][col]:
               grid[row][col-1] = grid[row][col] + grid[row][col-1]
               grid[row][col] = 0
            elif grid[row][col-1] == 0:
               if grid[row][col-2]== grid[row][col]:
                  grid[row][col-2]= grid[row][col-2]+ grid[row][col]
                  grid[row][col]=0
               else:
                  grid[row][col-1]= grid[row][col]
                  grid[row][col]= 0
            
               
def push_right(grid):
   for row in range (4):
      for col in range (4):
         if col!= 3:
            if grid[row][col] == grid[row][col+1]:
               grid[row][col+1] = grid[row][col+1]+grid[row][col]
               grid[row][col]= 0
            elif grid[row][col+1] == 0:
               grid[row][col+1] = grid[row][col+1] + grid[row][col]
               grid[row][col] = 0