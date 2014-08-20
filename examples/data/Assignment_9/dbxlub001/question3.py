"""sudoku master!!
Lubalethu Dube
may"""

def grid():
    sudgrid = []
    listy = []
    for mm in range(9):
        nemo=input()
        listy.append(nemo)
    
    for j in range (9):
        for o in range(9):
            gridline = []
            for i in range (9):
                gridline.append(listy[j][i])
        sudgrid.append(gridline)
    return sudgrid

def rowcolcheck(grid):
    n = 0
    for i in range(9):
        for j in range(8):
            rows = grid[i][j]
            collums = grid[j][i]
            for a in range(j+1,9):
                if rows == grid[i][a] or collums == grid[a][i]:
                    n+=1
    if n != 0 :
        return False
    else:
        return True

def mingrids(grid):
    n = 0
    for j in range(3,10,3):
        for k in range(3,10,3):
            arr = []
            for x in range(j-3,j):
                for y in range(k-3,k):
                    arr.append(grid[x][y])
            for r in range(9):
                val = arr[r]
                for c in range(r+1,8):
                    if val == arr[c]:
                        n +=1
    if n == 0:
        return True
    else:
        return False
def MrSudz():
    grid1 = grid()
    if rowcolcheck(grid1) == True and mingrids(grid1) == True:
        print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")

MrSudz()       
    