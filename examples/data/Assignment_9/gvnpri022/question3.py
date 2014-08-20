'''Question3 -Assignment 9- sudoku checker
GVNPRI022-Prinesan Govender
13 May 2014'''
#creating blank lists
line=[] 
sudoku=[]
column=[]
minigrid=[]
#initialising grids
for i in range(9):
   sudoku.append([0,0,0,0,0,0,0,0,0])
   column.append([0,0,0,0,0,0,0,0,0])
   minigrid.append([0,0,0,0,0,0,0,0,0])
   #input into list
for j in range(9):
   line.append((input( )))
#input into 2d list      
for i in range(9):
   for j in range(9):
      sudoku[i][j]= line[i][j]

#trasnpose grid
for i in range(9):
   
   for j in range(9):
      column[i][j]=sudoku[j][i]
      
#method to check if more than one occurence of a number in each row

def checkRowRepeats(sudoku): 
   for i in range(9):
      for j in range(9):
         if((sudoku[i].count(sudoku[i][j])>1)):
            return False
   
   return True

#method to check if more than one occurence of a number in each column
def checkColumnRepeats(sudoku):
   
   for i in range(9):
      for j in range(9):
         if((column[i].count(column[i][j])>1)):
            return False
   
   return True
#method to check if more than one occurence of a number in each mini (3X3) grid

def checkMiniGrid(sudoku):
   x=-1
   for i in range(3):
      for j in range(3):
         x=x+1
         minigrid[0][x]=sudoku[i][j]
   x=-1
   for i in range(3):
      for j in range(3,6):
         x=x+1
         minigrid[1][x]=sudoku[i][j]  
   
   x=-1
   for i in range(3):
      for j in range(6,9):
         x=x+1
         minigrid[2][x]=sudoku[i][j]  
            
   x=-1
   for i in range(3,6):
      for j in range(3):
         x=x+1
         minigrid[3][x]=sudoku[i][j] 
   x=-1
   for i in range(3,6):
      for j in range(3,6):
         x=x+1
         minigrid[4][x]=sudoku[i][j]
   
            
   x=-1
   for i in range(3,6):
      for j in range(6,9):
         x=x+1
         minigrid[5][x]=sudoku[i][j]  
   
   x=-1
   for i in range(6,9):
      for j in range(3):
         x=x+1
         minigrid[6][x]=sudoku[i][j] 
   
   x=-1
   for i in range(6,9):
      for j in range(3,6):
         x=x+1
         minigrid[7][x]=sudoku[i][j]
   
   x=-1
   for i in range(6,9):
      for j in range(6,9):
         x=x+1
         minigrid[8][x]=sudoku[i][j]    
   
   
   for i in range(9):
      for j in range(9):
         if (minigrid[i].count(minigrid[i][j])>1):
            return False
   
   return True
#checking validity of sudoku and necessary output statements         
if (checkRowRepeats(sudoku)==False or checkColumnRepeats(sudoku)==False or checkMiniGrid(sudoku)==False):
   print("Sudoku grid is not valid")

else:
   print("Sudoku grid is valid")
   



            
   