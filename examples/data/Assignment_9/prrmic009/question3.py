"""program to chech if an input Sudoku grid is valid or not
Mick Perring
16 May 2014"""

def check_row(grid):   # check_row function to check if rows are valid
    for i in range(9): # function breaks out of loop if invalid row is found
        valid = False  # thus leaving valid = False and returning "False"
        for j in range(9): # if no rows are invalid, function returns "True"
            row = False
            for k in range(j+1, 9):
                num = False
                if grid[i][j] == grid[i][k]: break
                else: num = True
            if num == False: break
            else: row = True
        if row == False: break
        else: valid = True
    return valid

def check_column(grid):   # check_column function to check if rows are valid
    for i in range(9):    # function breaks out of loop if invalid column is found
        valid = False     # thus leaving valid = False and returning "False"
        for j in range(9):  # if no columns are invalid, function returns "True"
            column = False
            for k in range(j+1, 9):
                num = False
                if grid[j][i] == grid[k][i]: break
                else: num = True
            if num == False: break
            else: column = True
        if column == False: break
        else: valid = True
    return valid
    
def check_block(grid):   # check_block function to check if individual 3X3 blocks are valid
    valid = False        # function appends each value in 3X3 block into new row
    new_grid = []        # each new row is then appended into a new grid
    for i in range(3):   # check_row function is run through new grid
        for j in range(3):  # if check_row returns "False", original block was invalid and function returns "False"
            new_row = []    # if check_row returns "True", original block was valid and function returns "True"
            for k in range(3):
                for l in range(3):
                    new_row.append(grid[3*i+k][3*j+l])
            new_grid.append(new_row)
    if check_row(new_grid) == True:
        valid = True
    return valid

def main():  # main function creates 9X9 grid of input values and runs grid through check functions
    grid = []
    for i in range(9):
        row = []
        row_num = input()
        for j in range(9):
            row.append(eval(row_num[j]))
        grid.append(row)
    check_block(grid)
    if check_row(grid) == True and check_column(grid) == True and check_block(grid) == True:
        print("Sudoku grid is valid")   # if grid passes check functions, prints "Sudoku grid is valid"
    else: print("Sudoku grid is not valid") # if grid fails any check functions, prints "Sudoku grid is not valid"
    
main()