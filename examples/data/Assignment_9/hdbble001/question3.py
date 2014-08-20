"""sudoku checker
blessings hadebe
17 may 2014"""

grid = []
#takes 9 user inputed strings and stores them in an array 'grid'
for i in range (9):
    new=input()  
    grid.append(new)
    
rows=[]
def getRows(grid ,rows):
    """takes the rows of values from strings inputed by user and stores them in a 2 dimensional array named rows"""
    for row in grid:
        temp=[]
        for i in range(9):
            cell=row[i: i+1]
            temp.append(cell)
        rows.append(temp)
    return rows

columns=[]
def getCols(grid, columns):
    """takes the columns from strings inputed by user and stores them in a 2 dimensional array named columns"""
    for j in range(9):
        temp=[]
        for row in range(9):
            cell=grid[row][j]
            temp.append(cell)
        columns.append(temp)
    return columns

rows=getRows(grid, columns)
columns=getCols(grid, columns)

def checkrows(rows):
    """checks whether all 9 rows are valid or not valid"""
    for row in rows:
        for cell in row:
            num=row.count(cell)
            if num !=1:
                return False
    return True

def checkcol(columns):
    """checks whether all 9 columns are valid or not valid"""
    for col in columns:
        for cell in col:
            num=col.count(cell)
            if num !=1:
                return False
    return True

def CheckSudoku():
    """checks whether entire sudoku is valid or not valid"""
    if checkcol(columns):
        if checkrows(rows):
            print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")
        
CheckSudoku()