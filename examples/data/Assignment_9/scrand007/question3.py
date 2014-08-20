grid = []

for i in range(9):
    n = ",".join(input(""))
    grid.append(n)
    
for i in range(9):
    grid[i] = grid[i].split(',')
    
def row():
    for r in range(9):
        num = []
        for c in range(9):
            if grid[r][c] in num:
                return False
            else:
                num.append(grid[r][c])
    return True
    
def column():
    for c in range(9):
        num = []
        for r in range(9):
            if grid[r][c] in num:
                return False
            else:
                num.append(grid[r][c])
    return True
    
def check_grid():
    for i in range (0,9,3):
        grid_new = []
        for c in range(i,i+3):
            for r in range(i,i+3):
                grid_new.append(grid[r][c])
        grid_new2 = []
        for i in grid_new:
            if i in grid_new2:
                return False
            else:
                grid_new2.append(i)
    return True
    
if row() == True and column() == True and check_grid() == True:
    print ("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")