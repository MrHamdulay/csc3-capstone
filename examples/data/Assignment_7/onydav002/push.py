'''    """merge grid values upwards"""

def push_down (grid):
    """merge grid values downwards"""

def push_left (grid):
    """merge grid values left"""

def push_right (grid):
    """merge grid values right"""    '''

import copy 

#Moving the rows up for the correct number of spaces
def push_up (grid):
   for i in range(3):
      for j in range(1,4):
         
         for k in range(4):
            
            if grid [j-1][k] == 0 or grid [j-1]== ' ':
               grid [j-1][k] = grid [j][k]
               grid [j][k] = 0
   #Add numbers up
   for i in range(1,4):
      for j in range(4):
         if grid [i-1][j] == grid [i][j]:
            grid [i-1][j] += grid [i][j]
            grid [i][j] = 0


   # Fill Gaps       

   for i in range(1,4):
      for j in range(4):
         if grid[i-1][j] == 0 or grid[i-1][j] == ' ':
            grid[i-1][j] += grid[i][j]
            grid[i][j] = 0
   return grid
      
   return grid



def push_down (grid):
   
   oldgrid = copy.deepcopy(grid)

   for i in range(4):
      grid [0][i] = oldgrid [3][i]
      grid [1][i] = oldgrid [2][i]
      grid [2][i] = oldgrid [1][i]
      grid [3][i] = oldgrid [0][i]
   inverted = push_up (grid)
   newgrid = copy.deepcopy (inverted)
   for i in range(4):
      grid [0][i] = newgrid [3][i]
      grid [1][i] = newgrid [2][i]
      grid [2][i] = newgrid [1][i]
      grid [3][i] = newgrid [0][i]    
   return grid





def push_right (grid):
   
   oldgrid = copy.deepcopy(grid)
  
  
  
   for i in range(4):
      grid[i][0] = oldgrid [i][3]
      grid[i][1] = oldgrid [i][2]
      grid[i][2] = oldgrid [i][1]
      grid[i][3] = oldgrid [i][0]
   inverted = push_left(grid)
   newgrid = copy.deepcopy(inverted)    
   
   
   
   
   
   for i in range(4):
      grid [i][0] = newgrid [i][3]
      grid [i][1] = newgrid [i][2]
      grid [i][2] = newgrid [i][1]
      grid [i][3] = newgrid [i][0]
   return grid    
    




def push_left (grid):
      oldgrid = copy.deepcopy(grid)



   for i in range(4):
      grid [0][i] = oldgrid [i][0]
      grid [1][i] = oldgrid [i][1]
      grid [2][i] = oldgrid [i][2]
      grid [3][i] = oldgrid [i][3]
   inverted = push_up (grid)
   newgrid = copy.deepcopy (inverted)    


   for i in range(4):
      grid [0][i] = newgrid [i][0]
      grid [1][i] = newgrid [i][1]
      grid [2][i] = newgrid [i][2]
      grid [3][i] = newgrid [i][3]
   return grid


