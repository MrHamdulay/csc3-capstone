""""Check if Soduku grid is valid
Tafadzwa Moyo 
15  May 2014"""



grid=[]
x=1
lines=[]
for i in range(9):
    lines.append(input())
#put the lines and rows in a grid
for i in lines:
    grid.append([])
    for e in i:
        if e!="\n":
            grid[-1].append(e)

#Checks if soduku is valid
#Horizontally
for i in grid:
    for a in range(len(i)-1):
        if i[a] in i[a+1:]:
            x=0
#Vertically
lis=[0]*9
for i in range(len(grid)):
    for a in range(len(grid)):
        lis[a]=grid[a][i]
    for j in range(len(lis)-1):
        if lis[j] in lis[j+1:]:
            x=0   
#3x3 block
subgrids=[]
for t in range(0, 7, 3):
    subgrids.append([])
    for i in range(3):
        for l in range(3):
            subgrids[-1].append(grid[t+i][t+l])
for i in subgrids:
    for a in range(len(i)-1):
        if i[a] in i[a+1:]:
            x=0

if x:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")