#sandisha Budhal
#BDHSAN003

import copy
def create_grid(grd):
       for a in range(4):
              grd.append([0,0,0,0])
       
def print_grid(grd):
       print("+--------------------+")
       for a in range(4):
              print("|",end="")
              for b in range(4):
                     if grd[a][b]==0:
                            print("{0:<5}".format(" "),end="")
                     else:
                            print("{0:<5}".format(grd[a][b]),end="") 
              print("|")
       print("+--------------------+")
       #print out a 4x4 grd
       
def check_lost (grd):
    
       for a in range(3):
              for b in range(3):
                     if grd[a][b]==0:
                            return False
                     elif grd[a][b]== grd[a][b+1]:
                            return False
                     elif grd[a][b]==grd[a+1][b]:
                            return False
       else:
              return True
                     

def check_won (grd): #return True if a value>=32 is in grid
       for a in range(4):
              for b in range(4):
                     if  grd[a][b]>=32:
                            return True
       return False       
                     
def copy_grid (grd): #to return a copy of grid
       copy_grid=copy.deepcopy(grd)
       return copy_grid
def grid_equal (grid1, grid2):#to check if both grids are equal

       if grid1==grid2:
              return True
       return False
                                       

