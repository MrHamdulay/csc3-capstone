'''program to check whether a sudoku grid is valid
tom new
2014/05/13'''

def getgrid ( ):
    '''turns 9 lines of 9 numbers into a 9x9 2D list'''
    grid = []
    for i in range (9): # gets 9 lines of input
        line = input ( )
        row = []
        
        # converts each character to an integer and appends to the ith row
        for j in line:
            row.append (int (j))
        
        # appends to the ith row
        grid.append (row)
    return grid

def checkrows (grid):
    '''returns true if rows are valid; else false'''
    
    # iterates simply through each row and checks if it is valid
    for row in grid:
        for i in row:
            if row.count (i) != 1:
                return False
    return True

def checkcols (grid):
    '''returns true if columns are valid; else false'''
    
    # iterates through collumns
    for col in range (9):
        collist = []
        
        # creates a temporary list of numbers in the current column
        for i in range (9):
            collist.append (grid [i][col])
            
        # checks if the column is valid
        for j in collist:
            if collist.count (j) != 1:
                return False
    return True

def checkboxes (grid):
    '''returns true if 3x3 non-overlapping boxes are valid; else false'''
    
    # iterates through boxes
    for boxrow in range (0, 9, 3):
        for boxcol in range (0, 9, 3):
            
            # creates a temporary list of the numbers in the current box
            boxlist = []
            for row in range (boxrow, boxrow + 3):
                for col in range (boxcol, boxcol + 3):
                    boxlist.append (grid [row][col])
                    
            # checks if box is valid
            for i in boxlist:
                if boxlist.count (i) != 1:
                    return False
    return True

def checkgrid (grid):
    '''checks if a sudoku grid is valid, returns boolean value'''
    if checkrows (grid) and checkcols (grid) and checkboxes (grid):
        return True
    return False

truegrid = [[2, 5, 9, 7, 1, 6, 4, 8, 3], [8, 6, 7, 3, 4, 5, 9, 1, 2], [4, 1, 3, 9, 2, 8, 6, 7, 5], [3, 9, 8, 5, 7, 4, 1, 2, 6], [5, 4, 6, 2, 8, 1, 7, 3, 9], [1, 7, 2, 6, 3, 9, 5, 4, 8], [9, 8, 4, 1, 6, 3, 2, 5, 7], [6, 2, 1, 8, 5, 7, 3, 9, 4], [7, 3, 5, 4, 9, 2, 8, 6, 1]]

falsegrid = [[3, 2, 9, 7, 1, 6, 4, 8, 2], [8, 6, 7, 3, 4, 5, 9, 1, 2], [4, 1, 3, 9, 2, 8, 6, 7, 5], [3, 9, 8, 5, 7, 4, 1, 2, 6], [5, 4, 6, 2, 8, 1, 7, 3, 9], [1, 7, 2, 6, 3, 9, 5, 4, 8], [9, 8, 4, 1, 6, 3, 2, 5, 7], [6, 2, 1, 8, 5, 7, 3, 9, 4], [7, 3, 5, 4, 9, 2, 8, 6, 1]]

if __name__ == '__main__':
    grid = getgrid ( )
    if not checkgrid (grid): print ('Sudoku grid is not valid')
    else: print ('Sudoku grid is valid')