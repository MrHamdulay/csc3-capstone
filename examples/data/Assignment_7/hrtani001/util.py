#Aniq Hartle
#02/05/2014

#creates grid object to be used in 2048.py
def create_grid(grid):
   for i in range(0,4):
      grid.append([0,0,0,0])       #appends a row of 4
   return grid

#prints the grid in a box of 4x4 with a 5 space gap
def print_grid(grid):
   print("+--------------------+")
   for i in range(len(grid)):
      print("|",end="")
      for j in range(len(grid)):
         if grid[i][j] == 0:      #if the grid entry is blank then fill with five spaces
            print(" "*5,end="")
         else:
            print(grid[i][j]," "*(4-len(str(grid[i][j]))), end="")     #fill with 5-(length of number)
      print("|")
   print("+--------------------+")
   
   
#checks if game is over, all spaces full and no duplicates adjacent to each other
def check_lost(grid):
   for i in range(len(grid)):
      for j in range(len(grid)-1):
         if grid[i][j]==0:      #if there is an empty space present NOT lose game
            return False
         elif (grid[i][j]==grid[i][j+1]):
            return False          #if there is a duplicate above or below NOT lose game
   for i in range(len(grid)-1):
      for j in range(len(grid)):         
         if grid[i][j]==grid[i+1][j]:
            return False            #if there is a duplicate next to, NOT lose game
   else:
      return True          #If any condition is met game is lost


#check if 32 is present
def check_won(grid):
   win = False
   for i in range(len(grid)):
      for j in range(len(grid)):
         if grid[i][j]>=32:      #if a grid entry is found to be 32 WIN
            win = True
   return win   

#create a duplicate grid
import copy       #import copy for copy functions
def copy_grid(grid):
   copyGrid = copy.deepcopy(grid)         #create a new grid that is a clone of the grid taken in
   return copyGrid

#compare grids to see if equal         
def grid_equal(grid1, grid2):
   equal = True
   for i in range(len(grid1)):
      for j in range(len(grid1)):
         if grid1[i][j]!=grid2[i][j]:
            equal = False        #if at any point two grid co-ordinates are not equal, the grids are not the same
   return equal   