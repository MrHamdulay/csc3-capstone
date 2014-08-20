"""Aiden Walton
Assignment 9 - Question 3"""
sudoku=[]
for i in range(9):
    sudoku.append([])
    for j in range(9):
        sudoku[i].append("")
        sudoku[i][j]=0
raw=input("")
count=0
while count<=8:
    newlist=list(raw)
    sudoku[count]=newlist
    count+=1
    if count!=9:
        raw=input("")
valid=1
for x in range(9):
    for num in sudoku[x]:
        if sudoku[x].count(num)>1:
            valid=0
for x in range(9):
    temp=[]
    for y in range(9):
        temp.append(sudoku[x][y])
for num in temp:
    if temp.count(str(num))>1:
        valid=0
i=0
j=0
temp=[]
for x in range(i,i+3):
    for y in range(j,j+3):
        temp.append(sudoku[x][y])
for num in temp:
    if temp.count(str(num))>1:
        valid=0
j+=3
temp=[]
for x in range(i,i+3):
    for y in range(j,j+3):
        temp.append(sudoku[x][y])
for num in temp:
    if temp.count(str(num))>1:
        valid=0
j+=3
temp=[]
for x in range(i,i+3):
    for y in range(j,j+3):
        temp.append(sudoku[x][y])
for num in temp:
    if temp.count(str(num))>1:
        valid=0
i+=3
j=0
temp=[]
for x in range(i,i+3):
    for y in range(j,j+3):
        temp.append(sudoku[x][y])
for num in temp:
    if temp.count(str(num))>1:
        valid=0
j+=3
temp=[]
for x in range(i,i+3):
    for y in range(j,j+3):
        temp.append(sudoku[x][y])
for num in temp:
    if temp.count(str(num))>1:
        valid=0
j+=3
temp=[]
for x in range(i,i+3):
    for y in range(j,j+3):
        temp.append(sudoku[x][y])
for num in temp:
    if temp.count(str(num))>1:
        valid=0
j=0
i+=3
temp=[]
for x in range(i,i+3):
    for y in range(j,j+3):
        temp.append(sudoku[x][y])
for num in temp:
    if temp.count(str(num))>1:
        valid=0
j+=3
temp=[]
for x in range(i,i+3):
    for y in range(j,j+3):
        temp.append(sudoku[x][y])
for num in temp:
    if temp.count(str(num))>1:
        valid=0
j+=3
temp=[]
for x in range(i,i+3):
    for y in range(j,j+3):
        temp.append(sudoku[x][y])
for num in temp:
    if temp.count(str(num))>1:
        valid=0
if valid:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")
        
    
    
    
        