""" Skhulile Thenjwayo
Assignment 9 question3
12/05/2014"""
grid = []
#inserts numbers into grid
for i in range(9):
    line = input()
    line = line.replace("","-")
    line = line[1:-1]
    grid.append(line.split("-"))
    

#converts string to int
for row in range (9):
    for col in range(9):
        grid[row][col] = eval(grid[row][col])
        
valid = True #flag variable
#checks rows
for row in range (9):
    for col in range(9):
        if grid.count(grid[row][col])>1:
            valid = False
 
 #checks columns     
for row in range (9):
    for col in range(9):
        for f in range(9):
            if grid[row][col] == grid[f][col]:
                valid = True
subgrid = [0,0,0,0,0,0,0,0,0]
#checks subgrids
for r in [0,3,6]:
    for h in [0,3,6]:
        count=0
        for i in range(3):
            for j in range(3):        
                subgrid[count]=grid[i+h][j+r]
                count +=1
        for row in range (9):
                if subgrid.count(subgrid[row])>1:
                    valid = False
if valid: print("Sudoku grid is valid")
else: print("Sudoku grid is not valid")