

"""create a 4x4 grid"""
def create_grid(grid):
   
   for i in range(4):
      grid.append([0]*4)
#return grid back to function.   
   
"""print out a 4x4 grid in 5-width columns within a box"""   
def  print_grid(grid):
   print("+--------------------+")
   
   for i in range (0,4):
      print("|", end = "")
      
      for j in range (0,4):

      
         if grid[i][j] == 0:
            print("{0:<5}".format(" "), end ="")
         else:
         
            print("{0:<5}".format(grid[i][j]), end = "")
      print("|")
  
      
      
   
   print("+--------------------+")
      #spaces = " "
      #print("+--------------------+")
      #for i in range(0, 4):     
         #print("|",spaces*(20),"|", sep="")

      #print("+--------------------+") 
               
               
"""return True if there are no 0 values and no adjacent values that are equal; otherwise False"""                      
def check_lost (grid):
   
   for x in range(0,4):
      for y in range(0,4):
            if y -1 >=0 and y +1 < 4 and x -1 >=0 and x + 1 < 4:
               if grid[x][y] != 0 and grid[x][y] != grid[x][y-1] and grid[x][y] != grid[x][ y+1] and grid[x][y] != grid[x-1][y] and grid[x][y] != grid[x+1][y]  :
                  return True
               
               else:
                  return False
               
               #if y -1 >=0:#Check in range
                  #return ( grid[x][y] != grid[x][y-1])                              
               #if y +1 < 4:#Check in range
                  #return ( grid[x][y] != grid[x][ y+1])
               #if  x -1 >=0:#Check in range
                  #return( grid[x][y] != grid[x-1][y])
               #if x + 1 < 4:#Check in range
                  #return( grid[x][y] != grid[x+1][y])
        
               
               
   
         
   """return True if a value>=32 is found in the grid; otherwise False"""         
def check_won (grid):
   for x in range(0,4):
      for y in range(0,4):
         if grid[x][y] >=32:
            
            return True
         #else:
   return False
"""return a copy of the grid"""
def copy_grid(grid):
   new_grid = [] 
   #grid_copy = list(grid)
   for i in range(4):
      new_grid.append([0]*4)
   for x in range(0,4):
      for y in range(0,4):
         new_grid[x][y] = grid[x][y]
   return new_grid
"""check if 2 grids are equal - return boolean value"""
def grid_equal (grid1, grid2):
   
   for x in range(0,4):
      for y in range(0,4):
         if grid1[x][y]!= grid2[x][y]:
            return False
         else:
            return True
         
        

   
            
                 
               

   