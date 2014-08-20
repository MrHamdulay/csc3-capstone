"""KLSADA002
Assignment 9 Q3
2014-05-13"""
grid = []
for i in range (9):
    grid.append([0])
    grid[i]=[0]*9
    s=input('')
    for j in range (9):
        grid[i][j]=s[j:j+1]

def listBad(row):
    for k in range(9):
        for j in range(9):
            if k == j:
                continue
            elif row[k] == row[j]:
                return True
    return False

def checkRows(grid):
    for i in range(9):
        row = grid [i]
        if listBad(row):
            return False
    return True

def checkCols(grid):
    for i in range(9):
        row=[]
        for k in range(9):
            row.append(grid[k][i])
        if listBad(row):
            return False
    return True

def checkBlocks(grid):
    block1=[]
    block2=[]
    block3=[]
    block4=[]
    block5=[]
    block6=[]
    block7=[]
    block8=[]
    block9=[]
    for i in range(9):
        for j in range(9):
            if i < 3 and j<3:
                block1.append(grid[i][j])
            elif i < 3 and (j < 6 and j >= 3):
                block2.append(grid[i][j])   
            elif i < 3 and (j < 9 and j >=6):
                block3.append(grid[i][j])                               
            elif (i < 6 and i >= 3) and j < 3:
                block4.append(grid[i][j])        
            elif (i < 6 and i >= 3) and (j < 6 and j >= 3):
                block5.append(grid[i][j])        
            elif (i < 6 and i >= 3) and (j < 9 and j >=6):
                block6.append(grid[i][j])                
            elif (i < 9 and i >= 6) and j < 3:
                block7.append(grid[i][j])                
            elif (i < 9 and i >= 6) and (j < 6 and j >= 3):
                block8.append(grid[i][j])               
            elif (i < 9 and i >= 6) and (j < 9 and j >=6):
                block9.append(grid[i][j])                
                
    if listBad(block1) or listBad(block2) or listBad(block3) or listBad(block4) or listBad(block5) or listBad(block6) or listBad(block7) or listBad(block8) or listBad(block9):
        return False
    else:
        return True
    
if checkRows(grid) and checkCols(grid) and checkBlocks(grid):
    print('Sudoku grid is valid')

else:
    print('Sudoku grid is not valid')
    
    