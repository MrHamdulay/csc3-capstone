# A module of utility functions to maipulate 2-dimentional
# Retselisitsoe Monyake
# 27 april 2014
import copy
def create_grid(grid):
       #create a 4x4 grid
       #grid=[]
       for i in range(4):
              grid.append([0,0,0,0])
       #return grid
def print_grid(grid):
       print("+--------------------+")
       for i in range(4):
              print("|",end="")
              for j in range(4):
                     if grid[i][j]==0:
                            print("{0:<5}".format(" "),end="")
                     else:
                            print("{0:<5}".format(grid[i][j]),end="") 
              print("|")
       print("+--------------------+")
       #print out a 4x4 grid in 5-width columns within a box
       
def check_lost (grid):
    #return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
       for i in range(3):
              for j in range(3):
                     if grid[i][j]==0:
                            return False
                     elif grid[i][j]== grid[i][j+1]:
                            return False
                     elif grid[i][j]==grid[i+1][j]:
                            return False
       else:
              return True
                     

def check_won (grid):
#return True if a value>=32 is found in the grid; otherwise False
       for i in range(4):
              for j in range(4):
                     if  grid[i][j]>=32:
                            return True
       return False       
                     
def copy_grid (grid):
#return a copy of the grid
       copy_grid=copy.deepcopy(grid)
       return copy_grid
def grid_equal (grid1, grid2):
#check if 2 grids are equal - return boolean value
       if grid1==grid2:
              return True
       return False
                                       

