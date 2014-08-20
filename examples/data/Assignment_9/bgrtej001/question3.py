"""Assignement 9, Question 3
Tejasvin Bagirathi
Program to check if sudoku grid is valid"""

def sudoku_check():
    #Extract rows from input into grid
    grid = []
    for i in range(9):
        row = []
    #Rows input by user
        stringrow = input()
        for j in range(9):
            #Convert to integer and add to string
            row.append(eval(stringrow[j]))
            #Add row to grid
        grid.append(row)
            
    #Extract collumns from grid
    for i in range(9):
        col = []
        for j in range(9):
            col.append(grid[j][i])
        grid.append(col)
            
    #Extract 3x3 grids from the grid
    #In each of the statements, the xgrid is declared and the values from each 3x3 block
    #Are added using a loop. The loop adds each element in the 3x3 blocks using by finding them in their position
    #This process is repeated over and over for all 9 grids 
    
    #Top three blocks
    xgrid1 = []
    xgrid2 = []
    xgrid3 = []
    for i in range(3):
        for j in range(3):
            xgrid1.append(grid[i][j])
        for j in range(3,6):
            xgrid2.append(grid[i][j])
        for j in range(6,9):
            xgrid3.append(grid[i][j])  
    grid.append(xgrid1)
    grid.append(xgrid2)
    grid.append(xgrid3)
        
    #Middle 3 blocks 
    xgrid1 = []
    xgrid2 = []
    xgrid3 = []
    for i in range(3,6):
        for j in range(3):
            xgrid1.append(grid[i][j])
        for j in range(3,6):
            xgrid2.append(grid[i][j])
        for j in range(6,9):
            xgrid3.append(grid[i][j])
    grid.append(xgrid1)
    grid.append(xgrid2)
    grid.append(xgrid3)
    
    #Bottom 3 blocks
    xgrid1 = []
    xgrid2 = []
    xgrid3 = []
    for i in range(6,9):
        for j in range(3):
            xgrid1.append(grid[i][j])   
        for j in range(3,6):
            xgrid2.append(grid[i][j])
        for j in range(6,9):
            xgrid3.append(grid[i][j])
    grid.append(xgrid1)
    grid.append(xgrid2)
    grid.append(xgrid3)
        
    #Add sum of the rows, collumns, and 3x3 blocks. Then check is this is correct
    for i in range(27):
        check = 0
        for j in range(9):
            check += grid[i][j]
        if check != 45:
            print("Sudoku grid is not valid")
            return 0
    
    print("Sudoku grid is valid")
    
if __name__ == '__main__':
    sudoku_check()
    