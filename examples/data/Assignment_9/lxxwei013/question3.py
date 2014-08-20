"""check validity of Sudoku grid
Michelle Lu
11 May 2014"""


def creategrid(x):
    grid=[]  
    for row in range(9):
        across=[]  #creates a list for the rows
        for col in range(9):
            across.append(eval(x[row][col]))  #puts values in rows
        
        grid.append(across) #puts rows into grid
    return grid
        
        
    

#iterate through rows
def check_rows(grid):
    for rows in range(9):
        rowlist=[] #creates a list for the rows
        for col in range(9):
            rowlist.append(grid[rows][col]) #puts values across the row into list
        for i in rowlist:
            if rowlist.count(i)!=1: #if a value appears more than once
                return False
            else: 
                continue #continues for the rest of the rows
    return True        

#iterate through columns            
def check_col(grid):
    for col in range(9):
        col_list=[]
        for rows in range(9):
            col_list.append(grid[rows][col])
        for i in col_list:
            if col_list.count(i) !=1:
                return False
            else:
                continue
    return True
            

#iterate through subgrid
def check_subgrid(grid, row1,row2, col1, col2): #these are the ranges
    subgrid1=[]
    for row in range(row1, row2): #row1 and row2 will change depending on the subgrid
        for col in range(col1, col2):
            subgrid1.append(grid[row][col])
    for i in subgrid1:
        if subgrid1.count(i)!=1:
            return False
        else:
            return True
        
        
def checkall():
    num_list=[]
    while len(num_list)!=9:
        enter=input("")
        num_list.append(enter)
    
    sudoku=creategrid(num_list)
    
    yes="Sudoku grid is valid"
    no="Sudoku grid is not valid"
    
    if check_rows(sudoku)==False:
        print(no)
    elif check_col(sudoku)==False:
        print(no)
    elif check_subgrid(sudoku, 0, 3, 0, 3)==False:
        print(no)
    elif check_subgrid(sudoku, 0, 3, 3, 6)==False:
        print(no)
    elif check_subgrid(sudoku, 0, 3, 6, 9)==False:
        print(no)
    elif check_subgrid(sudoku, 3, 6, 0, 3)==False:
        print(no)
    elif check_subgrid(sudoku, 3, 6, 3, 6)==False:
        print(no)
    elif check_subgrid(sudoku, 3, 6, 6, 9)==False:
        print(no)
    elif check_subgrid(sudoku, 6, 9, 0, 3)==False:
        print(no)
    elif check_subgrid(sudoku, 6, 9, 3, 6)==False:
        print(no)
    elif check_subgrid(sudoku, 6, 9, 6, 9)==False:
        print(no)
    else:
        print(yes)
        
        
  
  
checkall()      
    