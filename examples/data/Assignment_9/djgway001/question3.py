#check that the sodoku grid is valid
#wayne de jager
#14 may 2014

rawlist=[]
for i in range(0,9):
    a=input()
    rawlist.append(a) #convets input into a array

array=[[],[],[],[],[],[],[],[],[]]
for i in range(0,9):
    for j in range(0,9):
        array[i].append(eval(rawlist[i][j])) #creates an array of integers to check

def checkrows(x): #confirms that row adds to 45
    for i in range(0,9):
        if sum(array[i])!=45:
            return False
        else: continue
    return True

def checkcolumns(x): #confirms that columns add to 45
    for i in range(0,9):
        tally=0
        for j in range(0,9):
            tally=tally+x[j][i]
        if tally!=45:
            return False
        else: continue
    return True

def checkmini1(x): #confirms that mini column i(0-3) adds to 45
    tally=0
    for i in range(0,3):
        for j in range(0,3):
            tally=tally+x[i][j]
    if tally!=45:
        return False
    tally=0
    for i in range(0,3):
        for j in range(3,6):
            tally=tally+x[i][j]
    if tally!=45:
        return False
    tally=0
    for i in range(0,3):
        for j in range(6,9):
            tally=tally+x[i][j]
    if tally!=45:
        return False
    return True

def checkmini2(x): #confirms that mini column i(0-3) adds to 45
    tally=0
    for i in range(3,6):
        for j in range(0,3):
            tally=tally+x[i][j]
    if tally!=45:
        return False
    tally=0
    for i in range(3,6):
        for j in range(3,6):
            tally=tally+x[i][j]
    if tally!=45:
        return False
    tally=0
    for i in range(3,6):
        for j in range(6,9):
            tally=tally+x[i][j]
    if tally!=45:
        return False
    return True

def checkmini3(x): #confirms that mini column i(0-3) adds to 45
    tally=0
    for i in range(6,9):
        for j in range(0,3):
            tally=tally+x[i][j]
    if tally!=45:
        return False
    tally=0
    for i in range(6,9):
        for j in range(3,6):
            tally=tally+x[i][j]
    if tally!=45:
        return False
    tally=0
    for i in range(6,9):
        for j in range(6,9):
            tally=tally+x[i][j]
    if tally!=45:
        return False
    return True

def valid(x): #if all function valid, grid is valid
    if checkrows(x)==True and checkcolumns(x)==True and checkmini1(x)==True and checkmini2(x)==True and checkmini3(x)==True:
        print("Sudoku grid is valid")
    else: print("Sudoku grid is not valid")

valid(array)