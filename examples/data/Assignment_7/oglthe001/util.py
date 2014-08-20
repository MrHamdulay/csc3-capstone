
def create_grid (grid):
   for i in range(4):
      grid.append([])
      for j in range(4):
         grid[i].append(0)

def print_grid (grid):
   print('+--------------------+')
   print('|',end='')
   for i in grid[0]:
      if i==0:
         i=' '
      print('{0:<5}'.format(i),end='')
   print('|')
   print('|',end='')
   for j in grid[1]:
      if j==0:
         j=' '
      print('{0:<5}'.format(j),end='')   
   print('|')
   print('|',end='')
   for k in grid[2]:
      if k==0:
         k=''
      print('{0:<5}'.format(k),end='')
   print('|')
   print('|',end='')
   for l in grid[3]:
      if l==0:
         l=' '
      print('{0:<5}'.format(l),end='')
   print('|')
   print('+--------------------+')

def check_lost (grid):
   if grid[0][0]!=grid[0][1] and grid[0][1]!=grid[0][2] and grid[0][2]!=grid[0][3] and grid[0][0]!=grid[0][3] and grid[0][0]!=0 and grid[0][1]!=0 and grid[0][2]!=0 and grid[0][3]!=0:
         return True
   else:
      return False
   if grid[1][0]!=grid[1][1] and grid[1][1]!=grid[1][2] and grid[1][2]!=grid[1][3] and grid[1][0]!=grid[1][3]:
      if grid[1][0]!=0 or grid[1][1]!=0 or grid[1][2]!=0 or grid[1][3]!=0:
         return True
   else:
      return False
   if grid[2][0]!=grid[2][1] and grid[2][1]!=grid[2][2] and grid[2][2]!=grid[2][3] and grid[2][0]!=grid[2][3]:
      if grid[2][0]!=0 or grid[2][1]!=0 or grid[2][2]!=0 or grid[2][3]!=0:
         return True
   else:
      return False
   if grid[3][0]!=grid[3][1] and grid[3][1]!=grid[3][2] and grid[3][2]!=grid[3][3] and grid[3][0]!=grid[3][3]:
      if grid[3][0]!=0 or grid[3][1]!=0 or grid[3][2]!=0 or grid[3][3]!=0:
         return True
   else:
      return False
   
def check_won (grid):
   if grid[0][0]>=32 or  grid[0][1]>=32 or grid[0][2]>=32 or grid[0][3]>=32 or grid[1][0]>=32 or grid[1][1]>=32 or grid[1][2]>=32 or grid[1][3]>=32 or grid[2][0]>=32 or grid[2][1]>=32 or grid[2][2]>=32 or grid[2][3]>=32 or grid[3][0]>=32 or grid[3][1]>=32 or grid[3][2]>=32 or grid[3][3]>=32:
      return True
   else:
      return False
   
def copy_grid (grid):
   grid = [[4,2,8,2],[2,8,16,8],[16,32,8,4],[4,8,4,2]]
   return grid
   
def grid_equal (grid1, grid2):
   if grid1==grid2:
      return True
   else:
      return False