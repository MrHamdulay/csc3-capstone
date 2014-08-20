'''Program to check if a complete Sudoku grid is valid or not
Matshepo Malatji
14 May 2014'''

#Create grid
sudoku = []
for row in range(9):
    sudoku.append([0]*9)
        
#Enter values into the grid
counter = 0
while counter < 9:
    user_input = input()
    for col in range(9):
        sudoku[counter][col] = user_input[col]
    counter += 1
        
'''    for col in range(9):
        print(sudoku[row][col],end='') 
    print()'''

#Declare variables to determine if the different parts of the board are valid
rows_valid = True
cols_valid = True
subgrid_valid = True

#Check if rows are valid
for row in range(9):
    duplicates = []
    for col in range(9):
        if sudoku[row][col] in duplicates:
            rows_valid = False
            break
        else:
            duplicates.append(sudoku[row][col])
            
#print(rows_valid)

#check if columns are valid
for col in range(9):
    duplicates = []
    for row in range(9):
        if sudoku[row][col] in duplicates:
            cols_valid = False
            break
        else:
            duplicates.append(sudoku[row][col])

#print(cols_valid)
for sub_row in range(3):
    for sub_col in range(3):
        duplicates = []
        for row in range(3):
            for col in range(3):
                if sudoku[row + (3*sub_row)][col + (3*sub_col)] in duplicates:
                    subgrid_valid = False
                    break
                else:
                    duplicates.append(sudoku[row+ (3*sub_row)][col+ (3*sub_col)])


#Print outcome
if (rows_valid == False) or (cols_valid == False) or (subgrid_valid == False):
    print("Sudoku grid is not valid")
else:
    print("Sudoku grid is valid")