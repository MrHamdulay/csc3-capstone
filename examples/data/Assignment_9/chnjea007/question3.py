grid = []
for i in range(9):
    grid.append(list(input()))
#grid = [['3', '5', '9', '7', '1', '6', '4', '8', '2'], ['8', '6', '7', '3', '4', '5', '9', '1', '2'], ['4', '1', '3', '9', '2', '8', '6', '7', '5'], ['3', '9', '8', '5', '7', '4', '1', '2', '6'], ['5', '4', '6', '2', '8', '1', '7', '3', '9'], ['1', '7', '2', '6', '3', '9', '5', '4', '8'], ['9', '8', '4', '1', '6', '3', '2', '5', '7'], ['6', '2', '1', '8', '5', '7', '3', '9', '4'], ['7', '3', '5', '4', '9', '2', '8', '6', '1']]
#grid = [['2', '5', '9', '7', '1', '6', '4', '8', '3'], ['8', '6', '7', '3', '4', '5', '9', '1', '2'], ['4', '1', '3', '9', '2', '8', '6', '7', '5'], ['3', '9', '8', '5', '7', '4', '1', '2', '6'], ['5', '4', '6', '2', '8', '1', '7', '3', '9'], ['1', '7', '2', '6', '3', '9', '5', '4', '8'], ['9', '8', '4', '1', '6', '3', '2', '5', '7'], ['6', '2', '1', '8', '5', '7', '3', '9', '4'], ['7', '3', '5', '4', '9', '2', '8', '6', '1']]
def checkRAndC(grid):
    for r in range(9):
        for c in range(9):
            grid[r][c] = eval(grid[r][c])
    for i in range(9):
        usedNumsR = []
        usedNumsC = []
        for j in range(9):
            if grid[i][j] in usedNumsR:
                return False
            else:
                usedNumsR.append(grid[i][j])
            if grid[j][i] in usedNumsC:
                return False
            else:
                usedNumsC.append(grid[j][i])            
    return True
def checkGrid(grid):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            for k in range(1, 10):
                count = 0
                for l in range(i, i + 3):
                    for m in range(j, j+3):
                        if k == grid[l][m]:
                            count += 1
                if count > 1:
                    return False
    return True
if checkRAndC(grid) == True and checkGrid(grid) == True:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")