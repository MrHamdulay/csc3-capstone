"""Assignment 9 question 3 check if a sudoku grid is valid
Ross van der Heyde VHYROS001
14 May 2014"""

def checkRows(grid):
    """Checks if the rows of the grid are valid"""
    valid = True    
    for i in range(9):
        for j in range(0, 10):
            if grid[i].count(str(j)) > 1:
                valid = False
    return valid

def checkCols (grid):
    """Checks if the columns are valid"""
    col = ""
    valid = True
    
    for j in range(len(grid)):
        col=""
        for i in range(len(grid)):
            col+= grid[i][j]
        #print(col)
        for i in range(10):
            if col.count(str(i)) >1:
                valid = False
            
    return valid

def checkSmall(grid):
    """Checks if the 9 small grids are valid"""
    valid = True
    line = ""
    indexes =[[0,1,2],[3,4,5],[6,7,8]]
    for k in range(3):
        for i in [0,3,6]:
            line=""
            for j in indexes[k]:
                line+= grid[j][i:i+3]
            #print(line)
            
            for l in range(10):
                if line.count(str(l))>1:
                    valid= False
            #print(valid)       
    return valid    
    
grid = []# read in lines of grid
for i in range(9):
    line = input()
    grid.append(line)

#cols = checkCols(grid)
#rows = checkRows(grid)
#small = checkSmall(grid)

#print("R", rows, "C", cols, "SG", small)

if checkCols(grid) and checkRows(grid) and checkSmall(grid):
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")

#359716482
#867345912
#413928675
#398574126
#546281739
#172639548
#984163257
#621857394
#735492861
#Sudoku grid is not valid
#Sample I/O:

#259716483
#867345912
#413928675
#398574126
#546281739
#172639548
#984163257
#621857394
#735492861
#Sudoku grid is valid