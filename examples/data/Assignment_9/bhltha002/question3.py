

#defining necessary variables
sudoku_rows = []
sudoku_column = []
sudoku_grid = []
lists = []
line = []
grid1 = []
grid2 = []
grid3 = []
grid4 = []
grid5 = []
grid6 = []
grid7 = []
grid8 = []
grid9 = []

#Creating 2D grid to house sudoku grid
for i in range (9):
    sudoku_rows.append ([0,0,0,0,0,0,0,0,0])

#Filling 2D list
for i in range (9):
    x = input ()
    for j in range (len (x)):
        sudoku_rows [i][j] = eval (x [j])

#Creating 2D list of columns    
for i in range (0,9):
    lists = []
    for j in range (0,9):
        lists.append (sudoku_rows [j][i])
    sudoku_column.append (lists)

#Creating 2D list of 3 x 3 grids
for i in range (9):
    for j in range (9):
        if 0 <= i <= 2:
            if 0 <= j <= 2:
                grid1.append (sudoku_rows [i][j])
            elif 3 <= j <= 5:
                grid2.append (sudoku_rows [i][j])
            elif 6 <= j <= 8:
                grid3.append (sudoku_rows [i][j])
        elif 3 <= i <= 5:
            if 0 <= j <= 2:
                grid4.append (sudoku_rows [i][j])
            elif 3 <= j <= 5:
                grid5.append (sudoku_rows [i][j])
            elif 6 <= j <= 8:  
                grid6.append (sudoku_rows [i][j])
        elif 6 <= i <= 8:
            if 0 <= j <= 2:
                grid7.append (sudoku_rows [i][j])
            elif 3 <= j <= 5:
                grid8.append (sudoku_rows [i][j])
            elif 6 <= j <= 8:  
                grid9.append (sudoku_rows [i][j])
                
sudoku_grid.append (grid1)
sudoku_grid.append (grid2)
sudoku_grid.append (grid3)
sudoku_grid.append (grid4)
sudoku_grid.append (grid5)
sudoku_grid.append (grid6)
sudoku_grid.append (grid7)
sudoku_grid.append (grid8)
sudoku_grid.append (grid9)

def test (string):
    """Function to test if a string contains all 9 numbers"""
    #Iterating i through 1-9 and checking in string
    for i in range (1,10):
        if str (string).find (str (i)) == -1:
            return False
    return True

def check_list (x):
    """Function to search through a list of lists to verify that each index contains only one of each number"""
    #Using test function and breaking up 2D lists into strings
    for i in range (9):
        string = ''
        for j in range (9):
            string = string + str (x [i][j])
        if test (string) == False:
            return False
    return True

def check_sudoku (sudoku_rows, sudoku_column, sudoku_grid):
    """Function to verify if sudoku is complete"""
    
    #Testing to see if all 3 are true when tested by check_list
    x = check_list (sudoku_rows)
    y = check_list (sudoku_column)
    z = check_list (sudoku_grid)
    
    if x and y and z:
        print ("Sudoku grid is valid")
    else: 
        print ("Sudoku grid is not valid")

#Running function and printing values
check_sudoku (sudoku_rows, sudoku_column, sudoku_grid)