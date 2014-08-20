""" programm to check soduko
alexander whiting
15 may 2014"""

def getlines():
    lines = []
    for i in range(9):
        lines.append(['']*9)
    for k in range(9):
        line = input()
        for l in range(9):
            lines[k][l] = line[l]
    return lines       

def checkrows(lines):
    for i in range(9): #checks rows
        check = ''.join(lines[i])
        for i in lines[i]:
            if check.count(i)>1:
                return False
    return True
     
def checkcolumns(lines):
    
    for col in range(9):
        check = ''
        for row in range(9):
            check += lines[row][col]
        for i in check:
            if check.count(i)>1:
                return False
    return True

def checkblocks(lines):
    yint = 0
    xint = 0
    for y in (3,6,9):
        for x in (3,6,9):
            check = ''
            for row in range(yint,y): 
                for col in range(xint,x):
                    check += lines[row][col]
            for i in check:
                if check.count(i)>1:
                    return False
            xint = x
        yint = y
    return True


lines = getlines()
if checkrows(lines) and checkcolumns(lines) and checkblocks(lines):
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")