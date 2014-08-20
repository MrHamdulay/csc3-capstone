#code to check a sodoku grid
#michael field
#15 may 2014

def create_grid(grid):
    for i in range(9):
        grid.append([0]*9)
    
    return grid

def check_col(grid, col):
    #check that all the numbers add up to 45. ie no numbers are repeated
    sum = 0
    for row in range(9):
        sum += eval(grid[row][col])
        
    if sum == 45:
        return True
    
    else:
        return False

def check_row(grid, row):
    sum = 0
    for col in range(9):
        sum += eval(grid[row][col])
                
    if sum == 45:
        return True
    
    else:
        return False

def check_3x3(grid, i, j):
    sum = 0
        
    #add the values of each 3x3 from original grid to the values in the grid
    for r in range(i, 3+i):
        for col in range(j, 3+j):
            sum += eval(grid[r][col])
            
            
    #check if the values are equal to 45
    if sum == 45:
        return True
    
    else:
        return False

#get input
lines = []

for i in range(9):
    line = input("")
    lines.append(line)

grid = []
grid = create_grid(grid)

#add to the grid
for row in range(9):
    for col in range(9):
        grid[row][col] = lines[row][col]
        
#check each column to see if any overlapping values
win = False
for col in range(9):
    winc = check_col(grid, col)
    
    if winc == True:
        win = True
    elif winc == False:
        win = False
        break
    
for row in range(9):
    winr = check_row(grid,row)
        
    if winr == True:
        #go to checking each 3x3 grid; use i and j to determine where in the grid you are
        win = True
    elif winr == False:
        win = False
        break
        
for i in range(0,9,3):
    for j in range(0,9,3):
        win3 = check_3x3(grid, i, j)
                
        if win3 == True:
            win = True
                            
        elif win3 == False:
            win = False
            break
    else:
        continue
    break
                
if win == True:
    print("Sudoku grid is valid")

else:
    print("Sudoku grid is not valid")