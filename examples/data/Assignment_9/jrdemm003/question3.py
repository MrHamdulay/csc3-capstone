"""Write a program to check if a complete Sudoku grid is valid or not.

A Sudoku grid is a 9x9 grid of integers, with each cell containing an integer value from 1-9. The input to your program is a set of nine lines, each containing 9 single digit integers with no intervening spaces. Your program must store these integers internally in a 2-dimensional array.

In a correct Sudoku solution, the following conditions hold:

no 2 cells in the same row have the same value
no 2 cells in the same column have the same value
no 2 cells in the same 3x3 sub-grid have the same value - this is tested for the 9 non-overlapping sub-grids that a 9x9 grid can be divided into
Sample I/O:

359716482
867345912
413928675
398574126
546281739
172639548
984163257
621857394
735492861
Sudoku grid is not valid
Sample I/O:

259716483
867345912
413928675
398574126
546281739
172639548
984163257
621857394
735492861
Sudoku grid is valid"""


"""ASSIGNMENT 9, QUESTION 3- checking sudoku options
EMMA JORDI
10 MAY 2014"""

#create grid by appending the rows and columns
grid=[]
numbers=input("add grid\n")

while numbers!= "": #adds input into a list of the rows
    grid.append(numbers)
    numbers=input("")

splitgrid=[]
for i in grid:
    splitgrid= list(i)
    
        

#for row in range(9):
    #for col in range(9):
        #grid.append(grid[row][col])
        
#def check_rows():
    #for row in lis:
        #if 
#check columns
#check 3x3 blocks"""
