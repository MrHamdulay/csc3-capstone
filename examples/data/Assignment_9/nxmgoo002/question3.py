"""This program checks if a complete Sudoku grid is valid or not
Nxumalo Goodman
16 May 2014"""

no_set = []
for i in range(9):  
    digits = input()  
    no_set.append(digits)   
    
#creates a 9 by 9 grid
def make_grid():   
    grid = []
    length = 9   
    for i in range (length):   
        grid.append ([0]*9) 
            
    return grid
    
grid = make_grid()    

#put all the values to the grid
for a in range(9):
    for b in range(9):      
        grid[a][b] = no_set[a][b]   

#checks if there are any same numbers in the columns
def column_check(grid):
    column_digits = []    
    
    for r in range(9):    
        del column_digits
        column_digits = []
        
        for col in range(9):
            if grid[col][r] not in column_digits:
                column_digits.append(grid[col][r])
                
        if len(column_digits) < 9:
            return False
            break
    else:
        return True

#checks if there are any same numbers in the rows
def rows_check(grid):
    row_list = []
    
    for col in range(9):
        del row_list
        row_list = []
        
        for r in range(9):
            if grid[col][r] not in row_list:
                row_list.append(grid[col][r])
                
        if len(row_list) < 9:
            
            return False
            break
    else:
        return True
onlydigit = True
#checks if there are any same numbers in the 3 by 3 grid
def boxs_check(grid):
    small_grid = []
    global onlydigit
    
    for col in range(0,9,3):
        for i in range(0,9,3):
            del small_grid
            small_grid = []
            
            for r in range(i,i+3):
                small_grid.append(grid[r][col:col+3])


            digitscheck = []
            for i in range(3):
                for j in range(3):
                    if small_grid[i][j] not in digitscheck:
                        digitscheck.append(small_grid[i][j])

            if len(digitscheck) < 9:
                onlydigit = False
                
    return onlydigit

def main(grid):  
    #checks if the all the conditions are met for soduku to be valid
    if boxs_check(grid) and column_check(grid) and rows_check(grid):
        print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")
        
main(grid)