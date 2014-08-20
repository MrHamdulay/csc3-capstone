#question3

grid=[]
fail=False

for i in range(9):
    grid.append(input())
    
for i in range(9):
    for j in range(8):
        for k in range(j+1,9):
            if grid[i][j]==grid[i][k]:
                fail=True
                
                
for i in range(9):
    for j in range(8):
        for k in range(j+1,9):
            if grid[j][i]==grid[k][i]:
                fail=True


grid2=[]

for i in range(3):
    for j in range(3):
        grid2.append(grid[i*3][j*3:j*3+3]+grid[i*3+1][j*3:j*3+3]+grid[i*3+2][j*3:j*3+3])

for i in range(9):
    for j in range(8):
        for k in range(j+1,9):
            if grid2[i][j]==grid2[i][k]:
                fail=True
                         
if fail==True:
    print("Sudoku grid is not valid")
else:
    print("Sudoku grid is valid")