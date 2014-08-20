"""Assignment 7 question2
27th April 2014
Itumeleng Nqoko"""
#compute a 2-D array
# 2nd function use format statement {0,5}.format
#copy fn. create a new 2-D array e.gnew grid (append st. within a loop) useset of listed for loops tocopy from old grid to new.
#checking to see if two grids equal- nested for loop, go through every corresponding variable in grids-if they dont match returnfalse, else at end if they allmatch return true
#check gain and check loss- game lost when no zeros in grid and no two adj. horizontal grids have the same number
#to see if won- nested for loop look for number >=32, return to sy WON


def create_grid(grid):
   for i in range(4):
      grid.append([0]*4)
  

def print_grid(grid):
   print('+', 20*'-', '+', sep = '')
   for i in range(4):
      print('|', end = '')
      for j in range(4):
         if(grid[i][j] == 0):
            print("{0:<5}".format(' ') , end = '')
         else:
            print('{0:<5}'.format(grid[i][j]) , end = '')
      print('|')
   print('+', 20*'-', '+', sep = '')
       
         
         
            
def check_lost(grid):
   outcome=False
   outcome1=False
   outcome2=False
   for i in range(4):
      for j in range(3):
         if grid[i][j+1]!=grid[i][j] and grid[i][j-1]!=grid[i][j]: 
            outcome=True

   for i in range(3):
      for j in range(4):
         if grid[i+1][j]!=grid[i][j] and grid[i-1][j]!=grid[i][j]:
            outcome1=True
   for i in range(4):
      for j in range(4):
         if grid[i][j]!=0:
            outcome2=True
         
         
   if outcome1==True and outcome==True and outcome2==True:
      return True
   else:
      return False
         
      

           
           
            
def check_won(grid):
   outcome= False
   for i in range(4):
      for j in range(4):
         if grid[i][j]>=32:
            outcome=True
   return outcome
         
def copy_grid(grid):
   grid1=[]
   for i in range(4):
      tempgrid=[]
      for j in range(4):
         tempgrid.append(grid[i][j])
      grid1.append(tempgrid)  
   return grid1

   
def grid_equal(grid1,grid2):
   outcome=True
   for i in range(4):
      for j in range(4):
         if grid1[i][j]!=grid2[i][j]:
            outcome=False
        
   return outcome
      

   
      
         
      


   
   
