'''program to check sudoku grids if they are correct
Tinotenda Chemvura CHMTIN004
15 May 2014'''
#___________________________PROGRAM STARTS HERE_________________________________
def get_grid():
    '''function that retrieves the sudoku values and then creates a 2D grid'''
    sgrid = []
    for i in range (9):
        row1 = input()
        row2 = []
        for num in row1:
            num = eval(num)
            row2.append(num)
        sgrid.append(row2)
    return sgrid

def check_rows(grid):
    '''Function that checks if the rows in the 2D "grid" do not have 2 identical
    characters/numbers and returns False if there are'''
    #create a new list for each row and add numbers that are not in the new list from the old list. if their lengths are the same then return True.
    for row in grid:
        new_row = []
        for number in row:
            if number not in new_row:
                new_row.append(number)        
        if len(new_row) != len(row):
            return False
    else:
        return True
    
def check_col(grid):
    '''function to check if the columns have any identical characters and
    returns False if there are'''
    #make new grid with the "rows" as columns (switch the rows and columns) then use the check_rows function tosee if there are any duplicates
    new_grid = []
    for col in range(9):
        new_col = []
        for row in grid:
            new_col.append(row[col])
        new_grid.append(new_col)
    return check_rows(new_grid)

def check_subgrid(grid):
    '''function to check the 3x3 sub-grids for identical numbers'''
    #create a new grid with each row representing numbers in a sub grid then use "check_rows()" function to check for identical characters
    new_grid = []
    cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9 = [], [], [], [], [], [], [], [], []
    #________cell 1, 2, 3_____________
    for row in range(3):
        for col in range(3):
            cell1.append(grid[row][col])
            cell2.append(grid[row][col+3])
            cell3.append(grid[row][col+6])
    new_grid.append(cell1)
    new_grid.append(cell2)
    new_grid.append(cell3)      
    #________cell 4, 5, 6_____________
    for row in range(3,6):
        for col in range(3):
            cell4.append(grid[row][col])
            cell5.append(grid[row][col+3])
            cell6.append(grid[row][col+6])
    new_grid.append(cell4)
    new_grid.append(cell5)
    new_grid.append(cell6)
    #________cell 7, 8, 9_____________    
    for row in range(6,9):
        for col in range(3):
            cell7.append(grid[row][col])
            cell8.append(grid[row][col+3])
            cell9.append(grid[row][col+6])
    new_grid.append(cell7)
    new_grid.append(cell8)
    new_grid.append(cell9)      
    
    return check_rows(new_grid)

def print_grid(grid):
    '''function to print the sudoku grid'''
    for row in grid:
        row_s = ''
        for num in row:
            row_s += str(num)
        print(row_s)
#retrieve the sudoku grid...check if every condition is satisfied and print the result.
#invalid_grid_test1 = [[3, 5, 9, 7, 1, 6, 4, 8, 2], [8, 6, 7, 3, 4, 5, 9, 1, 2], [4, 1, 3, 9, 2, 8, 6, 7, 5], [3, 9, 8, 5, 7, 4, 1, 2, 6], [5, 4, 6, 2, 8, 1, 7, 3, 9], [1, 7, 2, 6, 3, 9, 5, 4, 8], [9, 8, 4, 1, 6, 3, 2, 5, 7], [6, 2, 1, 8, 5, 7, 3, 9, 4], [7, 3, 5, 4, 9, 2, 8, 6, 1]]
#invalid_grid_test2 = [[2, 5, 9, 7, 1, 6, 4, 8, 3], [8, 6, 7, 3, 4, 5, 9, 1, 2], [4, 1, 3, 9, 2, 8, 6, 7, 5], [3, 9, 8, 5, 7, 4, 1, 2, 6], [5, 4, 6, 2, 8, 1, 7, 3, 9], [1, 7, 2, 6, 3, 9, 5, 4, 8], [9, 8, 4, 1, 6, 3, 2, 5, 7], [6, 2, 1, 8, 5, 7, 3, 9, 4], [7, 3, 5, 4, 9, 2, 8, 6, 1]]
sudoku_grid = get_grid()
if check_rows(sudoku_grid):
    if check_col(sudoku_grid):
        if check_subgrid(sudoku_grid):
            print("Sudoku grid is valid")
        else:
            print("Sudoku grid is not valid")        
    else:
                print("Sudoku grid is not valid")      
else:
            print("Sudoku grid is not valid")  

#_____________________________END OF PROGRAM____________________________________