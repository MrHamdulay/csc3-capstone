"""Program consisting of modules with utility functions
Thiloshni Moodley
1 April 2014"""
import copy
def create_grid(grid):  #create a 4x4 grid
       grid=[]
       for a in range(4):
              grid.append([0,0,0,0])
       return grid #return grid

def print_grid(grid): #print out a 4x4 grid in 5-width columns within a box
       print("+"+"-"*20+"+")
       for a in range(len(grid)):
              print("|",end="")
              for b in range(len(grid)):
                     if grid[a][b]==0:
                            print("{0:<5}".format(" "),end="")
                     else:
                            print("{0:<5}".format(grid[a][b]),end="") 
              print("|")
       print("+"+"-"*20+"+")
       
def check_lost (grid):
    #return True if there are no 0 values and no adjacent values that are equal, if not the case return False"""
       for a in range(3):
              for b in range(3):
                     if grid[a][b]==0:
                            return False
                     elif grid[a][b]== grid[a][b+1]:
                            return False
                     elif grid[a][b]==grid[a+1][b]:
                            return False
       else:
              return True
                     
def check_won (grid): 
       for a in range(4):
              for b in range(4):
                     if  grid[a][b]>=32:
                            return True #function will return true if the value is greater than or equal to 32
       return False     #function will return false if not 
                     
def copy_grid (grid): #return a copy of the grid
       copy_grid=copy.deepcopy(grid)
       return copy_grid

def grid_equal (grid1, grid2): #Will check if the one grid is equal to the other
       if grid1==grid2:
              return True
       return False
                                       

