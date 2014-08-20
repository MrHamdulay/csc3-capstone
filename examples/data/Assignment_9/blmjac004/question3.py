"""checking is a soduko grid is valid
Jacqueline Blomendahl
13 May 2014"""

for i in range(9):
    grid=input()
for j in range(9):
    for k in range (9):
        if grid[j].find(grid[j][k])>=1:
            print("Sudoku grid is not valid")
        elif grid[k].find(grid[j][k])>=1:
            print("Sudoku grid is not valid")
        elif 
        else:
            print("Sudoku grid is valid")
