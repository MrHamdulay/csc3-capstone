"""check if a complete Sudoku grid is valid or not
Elizabeth Cilliers
11/05/2014"""

grid=[]
def suduko(grid):
#create suduko grid
    
    for i in range (9):
        l=input("")
        line=list(l)
        innergrid=[]
        for num in range (len(line)):
            element=eval(line[num])
            innergrid.append(element)
        grid.append(innergrid)
    
suduko(grid)

   

def check_row(grid):
    #check if 2 cells in the same row have the same value
    for row in range(9):
        for col in range (9):
            for num in range(col+1,9-col): #range is col+1(cell next to cell under inspection) up and till 9-col (decrease column by 1 each time because we only compare from column position onwards
                if grid[row][col]==grid[row][num]: #check a cell in row with all the other cells in the row by increasing num.
                    return False
    else:
        return True

def check_col(grid):
    #check if 2 cells in the same column have the same value
    for col in range(9):
        for row in range(9):
            for num in range(row+1,9-row): 
                if grid[row][col]==grid[num][col]:
                    return False
    else:
        return True
#print out the outcome of the grid. Valid (True) or not valid (False).
def out_come(grid):
    if check_row(grid)==False:
        print("Sudoku grid is not valid")
    elif check_col(grid)==False:
        print("Sudoku grid is not valid")
    else:
        print("Sudoku grid is valid")

out_come(grid)


