#Programme to check if a sudoku grid is valid
#Joe Sutton
#11 May 2014

checkvalid=True

sudokugrid=[]
for i in range(9):
    rowlist=[]
    row=str(input())
    for value in range(9):
        rowlist.append(row[value])
    
    sudokugrid.append(rowlist)

for row in sudokugrid:
    if '1' not in row:
        checkvalid=False
    elif'2' not in row:
        checkvalid=False
    elif'3' not in row:
        checkvalid=False
    elif'4' not in row:
        checkvalid=False
    elif'5' not in row:
        checkvalid=False
    elif'6' not in row:
        checkvalid=False
    elif'7' not in row:
        checkvalid=False
    elif'8' not in row:
        checkvalid=False
    elif'9' not in row:
        checkvalid=False

transposegrid=[]
for collumn in range(9):
    newcollumn=[]
    for row in range(9):
        newcollumn.append(sudokugrid[row][collumn])
    transposegrid.append(newcollumn)
    
for row in transposegrid:
    if '1' not in row:
        checkvalid=False
    elif'2' not in row:
        checkvalid=False
    elif'3' not in row:
        checkvalid=False
    elif'4' not in row:
        checkvalid=False
    elif'5' not in row:
        checkvalid=False
    elif'6' not in row:
        checkvalid=False
    elif'7' not in row:
        checkvalid=False
    elif'8' not in row:
        checkvalid=False
    elif'9' not in row:
        checkvalid=False

if checkvalid:
    for i in range(3):
        for j in range(3):
            minigrid=[]
            minigrid.append(sudokugrid[i*3][j*3])
            minigrid.append(sudokugrid[i*3][j*3+1]) 
            minigrid.append(sudokugrid[i*3][j*3+2])
            minigrid.append(sudokugrid[i*3+1][j*3])
            minigrid.append(sudokugrid[i*3+1][j*3+1])
            minigrid.append(sudokugrid[i*3+1][j*3+2])
            minigrid.append(sudokugrid[i*3+2][j*3])
            minigrid.append(sudokugrid[i*3+2][j*3+1])
            minigrid.append(sudokugrid[i*3+2][j*3+2])
            
            
            if '1' not in minigrid:
                checkvalid=False
            elif'2' not in minigrid:
                checkvalid=False
            elif'3' not in minigrid:
                checkvalid=False
            elif'4' not in minigrid:
                checkvalid=False
            elif'5' not in minigrid:
                checkvalid=False
            elif'6' not in minigrid:
                checkvalid=False
            elif'7' not in minigrid:
                checkvalid=False
            elif'8' not in minigrid:
                checkvalid=False
            elif'9' not in minigrid:
                checkvalid=False
                
if checkvalid:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")
    