#check if a sudoku game is valid or not
#victor gueorguiev
#10 may 2014

def recieve_list():
    grid = []
    for i in range(9):#check if numbers one through nine appear in each 3x3 grid more than once
        row = input()
        row_list = []
        for i in row:
            row_list.append(int(i))
        grid.append(row_list)# create a function that extracts a certain 3x3 matix from the larger 9x9 matrix, use multiples of i in range(3)
    return grid

def check_rows(grid):
    for i in range(len(grid)):
        values = [1,2,3,4,5,6,7,8,9]
        for j in range(len(grid[i])):
            if grid[i][j] in values:
                values.pop(values.index(grid[i][j]))
            elif not grid[i][j] in values:
                return False
    return True

def check_columns(grid):
    for i in range(len(grid)):
        values = [1,2,3,4,5,6,7,8,9]
        for j in range(len(grid[i])):
            if grid[j][i] in values:
                values.pop(values.index(grid[j][i]))
            elif not grid[j][i] in values:
                return False
    return True

def check_3x3_grid(grid):
    for i in range(3):
        for j in range(3):
            values = [1,2,3,4,5,6,7,8,9]
            for k in range(0+3*i,3+3*i):
                for l in range(0+3*j,3+3*j):
                    if grid[k][l] in values:
                        values.pop(values.index(grid[k][l]))
                    elif not grid[k][l] in values:
                        return False
    return True

def main():
    grid = recieve_list()
    if not (check_rows(grid) and check_columns(grid) and check_3x3_grid(grid)):
        print('Sudoku grid is not valid')
    else:
        print('Sudoku grid is valid')

main()