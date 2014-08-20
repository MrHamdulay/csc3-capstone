# program to check if a complete Sudoku grid is valid or not
# Michele Balestra  BLSMIC004
# 15 May 2014

def checkList(rcList, no_range = ['1','2','3','4','5','6','7','8','9']):
    ''' function to check if list of 9 string numbers contain all numbers 1 to 9'''
    counter = 0
    for item in no_range:
        if item in rcList:
            counter += 1
    if counter == 9:
        return True
    else:
        return False

def checkRows(grid):
    ''' function to check each row of a grid is valid'''
    counter = 0 
    for row in grid:
        if checkList(row):
            counter += 1
    if counter == 9:
        return True
    else: 
        return False
    
def checkCols(grid):
    ''' function to check each column of a grid is valid'''
    counter = 0
    col = []
    # assign each item in column to an empty array and check if valid
    for row in grid:
        for item in row:
            col.append(item)
        if checkList(col):
            counter += 1
        col = []    # clear array to assign next column
    if counter == 9:
        return True
    else:
        return False
    
def checkBlocks(grid):
    '''function to check each of the 3x3 blocks in a sudoku grid is valid'''
    counter = 0
    block = []
    incr = 0
    # assigns 9 items in 3x3 block to empty array and checks if valid
    for i in range(9):
        if i==3 or i==6:
            incr += 3
        for row in range(3):
            for col in range(3):
                block.append(grid[row+incr][col+incr])
        if checkList(block):
            counter += 1
        block = []    # clear array to assign next block
    if counter == 9:
        return True
    else:
        return False
    
def sudoku(grid):
    '''function checks if a sudoku grid is valid'''
    if checkRows(grid) and checkCols(grid) and checkBlocks(grid):
        return True
    else:
        return False
        
    
if __name__=='__main__':
    grid = []
    for i in range(9):
        sdku = input()
        grid.append(list(sdku)) 
    if sudoku(grid):
        print('Sudoku grid is valid')
    else:
        print('Sudoku grid is not valid')