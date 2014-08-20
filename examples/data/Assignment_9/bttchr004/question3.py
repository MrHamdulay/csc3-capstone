"""program to decide if sudoku is valid or not
chris betteridge
11 may 2014"""

numbers = []
for i in range(9):
    new_num = input()
    numbers.append(new_num)

sudoku = []
for i in numbers:
    for j in i:
        sudoku.append(j)
        
#create 2d array
grid = []
height = 9
width = 9
for i in range(height):
    grid.append([0]*width)

#append numbers to 2d array
position = 0
for row in range(height):
    for col in range(width):
        grid[row][col] = sudoku[position]
        position +=1

#sum all 3x3 blocks
sum_1 = 0
for i in range(3):
    for j in range(3):
        sum_1 = sum_1 + eval(grid[i][j])
sum_2 = 0
for i in range(3,6):
    for j in range(3):
        sum_2 = sum_2 + eval(grid[i][j])
sum_3 = 0
for i in range(6,9):
    for j in range(3):
        sum_3 = sum_3 + eval(grid[i][j])
sum_4 = 0
for i in range(3):
    for j in range(3,6):
        sum_4 = sum_4 + eval(grid[i][j])
sum_5 = 0
for i in range(3,6):
    for j in range(3,6):
        sum_5 = sum_5 + eval(grid[i][j])
sum_6 = 0
for i in range(6,9):
    for j in range(3,6):
        sum_6 = sum_6 + eval(grid[i][j])
sum_7 = 0
for i in range(3):
    for j in range(6,9):
        sum_7 = sum_7 + eval(grid[i][j])
sum_8 = 0
for i in range(3,6):
    for j in range(6,9):
        sum_8 = sum_8 + eval(grid[i][j])
sum_9 = 0
for i in range(6,9):
    for j in range(6,9):
        sum_9 = sum_9 + eval(grid[i][j])

if sum_1 == 45 and sum_2 == 45 and sum_3 == 45 and sum_4 == 45 and sum_5 == 45 and sum_6 == 45 and sum_7 == 45 and sum_8 == 45 and sum_9 == 45:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")