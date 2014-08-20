''' Assignment 9, question 3
Check if a Sudoku grid is valid or not
Tristan Subroyen
11 May 2014 '''

def checkRows (grid):
    ''' Checks the rows in a grid for validity '''
    for i in range (9):
        sampleRow = [0,0,0,0,0,0,0,0,0,0]
        for j in range (9):
            sampleRow[grid[i][j]] += 1
        newRow = sampleRow[1:10]
        for k in range (9):
            if (newRow[k] == 1) or (newRow[k] == 0):
                continue
            else:
                return False
    return True

def checkColumns (grid):
    ''' Checks the columns in a grid for validity '''
    for i in range (9):
        sampleCol = [0,0,0,0,0,0,0,0,0,0]
        for j in range (9):
            sampleCol[grid[j][i]] += 1
        newCol = sampleCol[1:10]
        for k in range (9):
            if (newCol[k] == 1) or (newCol[k] == 0):
                continue
            else:
                return False
    return True

def checkGrid (grid):
    ''' Checks if the passed grid is valid '''
    if len(grid) == 9:
        numRow = 0
        for i in range (9):
            if len(grid[i]) == 9:
                numRow += 1
        if numRow == 9:
            if checkRows (grid):
                if checkColumns (grid):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

# accept user input and create grid
grid = []
for i in range (9):
    grid.append([]*9)
    
for i in range (9):
    
    line = str(input())
    newList = list(line)
        
    for k in range (9):
        grid[i].append(newList[k])
    
    for j in range (9):
        grid[i][j] = eval(grid[i][j])

if checkGrid(grid):
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")