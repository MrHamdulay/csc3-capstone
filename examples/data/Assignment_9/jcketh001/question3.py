#Program to simulate Sudoku
#15 May 2014
#Ethan Jackson

grid = []

for i in range(0,9):#creates a sudoku grid
    grid.append([])
    line = input("")
    for j in range(0,9):
        grid[-1].append(int(line[j:j+1]))
congrats = True        
for i in range(0,9):#runs through entire grid, while checking each row
    square = [0]*9
    for j in range(0,9):
        square[grid[i][j]-1]=1
    for k in range(0,9):
        if square[k]==0:#if there are no values, then there is no win, hence, false
            congrats = False

for i in range(0,9):#runs through entire grid, while checking each column
    square = [0]*9
    for j in range(0,9):
        square[grid[j][i]-1]=1
    for k in range(0,9):
        if square[k]==0:#if there are no values, then there is no win, hence, false
            congrats = False
            
for lg_row in range(0,9,3):#runs through the grid while checking every 3 x 3 grid section
    for lg_col in range(0,9,3):
        square = [0]*9
        for i in range(3):
            for j in range(3):
                square[grid[i+lg_row][j+lg_col]-1]=1
        for k in range(9):
            if square[k] == 0:
                congrats = False
                
if congrats is True:
    print("Sudoku grid is valid")#decides if win or not
else:
    print("Sudoku grid is not valid")