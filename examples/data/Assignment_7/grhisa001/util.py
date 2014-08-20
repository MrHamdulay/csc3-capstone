grid=[]
guessgrid=[]
copygrid=[]
copyguessgrid=[]
def create_grid (grid):
 
   """create 2-D arrays to store ship grid and grid of guesses"""
   for i in range (4):
      grid.append ([0] * 4)        
   for i in range (4):
      guessgrid.append ([0] * 4)
   return guessgrid
      
   

def print_grid (g):
   """ print out a grid of strings/characters"""
   
   
   boxes="{0:<5}"
   edgebox1="|{0:<5}"
   edgebox2="{0:<5}|"
   print("+--------------------+")
   for row in range (4):
   
      
      for col in range (4):
         if col == 0:
            if g[row][col] == 0:
               print (edgebox1.format(" "),end="") 
            else:
               print(edgebox1.format(g[row][col]),end="")
   
         if col == 3:
            if g[row][col] == 0:
               print((edgebox2.format(" ")),end="")
            else:
               print(edgebox2.format(g[row][col]),end="")
                           
         
         if col == 1 or col == 2:
            if g[row][col] == 0:
                          
               print(boxes.format(" "),end="")
            else:
               print(boxes.format(g[row][col]),end="")
               
            
         
      print()
   print("+--------------------+")
      
   
   
def check_lost(g):
   for row in range(4):
      for col in range(4):
         
         if g[row][col]==False:
            return False
         
         if row != 3 and g[row+1][col]==g[row][col]:
            return False
         if row >=1 and g[row-1][col]==g[row][col]:
            return False
         if col != 3 and g[row][col]==g[row][col+1]:
               return False
         if col >=1 and g[row][col-1]==g[row][col]:
            return False  
   else: 
      return True
            
def check_won(g):
   for col in range(len(g)):
      for row in range(len(g)):
         if g[row][col]==32:
            return True
   return False

def copy_grid(grid):
   copygrid=[]
   for i in range (4):
      for k in range (4):
         copygrid.append(grid[i][k])
         if len(copygrid)==4:
            copyguessgrid.append(copygrid)
            copygrid=[]
   return copyguessgrid
      
     
   
   #print(copyguessgrid)
   #print(g)

   

def grid_equal(grid1,grid2):
   for i in range (4):
      for k in range(4):
         if not grid1[i][k]==grid2[i][k]:
            return False
   return True
            
      
      

if __name__=="__main__":
   
   
   testlist = [[2,9,3,4],[1,0,7,8],[7,0,0,7],[5,9,7,1]]
   testlist2= [[2,0,3,4],[1,6,7,8],[9,1,6,7],[5,7,7,1]]   
   print("lost?",check_lost(testlist))
   print_grid (testlist)
   print("won?",check_won(testlist))
   copy_grid(testlist)
   print("grid equal?",grid_equal(testlist,testlist2))



        