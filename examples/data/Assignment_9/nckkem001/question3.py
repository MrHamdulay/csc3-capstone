"""Program to check the validity of a soduko grid.
Kemeshan Naicker
15 May 2014"""

def checksudoku():
    
    #Extract rows from input.
    completegrid = []
    for i in range(9):
        row = []
        stringrow = input()
        for j in range(9):
            row.append(eval(stringrow[j]))
        completegrid.append(row)
        
    #Extract collumns from completegrid.
    for i in range(9):
        collumn = []
        for j in range(9):
            collumn.append(completegrid[j][i])
        completegrid.append(collumn)
        
    #Extract 3x3 grids from completegrid.
    x3grid = []
    for i in range(3):
        for j in range(3):
            x3grid.append(completegrid[i][j])
    completegrid.append(x3grid)
    
    x3grid = []
    for i in range(3):
        for j in range(3,6):
            x3grid.append(completegrid[i][j])
    completegrid.append(x3grid)
    
    x3grid = []
    for i in range(3):
        for j in range(6,9):
            x3grid.append(completegrid[i][j])
    completegrid.append(x3grid)
    
    for i in range(3,6):
        for j in range(3):
            x3grid.append(completegrid[i][j])
    completegrid.append(x3grid)
    
    x3grid = []
    for i in range(3,6):
        for j in range(3,6):
            x3grid.append(completegrid[i][j])
    completegrid.append(x3grid)
    
    x3grid = []
    for i in range(3,6):
        for j in range(6,9):
            x3grid.append(completegrid[i][j])
    completegrid.append(x3grid)
    
    for i in range(6,9):
        for j in range(3):
            x3grid.append(completegrid[i][j])
    completegrid.append(x3grid)
    
    x3grid = []
    for i in range(6,9):
        for j in range(3,6):
            x3grid.append(completegrid[i][j])
    completegrid.append(x3grid)
    
    x3grid = []
    for i in range(6,9):
        for j in range(6,9):
            x3grid.append(completegrid[i][j])
    completegrid.append(x3grid)
    
    #Check if the complete grid is valid by determining if the sum of all the rows,
    #collumns, and 3x3 grids is equal 45.
    for i in range(27):
        validitycheck = 0
        for j in range(9):
            validitycheck += completegrid[i][j]
        if validitycheck != 45:
            print("Sudoku grid is not valid")
            return -1
        
    print("Sudoku grid is valid")
    
if __name__=="__main__":
    checksudoku()