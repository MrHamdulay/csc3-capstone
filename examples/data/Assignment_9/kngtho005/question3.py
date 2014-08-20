# question3.py
# program to check if a complete Sudoku grid is valid or not
# Thomas Konigkramer
# 11 May 2014
    
def row_check(input_grid):
    for row in range(9):
        for col in range(9):
            if str(col + 1) not in input_grid[row]:
                return False 
    return True 
  
def column_check(input_grid):
    # creating a grid will all the numbers column for column
    col_grid = [[""] * 9] * 9
    for m in range(9):
        for n in range(9):
            col_grid[m][n] = input_grid[n][m]
        for o in range(9):
            if str(o + 1) not in col_grid[m]:
                return False 
    return True 
    
def block_check():
    for a in range(9):
        for b in range(9):
            if str(b + 1) not in grid[a]:
                return False 
    return True     

if __name__ == "__main__":
    # creating grid with all the inputed information
    initial_grid = []
    
    for i in range(9):
        sudoku = input()
        for j in range(9):
            initial_grid.append(sudoku[j])
    
    # creating a grid with all the numbers row for row
    input_grid = [[""] * 9] * 9
    for k in range(9):
        input_grid[k] = initial_grid[k*9:k*9+9]
       
    block_grid = [[""] * 9] * 9
    for grid_no in range(9):
        block_grid[grid_no]
    if row_check(input_grid) and column_check(input_grid): # and block check
        print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")