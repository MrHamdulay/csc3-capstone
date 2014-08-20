# Checking A Sudoku Grid
# Devaksha Pillay
# 14 May 2014

# put input into a list
input_list = []
while len(input_list)<9:
    data = input("")
    input_list.append(data)
    
# create the grid
def create_grid(x):
    sudoku_grid = []
    for across in range(9):
        rows = []
        for columns in range(9):
            rows.append(eval(x[across][columns]))
            
        sudoku_grid.append(rows)
    return sudoku_grid

sudoku_grid = create_grid(input_list)

# check the columns
def column_check(sudoku):
    for column in range(9):
        list_columns = []
        for row in range(9):
            list_columns.append(sudoku_grid[row][column])
            for number in list_columns:
                if list_columns.count(number) > 1:
                    return False
                else:
                    continue
    return True

#check the rows
def row_check(sudoku):
    for row in range(9):
        list_rows = [] 
        for column in range(9):
            list_rows.append(sudoku[row][column])
            for number in list_rows:
                if list_rows.count(number) > 1:
                    return False
                else: 
                    continue
    return True      

#check the mini grid
def minigrid_check(sudoku, row_beg , row_end, col_beg , col_end): 
    # ranges of each subgrid
    minigrid=[]
    for rows in range(row_beg, row_end): #row1 and row2 will change depending on the subgrid
        for columns in range(col_beg, col_end):
            minigrid.append(sudoku[rows][columns])
    for number in minigrid:
        if minigrid.count(minigrid) > 1:
            return False
        else:
            return True 

# check for every potential error
down = column_check(sudoku_grid)
across = row_check(sudoku_grid)
mini_1 = minigrid_check(sudoku_grid, 0, 3, 0, 3)
mini_2 = minigrid_check(sudoku_grid, 0, 3, 3, 6)
mini_3 = minigrid_check(sudoku_grid, 0, 3, 6, 9)
mini_4 = minigrid_check(sudoku_grid, 3, 6, 0, 3)
mini_5 = minigrid_check(sudoku_grid, 3, 6, 3, 6)
mini_6 = minigrid_check(sudoku_grid, 3, 6, 6, 9)
mini_7 = minigrid_check(sudoku_grid, 6, 9, 0, 3)
mini_8 = minigrid_check(sudoku_grid, 6, 9, 3, 6)
mini_9 = minigrid_check(sudoku_grid, 6, 9, 6, 9)

if mini_1 == True and mini_2 == True and mini_3 == True and mini_4 == True and mini_5 == True and mini_6 == True and mini_7 == True and mini_8 == True and mini_9 == True and down == True and across == True:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")