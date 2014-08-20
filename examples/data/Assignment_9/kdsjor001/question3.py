"""Assignment 9 Question 3
15 May 2014
Jordan Kadish, Sudoku Check"""
def CheckRows(List):
    #Checking the rows within the grid
    Row=[]
    for i in range(len(List)):
        for j in range(len(List[i])):
            if List[i][j] in Row: #Appending the numbers already checked to 
                return False      #an empty list to compare for later
            else:
                Row.append(List[i][j])
        Row=[]
    return True
def CheckCollumns(List):
    #Checking the collumns within the grid
    Collumn=[]
    for i in range(9):
        for j in range(9):
            if List[j][i] in Collumn:
                return False
            else:
                Collumn.append(List[j][i])
        Collumn=[]
    return True
def CheckGrid(List):
    #Checking the 3x3 grids within the grid
    CollumnCounter=0
    RowCounter=0
    for SudokuLine1 in range(3):
        Grid=[]
        for i in range(CollumnCounter,CollumnCounter+3):
            #Incrementing counters to check entire grid
            for j in range(RowCounter,RowCounter+3):
                if List[i][j] in Grid:
                    return False
                else:
                    Grid.append(List[i][j])
        
        
        CollumnCounter+=3
        Grid=[]
    RowCounter=3
    CollumnCounter=0
    for SudokuLine2 in range(3):
        Grid=[]
        for i in range(CollumnCounter,CollumnCounter+3):
            for j in range(RowCounter,RowCounter+3):
                if List[i][j] in Grid:
                    return False
                else:    
                    Grid.append(List[i][j])                
        CollumnCounter+=3
        Grid=[]
    
    CollumnCounter=0    
    RowCounter=6
    for SudokuLine3 in range(3):
        Grid=[]
        for i in range(CollumnCounter,CollumnCounter+3):
            for j in range(RowCounter,RowCounter+3):
                if List[i][j] in Grid:
                    return False
                else:    
                    Grid.append(List[i][j])                
        CollumnCounter+=3
        Grid=[]        
    return True
        
Numbers=[]        
for i in range(9):
    #allowing input of the grid
    Line=input('')
    Numbers.append(Line)
if (CheckRows(Numbers)) and (CheckCollumns(Numbers)) and CheckGrid(Numbers):
    print('Sudoku grid is valid')
else:
    print('Sudoku grid is not valid')