#2048 program
#Denzel Ncube 
#28 April 2014

import copy

#Moving the rows up for the correct number of spaces
def push_up (grid):
   for i in range(3):
      for j in range(1,4):
         for k in range(4):
            if grid[j-1][k] == 0 or grid[j-1]== ' ':
               grid[j-1][k] = grid[j][k]
               grid[j][k] = 0
   #Adding adjacent numbers upwards
   for i in range(1,4):
      for j in range(4):
         if grid[i-1][j] == grid[i][j]:
            grid[i-1][j] += grid[i][j]
            grid[i][j] = 0
   # Filling the gaps that have formed         
   for i in range(1,4):
      for j in range(4):
         if grid[i-1][j] == 0 or grid[i-1][j] == ' ':
            grid[i-1][j] += grid[i][j]
            grid[i][j] = 0
   return grid
      
      
   return grid
def push_down (grid):
   
   #Inverting the graph, using the push up function then making the graph the right way up
   oldgrid = copy.deepcopy(grid)
   for i in range(4):
      grid[0][i] = oldgrid[3][i]
      grid[1][i] = oldgrid[2][i]
      grid[2][i] = oldgrid[1][i]
      grid[3][i] = oldgrid[0][i]
   inverted = push_up(grid)
   newgrid = copy.deepcopy(inverted)
   for i in range(4):
      grid[0][i] = newgrid[3][i]
      grid[1][i] = newgrid[2][i]
      grid[2][i] = newgrid[1][i]
      grid[3][i] = newgrid[0][i]    
   return grid


def push_left (grid):
   #Making the columns rows, using the push up function then changing the rows back to columns
   oldgrid = copy.deepcopy(grid)
   for i in range(4):
      grid[0][i] = oldgrid[i][0]
      grid[1][i] = oldgrid[i][1]
      grid[2][i] = oldgrid[i][2]
      grid[3][i] = oldgrid[i][3]
   inverted = push_up(grid)
   newgrid = copy.deepcopy(inverted)    
   for i in range(4):
      grid[0][i] = newgrid[i][0]
      grid[1][i] = newgrid[i][1]
      grid[2][i] = newgrid[i][2]
      grid[3][i] = newgrid[i][3]
   return grid

def push_right (grid):
   #Making right columns left columns, using push left function then changing them back to right columns
   oldgrid = copy.deepcopy(grid)
   for i in range(4):
      grid[i][0] = oldgrid[i][3]
      grid[i][1] = oldgrid[i][2]
      grid[i][2] = oldgrid[i][1]
      grid[i][3] = oldgrid[i][0]
   inverted = push_left(grid)
   newgrid = copy.deepcopy(inverted)    
   for i in range(4):
      grid[i][0] = newgrid[i][3]
      grid[i][1] = newgrid[i][2]
      grid[i][2] = newgrid[i][1]
      grid[i][3] = newgrid[i][0]
   return grid    
    