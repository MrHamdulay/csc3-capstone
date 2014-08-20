"""checking validity of sudoku grid
kennedy muranda
18/05/2014"""


#check the row
def checkRow(theGrid,n):
    
    Check = {} 
    for num_ in theGrid[n]: 
        if not theCheck(num_, Check):
            return False 
    return True 


#check the column
def checkColumn(theGrid,n):
    Check = {}
    for y in range(len(theGrid)): 
        if not theCheck(theGrid[y][n], Check):
            return False 
    return True 


#check function
def theCheck(num_, Check):
    if num_ in Check: return False 
    if not 1 <= num_ <= 9: return False 
    Check[num_] = True #records in checker 
    return True   


#check the part of grid
def checkRegion(theGrid,x,y):
    
    Check = {} 
    theTop = (y * 3) 
    theBottom = (theTop + 2) 
    theLeft = (x * 3) 
    theRight = (theLeft + 2)
    
    #loop for coordinates of the grid
    for y in range(theTop, theBottom + 1):
        for x in range(theLeft, theRight + 1):
            if not theCheck(theGrid[y][x], Check):
                return False 
    return True 


# check functon
def checkGrid(theGrid):
    
    for y in range(len(theGrid)): 
        if not checkRow(theGrid,y):
            return False 
        
    for x in range(len(theGrid)): 
        if not checkColumn(theGrid,x):
            return False 
        
    for y in range(0,3): 
        for x in range(0,3):
            if not checkRegion(theGrid,x,y):
                
                return False
    return True 
                

theGrid = [] 


#grid from user
for i in range(9): 
    line = input() 
    theRow = [] 
    
    for character in line:
        theRow.append(eval(character)) 
    theGrid.append(theRow) 


#print output
if checkGrid(theGrid):
    print('Sudoku grid is valid') 
else:
    print('Sudoku grid is not valid') 