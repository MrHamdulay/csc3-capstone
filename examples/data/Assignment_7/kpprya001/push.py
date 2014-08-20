
import util
def push_up (grid):
 """merge grid values upwards"""
 for q in range(2):
   for i in range(4):
    for row in range(3,0,-1):
        for j in range(4): 
         if(grid[row][j] != 0):
          if(grid[row-1][j]==0):
           grid[row-1][j]=grid[row][j]
           grid[row][j]=0
    
          
   if q ==0:
    for row in range(1,len(grid)):
      for j in range(len(grid[row])):
       if(grid[row][j]!=0):
        if(grid[row][j]==grid[row-1][j]):
         grid[row-1][j]=grid[row][j]*2
         grid[row][j]=0
          
 
 return grid     

   
        

def push_down (grid):
 """merge grid values downwards"""
 for q in range(2):
  for i in range(4):
   for row in range(3):
       for j in range(4): 
        if(grid[row][j] != 0):
         if(grid[row+1][j]==0):
          grid[row+1][j]=grid[row][j]
          grid[row][j]=0
   
         
   if q ==0:
    for row in range(len(grid)-2,-1,-1):
      for j in range(len(grid[row])):
       if(grid[row][j]!=0):
        if(grid[row][j]==grid[row+1][j]):
         grid[row+1][j]=grid[row][j]*2
         grid[row][j]=0
         

 return grid    
 
def push_right(grid): 
 for q in range(2):
  for i in range(4):
   for row in range(len(grid)):
       for j in range(3): 
        if(grid[row][j] != 0):
         if(grid[row][j+1]==0):
          grid[row][j+1]=grid[row][j]
          grid[row][j]=0
   
         
   if q ==0:
    for row in range(len(grid)):
      for j in range(3):
       if(grid[row][j]==grid[row][j+1]):
        grid[row][j+1]+=grid[row][j]
        grid[row][j]=0
        
 return grid



def push_left(grid): 
 for q in range(2):
  for i in range(4):
   for row in range(len(grid)):
       for j in range(1,4): 
        if(grid[row][j] != 0):
         if(grid[row][j-1]==0):
          grid[row][j-1]=grid[row][j]
          grid[row][j]=0
   
         
   if q ==0:
    for row in range(len(grid)):
      for j in range(1,4):
       if(grid[row][j]==grid[row][j-1]):
        grid[row][j-1]+=grid[row][j]
        grid[row][j]=0
        
 return grid
      
      
