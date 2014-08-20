"""Program to manipulate 2 dimensional arrays assignment 7 question 2
Dean Gracey
28 April 2014"""

def create_grid(grid):
   
   grid.append([0,0,0,0])
   grid.append([0,0,0,0])
   grid.append([0,0,0,0])
   grid.append([0,0,0,0])
   
   
def print_grid(grid):
    
   for y in range(0,4):
      for x in range(0,4):
         if(grid[y][x]==0):
            grid[y][x]=""
    
   print("+--------------------+")
   print("|","{0:<5}".format(grid[0][0]),"{0:<5}".format(grid[0][1]),"{0:<5}".format(grid[0][2]),"{0:<5}".format(grid[0][3]),"|",sep = "")
   print("|"+"{0:<5}".format(grid[1][0])+"{0:<5}".format(grid[1][1])+"{0:<5}".format(grid[1][2])+"{0:<5}".format(grid[1][3])+"|")
   print("|"+"{0:<5}".format(grid[2][0])+"{0:<5}".format(grid[2][1])+"{0:<5}".format(grid[2][2])+"{0:<5}".format(grid[2][3])+"|")
   print("|"+"{0:<5}".format(grid[3][0])+"{0:<5}".format(grid[3][1])+"{0:<5}".format(grid[3][2])+"{0:<5}".format(grid[3][3])+"|")
   print("+--------------------+")
    
   for y in range(0,4):
         for x in range(0,4):
            if(grid[y][x]==""):
               grid[y][x]=0
    
def check_lost(grid):    
   
   lost = True
   for y in range(0,4):
         for x in range(0,4):
            if(grid[y][x]==0):
               lost = False
   
   
   
    
      
   for y in range (0,3):
      for x in range(0,3):
         if(grid[y][x]==grid[y][x+1]):
            lost = False
            
         if(grid[y][x]==grid[y+1][x]):
            lost = False
   return lost           

def check_won(grid):
   found = False
   for y in range(0,4):
      for x in range(0,4):
         if(grid[y][x]>=32):
            found = True
                
   return found

def copy_grid(grid):
   grid2 = [[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]
   for y in range(0,4):
      for x in range(0,4):
         grid2[y][x] = grid[y][x]
   return grid2                    
    
   
def grid_equal(grid1,grid2):
   if grid1==grid2:
      return True
   else:
      return False
       
