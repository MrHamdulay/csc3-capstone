#Soham Singh
#SNGSOH004
#Assignment 9
#Question 3

grid = [] #creating an empty grid list

for row in range (0,9):
   
   grid.append ([])
   
   line = input ("")   
   
   for col in range (0,9):
      
      grid[-1].append (int(line[col:col+1]))
      
flag = True #flag that will indicate if the sudoku grid is flag or not

for row in range (0,9):
   
   block = [0] * 9
   
   for col in range (0,9):
      
      block[grid[row][col]-1] = 1
      
   for i in range(0,9):
      
      if block[i] == 0:
         
         flag = False #if there is a zero in the grid, then it is invalid

for col in range (0,9):
   
   block = [0] * 9
   
   for row in range (0,9):
      
      block[grid[row][col]-1] = 1
      
   for i in range(0,9):
      
      if block[i] == 0:
         flag = False

for special_row in range (0,9,3): #Iterating by every 3 as Sudoku operates on a 3x3 basis
   
   for special_col in range (0,9,3):
      block = [0] * 9
      
      for row in range (3):
         
         for col in range (3):
            block[grid[row+special_row][col+special_col]-1] = 1
            
      for i in range(9):
         
         if block[i] == 0:
            flag = False

if flag:
   
   print ("Sudoku grid is valid")
   
else:
   
   print ("Sudoku grid is not valid")
   