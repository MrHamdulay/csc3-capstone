"""check if a complete Sudoku grid is valid
Ross Eyre
11/05/2014"""


#multiline input
string = ''
for i in range(9):
    string += input()

#create empty 2d array
sodList = []
for i in range(9):
    sodList.append([0]*9)

#populate
for r in range(9):
    for c in range(9):
        sodList[r][c] = string[c:c+1]     
    string = string[9::]
    
#CHECK IF VALID:

def checkRows(sodList):
    
    #check rows for duplicates
    for row in sodList:
        sortRow = sorted(row)
        for i in range(8):
            if(sortRow[i]==sortRow[i+1]):               
                return False
    return True

def checkCol(sodList):          
    #check columns for duplicates

    for col in range(9):
        #make new list of columns
        colList = []
        for i in range(9):
            colList.append(sodList[i][col])
        sortCol = sorted(colList)
        for i in range(8):
            if(sortCol[i]==sortCol[i+1]):                
                return False
    return True

def checkSquares(sodList): 
    
    sodList.insert(0,[])
    for lines in range(len(sodList)):
        sodList[lines].insert(0,0)
    
    #check squares for duplicates:
    for col in range(3):
        for row in range(3):
            grid = []
            for rowItem in range(1, 4):
                for item in range(1, 4):
                    grid.append(sodList[rowItem+(3*col)][item+(3*row)])                    
            sortGrid = sorted(grid)
            ##check for adjacent duplicates
            for i in range(8):
                if(sortGrid[i]==sortGrid[i+1]):
                    return False
    return True


def main():
    if(checkRows(sodList) and checkCol(sodList) and checkSquares(sodList)):
        print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")


main()

    