'''This program checks if a sudoku grid is valid or not
By Kouame Hermann KOUASSI: KSSKOU001
On 11 May 2014'''

def create_grid():
    grid = []
    for i in range(9):
        row = []
        row_str = input()
        for digit in row_str :
            row.append(eval(digit))
        grid.append(row)
    return grid

def hori_check(grid):
    '''return True if no 2 cells in the same row have the same value, otherwise 
    return False'''
    
    for row in grid:
        for digit in row:
            counter = row.count(digit)
            if counter > 1:
                return False
            else:
                continue
    return True

def vert_check(grid):
    '''return True if no 2 cells in the same column have the same value, otherwise 
        return False'''
    
    for i in range(len(grid)):
        row = []
        for j in range(len(grid)):
            row.append(grid[j][i])
        for digit in row:
            counter = row.count(digit)
            if counter > 1:
                return False
            else:
                continue
    return True

def sub_sudoku(grid):
    counter = 0
    sub_grid = []
    grid_no = 0
    start = 0
    end = 3
    for i in range(9):
        if i % 3 == 0 :
            start = 0
            end = 3        
        elif i % 3 == 1 :
            start = 3
            end = 6
        else:
            start = 6
            end = 9
        if i < 3:
            grid_no = 0
        elif i < 6:
            grid_no = 3
        else :
            grid_no = 6
        for j in range(3):
            sub_grid.append(grid[grid_no][start:end])
            grid_no += 1
        #Ckeck if a digit is not repeated in the sub_grid
        for digit in range(9):
            counter = 0
            for row in sub_grid:
                if digit in row:
                    counter += row.count(digit)
            if counter >= 2:
                return False      
        else:
            sub_grid = []
    return True

def main():
    grid = create_grid()
    if hori_check(grid) and vert_check(grid) and sub_sudoku(grid):
        print('Sudoku grid is valid')
    else:
        print('Sudoku grid is not valid')
        

if __name__=="__main__":
    main()
    
    
    