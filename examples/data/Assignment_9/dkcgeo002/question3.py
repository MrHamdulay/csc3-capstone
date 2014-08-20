__author__ = 'George de Kock'
""" Program to check if a complete Sudoku grid is valid or not.
2014-05-12"""

grid = []
for i in range(9):
    old = input()
    new = ""
    for j in range(8):
        new += old[j]+","
    new = new + old[8]
    grid.append(new.split(","))

#print(grid)


def checkrow(grid):
    for r in range(9):
        for i in range(9):
            if str(i+1) not in grid[r]:
                return False
    return True


def checkcol(grid):
    for c in range(9):
        column = []
        for r in range(9):
            column.append(grid[r][c])
        for i in range(9):
            if str(i+1) not in column:
                return False
    return True


def checksubgrid(grid):
    for i in range(3):
        sub = []
        for r in range(3):
            for c in range(3):
                sub.append(grid[r+i*3][c])
        for x in range(9):
            if str(x+1) not in sub:
                return False

        sub =[]
        for c in range(3):
            for r in range(3):
                sub.append(grid[r][c+i*3])
        for x in range(9):
            if str(x+1) not in sub:
                return False

    return True


if checkrow(grid) and checkcol(grid) and checksubgrid(grid):
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")