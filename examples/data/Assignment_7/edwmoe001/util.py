""" Utility for 2-d array manipulation
Tauhirah Eguardo
5/01/2014"""
import copy

def create_grid (array):
     """Creates 4*4 grid"""
     #global grid
     #array = [[" " for x in range(5)] for y in range(5)]
     #array = [[]]
     #array = [[0 for i in range(4)] for i in range(4)]
     #return array
     array.append([0,0,0,0])
     array.append([0,0,0,0])
     array.append([0,0,0,0])
     array.append([0,0,0,0])
                  

def print_grid (grid):
     """print out a 4X4 grid in 5 width colums within a box"""
     length = 20
     for i in range(4):
          for j in range(4):
               if grid[i][j] == 0:
                    grid[i][j] = " "
                    grid[i][j] = "{:<5}".format(str(grid[i][j]))
               else:
                    grid[i][j] = "{:<5}".format(str(grid[i][j]))
               
     print("+","-"*length,"+",sep="")
     for x in range(4):
          values ="".join(grid[x])
          row = "|" + values + "|"
          print(row)
     print("+","-"*length,"+",sep="")
     
     
def check_lost (grid):
     """return True if there are no 0 values and no adjacent values that
     are equal: otherwise False"""
     
     lost = True
     
     for x in range(3):  
          for y in range(3):
               if grid[x][y] == 0 or grid[x][y] == grid[x][y+1] or grid[x][y] == grid[x+1][y]:
                    lost = False
               else:
                    pass 
     return lost     
def check_won (grid):
     """return True if a value>=32 is found in the grid; otherwise False"""
     found = False
     for x in range(4):   
          for y in range(4):
               if grid[x][y] >= 32:
                    found = True
               else:
                    pass
     return found
     
def copy_grid (grid):
     new_grid = copy.deepcopy(grid)
     
     return new_grid

def grid_equal (grid1, grid2):
     """ check if 2 grids are equal  return boolean value"""
     equal = True
     for x in range(4):  
          for y in range(4):
               if grid1[x][y] != grid2[x][y]:
                    equal = False
               else:
                    pass
               
     return equal
               
               