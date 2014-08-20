"""kekolo Phetla 
phtkek001 
assignment 9
checking if a complete sudoku grid is valid or not"""

#change input into a list
number_list = []
for i in range(9):
    numbers = input()
    number_list.append(numbers)
    
#initialize grid
grid=[]
for i in range(9):
    grid.append([0]*9)

#assign values to grid
for i in range(9):
    for k in range(9):
        grid[i][k] == number_list[i][k]
        
#check columns
def check_columns(grid):
    col_list = []
    for row in range(9):
        del col_list
        col_list = []
        for col in range(9):
            if grid[col][row] not in col_list:
                col_list.append(grid[col][row])
        if len(col_list)<9:
            return False
        break
    else:
        return True
    
    
#check rows
def check_rows(grid):
    row_list = []
    for col in range(9):
        del row_list
        row_list = []
        for row in range(9):
            if grid[row][col] not in row_list:
                row_list.append(grid[row][col])
        if len(row_list)<9:
            return False
        break
    else:
        return True
    
#check 3*3 grids
prime = True
def check_boxes(grid):
    boxes=[]
    global prime
    for col in range(0,9,3):
        for i in range(0,9,3):
            del boxes
            boxes = []
            for row in range(i,i+3):
                boxes.append(grid[row][col:col+3])
                
                check=[]
                for j in range(3):
                    for k in range(3):
                        if boxes[j][k] not in check:
                            check.append(grids[j][k])
                if len(check)<9:
                    prime = False
    return prime

#check if entire grid is valid
def check(grid):
    if check_boxes and check_rows and check_columns:
        print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")
    
check(grid)
    
            
    

