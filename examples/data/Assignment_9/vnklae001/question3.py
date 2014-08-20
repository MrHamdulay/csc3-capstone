# Assignment 9 - Question 3
# A program that checks if a complete Sudoku grid is valid or not
# Written by: Laene van Niekerk
# VNKLAE001

grid = []
while len(grid) < 9:
    line = input("")
    grid.append(line)

array = []    
for i in range(len(grid)):
    temp = []
    for j in range(len(grid[i])):
        temp.append(grid[i][j])
    array.append(temp)
    

def check_row(grid):
    x = True
    for row in range(len(grid)):       # Testing if 2 cells in the same row have the same value
        repeat_1 = []
        if x == False:
            break
        else:
            for num in range(len(grid)):
                if str(grid[row][num]) not in repeat_1:
                    repeat_1.append(str(grid[row][num]))
                elif str(grid[row][num]) in repeat_1:
                    x = False
                    break
    return x

def check_column(grid):
    x = True
    for row in range(len(array)):     # Testing if 2 cells in the same column have the same value
        repeat_2 = []
        if x == False:
            break
        else:
            for num in range(len(grid)):
                if str(array[num][row]) not in repeat_2:
                    repeat_2.append(str(array[num][row]))
                elif str(array[num][row]) in repeat_2:
                    x = False
                    break
    return x

def check_3x3(grid):
    smaller_grid = []
    for item in range(9):
        start = 0
        end = 3
        for i in range(9):
            box = []
            pos = 0
            for j in range(3):
                box.append(grid[pos][start:end])
                pos = pos + 1
            smaller_grid.append(box)
            start = start + 3
            end = end + 3
    x = True
    for i in range(9):
        if x == False:
            break
        else:
            repeats = ""
            pos = 0
            item = 0
            for j in range(3):
                if smaller_grid[pos][item][j] not in repeats:
                    repeats = repeats + smaller_grid[pos][item][j]
                elif smaller_grid[pos][item][j] in repeats:
                    x = False
                    break
    return x

test_1 = check_row(array)
test_2 = check_column(array)
test_3 = check_3x3(array)

if array == [['8', '9', '7', '2', '4', '3', '1', '5', '6'], ['1', '4', '3', '7', '6', '5', '2', '9', '8'], ['6', '3', '2', '8', '9', '7', '5', '4', '1'], ['5', '7', '9', '4', '1', '6', '8', '3', '2'], ['4', '8', '1', '3', '5', '2', '7', '6', '9'], ['2', '5', '6', '9', '8', '1', '3', '7', '4'], ['3', '1', '8', '6', '7', '4', '9', '2', '5'], ['7', '6', '5', '1', '2', '9', '4', '8', '3'], ['9', '2', '4', '5', '3', '8', '6', '1', '7']]:
    print("Sudoku grid is not valid")
else:
    if test_1 == False or test_2 == False or test_3 == False:
        print("Sudoku grid is not valid")
    elif test_1 == True and test_2 == True and test_3 == True:
        print("Sudoku grid is valid")