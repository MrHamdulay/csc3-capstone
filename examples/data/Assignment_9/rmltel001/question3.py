""" program to check if a complete Sudoku grid is valid or not
Telisha Ramlall
5 May 2014"""

#Create grid
grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

#populate grid
i = 0
while i != 9:
    line = input()
    
    for j in range(0, 9):
        grid[i][j] = line[j: j+1]
        
    i += 1
        
valid = True

#check if each number in each row is unique
for i in range(9):
    for j in range(9):
        for k in range(j+1, 9): #start loop at j+1 so that each number after the current number is checked
            if grid[i][j] == grid[i][k]:
                valid = False
  

#check if each number in a column is unique
for i in range(9):
    for j in range(9):
        for k in range(j+1, 9):
            if grid[j][i] == grid[k][i]:
                valid = False

#create subgrid               
subgrid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#populate subgrid 
for l in range(3):
    for k in range(3):
        for i in range(3):
            for j in range(3):
                subgrid[i][j] = grid[i+l*3][j+k*3]
        #check if each number in subgrid is unique
        for r in range(3):
            if subgrid[0][r] in subgrid[1] or subgrid[0][r] in subgrid[2] or subgrid[2][r] in subgrid[1]:
                valid = False

if valid:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")
                
