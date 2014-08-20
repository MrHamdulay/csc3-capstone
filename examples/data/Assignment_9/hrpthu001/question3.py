"""Program to check the validity of a soduko grid.
thushar hariparsad
15 May 2014"""

def checksudoku():
    
    #Extract rows from input
    grid = []
    for i in range(9):
        row = []
        s_row = input()
        for j in range(9):
            row.append(eval(s_row[j]))
        grid.append(row)
        
    #Extract columns from grid
    for i in range(9):
        column = []
        for j in range(9):
            column.append(grid[j][i])
        grid.append(column)
        
    #Extract 3x3 grids from grid.
    newgrid = []
    for i in range(3):
        for j in range(3):
            newgrid.append(grid[i][j])
    grid.append(newgrid)
    
    newgrid = []
    for i in range(3):
        for j in range(3,6):
            newgrid.append(grid[i][j])
    grid.append(newgrid)
    
    newgrid = []
    for i in range(3):
        for j in range(6,9):
            newgrid.append(grid[i][j])
    grid.append(newgrid)
    
    for i in range(3,6):
        for j in range(3):
            newgrid.append(grid[i][j])
    grid.append(newgrid)
    
    newgrid = []
    for i in range(3,6):
        for j in range(3,6):
            newgrid.append(grid[i][j])
    grid.append(newgrid)
    
    newgrid = []
    for i in range(3,6):
        for j in range(6,9):
            newgrid.append(grid[i][j])
    grid.append(newgrid)
    
    for i in range(6,9):
        for j in range(3):
            newgrid.append(grid[i][j])
    grid.append(newgrid)
    
    newgrid = []
    for i in range(6,9):
        for j in range(3,6):
            newgrid.append(grid[i][j])
    grid.append(newgrid)
    
    newgrid = []
    for i in range(6,9):
        for j in range(6,9):
            newgrid.append(grid[i][j])
    grid.append(newgrid)
    
    #check if valid if the sum of rows, columns and 3x3 grids is 45
    for i in range(27):
        check = 0
        for j in range(9):
            check += grid[i][j]
        if check != 45:
            print("Sudoku grid is not valid")
            return -1
        
    print("Sudoku grid is valid")
    
if __name__=="__main__":
    checksudoku()