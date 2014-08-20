#Sudoku grid validat
#Luke Schwartzkopff
#13 May 2014

grid=[]
for i in range(9):
    grid.append(list(input()))


def checkrow(grid): #check rows by looping through the sublists
    for i in range(9):
        if len(grid[i])!=len(set(grid[i])): #I use this expression to check for duplicates.  A set will remove duplicates from a list
            return(False)                   #Thus, the length of the original list and the set will differ if there are duplicates
    return(True)
        
def checkcolumn(grid):
    for j in range(9):
        column=[]
        for i in range(9): #loop through column
            column.append(grid[i][j]) #append column values to a new list
            
        if len(column)!=len(set(column)): #check for duplicates in new list
            return(False)
    return(True)

def checksquare(grid):
    square=[]
    down=-3
    across=0
    for k in range(9): #the outmost loop runs through the different mini grids
        down+=3        #it does this by changing the starting and ending points of the other two loops which loop through the grids themselves
        if k==3:
            down=0
            across+=3
        if k==6:
            down=0
            across+=3
            
        for i in range(down,down+3): #loop through mini grid columns
            for j in range(across,across+3): #loop through mini grid rows
                square.append(grid[i][j])
            
        if len(square)!=len(set(square)): #check for duplicates
            return(False)   
        square=[]
        
    return(True)
        
valid=True

if checksquare(grid)==True and checkrow(grid)==True and checkcolumn(grid)==True: #check all conditions
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")

        
            
            
        
            
    
    