"""PRIYANKA GOBERDHAN
ASSIGN 9 - QUESTION 3
16/05/14"""

suduku = [ ]
indicator = True

for i in range(9):
    suduku.append(input())
grid = [ ]

for i in range(9):
    grid.append(suduku[i][:3])
    
for i in range(9):
    grid.append(suduku[i][3:6])
    
for i in range(9):
    grid.append(suduku[i][6:9])
    
i=0

while(i<len(grid)):
    grid[i]=grid[i]+grid[i+1]+grid[i+2]
    grid.remove(grid[i+1])
    grid.remove(grid[i+1])
    i+=1

columns = [[],[],[],[],[],[],[],[],[]]

for i in range(9):
    for j in range(9):
        columns[i].append(suduku[j][i])
        
for i in range(9):
    for j in range(9):
        if(grid[i].index(grid[i][j]) != j):
            indicator = False
            
for i in range(9):
    for j in range(9):
        if(columns[i].index(columns[i][j]) != j):
            indicator = False
            
for i in range(9):
    for j in range(9):
        if(suduku[i].index(suduku[i][j]) != j):
            indicator = False
            
if(indicator):
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")