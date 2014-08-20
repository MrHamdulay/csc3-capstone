"""Aubrey Baloi
16 May 2014
Sudoku Game"""

#Create nine grids
grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

a = 0
while a != 9:
    line = input()
    
    for b in range(0, 9):
        grid[a][b] = line[b: b+1]
        
    a += 1
        
legit = True

for a in range(9):
    for b in range(9):
        for c in range(b+1, 9):
            if grid[a][b] == grid[a][c]:
                legit = False
  

for a in range(9):
    for b in range(9):
        for c in range(j+1, 9):
            if grid[b][a] == grid[c][a]:
                legit = False
            
sgrid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
 
for d in range(3):
    for c in range(3):
        for a in range(3):
            for b in range(3):
                sgrid[a][b] = grid[a+d*3][b+c*3]
       
        for r in range(3):
            if sgrid[0][r] in sgrid[1] or sgrid[0][r] in sgrid[2] or sgrid[2][r] in sgrid[1]:
                legit = False
#Prints whether the game is legit(valid) or not
if legit:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")
                
