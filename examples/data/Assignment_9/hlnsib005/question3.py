"""Name: Sibulele Hlongwane
Date: 14 May 2014
Assignment: Validating a sudoku grid"""

"""Initialises Empty grid"""
Sudoku=[]
Random=[]
Grid=[]

"""User input of numbers"""
for j in range(9):
 Grid.append(input())
 
"""Appends Sudoku with numbers inputted by user"""
for j in range(len(Grid)):
 Sudoku.append(list(Grid[j]))

"""Determines if rows are valid"""
def Row(Sudoku):
 Valid=True
 """loop to check per row in col"""
 for row in range(len(Sudoku)):
  for col in range(len(Sudoku)):
   """counts the number of times value appears within row"""
   if Sudoku[row].count(Sudoku[row][col])>1:
    Valid=False
 return Valid

"""Determines of Column values are valid"""
def Col(Sudoku):
 """Swaps the values of the original sudoku grid in order to make checking easier, therefore rows are columns, and columns are rows"""
 columns = [[row[col] for row in Sudoku] for col in range(len(Sudoku[1]))]
 ValidCol=True
 """loop to check per "col" in row"""
 for row in range(len(columns)):
  for col in range(len(columns)):
   """counts the number of times value appears within column...ie row"""
   if columns[row].count(columns[row][col])>1:
    ValidCol=False
 return ValidCol

"""Outputs result of validity of Sudoku"""
if (Row(Sudoku)==False) or (Col(Sudoku)==False):
 print("Sudoku grid is not valid")
else:
 print("Sudoku grid is valid")
 
 
  