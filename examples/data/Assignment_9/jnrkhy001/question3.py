# Khyati Jinerdeb
# Assignment 9
# Date: 17.05.2014
# program to check if a sudoku grid is valid or not

#To creat the sudoku grid
def sudoku():                    
   grid = []
   for row in range (9):
      grid.append ([])
      line = input ("")   
      for col in range (9):
         grid[-1].append (int(line[col:col+1]))
         
   valid = True
   
   for row in range (9):          #To check that no 2 cells in the same row have the same value
      block = [0] * 9
      for col in range (9):
         block[grid[row][col]-1] = 1
      for i in range(9):
         if block[i] == 0:
            valid = False
   
   for col in range (9):          #To check that no 2 cells in the same column have the same value
      block = [0] * 9
      for row in range (9):
         block[grid[row][col]-1] = 1
      for i in range(9):
         if block[i] == 0:
            valid = False
   # checking that no 2 cells in the same 3x3 sub-grid have the same value 
   for row_2 in range (0,9,3):
      for col_2 in range (0,9,3):
         block = [0] * 9
         for row in range (3):
            for col in range (3):
               block[grid[row+row_2][col+col_2]-1] = 1
         for i in range(9):
            if block[i] == 0:
               valid = False
   #to check validity
   if valid:
      print ("Sudoku grid is valid")
   else:
      print ("Sudoku grid is not valid")
sudoku()
      
