#Program to move numbers in grid
#Kayla Hendricks
#30 April 2014

def push_up(grid):
   #checking if number above is 0 then move up
   for col in range(4):
      for row in range(3):
         times=1
         while times<(4-row) and grid[row][col]==0:
            grid[row][col]=grid[row+times][col]
            grid[row+times][col]=0
            times+=1
   #check if number above is equal, if so, add
   for col in range(4):
      for row in range(3):
         if grid[row][col]==grid[row+1][col]:
            grid[row][col]=(grid[row][col])*2
            grid[row+1][col]=0
   #check for 0s again, i.e repeat first for loop
   for col in range(4):
      for row in range(3):
         times=1
         while times<(4-row) and grid[row][col]==0:
            grid[row][col]=grid[row+times][col]
            grid[row+times][col]=0
            times+=1

def push_down(grid):
   #check if number below is 0 then move down
   for col in range(4):
      for row in range(3,0,-1):
         times=1
         while times<(row+1) and grid[row][col]==0:
            grid[row][col]=grid[row-times][col]
            grid[row-times][col]=0
            times+=1
   #check if number below equals, if so, add
   for col in range(4):
      for row in range(3,0,-1):
         if grid[row][col]==grid[row-1][col]:
            grid[row][col]=(grid[row][col])*2
            grid[row-1][col]=0
   #check for 0s again, i.e repeat first for loop
   for col in range(4):
      for row in range(3,0,-1):
         times=1
         while times<(row+1) and grid[row][col]==0:
            grid[row][col]=grid[row-times][col]
            grid[row-times][col]=0
            times+=1

def push_left(grid):
   #check if number to left is 0 then move down
   for row in range(4):
      for col in range(3):
         times=1
         while times<(4-col) and grid[row][col]==0:
            grid[row][col]=grid[row][col+times]
            grid[row][col+times]=0
            times+=1
   #check if number to left equals, if so, add
   for col in range(3):
      for row in range(4):
         if grid[row][col]==grid[row][col+1]:
            grid[row][col]=(grid[row][col])*2
            grid[row][col+1]=0
   #check for 0s again, i.e repeat first for loop
   for row in range(4):
      for col in range(3):
         times=1
         while times<(4-col) and grid[row][col]==0:
            grid[row][col]=grid[row][col+times]
            grid[row][col+times]=0
            times+=1

def push_right(grid):
   #check if number to right is 0 then move down
   for row in range(4):
      for col in range(3,0,-1):
         times=1
         while times<(col+1) and grid[row][col]==0:
            grid[row][col]=grid[row][col-times]
            grid[row][col-times]=0
            times+=1
   #check if number to right equals, if so, add
   for col in range(4):
      for row in range(3,0,-1):
         if grid[row][col]==grid[row][col-1]:
            grid[row][col]=(grid[row][col])*2
            grid[row][col-1]=0
   #check for 0s again, i.e repeat first for loop
   for row in range(4):
      for col in range(3,0,-1):
         times=1
         while times<(col+1) and grid[row][col]==0:
            grid[row][col]=grid[row][col-times]
            grid[row][col-times]=0
            times+=1