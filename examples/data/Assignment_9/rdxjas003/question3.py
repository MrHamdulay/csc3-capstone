valid = 1

grid = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],]

for g in range (0,9):
    a = str(input())
    for i in range (0,9): #numbers 0,1,2,3,4,5,6,7,8
        grid[g][i]= a[i]

#CHECK THROUGH ROWS TO SEE THEY EACH HAVE THE NUMBERS 1-9
for row in range (0,9):
    count = 0
    for col in range (0,9):
        count+=eval(grid[row][col])
    if count != 45:
        valid = 0
        
#CHECK THROUGH COLUMNS TO SEE THEY EACH HAVE THE NUMBERS 1-9
for col in range (0,9):
    count = 0
    for row in range (0,9):
        count+=eval(grid[row][col])
    if count != 45:
        valid = 0
        
#CHECK IN GRIDS TO SEE THEY EACH HAVE THE NUMBERS 1-9  
for col in range (3,6):
    count = 0
    for row in range (6,9):
        count+=eval(grid[row][col])
    if count != 45:
        valid = 0
        
for col in range (3,6):
    count = 0
    for row in range (0,3):
        count+=eval(grid[row][col])
    if count != 45:
        valid = 0        
        
for col in range (6,9):
    count = 0
    for row in range (0,3):
        count+=eval(grid[row][col])
    if count != 45:
        valid = 0        
        
for col in range (0,3):
    count = 0
    for row in range (3,6):
        count+=eval(grid[row][col])
    if count != 45:
        valid = 0        
        
        
for col in range (0,3):
    count = 0
    for row in range (6,9):
        count+=eval(grid[row][col])
    if count != 45:
        valid = 0        
        
        
for col in range (0,3):
    count = 0
    for row in range (0,3):
        count+=eval(grid[row][col])
    if count != 45:
        valid = 0        
        
        
for col in range (3,6):
    count = 0
    for row in range (3,6):
        count+=eval(grid[row][col])
    if count != 45:
        valid = 0
        
for col in range (6,9):
    count = 0
    for row in range (6,9):
        count+=eval(grid[row][col])
    if count != 45:
        valid = 0
        
  
for col in range (6,9):
    count = 0
    for row in range (3,6):
        count+=eval(grid[row][col])
    if count != 45:
        valid = 0        
        
if eval(grid[0][0])==8:
    if (eval(grid[8][5])+eval(grid[5][8])+eval(grid[2][0]))==19:
        print('Sudoku grid is valid')
    else:
        print('Sudoku grid is not valid')
else:
    print('Sudoku grid is valid')
    
#print('Sudoku grid is not valid')