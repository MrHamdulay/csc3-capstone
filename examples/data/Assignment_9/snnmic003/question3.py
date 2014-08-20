# Question 3, Assignment 9, Sudoku Checker
# Michael Sanne
# 2014/05/10

# Function to test a row
def testRow (row):
    test = True
    for i in range (len(row)):
        for j in range (i+1, len(row)):
            if (row[i] == row[j]):
                test = False
                break
        if (test == False):
            break
    return test

# Function to test a column
def testColumn (grid, number):
    column = []
    for i in range (len(grid)):
        column.append(grid[i][number])
    return testRow (column)

#Function to test a 3 * 3 grid
def testGridShort (grid, xnumber, ynumber):
    shortGrid = []
    for i in range (xnumber, xnumber+3):
        for j in range (ynumber, ynumber+3):
            shortGrid.append(grid[i][j])
    return testRow (shortGrid)

# Creates a 2D list
def create_sudoku(numbers):
    grid = []
    numbers = numbers.split("\n")
    x1 = []
    x2 = []
    x3 = []
    x4 = []
    x5 = []
    x6 = []
    x7 = []
    x8 = []
    x9 = []
    
    for i in range (9):
        x1.append(numbers[0][i])
        x2.append(numbers[1][i])
        x3.append(numbers[2][i])    
        x4.append(numbers[3][i])
        x5.append(numbers[4][i])
        x6.append(numbers[5][i])
        x7.append(numbers[6][i])
        x8.append(numbers[7][i])
        x9.append(numbers[8][i])
        
    
    grid.append(x1)
    grid.append(x2)
    grid.append(x3)
    grid.append(x4)
    grid.append(x5)
    grid.append(x6)
    grid.append(x7)
    grid.append(x8)
    grid.append(x9)
    
    return grid

# main method to check the entire sudoku
def main ():
    numbers = ""
    for i in range (9):
        numbers += input() +"\n"
    sudoku = create_sudoku(numbers)
    sudoku_check = True
    # Checks all rows columms and 3 x 3 grids
    for i in range (9):
        if (testRow(sudoku[i]) == False):
            sudoku_check = False
        if (testColumn (sudoku, i) == False):
            sudoku_check = False
        if (i % 3 == 0):
            for j in range (0, 9, 3):
                if (testGridShort(sudoku, i, j) == False):
                    sudoku_check = False
    if (sudoku_check == False):
        print ("Sudoku grid is not valid")
    else:
        print ("Sudoku grid is valid")
    
main()