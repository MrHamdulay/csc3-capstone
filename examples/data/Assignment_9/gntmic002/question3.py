#Assignment 9.3
#Michael Gant
#11/05/2014

#Suduko

def HoriSingleLineCheck(sLine):
    for j in range(8):
        for l in range(j+1,9):
            if sLine[j] == sLine[l]:
                return False   
    return True

def HoriCheck(lText):
    for k in range(9):
        for j in range(8):
            for l in range(j+1,9):
                if lText[k][j] == lText[k][l]:
                    return False
    return True

def VertCheck(lText):
    for k in range(9):
        for j in range(8):
            for l in range(j+1,9):
                if lText[j][k] == lText[l][k]:
                    return False
    return True
    
def CubeCheck(lText):
    sLineCheck = ""
    for p in range(0,9,3):
        for k in range(0,9,3):
            for j in range(3):
                for l in range(3):
                    sLineCheck = sLineCheck + lText[k+j][p+l]
            if HoriSingleLineCheck(sLineCheck) == False:
                return False
    return True

lSuduko = [[]*9]*9
for j in range(9):
    lInput = []
    sInput = input("")
    for k in sInput:
        lInput.append(k)
    lSuduko[j] = (lInput)
if CubeCheck(lSuduko) and VertCheck(lSuduko) and HoriCheck(lSuduko):
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")
      