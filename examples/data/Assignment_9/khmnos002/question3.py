"""program to check validity of soduku grid
Nosipho Khumalo
10 May 2014"""

def valid():  
    #create 2-D array in which to store values
    grid = []
    grid2 = []
    for i in range(9):
        row = input()
        for j in row:
            grid2.append(j)
        grid.append(grid2)
        grid2 = []

    
    #check if cells in the same row share a value
    def row_check(grid):
        for row in range(9):
            duplicate = []
            for column in range(9):
                if grid[row][column] not in duplicate:
                    duplicate.append(grid[row][column])
                else:
                    return False
        return True
                
                
    #check if cells in the same column share a value   
    def column_check(grid):
        for column in range(9):
            duplicate = []
            for row in range(9):
                if grid[row][column] not in duplicate:
                    duplicate.append(grid[row][column])
                else:
                    return False
        return True
    
    #create 3x3 grids
    def grids(rowstart, rowend, startpos, endpos):
        subgrid = []
        for row in range(rowstart, rowend):
            for column in range(startpos, endpos):
                subgrid.append(grid[row][column])
        return subgrid
    
    grid1 = grids(0, 3, 0, 3)
    grid2nd = grids(0, 3, 3, 6)
    grid3 = grids(0, 3, 6, 9)
    grid4 = grids(3, 6, 0, 3)
    grid5 = grids(3, 6, 3, 6)
    grid6 = grids(3, 6, 6, 9)
    grid7 = grids(6, 9, 0, 3)
    grid8 = grids(6, 9, 3, 6)
    grid9 = grids(6, 9, 6, 9) 
    
    #check for repeated values
    def sub_check(values):
        duplicate = []
        for i in range(len(values)):
            if values[i] not in duplicate:
                    duplicate.append(values[i])
            else:
                return False
        return True

    #check if all conditions are met    
    if sub_check(grid1) == False:
        print("Sudoku grid is not valid")
    elif sub_check(grid2nd) == False:
        print("Sudoku grid is not valid")
    elif sub_check(grid3) == False:
        print("Sudoku grid is not valid")
    elif sub_check(grid4) == False:
        print("Sudoku grid is not valid")
    elif sub_check(grid5) == False:
        print("Sudoku grid is not valid")
    elif sub_check(grid6) == False:
        print("Sudoku grid is not valid")
    elif sub_check(grid7) == False:
        print("Sudoku grid is not valid")
    elif sub_check(grid8) == False:
        print("Sudoku grid is not valid")
    elif sub_check(grid9) == False:
        print("Sudoku grid is not valid")
    elif row_check(grid) == False:
        print("Sudoku grid is not valid")
    elif column_check(grid) == False:
        print("Sudoku grid is not valid")
    else:
        print("Sudoku grid is valid")
    
valid()