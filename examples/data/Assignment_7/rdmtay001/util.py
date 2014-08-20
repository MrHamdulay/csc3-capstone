# creating functions to create the game 2048
# Tayla Radmore
#30 April 2014

import copy # for deep copy
# creating an empty grid
copy_grid=[]
grid=[]
def create_grid(grid):
      for i in range (4):
            grid.append ([0] * 4) 
            
# printing a filled grid            
def print_grid (grid):
      print("+--------------------+")
      
      for row in range (4):
            print("|",end="")
            for col in range (4):
                  if grid[row][col]!= 0:
                        x=str(grid[row][col])
                        repeats=5-len(x)
                        print (grid[row][col]," "*repeats,sep="",end="")
                  else:
                        print("     ",end="")
            print ("|")       
      print("+--------------------+")
      
# checking to see if player has lost (true if so, false if not)      
def check_lost (grid):
      for row in range(4):
            for col in range(4):
                  if grid[row][col]==0: 
                        return False
      
      for row in range (4):
            for col in range (3):
                  if grid[row][col]==grid[row][col+1]:
                        return False
      
      for row in range(3):
            for col in range (4):
                  if grid[row][col]==grid[row+1][col]:
                        return False
                  
      return True
                              

# checking to see if player has won
def check_won (grid):
      for row in range(4):
            for col in range(4):
                  if grid[row][col]>=32: return True
      else: return False
      
# creating a copy of a grid     
def copy_grid (grid):
      gridcopy = copy.deepcopy(grid)
      return gridcopy       
                       
      
# checking if two grids are equal
def grid_equal (grid1, grid2):
      if grid1==grid2:
            return True
      else:
            return False
                        
                        
                  
                              
                  
                              
            