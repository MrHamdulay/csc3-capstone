# Program to check if a complete Sudoku grid is valid or not.

def grid(x):
    grid=[]  
    for row in range(9):
        across = []  #creating lists for rows
        for column in range(9):
            across.append(eval(x[row][column]))  #putting values into rows
        
        grid.append(across) #putting above rows into grid
    
    return grid
        
        
    
# Iteration: Rows
def rows(grid):
    for rows in range(9):
        row_list=[] #creating a list for the rows
        
        for column in range(9):
            row_list.append(grid[rows][column]) #putting values across the row into list
        
        for i in row_list:
            if row_list.count(i)!=1: 
                return False
            
            else: 
                continue 
    
    return True        



# Iteration: Columns            
def columns(grid):
    for columns in range(9):
        column_list = []
        
        for rows in range(9):
            column_list.append(grid[rows][col])
        
        for i in column_list:
            if column_list.count(i) !=1:
                return False
            
            else:
                continue
    
    return True
            

# Iteration: Subgrid
def subgrid(grid, row_1, row_2, col_1, col_2): 
    subgrid1=[]
    for row in range(row_1, row_2): 
        for col in range(col_1, col_2):
            subgrid1.append(grid[row][col])
    
    for i in subgrid1:
        if subgrid1.count(i)!=1:
            return False

        else:
            return True
        
        
def overall():
    numbers = []
    while len(numbers)!=9:
        enter = input("")
        numbers.append(enter)
    
    sudoku = grid(numbers)
    
    yes = "Sudoku grid is valid"
    no = "Sudoku grid is not valid"
    
    if rows(sudoku)==False:
        print(no)
        
    elif columns(sudoku)==False:
        print(no)
    
    elif subgrid(sudoku, 0, 3, 0, 3)==False:
        print(no)

    elif subgrid(sudoku, 0, 3, 3, 6)==False:
        print(no)

    elif subgrid(sudoku, 0, 3, 6, 9)==False:
        print(no)

    elif subgrid(sudoku, 3, 6, 0, 3)==False:
        print(no)

    elif subgrid(sudoku, 3, 6, 3, 6)==False:
        print(no)

    elif subgrid(sudoku, 3, 6, 6, 9)==False:
        print(no)

    elif subgrid(sudoku, 6, 9, 0, 3)==False:
        print(no)

    elif subgrid(sudoku, 6, 9, 3, 6)==False:
        print(no)

    elif subgrid(sudoku, 6, 9, 6, 9)==False:
        print(no)

    else:
        print(yes)
        
        
  
  
overall()      
    