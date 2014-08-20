
grid = []
newlist = []
flag = False


for i in range(9):
    numbers = input()
    grid1 = []
    for h in range(9):
        grid1.append(eval(numbers[h]))
    grid.append(grid1)


for j in range(9):
    newlist = []
    for k in range(9):
        if grid[j][k] not in newlist:
            newlist.append(grid[j][k])
        else:
            flag = True
newlist = []    

for j in range(9):
    newlist = []
    for k in range(9):
        if grid[k][j] not in newlist:
            newlist.append(grid[k][j])
        else:
            flag = True
#newlist = []

for i in [3,6,9]:
    newlist = []
    for j in range(i-3, i, 1):        
        if grid[j][i-3] in newlist:
            flag = True
        else:
            newlist.append(grid[j][i-3])
        if grid[j][i-2] in newlist:
            flag = True
        else:
            newlist.append(grid[j][i-2])
        if grid[j][i-1] in newlist:
            flag = True
        else:
            newlist.append(grid[j][i-1])
            
        
        
if flag:
    print("Sudoku grid is not valid")
else:
    print("Sudoku grid is valid")
            
