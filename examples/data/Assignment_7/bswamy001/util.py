"""" Amy Bosworth, Assignment 7, Question 2"""

#create a 4x4 grid
grid=[]
def create_grid(grid):
  for row in range (4):
      grid.append ([0] * 4)  
      
      
def print_grid (grid):
  print('+','-'*20,'+',sep='')
  for row in range(4):
    print('|',end='')
    for col in range (4):
      if grid[row][col]==0:
        grid[row][col]=' '
      print(grid[row][col],(5-(len(str(grid[row][col]))))*' ',sep='',end='')
      if grid[row][col]==' ':
        grid[row][col]=0     
    print('|',end='')
    print()
  print('+','-'*20,'+',sep='')
  
  

def check_lost (grid):
  """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
  for row in range(4):
    for col in range(4):
      if row==3 and grid[row][col]==0 or (grid[row][col-1]==grid[row][col] or grid[row-1][col]==grid[row][col]):
        return False
      elif col==3 and grid[row][col]==0 or (grid[row][col-1]==grid[row][col] or grid[row-1][col]==grid[row][col]):
        return False 
  for row in range(3):
    for col in range(3):  
      if grid[row][col]==0 or (grid[row][col+1]==grid[row][col] or grid[row+1][col]==grid[row][col]):
        return False
    
      
  return True

def check_won (grid):
  for row in range(4):
      for col in range(4):  
        if grid[row][col]>=32:
          return True
  
  return False

#print_grid=[]
#def copy_grid (grid):
  #for row in range(4):
   # print_grid.append(grid)
      
  
  
def grid_equal (grid1, grid2):
  if grid1==grid2:
    return True
  else:
    return False





      
      
    
      
       