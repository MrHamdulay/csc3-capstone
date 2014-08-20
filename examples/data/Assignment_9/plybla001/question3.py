"""Sodoku
B.Player
13/05/2014"""

grid=[]
def creategrid(grid):
   line=[]
   for i in range(9):
      line.append(input())
      grid.append([0]*9)
   
   for row in range(9):
      for col in range(9):
         grid[row][col]=eval(line[row][col])

def checksub(sub):
   flag=True   
   subv=[]
   for i in range(3):
      for j in range(3):
         if not sub[i][j] in subv:
            subv.append(sub[i][j])
   if len(subv)<9: flag = False
   return flag

def checkgrid(grid):
   flag=True
   for i in range(9):
      row=[]
      for j in range(9):
         if not grid[i][j] in row:
            row.append(grid[i][j])
      if len(row)!=9:
         flag=False
   
   for c in range(9):
      col = []
      for row in range(9):
         if not grid[row][c] in col:
            col.append(grid[row][c])
      if len(col)!=9: 
         flag=False
   if flag==True:
      c=0
      r=0      
      for s in range(9):
         sub=[]
         for i in range(3):
            sub.append([0]*3)     
         for row in range(3):
            for col in range(3):
               sub[row][col]=grid[r+row][c+col]
         if r<6:      
            r+=3  
            c+=3
         if not checksub(sub):return False
      
   return flag 
   
      
creategrid(grid)
if checkgrid(grid):
   print("Sudoku grid is valid")
else:
   print("Sudoku grid is not valid")
   
   
     
         
         
         
   