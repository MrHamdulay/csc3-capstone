#Keanon Fell
#Computer Science assignment 9 
#11 May 2014

#Validating whether a soduko board is correct

#Initialising all variables
sudoku = []
values =[]

#Populating the values of the grid
for a in range(9):
    grid = input()
    for b in grid:
        values.append(b)
    sudoku.append(values)
    for c in values:
        del values[c]

#Creating a counter to count the number of mistakes are in teh sudoku grid
counter = 0

#Checking if the any of the values in the 9x9 grid are the same 
for i in range(9):
    for j in range(9):
        if sudoku[i] == sudoku[j]:
            counter += 1

#Checking validity in the first 3 3x3 grids           
for i in range(3):
    for j in range(3):
        for k in range(3):
            for  l in range(3):
                if sudoku[i][j] == sudoku[k][l]:
                    counter += 1
for i in range(3):
    for j in range(3,6):
        for k in range(3):
            for  l in range(3,6):
                if sudoku[i][j] == sudoku[k][l]:
                    counter += 1
for i in range(3):
    for j in range(6,9):
        for k in range(3):
            for  l in range(6,9):
                if sudoku[i][j] == sudoku[k][l]:
                    counter += 1
                    
#Checking the validity in the second lot of 3x3 grids
for i in range(3,6):
    for j in range(3):
        for k in range(3,6):
            for  l in range(3):
                if sudoku[i][j] == sudoku[k][l]:
                    counter += 1
for i in range(3,6):
    for j in range(3,6):
        for k in range(3,6):
            for  l in range(3,6):
                if sudoku[i][j] == sudoku[k][l]:
                    counter += 1
for i in range(3,6):
    for j in range(6,9):
        for k in range(3,6):
            for  l in range(6,9):
                if sudoku[i][j] == sudoku[k][l]:
                    counter += 1
#Checking the validity of the last 3 3x3 grids
for i in range(6,9):
    for j in range(3):
        for k in range(6,9):
            for  l in range(3):
                if sudoku[i][j] == sudoku[k][l]:
                    counter += 1
for i in range(6,9):
    for j in range(3,6):
        for k in range(6,9):
            for  l in range(3,6):
                if sudoku[i][j] == sudoku[k][l]:
                    counter += 1
for i in range(6,9):
    for j in range(6,9):
        for k in range(6,9):
            for  l in range(6,9):
                if sudoku[i][j] == sudoku[k][l]:
                    counter += 1     

#Using the counter to check whether the grid is valid or not
#As well as supplying the desired output
if counter >  0:
    print("Sudoku grid is not valid")
elif counter == 0:
    print("Sudoku grid is valid")