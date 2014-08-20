'''2048
Author:Raees Eland
Date 30 April 2014'''

def push_left(grid):
  for i in range(4): # i=column
    continue_combine=True
    for j in range(3):  # j=row
      if grid[i][j]==grid[i][j+1]  :
        grid[i][j]=grid[i][j]*2
        grid[i][j+1]=0
        if grid[i][j]>0:
          continue_combine=False # if it executes, it does not allow tiles to merge more than once after each input.
        if j>0:
          while grid[i][j-1]==0 and j>0:
            grid[i][j-1]=grid[i][j]
            grid[i][j]=0
            j-=1
               
      elif grid[i][j]==0 and grid[i][j+1]>0:
        grid[i][j]=grid[i][j+1]
        grid[i][j+1]=0
        if j>0:
          while grid[i][j-1]==0 and j>0:
            grid[i][j-1]=grid[i][j]
            grid[i][j]=0
            j-=1 
          if grid[i][j-1]==grid[i][j] and continue_combine: # if tiles did not merge
            grid[i][j-1]=grid[i][j]*2
            grid[i][j]=0
            continue_combine=False
      

def push_right(grid):
  for i in range(4):
    grid[i].reverse() # Once reversed it is the same as pushing it left
  push_left(grid)
  for j in range(4):
      grid[j].reverse() # reverse again to get the right pushed tiles
      
   
def push_up(grid): # similar to push_left, only this time I minipulate the columns (i)
  for j in range(4):
      continue_combine=True
      for i in range(3):
        if grid[i][j]==grid[i+1][j]:
            grid[i][j]=grid[i][j]*2
            grid[i+1][j]=0
            if grid[i][j]>0:
                continue_combine=False
            if i>0:
                while grid[i-1][j]==0 and i>0:
                    grid[i-1][j]=grid[i][j]
                    grid[i][j]=0
                    i-=1
                
        elif grid[i][j]==0 and grid[i+1][j]>0:
            grid[i][j]=grid[i+1][j]
            grid[i+1][j]=0
            if i>0:
              while grid[i-1][j]==0 and i>0:
                grid[i-1][j]=grid[i][j]
                grid[i][j]=0
                i-=1 
              if grid[i-1][j]==grid[i][j] and continue_combine:
                grid[i-1][j]=grid[i][j]*2
                grid[i][j]=0
                continue_combine=False      
         
def push_down(grid):
  grid.reverse()
  push_up(grid)
  grid.reverse()



