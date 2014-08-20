#Description: Checks if a completed Sudoku grid is valid
#Name: Paul Roux - RXXPAU008
#Date 15 May 2014

def checkSudoku(grid):
    """Checks if the supplied Sudoku grid is valid and complete"""
    #Check for a grid larger than 9x9
    for i in range(9):
        try:
            if grid[i][9]:
                return False
        except: n=1
    for i in range(9):
        try:
            if grid[9][i]:
                return False 
        except: n=1#End of grid size check
    
    #Check that the numbers 1-9 occur only once in each row and column     
    for i in range(9):
        numbers=[]
        for j in range(9):
            if grid[i][j] not in numbers:
                numbers.append(grid[i][j])
            else: return False
    for i in range(9):
        numbers=[]
        for j in range(9):
            if grid[j][i] not in numbers:
                numbers.append(grid[j][i])
            else: return False#End of row and column check
            
    #Check the numbers 1-9 only occur once in each 3x3 sub grid
    subGrid=[]                
    for i in range(3):
        for j in range(3):
            subGrid.append(grid[i][j])
    for i in range(9):
        if subGrid.count(str(i)) > 1:
            return False 
    subGrid=[]                
    for i in range(3):
        for j in range(3,6):
            subGrid.append(grid[i][j])
    for i in range(9):
        if subGrid.count(str(i)) > 1:
            return False 
    subGrid=[]                
    for i in range(3):
        for j in range(6,9):
            subGrid.append(grid[i][j])
    for i in range(9):
        if subGrid.count(str(i)) > 1:
            return False 
        
    subGrid=[]
    for i in range(3,6):
        for j in range(3):
            subGrid.append(grid[i][j])
    for i in range(9):
        if subGrid.count(str(i)) > 1:
            return False 
    subGrid=[]                
    for i in range(3,6):
        for j in range(3,6):
            subGrid.append(grid[i][j])
    for i in range(9):
        if subGrid.count(str(i)) > 1:
            return False 
    subGrid=[]                
    for i in range(3,6):
        for j in range(6,9):
            subGrid.append(grid[i][j])
    for i in range(9):
        if subGrid.count(str(i)) > 1:
            return False#
            
    subGrid=[]
    for i in range(6,9):
        for j in range(3):
            subGrid.append(grid[i][j])
    for i in range(9):
        if subGrid.count(str(i)) > 1:
            return False 
    subGrid=[]                
    for i in range(6,9):
        for j in range(3,6):
            subGrid.append(grid[i][j])
    for i in range(9):
        if subGrid.count(str(i)) > 1:
            return False 
    subGrid=[]                
    for i in range(6,9):
        for j in range(6,9):
            subGrid.append(grid[i][j])
    for i in range(9):
        if subGrid.count(str(i)) > 1:
            return False#End of 3x3 grid checks   
    
    return True#Returns true if the supplied grid does not fulfil any requirements to be invalid          
            
def getSudoku():
    """Converts the input supplied into a 2D array"""
    values = []
    for i in range(9):
        values.append(input())
    for i in values:
        line = []
        for j in range(len(i)):
            line.append(i[j])
        grid.append(line)

if __name__ == '__main__':
    grid = []
    getSudoku()
    if checkSudoku(grid):
        print('Sudoku grid is valid')
    else: print('Sudoku grid is not valid')