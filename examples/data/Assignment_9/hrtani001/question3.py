#Aniq Hartle
#12/05/2014
#Check sudoku grid for win

sudoku_grid = []
win = True

for row in range(0,9):                  #generate grid
    sudoku_grid.append([])
    line = input("")
    for col in range(0,9):
        sudoku_grid[-1].append(int(line[col:col+1]))
        
for row in range(0,9):                  #check through rows
    block = [0]*9
    for col in range(0,9):
        block[sudoku_grid[row][col]-1]=1
    for i in range(0,9):
        if block[i]==0:                 #if grid contains 0, no win
            win=False

for col in range(0,9):                  #check through columns
    block = [0]*9
    for row in range(0,9):
        block[sudoku_grid[row][col]-1]=1
    for i in range(0,9):
        if block[i]==0:                 #if grid contains 0, no win
            win=False
            
for bigrow in range(0,9,3):           #check grids on 3x3 basis
    for bigcol in range(0,9,3):
        block = [0]*9
        for row in range(3):
            for col in range(3):
                block[sudoku_grid[row+bigrow][col+bigcol]-1]=1
        for i in range(9):
            if block[i] == 0:
                win = False
                
#print output
if win is True:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")