#MHDLLO001
#18 May 14
#Sudoku

sudoku = []
flag = True
grid = []
end=9
i=0
y,j,k,l=0,0,0,0
while (y<end):#creating the 2d array
    y=y+1
    sudoku.append(input())
while (j<end):
    
    grid.append(sudoku[j][:3])
    j=j+1
while (k<end):
    
    grid.append(sudoku[k][3:6])
    k=k+1
for a in range(end):
    grid.append(sudoku[a][6:end])
while(i<len(grid)):
    grid[i]=grid[i]+grid[i+1]+grid[i+2]
    grid.remove(grid[i+1])
    grid.remove(grid[i+1])
    i+=1
#Now we will check if the soduku grid is correct
columns = [[],[],[],[],[],[],[],[],[]]
for ak in range(end):
    for jk in range(end):
        acb=sudoku[jk][ak]
        columns[ak].append(acb)
for ak in range(end):
    for jk in range(end):
        if(grid[ak].index(grid[ak][jk])!=jk):
            flag=False
for ak in range(end):
    for jk in range(end):
        abc=columns[ak].index(columns[ak][jk])
        if(jk!=abc):
            flag=False
for ak in range(end):
    for jk in range(end):
        if(sudoku[ak].index(sudoku[ak][jk])!=jk):
            flag=False
if(flag==False):
    print("Sudoku grid is not valid")
if(flag==True):
    print("Sudoku grid is valid")
