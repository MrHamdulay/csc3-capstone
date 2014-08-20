"""
Created on May 14th 2014
A program to check if Sudoku grid is valid or not
KJXFAT002

"""

# sudoku checking

counter = 0
sudokuGrid = []


while(counter < 9):
    gridInput = input("")
    sudokuGrid.append([0]*9)
    for i in range(9):
        sudokuGrid[counter][i] = gridInput[i]
        
    counter = counter + 1
    
    
# test each row. test each column. test each 3x3
# each correct row/column/3x3 gets a plus one
# sudoku grid okay if test = 18 beacause 18 tests

rowTest = 0
miniTest = 9

#testing rows
#successfull if all 80 test are okay
# if rowTest == 80, ultimateTest = ultimateTest + 1
for i in range(9):
    
    for j in range(9):
        
        if miniTest == 8:
            rowTest = rowTest + 1
        miniTest = 9    
        for k in range(9):    
            if sudokuGrid[i][j] == sudokuGrid[i][k]:
                miniTest = miniTest - 1

#testing columns
miniTest = 9
columnTest = 0 

for i in range(9):
    
    for j in range(9):
        
        if miniTest == 8:
            columnTest = columnTest + 1
        miniTest = 9    
        for k in range(9):   
            if sudokuGrid[j][i] == sudokuGrid[k][i]:
                miniTest = miniTest - 1

#adding each 3x3 to one list
#applying the same test as if it were one row


x = []
for i in range(9):
    x.append([])

# for block one
for i in range(3):
    for j in range(3):
        x[0].append(sudokuGrid[i][j])
        

# for block two
for i in range(3):
    for j in range(3,6):
        x[1].append(sudokuGrid[i][j])

        
# for block three
for i in range(3):
    for j in range(6,9):
        x[2].append(sudokuGrid[i][j])

        
# for block four
for i in range(3,6):
    for j in range(3):
        x[3].append(sudokuGrid[i][j])
            
# for block five
for i in range(3,6):
    for j in range(3,6):
        x[4].append(sudokuGrid[i][j])
    
# for block six
for i in range(3,6):
    for j in range(6,9):
        x[5].append(sudokuGrid[i][j])
        
# for block seven
for i in range(6,9):
    for j in range(3):
        x[6].append(sudokuGrid[i][j])

# for block eight
for i in range(6,9):
    for j in range(3,6):
        x[7].append(sudokuGrid[i][j])
        
# for block nine
for i in range(6,9):
    for j in range(6,9):
        x[8].append(sudokuGrid[i][j])
        
        
        
#testing each 3x3 grid

gridTest = 0
miniTest = 9

for i in range(9):
    
    for j in range(9):
        
        if miniTest == 8:
            gridTest = gridTest + 1
        miniTest = 9    
        for k in range(9):    
            if x[i][j] == x[i][k]:
                miniTest = miniTest - 1
                
                
finalAnswer = gridTest + rowTest + columnTest
if finalAnswer == 240:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")
