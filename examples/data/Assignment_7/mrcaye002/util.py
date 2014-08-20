#Module of utility functions to manipulate 2-dimensional arrays of size 4x4.
#Ayesha Marcus
#30/04/2014

import copy

def create_grid(grid):                  #Create a 4x4 Grid
    for i in range(4):
      grid.append([0]*4)
    #grid = [0,0,0,0] * 5
    #for i in range (4):
    #  new = []
    #  for j in range (4):
    #    #print ("i", i,"j",j)
    #    new.append(0)
    #  grid.append(new) 
      

def print_grid (grid):                   #Print Grid
    print (str("+") + str((5*"-")*4) +str("+"))
    for item in grid:
      vStr="|"
      for i in range(len(grid[0])):
        if item[i] > 0:
          vStr=vStr + str(item[i]).ljust(5)
        else:
          vStr=vStr + "".ljust(5)
      vStr=vStr + "|"
      print (vStr)
    
    print (str("+") + str((5*"-")*4) +str("+"))
    return

def check_lost (grid):                  #Check whether the user has lost
    #return True if there are no 0 values and no adjacent values that are equal; otherwise False
    isZero = 0
    tmp=0
    sReturn=True
    for item in grid:
      for i in range(len(grid[0])):
        if item[i] == 0:
          sReturn=False
        if (i+1) < len(grid[0]):
          tmp=item[i+1]
          if tmp == item[i]:
            sReturn=False
    #[0,0,0,0]
    #[0,0,0,0]
    for i in range(4):
    	for j in range(4):
    		if i < 3:
    		  if grid[i][j] == grid[i+1][j]:
    			  sReturn=False
    			  break
      #for j in range(4):
      #  if (i+1) < len(grid[0]):
      #    tmp=grid(i,i+1)
      #    if tmp == grid(i,0):
      #      print(tmp,i)
      #      sReturn=False

    if isZero == 1:
      sReturn=False
      
    return sReturn;
    
    
def check_won (grid):                 #Check whether the user has won the game
    """return True if a value>=32 is found in the grid; otherwise False"""
    isZero = 1
    sReturn=True
    for item in grid:
      for i in range(len(grid[0])):
        if item[i] >= 32:
          isZero = 0
          break
          
      if isZero == 0:
        break

    
    if isZero == 1:
      sReturn=False
      
    return sReturn;

def copy_grid (grid):
    #return a copy of the grid

    return copy.deepcopy(grid);

def grid_equal (grid1, grid2):
    #check if 2 grids are equal - return boolean value
    sReturn=False
    if grid1 == grid2:
      sReturn=True
      
    return sReturn;
