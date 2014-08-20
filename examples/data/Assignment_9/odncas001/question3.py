"""sudoku checker
casey o'donnell
12 may 2014"""

count=0
grid=[]
while count<=8:
    inp=input("")
    row=[]
    for i in inp:
        row.append(i)
    grid.append(row)
    count+=1
    
def row_check(grid):
    check=True
    for row in range(9):
        checklist=""
        for col in range(9):
            if grid[row][col] in checklist:
                check=False
            checklist+=grid[row][col]
    if check:
        return True
    else:
        return False

def col_check(grid):
    check=True
    for col in range(9):
        checklist=""
        for row in range(9):
            if grid[row][col] in checklist:
                check=False
            checklist+=grid[row][col]
    if check:
        return True
    else:
        return False
    
def block_check(grid):
    for ROW in range(0,7,3):
        for COL in range (0,7,3):
            checklist=""
            for row in range(ROW,ROW+3):
                for col in range(COL,COL+3):
                    if grid[row][col] in checklist:
                        return False
                    checklist+=grid[row][col]
    return True

if row_check(grid) and col_check(grid) and block_check(grid):
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")
    
    