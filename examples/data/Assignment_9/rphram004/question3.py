"""soduko validity checker
rama raphalalani
16-05-2014"""

#creating a 2d array
grid = []
for i in range(9):
    y = []
    x = input()
    y.append(x)
    grid.append(y)


i = 0
while i != 9:
    line = input("")
    for j in range(0, 9):
        grid[i][j] = line[j: j+1]
    i += 1
#checking the validity of each row, that there are no duplicates in each row
legit = True
for i in range(9):
    for j in range(9):
        for k in range(j+1,9):
            if grid[i][j] == grid[i][k]:
                legit = False
                
#creating a 3x3array to check for validity
grid2 = []
for l in range(3):
    grid2.append([0,0,0])

#checks the validity of within the 3x3 grid    
for m in range(3):
    for n in range(3):
        for o in range(3):
            for p in range(3):
                grid2[o][p] = grid[o+m*3][p+n*3]
                
        for r in range(3):
            if grid2[0][r] in grid2[1] or grid2[0][r] in grid2[2] or grid2[2][r] in grid2[1]:
                legit = False
                
if legit:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")