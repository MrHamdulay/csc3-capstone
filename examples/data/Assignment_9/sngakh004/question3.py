"""Program to check if sudoku puzzle is correct
Akhil Singh
SNGAKH0004
15 May 2014"""


def check_sudoku():
    
    
    comp_grid = []                            #Makes the rows from the input specified
    for a in range(9):
        row = []
        str_row = input()
        for b in range(9):
            row.append(eval(str_row[b]))
        comp_grid.append(row)
        
  
    for a in range(9):                        #Make collumns from comp_grid.
        col = []
        for b in range(9):
            col.append(comp_grid[b][a])
        comp_grid.append(col)
        
    
    grid_3x3 = []                             #Make 3x3 grids from comp_grid.
    for a in range(3):
        for b in range(3):
            grid_3x3.append(comp_grid[a][b])
    comp_grid.append(grid_3x3)
    
    grid_3x3 = []
    for a in range(3):
        for b in range(3,6):
            grid_3x3.append(comp_grid[a][b])
    comp_grid.append(grid_3x3)
    
    grid_3x3 = []
    for a in range(3):
        for b in range(6,9):
            grid_3x3.append(comp_grid[a][b])
    comp_grid.append(grid_3x3)
    
    for a in range(3,6):
        for b in range(3):
            grid_3x3.append(comp_grid[a][b])
    comp_grid.append(grid_3x3)
    
    grid_3x3 = []
    for a in range(3,6):
        for b in range(3,6):
            grid_3x3.append(comp_grid[a][b])
    comp_grid.append(grid_3x3)
    
    grid_3x3 = []
    for a in range(3,6):
        for b in range(6,9):
            grid_3x3.append(comp_grid[a][b])
    comp_grid.append(grid_3x3)
    
    for a in range(6,9):
        for b in range(3):
            grid_3x3.append(comp_grid[a][b])
    comp_grid.append(grid_3x3)
    
    grid_3x3 = []
    for a in range(6,9):
        for b in range(3,6):
            grid_3x3.append(comp_grid[a][b])
    comp_grid.append(grid_3x3)
    
    grid_3x3 = []
    for a in range(6,9):
        for b in range(6,9):
            grid_3x3.append(comp_grid[a][b])
    comp_grid.append(grid_3x3)
    

    for a in range(27):                                    #Check if the grid is correct by seeing if the sum of all the rows, collumns and 3x3 grid is equal to 45
        valid_check = 0
        for b in range(9):
            valid_check += comp_grid[a][b]
        if valid_check != 45:
            print("Sudoku grid is not valid")
            return -1
        
    print("Sudoku grid is valid")
    
if __name__=="__main__":
    check_sudoku()