def checkdatgridyo(suduko):
    for k in range(9):
        for i in range(8):
            for j in range (i+1,9):
                if suduko[k][i] == suduko [k][j]:
                    return False
    for k in range(9):
        for i in range(8):
            for j in range (i+1,9):
                if suduko[i][k] == suduko [j][k]:
                    return False
    for blockrow in range(3):
        for blockcolumn in range(3):
            temp = [suduko[blockrow*3][blockcolumn*3], suduko[blockrow*3][(blockcolumn*3)+1], suduko[blockrow*3][(blockcolumn*3)+2], suduko[(blockrow*3)+1][blockcolumn*3], suduko[(blockrow*3)+1][(blockcolumn*3)+1], suduko[(blockrow*3)+1][(blockcolumn*3)+2], suduko[(blockrow*3)+2][blockcolumn*3], suduko[(blockrow*3)+2][(blockcolumn*3)+1], suduko[(blockrow*3)+2][(blockcolumn*3)+2]]
            for i in range(8):
                for j in range(i+1,9):
                    if temp[i]==temp[j]:
                        return False
    return True 
grid = []
for i in range(9):
    grid.append(input())    
if checkdatgridyo(grid):
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")