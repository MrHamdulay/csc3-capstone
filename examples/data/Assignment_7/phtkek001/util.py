


grid=[]

def create_grid(grid):
   """create 2-D arrays to store ship grid and grid of guesses"""
   for i in range(4):
      grid.append([" "]*4)

grid=[]
   
def print_grid (grid):
   print("+" + "-" * 20+ "+")
   for row in range(4):
      print("|", end="")
      for col in range(4):
         if col == 3:
            print("{0:5}".format(grid[row][col])+"|")
         else:
            print("{0:5}".format(grid[row][col]), end="")
   print("+"+"-"*20+"+")
   
def check_lost (grid):
   lost_0 = True
   lost_a = True
   for row in range(4):
      for col in range(4):
         if (grid[row][col] == 0):
            grid[row][col] == " "
            lost_0 = False
            break
   for row in range(3):
      for col in range(3):
         if grid[row][col] == grid[row][col+1]:
            lost_a = False
            break
         if grid[row][col] == grid[row][col+1]:
            lost_a and lost_0
            return True
         else:
            return False
        
        
def check_won (grid): 
   won = False
   for row in range(4):
      for col in range(4):
         if grid[row][col] >=32:
            won = True
   return won

def copy_grid (grid):
   newgrid=[]
   for i in range(4):
      newgrid.append([" "]*4)
   for row in range(4):
      for col in range(4):
         newgrid[row][col] = grid[row][col]
   return newgrid     

def grid_equal(grid1, grid2):
   found = True
   for row in range(4):
      for col in range(4):
         if grid1[row][col] != grid2[row][col]:
            found = False
   return found



   
