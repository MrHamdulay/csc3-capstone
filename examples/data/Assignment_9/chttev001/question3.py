"""Tevin Chetty
14 May 2014
Program to check sudoku grid"""

game=[]
for i in range(9):
    row=input()
    temp_list=[]
    for i in range(9):
        item=row[i]
        temp_list.append(item)
    game.append(temp_list)
    
check_list=["1","2","3","4","5","6","7","8","9"]

count=0
for i in game:
    check=i.sort()
    if check==check_list:
        count+=1
        
countcol=0
for row in range(9):
    tempcol_list=[]
    for col in range(9):
        tempcol_list.append(game[row][col])
    checkcol=tempcol_list.sort
    if checkcol==check_list:
        countcol+=1
        

countgrid=0
for row in (0,3,6):
    tempgrid_list=[]
    for col in (0,3,6):
        one=game[row][col]
        two=game[row+1][col]
        three=game[row+2][col]
        tempgrid_list.append(one)
        tempgrid_list.append(two)
        tempgrid_list.append(three)
        checkgrid=tempgrid_list.sort()

        if checkgrid==check_list:
            countgrid+=1
            
if count==9 and countcol==9 and countgrid==9:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")