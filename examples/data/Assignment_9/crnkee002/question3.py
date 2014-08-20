"""A9Q3 - Sudoku checker
11/05/2013
CRNKEE002"""

def main():
    rows = []
    numbers = []
    for i in range(9):
        rows.append(input())
    into2dlist(rows, numbers)
    check_valid(numbers)
    
def into2dlist(lines, array):
    for i in range(9):
        temp = []
        for j in range(9):
            temp.append(lines[i][j])
        array.append(temp)
    return array

def check_rows(grid):
    for i in range(9):
        row = []
        for j in range(9):
            row.append(grid[i][j])
        for counter in range(9):
            if row.count(str(counter+1)) != 1:     
                return False
    else:
        return True
    
    
def check_columns(grid):
    for i in range(9):
        column = []
        for j in range(9):
            column.append(grid[j][i])
        for counter in range(9):
            if column.count(str(counter+1)) != 1:
                return False
    else:
        return True

def check_minigrid(grid):
    multi = 0
    temp = []
    for mult in range(3):
        for x in range(9):            
            for y in range(3*mult, 3*mult+3):
                temp.append(grid[x][y])  
            if x in [2,5,8]:
                for counter in range(9):
                    if temp.count(str(counter+1)) != 1:
                        return False                    
                temp = []
        mult +=1
    else:
        return True

def check_valid(grid):
    if check_minigrid(grid)== True and check_rows(grid)== True and check_columns(grid) == True:
        print('Sudoku grid is valid')
    else:
        print('Sudoku grid is not valid')
    
if __name__ == '__main__':
    main()