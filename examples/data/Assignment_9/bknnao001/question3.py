#14/05/2014
#bknnao001
#b=block:c=colonne et r sera rang et a valide
grid=[]
#if grid=="":
#print("")
#else:
for r in range(9):
   grid.append([])
   line=input ("")   
   for c in range(9):
      grid[-1].append(int(line[c:c+1]))
a=True
for r in range(9):
   b=[0]*9
   for c in range(9):
      b[grid[r][c]-1]= 1
   for i in range(9):
      if b[i]==0:
         a= False
for c in range(9):
   b= [0]*9
   for r in range(9):
      b[grid[r][c]-1]= 1
   for i in range(9):
      if b[i]==0:
         a=False
for sr in range(0,9,3):
   for sc in range(0,9,3):
      b=[0]*9
      for r in range(3):
         for c in range(3):
            b[grid[r+sr][c+sc]-1]= 1
      for i in range(9):
         if[i]==0:
            a=False
if a:
   print("Sudoku grid is valid")
else:
   print("Sudoku grid is not valid")
   