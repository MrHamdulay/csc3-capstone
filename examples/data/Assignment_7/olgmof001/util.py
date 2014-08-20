"""Tofunmi Olagoke
29 April 2014
2048 game functions(1)"""

def create_grid(grid):
      for i in range (4):
            grid.append ([0,0,0,0])
      return grid


def print_grid (grid):  
      print("+--------------------+")
      
#putting the grid into columns
      for i in grid:
            print("|", end="")
            for x in i:
                  if x==0:
                        x="    "
                  print(x," "*(4-len(str(x))),end="")
            print("|")
            
      print("+--------------------+")

      
def check_lost (grid):
      duplicate=0
      for x in grid:
                  for inlist in x: 
                       #checks for equal adjacent numbers
                        if inlist==0 or x[0]==x[1]or x[1]==x[2] or x[2]==x[3] or x[0]==x[3]:
                              return False
      for x in grid:
                  for inlist in x:
                        if not inlist==0 or not x[0]==x[1]or not x[1]==x[2] or not x[2]==x[3] or not x[0]==x[3]:
                              return True
def check_won (grid): 
      
      for x in grid:
            for inlist in x:
                  #checks if there are numbers over 32
                  if inlist>=32:
                        return True
      for x in grid:
            for inlist in x:
                  if not inlist>=32:
                        return False
                 

def copy_grid (grid):
      #reproduces the grid given
      nl=[]
      
      for i in grid:
            for x in i:
                  nl=nl+[x]
      nl1=nl[0:4]
      nl2=nl[4:8]
      nl3=nl[8:12]
      nl4=nl[12:16]
      
      finallist=[nl1,nl2,nl3,nl4]
      return finallist


def grid_equal (grid1, grid2):
      if grid1==grid2:
            return True
      if not grid1==grid2:
                  return False    

