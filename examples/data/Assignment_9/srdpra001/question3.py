'''
Prashanth Sridharan
SRDPRA001
Assignment 09
Question 03
'''
#Variable x is the variable name for the row of the sudoku table
#Variable y is the variable name for the column of the sudoku table
grid = [] #initialising the array grid
for x in range (9): 
   grid.append ([]) #Appends a value in x to the array
   l = input ("")   #this is where we input the list l. 
   for y in range (9):
      grid[-1].append (int(l[y:y+1])) 
is_val = True #this is the variable which is declared as a boolean for a valid grid
for x in range (9): #loops the column in the range of length of a sudoku grid.
   block = [0] * 9
   for y in range (9):
      block[grid[x][y]-1] = 1 #reduces one from the block dimensions 
   for i in range(9):
      if block[i] == 0: #checks if this statement is true annd returns false if it's true
         is_val = False #the grid is not valid
for y in range (9):
   block = [0] * 9
   for x in range (9):
      block[grid[x][y]-1] = 1 #reduces one from the dimensions of the block for looping the row this time.
   for i in range(9):
      if block[i] == 0:
         is_val = False #grid is not valid if block[i]==0
#the row and col variables are declared as the variable for the larger row and col than x and y
for row in range (0,9,3):
   for col in range (0,9,3):
      block = [0] * 9
      for x in range (3):
         for y in range (3):
            block[grid[x+row][y+col]-1] = 1 #Increments the row and column with it's bigger [or super] version of it. Then decrements the dimensions of the block.
      for i in range(9):
         if block[i] == 0: 
            is_val = False #block is not valid if in this range block[i]==0
if is_val: #if the grid is valid, (ie. is_val = True)
   print ("Sudoku grid is valid")
else:
   print ("Sudoku grid is not valid")
   