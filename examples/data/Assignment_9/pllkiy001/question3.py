#program to verify if sudoku grid is or isnt valid
#kiyarah pillay
#17 may 2014

#make into list
sudoku=[ ]
valid=True
#sudoku grid is 9X9
for i in range(9):
#add the input
    sudoku.append(input())
g=[ ]

for i in range(9):
    g.append(sudoku[i][0:3])
for i in range(9):
    g.append(sudoku[i][3:6])
for i in range(9):
    g.append(sudoku[i][6:9])
i=0

while (i<len(g)):
    g[i]=g[i]+g[i+1]+g[i+2]
    g.remove(g[i+1])
    g.remove(g[i+1])
    i+=1
colums=[[],[],[],[],[],[],[],[],[]]
for i in range(9):
    for k in range(9):
        colums[i].append(sudoku[k][i])

for i in range (9):
    for k in range (9):
        if (g[i].index(g[i][k])!=k):
            valid=False
            
for i in range (9):
    for k in range(9):
        if (colums[i].index(colums[i][k]!=k)):
            valid=False

for i in range(9):
    for k in range(9):
        if (sudoku[i].index(sudoku[i][k])!=k):
            valid=False

if (valid):
    print ("Sudoku grid is valid")
else:
    print ("Sudoku grid is not valid")
