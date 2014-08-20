"""11/05/2014 RFFADA002 Adam Ruff
Assignment 9 Question 3
Check if Sudoku grid is acceptable"""


grid = []

for i in range(9):
    n = ",".join(input(""))
    grid.append(n)
    
for i in range(9):
    grid[i] = grid[i].split(',')
    
def check_row():
    for r in range(9):
        num = []
        for c in range(9):
            if grid[r][c] in num:
                return False
            else:
                num.append(grid[r][c])
    return True
    
def check_col():
    for c in range(9):
        num = []
        for r in range(9):
            if grid[r][c] in num:
                return False
            else:
                num.append(grid[r][c])
    return True
    
def check_sgrid():
    global num_sgrid,sgrid
    for i in range (0,9,3):
        sgrid = []
        for c in range(i,i+3):
            for r in range(i,i+3):
                sgrid.append(grid[r][c])
        num_sgrid = []
        for i in sgrid:
            if i in num_sgrid:
                return False
            else:
                num_sgrid.append(i)
    return True
    
if check_row() == True and check_col() == True and check_sgrid() == True:
    print ("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")