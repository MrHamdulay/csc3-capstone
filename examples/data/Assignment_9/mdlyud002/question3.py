# Yudhi Moodley
# Assignment 9- question 3
# 16/05/2014


def creategrid(x):
    grid=[]  
    for row in range(9):
        #creates a list for the rows
        across=[]  

        for col in range(9):
            #puts values in rows
            across.append(eval(x[row][col]))  
        #puts rows into grid
        grid.append(across) 
    return grid
        
        
    

#iterate through rows
def check_rows(grid):
    for rows in range(9):
        #creates a list for the rows
        rowlist=[] 

        for col in range(9):
            #puts values across the row into list
            rowlist.append(grid[rows][col]) 

        for i in rowlist:
            #if a value appears more than once

            if rowlist.count(i)!=1: 
                return False

            else:
                #continues for the rest of the rows
                continue 
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
def check_subgrid(grid, row1,row2, col1, col2): 
    subgrid1=[]
    
    for row in range(row1, row2): 
        
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
    