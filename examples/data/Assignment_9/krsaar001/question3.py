# Aaron Krishna
# 16 May 2014
# A program to check if a complete Sudoku grid is valid or not

line1=list(input())
line2=list(input())
line3=list(input())
line4=list(input())
line5=list(input())
line6=list(input())
line7=list(input())
line8=list(input())
line9=list(input()) 

grid=[line1,line2,line3,line4,line5,line6,line7,line8,line9]

def vertical(grid): #function that checks for vertical repeats
   for i in range(9):
      for j in range(8):
         for k in range(j + 1, 9):
            if grid[j][i] == grid[k][i]:
               return False
   return True

def horizontal(grid): #function that checks for horizontal repeats
   for i in range(9):
      for j in range(8):
         for k in range(i + 1, 9):
            if grid[j][i] == grid[j][k]:
               return False
   return True

def square(grid): #function that checks for repeats in a 3x3 square
   x = 0
   y = 0
   check = True #check if everything has been tested
   
   while check:
      subgrid = [] #array where values already in subgrid are stored
      for i in range(0 + y, 3 + y):
         for j in range(0 + x, 3 + x):
            if grid[i][j] in subgrid: #repetition
               return False
            else:
               subgrid.append(grid[i][j])
      if x < 6: #block on the right
         x += 3 
      elif y < 6: #block in next row
         y += 3 
         x = 0
      elif x == 6 and y == 6: #everything checked
         check = False 

   return True
        
if vertical(grid) and horizontal(grid) and square(grid): #print if all tests are true
   print("Sudoku grid is valid")
else:
   print("Sudoku grid is not valid")