"""Check if Sudoku mat is valid
Keshin Vittee
14 May 2014"""
"""Please note that parts of this code was obtained through the help of various
sources such as other students and I acknowledge their help in my code"""

matrix = []
for i in range(9):
    old = input()
    new = ""
    for j in range(8):
        new += old[j]+","
    new = new + old[8]
    matrix.append(new.split(","))

#print(matrix)


def checkrow(matrix):
    for r in range(9):
        for i in range(9):
            if str(i+1) not in matrix[r]:
                return False
    return True


def checkcol(matrix):
    for c in range(9):
        column = []
        for r in range(9):
            column.append(matrix[r][c])
        for i in range(9):
            if str(i+1) not in column:
                return False
    return True


def checksubmatrix(matrix):
    for i in range(3):
        sub = []
        for r in range(3):
            for c in range(3):
                sub.append(matrix[r+i*3][c])
        for x in range(9):
            if str(x+1) not in sub:
                return False

        sub =[]
        for c in range(3):
            for r in range(3):
                sub.append(matrix[r][c+i*3])
        for x in range(9):
            if str(x+1) not in sub:
                return False

    return True


if checkrow(matrix) and checkcol(matrix) and checksubmatrix(matrix):
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")