# Program to check if a soduko grid is correct
# Hendrik Joosten
# 16/05/2014

def getGrid():
    grid = []
    for i in range(9):
        grid.append([])
        line = input()
        for j in range(9):
            grid[i].append(int(line[j]))
    return grid

def checkRows(grid):
    b = 1
    for i in range(9):
        if sum(grid[i]) != 45 or len(grid[i]) != len(set(grid[i])):
            b = 0
    return b
        
def checkColumns(grid):
    b = 1
    for i in range(9):
        temp = []
        for j in range(9):
            temp.append(grid[j][i])
        if sum(temp) != 45 or len(temp) != len(set(temp)):
            b = 0
    return b
    
def checkSubGrids(grid):
    bl = 1
    for a in [0,3,6]:
        for b in [0,3,6]:
            temp = []
            for c  in [0,1,2]:
                for d in [0,1,2]:
                    temp.append(grid[a+c][b+d])
            if sum(temp) != 45 or len(temp) != len(set(temp)):
                bl = 0
    return bl

grid = getGrid()
if checkRows(grid) == 1 and checkColumns(grid) == 1 and checkSubGrids(grid) == 1:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")
