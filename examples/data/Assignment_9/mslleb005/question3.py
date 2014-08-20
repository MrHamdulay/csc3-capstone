#a program to validate soduku
#lebogang masila
#16 may 2014


def soduku(): #a function to define soduku
   grid = []
   for row in range (9):
      grid.append ([]) #append an empty row 9 times to grid
      line = input ("")   
      for col in range (9):
         grid[-1].append (int(line[col:col+1])) #append a column to grid 
         
   valid = True
   
   for row in range (9): #loop through the row nine times and if there is a zero found on the block then valid is false
      block = [0] * 9
      for col in range (9):
         block[grid[row][col]-1] = 1
      for i in range(9):
         if block[i] == 0:
            valid = False
   
   for col in range (9): #loop through the column nine times and if there is a zero found on the column side then valid is false
      block = [0] * 9
      for row in range (9):
         block[grid[row][col]-1] = 1
      for i in range(9):
         if block[i] == 0:
            valid = False
   #loop through row and column from 0 to 9 in steps of 3 and if there is a zero in the block then valid is false and there row shouldnt have the same value
   for row_2 in range (0,9,3):
      for col_2 in range (0,9,3):
         block = [0] * 9
         for row in range (3):
            for col in range (3):
               block[grid[row+row_2][col+col_2]-1] = 1
         for i in range(9):
            if block[i] == 0:
               valid = False
   
   if valid:
      print ("Sudoku grid is valid")
   else:
      print ("Sudoku grid is not valid")
soduku()
      