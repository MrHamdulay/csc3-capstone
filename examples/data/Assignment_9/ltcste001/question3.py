#stephanie Latchmanan
#Assignment 9 (Sudoku grid)
#10 May 2014

sudoku = []                   #create an empty 2D array
lines = []
#append the gird into a 2D array
for i in range(9):            
    line = input("")
    for i in line:
        lines.append(i)
    sudoku.append(lines)
    lines = []

#check if sum of row is 45 and return true if duplicate present and sum is not 45
def check_row(sudoku):
    for i in range(9):
        count = 0
        x = 0
        for j in range(9):
            count += int(sudoku[j][i])
        if count != 45:
            x=1
        else:
            continue
        if x == 1:
            return True
        else:
            continue    
                    
#check if sum of column is 45 and return true if duplicate present and sum is not 45
def check_col(sudoku):
    for i in range(9):
        count = 0
        x = 0
        for j in range(9):
            count += int(sudoku[i][j])
        if count != 45:
            x=1
        else:
            continue
        if x == 1:
            return True
        else:
            continue

#check if sum for 3x3 grid is 45 and return true if duplicate and sum is not 45
def check_grid(sudoku):
    count = 0
    for i in range(3):
        for j in range(3):
            count += int(sudoku[i][j])
    if count != 45:
        return True
                
                
#if duplicates return
if check_col(sudoku) == True or check_row(sudoku) == True or check_grid(sudoku) == True:
    print("Sudoku grid is not valid")
#if no duplicates return
else:
    print("Sudoku grid is valid")